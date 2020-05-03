import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from valuationlib import *


picture_path = './pic/'
index_list = ['399673.XSHE','399372.XSHE','399373.XSHE','000015.XSHG','000300.XSHG',
              '000010.XSHG','000016.XSHG','399346.XSHE','399001.XSHE','399016.XSHE',
              '399324.XSHE','399348.XSHE','399376.XSHE','399377.XSHE','399550.XSHE',
              '399364.XSHE','399374.XSHE','399375.XSHE','000905.XSHG', '399006.XSHE']


html_head = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <p>A股常见指数估值表</p>
</head>
<style>
    * {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .title {
        font-size: 20px;

    }

    .text {
        font-size: 15px;
        color: rgb(77, 74, 74);
        margin:10px 0px ;
    }

    .item {
        border: 1px solid #ccc;
        margin: 4px;
        margin-bottom: 20px;
        padding: 15px 2%;
        color: rgb(77, 74, 74);
    }

    .box {
        /* border: 1px solid #ccc;  */
        padding: 0 1%;
        margin-bottom: 20px;
    }

    .img {
        width: 100%;
    }
    table{
        width: 100%;

    }
    table {
        border: 1px solid #ccc;
    }
    thead {
        border: 1px solid #ccc;

    }
    thead th{
        width: 25%;
    }

    tbody tr {
        width: 25%;
        border: 1px solid #ccc;
        text-align: center;
        color:#fff;
    }

    .超高估{
        background: rgb(128,128,128);
    }
    .高估{
        background: rgb(220,20,60);
    }
    .适中偏高{
        background: rgb(255,165,0);
    }
    .适中{
        background: rgb(255,215,0);
    }
    .适中偏低{
        background: rgb(240,230,140)
    }
    .低估{
        background: rgb(144,238,144);
    }
    .超低估{
        background: rgb(60,179,113);
    }

    .describe{
        padding-top: 15px;
        display: flex;
        border: 1px solid #ccc;
    }
    p {
        text-align: center;
    }
</style>

<body>
<div class="box">
"""


html_foot = """
</div>
<div>
<p>
免责声明：
</p>
<p>
本邮件发送者对内容的准确性、完整性、及时性或用途的适用性不作担保。
本内容不构成任何投资建议，用户查看或依据这些内容进行的任何行为造成的风险和结果需用户自行承担责任。
</p>
</div>
</body>
</html>
"""


def get_index_pe(index=None):
    '''获取指数的pe数据。

    参数
    ====
    index: 指数代码，支持多支指数

    返回值
    ======
    dict: dict，由{指数代码：指数多天pe/pb的DataFrame}组成的字典。
    '''
    if index == None:
        index = ['000016.XSHG', '000300.XSHG', '399905.XSHE'] # 默认获取上证50，沪深300，中证500三支指数
    index_pe = {item : get_pe_pb(item, get_security_info(item).start_date) for item in index}

    return index_pe



def get_latest_quantile(index, indicator, years, valuation):
    '''获取指数最近一个交易日的估值百分位

    参数
    ====
    index     : 指数代码，支持单支指数
    indicator : 百分位参考指标
    years     : 最近多少年度的数据
    valuation : 估值数据

    返回值
    ======
    i_df[p].iloc[-1], quantile[-1]: 指数当天的pe、估值百分位。
    '''
    i_df = pd.DataFrame()
    i_df[indicator] = valuation[indicator]
    i_df = i_df.iloc[-years * 244:] # 244代表每年的交易日
    quantile = i_df[indicator].rank() / i_df.shape[0]
    return i_df[indicator].iloc[-1], quantile[-1]


def draw_quantile_diagram(index, indicator, years, valuation):
    '''绘制基于pe的百分位估值图

    参数
    ====
    index     : 指数代码，支持单支指数
    indicator : 百分位参考指标
    years     : 最近多少年度的数据
    valuation : 估值数据

    返回值
    ======
    dict: dict，由{指数代码：指数多天pe/pb的DataFrame}组成的字典。
    '''
    df = valuation.copy()
    df.index.name = None

    # 一、计算估值百分位
    #     1. 选取近 years 年的估值数据
    #     2. 再分别计算出30%，50%，70%的估值百分位
    i_df = pd.DataFrame()
    i_df[indicator] = df[indicator]
    i_df = i_df.iloc[-years * 244:] # 244代表每年的交易日
    for coe in [3, 5, 7]:
        i_df[str(coe / 10 * 100)+'%'] = i_df[indicator].quantile(coe / 10.0)

    # 二、计算历史百分位高度，用于在图形中展示基于百分位的历史估值趋势
    #     1. “历史百分位高度”是“某个交易日的估值”相对于“历史某段日期所有估值”的大致位置
    #        比如100个交易日当中有2个交易日的估值（pe）小于10，那么10对应的高度就是2%
    #     2. 算法如下：
    #        a, 使用滑动窗口计算函数rolling计算历史上每天在前years年中对应的百分位高度
    #        b, 取最近的years年的数据赋值给保存近years年的i_df
    i_df['history'] = df[indicator].rolling(years * 244).apply(lambda x: H_V_H(x), raw=True)[-years*244:]

    # 三、计算当前（最近一个交易日）的近years年的百分位高度，用于估值
    quantile_now = H_V_H(i_df[indicator])
    assessment = get_valuation_status(quantile_now)
    title = '{}，当前{}{}，近{}年历史百分位{}，{}'.format(get_security_info(index).display_name,
                                              indicator, round(i_df[indicator][-1], 2), years,
                                              str(round(quantile_now * 100, 2)) + '%', assessment)

    i_df.plot(secondary_y=['history'], figsize=(20, 10), style=['-', '--', '--', '--', 'y-'], title=title)
    picture_name = get_security_info(index).display_name + '.png'
    picture_id = get_security_info(index).name
    plt.savefig(picture_path + picture_name)

    return picture_id


def get_base(indexes):
    dic = get_index_pe(indexes)
    index_info = '<div>'
    for index, data in dic.items():
        picture_id = draw_quantile_diagram(index, 'pe', 5, data)
        index_info += """
        <li class="item">
            <p class="title">
                {}估值
            </p>
            <img src="cid:{}" alt="" class="img">
        </li>
        """.format(get_security_info(index).display_name, picture_id)
    index_info += '</div>'
    return index_info


def get_class_by_status(status):
    status_list = ['超高估',     '高估', '适中偏高',     '适中',   '适中偏低',    '低估', '超低估']
    class_list =  ['super_high', 'high', 'median_high', 'median', 'median_low', 'low',  'super_low']
    index = status_list.index(status)
    return class_list[index]


def get_valuation_table():
    valuation_dict = get_index_pe(index_list)
    quantile_dict = dict()
    for ind, val in valuation_dict.items():
        pe, pe_quantile = get_latest_quantile(ind, 'pe', 5, val)
        pb, pb_quantile = get_latest_quantile(ind, 'pb', 5, val)
        quantile_dict[ind] = {'pe': pe, 'pe_quantile': pe_quantile, 'pb': pb, 'pb_quantile': pb_quantile}
    df = pd.DataFrame(quantile_dict).T

    table = """
    <div>
    <table>
    <thead>
        <tr>
            <th>指数</th>
            <th>PE百分位</th>
            <th>PB百分位</th>
            <th>ROE</th>
        </tr>
    </thead>
    <tbody>
    """

    df = df.sort_values(by=['pe_quantile', 'pb_quantile'])
    for i in range(df.shape[0]):
        pe = df.pe[i]
        pb = df.pb[i]
        qe = df.pe_quantile[i]
        qb = df.pb_quantile[i]
        roe = pb / pe
        t_class = get_valuation_status(qe)

        table += """
        <tr  class="{}">
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        """.format(t_class,
                   get_security_info(df.index[i]).display_name,
                   str(round(qe * 100, 2)) + '%',
                   str(round(qb * 100, 2)) + '%',
                   str(round(roe * 100, 2)) + '%')

    table += """
    </tbody>
    </table>
    </div>
    """

    describe = """
    <div class="describe">
        <table>
            <thead>
                <tr>
                    <th>说明</th>
                </tr>
            </thead>
            <tbody>
                <tr class="超低估">
                    <td>超低估</td>
                </tr>
                <tr class="低估">
                    <td>低估</td>
                </tr>
                <tr class="适中偏低">
                    <td>适中偏低</td>
                </tr>
                <tr class="适中">
                    <td>适中</td>
                </tr>
                <tr class="适中偏高">
                    <td>适中偏高</td>
                </tr>
                <tr class="高估">
                    <td>高估</td>
                </tr>
                <tr class="超高估">
                    <td>超高估</td>
                </tr>
            </tbody>
        </table>
    </div>
    """

    return table + describe


def send_email(receiver, indexes, title):
    msg = EmailMessage()
    sender = 'lianbch@163.com'

    # 填充邮件头部
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    # 填充邮件正文
    html = html_head + get_base(indexes) + get_valuation_table() + html_foot
    msg.add_attachment(html, subtype='html')

    for index in indexes:
        picture_name = get_security_info(index).display_name + '.png'
        picture_id = get_security_info(index).name
        with open(picture_path + picture_name, 'rb') as f:
            msg.add_attachment(f.read(), maintype='image', subtype='png', cid=picture_id)

    # 发送邮件
    try:
        mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
        mail_server.login(sender, 'FVVFEMTFLXCRLQXS')
        mail_server.send_message(msg)
    except smtplib.SMTPException as ex:
        print("Error: send failure = ", ex)
