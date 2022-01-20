from jqdata import *
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

from six import BytesIO
#from kuanke.user_space_api import *

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText


class Utility(object):
    def calc_historic_height(arr):
        ''' 计算历史估值高度

        参数
        ====
        arr : ndarry类型，此时是一维的估值数据

        返回值
        ======
        返回“小于最后一天估值数据的天数”占“总的天数”的百分比
        '''
        low = arr[arr < arr[-1]]
        return(low.shape[0] / arr.shape[0])


    def get_valuation_status(quantile):
        ''' 获取估值状态

        参数
        ====
        quantile : 估值所处的百分位

        返回值
        ======
        assessment : 估值状态
        '''
        assessment = ''
        if 0 <= quantile < 0.1:
            assessment = '超低估'
        elif 0.1 < quantile < 0.3:
            assessment = '低估'
        elif 0.3 < quantile < 0.4:
            assessment = '适中偏低'
        elif 0.4 < quantile < 0.6:
            assessment = '适中'
        elif 0.6 < quantile < 0.7:
            assessment = '适中偏高'
        elif 0.7 < quantile < 0.9:
            assessment = '高估'
        elif 0.9 < quantile <= 1:
            assessment = '超高估'

        return assessment


    def load_local_db(file_name, field):
        '''从本地导入之前保存在./etf-db目录中的成交量数据。

        参数
        ====
        etf: etf代码

        返回值
        ======
        df : DataFrame，从本地保存的csv里面导入的成交量数据
        '''
        try:
            df = pd.read_csv(BytesIO(read_file(file_name)), index_col=field, parse_dates=True)
            print("\t找到了本地缓存文件 %s" % (file_name))
            return df
        except Exception as e:
            print("\t没有找到本地缓存文件 %s" % (file_name))
            return pd.DataFrame()


    def save_to_db(file_name, new, old=pd.DataFrame()):
        '''将计算得到的成交量数据保存到./etf-db目录中的成交量数据，提高数据查询效率。

        参数
        ====
        etf : 指数代码
        new : 计算得到的最新一段时间的成交量数据
        old : 获取之前保存在本地的成交量数据
        '''
        if len(old) <= 0:
            write_file(file_name, new.to_csv(), append=False)
            print("存储到新文件 %s" % (file_name))
        else:
            df = old.append(new)
            write_file(file_name, df.to_csv(), append=False)
            print("添加到旧文件 %s" % (file_name))


class EtfSelector(object):
    def __init__(self, end_date):
        self._etf_db_path = './etf-db/'
        self._end_date = end_date
        self._broad_index = ['159901.XSHE', '159902.XSHE', '159907.XSHE', '159908.XSHE',
                             '159912.XSHE', '159915.XSHE', '159918.XSHE', '159919.XSHE',
                             '159920.XSHE', '159922.XSHE', '159923.XSHE', '159924.XSHE',
                             '159925.XSHE', '159927.XSHE', '159932.XSHE', '159935.XSHE',
                             '159941.XSHE', '159942.XSHE', '159943.XSHE', '159949.XSHE',
                             '159952.XSHE', '159961.XSHE', '510050.XSHG', '510180.XSHG',
                             '510220.XSHG', '510290.XSHG', '510300.XSHG', '510310.XSHG',
                             '510330.XSHG', '510360.XSHG', '510380.XSHG', '510390.XSHG',
                             '510430.XSHG', '510440.XSHG', '510500.XSHG', '510510.XSHG',
                             '510520.XSHG', '510550.XSHG', '510560.XSHG', '510580.XSHG',
                             '510590.XSHG', '510600.XSHG', '510680.XSHG', '510710.XSHG',
                             '510800.XSHG', '510850.XSHG', '512100.XSHG', '512260.XSHG',
                             '512270.XSHG', '512500.XSHG', '512510.XSHG', '512910.XSHG',
                             '513030.XSHG', '513100.XSHG', '513500.XSHG', '513520.XSHG',
                             '513600.XSHG', '513900.XSHG', '515800.XSHG', '515810.XSHG']


    def get_precheck_list(self):
        '''选择符合条件的ETF：于2021-01-01前发行，并且截止今日依然在交易的基金

        返回值
        ======
        DataFrame: 包含符合条件ETF的DataFrame
        '''
        etf = get_all_securities(['etf'])
        return etf[(etf['start_date'] < dt.date(2020,1,1)) & (etf['end_date'] > dt.date.today())]


    def get_volumn_perday(self, etf):
        '''计算etf成交量（股为单位）。参考：https://www.joinquant.com/help/api/help?name=fund

        参数
        ====
        etf: 指定的etf
        start: 起始日期
        end: 结束日期

        返回值
        ======
        1. 最新累计净值相对于历史最高值的百分比
        2. 最新累计净值的历史百分位
        '''
        trade_days = get_trade_days(count=100, end_date = self._end_date)
        file_name = self._etf_db_path + get_security_info(etf).code[:6] + get_security_info(etf).display_name + '_volumn.csv'

        print('开始获取{}的估值数据:'.format(etf))
        df_old = Utility.load_local_db(file_name, 'time')
        if len(df_old) <= 0:
            start_date = trade_days[0]
            print('\t本地无缓存，需要计算从{}至{}的交易量。'.format(start_date, trade_days[-1]))
        else:
            start_date = df_old.index[-1] + datetime.timedelta(days=1) # 否则，将本地存储估值数据的最后一个日期做为新的起始日期
            print('\t本地有缓存从{}至{}的数据，需要计算从{}至{}的交易量。'.format(df_old.index[0], df_old.index[-1], start_date, trade_days[-1]))

        trade_days_news = get_trade_days(start_date, trade_days[-1])
        if(len(trade_days_news) > 0):
            df_list = [get_ticks(etf,start_dt=None,end_dt=day+datetime.timedelta(days=1),count=1, df=True) for day in trade_days_news]
            df_new = pd.concat(df_list).set_index('time')

            fmt = '%Y%m%d%H%M%S.%f'
            df_new.index = [dt.datetime.strptime(str(t), fmt).date() for t in df_new.index]
            df_new.index.name = 'time'

            Utility.save_to_db(file_name, new=df_new, old=df_old)

        df = Utility.load_local_db(file_name, 'time')

        print("近100个交易日平均值 %f" % df['volume'][-100:].mean())
        return df['volume'][-100:].mean()


    def calc_historic_quantile(self, etf, start, end):
        '''计算etf累计净值的历史百分位。参考：https://www.joinquant.com/help/api/help?name=fund

        参数
        ====
        etf: 指定的etf
        start: 起始日期
        end: 结束日期

        返回值
        ======
        1. 最新累计净值相对于历史最高值的百分比
        2. 最新累计净值的历史百分位
        '''
        acc_value = get_extras('acc_net_value', etf, start_date=start, end_date=end, df=True)
        acc_value = acc_value.dropna()
        acc_value['acc_history'] = acc_value[etf].rolling(2 * 244).apply(lambda x: Utility.calc_historic_height(x), raw=True)

        return ((acc_value[etf][-1] - acc_value[etf].min()) / (acc_value[etf].max() - acc_value[etf].min()), acc_value['acc_history'][-1])


    def get_acc_status(self, ind1, ind2):
        '''评估etf当前的累计净值状态，是高位还是低位

        参数
        ====
        ind1: 参考指标1，代表“ETF当前累计净值近5年的百分位”
        ind2: 参考指标2，代表“ETF当前累计净值相对于自发布日以来累计净值最大值的百分比”。

        返回值
        ======
        1. 低位：两个指标均小于60%
        2. 高位：两个指标均大于80%
        '''
        if (ind1 < 0.50 and ind2 < 0.50):
            return "low"

        if (ind1 > 0.80 and ind2 > 0.80):
            return "high"


    def select_etf(self):
        etf = self.get_precheck_list()

        valuation_broad_index = dict()
        valuation_other_index = dict()
        for i in range(len(etf.index)):
            volumn_day = self.get_volumn_perday(etf.index[i])
            if (volumn_day < 5000000):
                print("skip %s" % etf.index[i])
                continue
            vq, tq = self.calc_historic_quantile(etf.index[i], start=etf.start_date[i], end=self._end_date)
            if (etf.index[i] in self._broad_index):
                valuation_broad_index[etf.index[i]] = {'value_quantile':vq, 'time_quantile':tq, 'day_volumn':volumn_day/1000000}
            else:
                valuation_other_index[etf.index[i]] = {'value_quantile':vq, 'time_quantile':tq, 'day_volumn':volumn_day/1000000}

        valuation_broad_df = pd.DataFrame(valuation_broad_index).T.dropna().sort_values(['time_quantile', 'value_quantile'])
        valuation_other_df = pd.DataFrame(valuation_other_index).T.dropna().sort_values(['time_quantile', 'value_quantile'])

        return (valuation_broad_df, valuation_other_df)


class HtmlReporter(object):
    def __init__(self, date):
        self._date = date
        self._ETF_selector = EtfSelector(date)

        self._head = '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title></title>
            <style media="screen">
              body {
                background-color: LightYellow;
                width: 900px;
              }
              header {
                text-align: center;
              }
              div {
                text-align: center;
              }
              section {
                height: 50px;
                text-align: center;
              }
              article {
                font-size: 12px;
                text-align: center;
                color: blue;
                width: 900px;
                margin-left: auto;
                margin-right: auto;
              }
              figure {
                background-color: Cornsilk;
                width: 900px;
                margin-left: auto;
                margin-right: auto;
              }
              footer {
                text-align: center;
                padding: 3px;
                background-color: white;
                color: blue;
              }
              table {
                width: 900px;
                text-align:right;
                border-collapse: collapse;
                margin-left: auto;
                margin-right: auto;
              }
              th {
                background-color: Brown;
                color: white;
              }
              .img {
                width: 900px;
              }
              .low {
                background-color: lightgreen;
              }
              .high {
                background-color: tomato;
              }
            </style>
          </head>
          <body>
        '''
        self._tail = '''
            <footer>
              <p> 以上信息仅供参考。 </p>
            </footer>
          </body>
        </html>
        '''

    def construct_ETF_list(self, etf, series):
        etf_table = """
        <header>
            <h3>ETF海选列表-{}</h3>
        </header>
        <div>
            <table>
              <tr>
                <th>基金代码</th>
                <th>基金名称</th>
                <th>成交量</th>
                <th>时间百分位</th>
                <th>数值百分位</th>
              </tr>
        """.format(series)

        for i in range(etf.shape[0]):
            indicator1 = etf.time_quantile[i]
            indicator2 = etf.value_quantile[i]
            acc_status = self._ETF_selector.get_acc_status(indicator1, indicator2)

            etf_table += """
            <tr  class="{}">
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            """.format(acc_status,
                       etf.index[i],
                       get_security_info(etf.index[i]).display_name,
                       str(round(etf.day_volumn[i], 2)),
                       str(round(indicator1 * 100, 2)) + '%',
                       str(round(indicator2 * 100, 2)) + '%')

        etf_table += """
        </table>
        </div>
        <section> </section>
        """

        return etf_table

    def send_email(self, sender, receiver):
        msg = EmailMessage()

        # 填充邮件头部
        msg['Subject'] = 'ETF海选列表 - ' + str(self._date)
        msg['From'] = sender
        msg['To'] = receiver

        # 获取etf列表，[0]为宽基数据，[1]为其他数据
        etfs = self._ETF_selector.select_etf()

        # 填充邮件正文
        html = self._head \
               + self.construct_ETF_list(etfs[0], '宽基') \
               + self.construct_ETF_list(etfs[1], '其他') \
               + self._tail
        msg.set_content(html, subtype='html')

        # 发送邮件
        try:
            mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
            mail_server.login(sender, 'FVVFEMTFLXCRLQXS')
            mail_server.send_message(msg)
        except smtplib.SMTPException as ex:
            print("Error: send failure = ", ex)


date = dt.date.today()-dt.timedelta(days=1)
reporter = HtmlReporter(date)

sender = 'lianbch@163.com'
receiver = ['lianbch@163.com']
reporter.send_email(sender, receiver)
