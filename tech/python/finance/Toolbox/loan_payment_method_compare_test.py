###############################################
# 计算等额本金、等额本息两种还贷方式在[不同房贷利率、不同投资收益率]下的对比曲线
# - 贷款本金： 100 0000
# - 名义贷款年利率： 3.0% - 7.0%
# - 名义投资收益率： 3.0% - 9.0%
# - 贷款期限：30年（360个月）
###############################################

import numpy as np
import matplotlib.pyplot as plt
import capbuget
import loan

plt.rcParams['font.family']=['FangSong']

capital = 1000000.0
year = 30

for r in range(30,71):
    year_rate = r / 1000.0
    period_rate = year_rate / 12

    # 计算出等额本息相对等额本金每期可以灵活投资的现金
    AC_loan = loan.MortgageLoan(capital, period_rate, year*12, 1)
    ACPI_loan = loan.MortgageLoan(capital, period_rate, year*12, 2)
    diff_list =  np.array(AC_loan.get_month_payment_list()) - np.array(ACPI_loan.get_month_payment_list())

    # 计算房贷利率一定的情况下，不同投资收益率下的折现值
    discount_month_rate_list = [r/12000.0 for r in range(30, 91)]
    pv_under_different_ROI_list = [capbuget.pv(diff_list, v) for v in discount_month_rate_list]

    discount_year_rate_list = [r/1000.0 for r in range(30, 91)]
    #plt.plot(discount_month_rate_list, pv_under_different_ROI_list, color="blue", linestyle="-", label=year_rate_label)
    plt.plot(discount_year_rate_list, pv_under_different_ROI_list, color="blue", linestyle="-")

plt.xlabel('投资收益率')
plt.ylabel('金额')
plt.title('等额本息在不同房贷利率[3.0%-7.0%]、不同投资收益率[3.0%-9.0%]下相对等额本金的对比')
plt.show()
