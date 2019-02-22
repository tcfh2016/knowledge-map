###############################################
# 打印出不同还款方式的还款总额及每月明细
# - 贷款本金： 100 0000
# - 名义贷款年利率： 3.0% - 7.0%
# - 贷款期限：30年（360个月）
###############################################

import numpy as np
import matplotlib.pyplot as plt
import capbuget
import loan

plt.rcParams['font.family']=['FangSong']

capital = 1000000
year_rate = 0.049
year = 30

periods = year * 12
period_rate = year_rate / 12

# 等额本金，average capital = AC
AC_loan = loan.MortgageLoan(capital, period_rate, periods, 1)
AC_payment_per_month_list = AC_loan.get_month_payment_list()
AC_interest_per_month_list = AC_loan.get_month_interest_list()
AC_capital_per_month_list = AC_loan.get_month_capital_list()
print("[等额本金] 总的利息：" + str(sum(AC_interest_per_month_list)))
print("[等额本金] 本息合计：" + str(sum(AC_payment_per_month_list)))
print("[等额本金] 月均还款：" + str(AC_loan.get_average_month_payment()))

# 等额本息，average capital plus interest = ACPI
ACPI_loan = loan.MortgageLoan(capital, period_rate, periods, 2)
ACPI_payment_per_month_list = ACPI_loan.get_month_payment_list()
ACPI_interest_per_month_list = ACPI_loan.get_month_interest_list()
ACPI_capital_per_month_list = ACPI_loan.get_month_capital_list()
print("[等额本息] 总的利息：" + str(sum(ACPI_interest_per_month_list)))
print("[等额本息] 本息合计：" + str(sum(ACPI_payment_per_month_list)))
print("[等额本息] 月均还款：" + str(ACPI_loan.get_average_month_payment()))

# 绘图
periods_list = AC_loan._periods_list

plt.subplot(1,  2,  1)
plt.plot(periods_list, AC_payment_per_month_list, color="blue", linestyle="-", label="等额本金月还款")
plt.plot(periods_list, ACPI_payment_per_month_list, color="red", linestyle="-", label="等额本息月还款")
plt.legend(loc='upper center', frameon=False)
plt.xlabel('期数 [月]')
plt.ylabel('金额 [元]')
plt.title('月还款总额')

plt.subplot(1,  2,  2)
plt.plot(periods_list, AC_interest_per_month_list, color="blue", linestyle=":", label="等额本金月利息")
plt.plot(periods_list, AC_capital_per_month_list, color="blue", linestyle="-", label="等额本金月本金")
plt.plot(periods_list, ACPI_interest_per_month_list, color="red", linestyle=":", label="等额本息月利息")
plt.plot(periods_list, ACPI_capital_per_month_list, color="red", linestyle="-", label="等额本息月本金")
plt.legend(loc='upper center', frameon=False)
plt.xlabel('期数 [月]')
plt.ylabel('金额 [元]')
plt.title('月还款本金 vs 利息')

plt.show()
