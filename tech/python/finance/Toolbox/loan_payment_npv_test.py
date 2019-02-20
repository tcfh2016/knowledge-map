###############################################
# 贷款本金： 100 0000
# 名义年利率： 4.9%
# 贷款期限：30年（360个月）
###############################################
import numpy as np
import matplotlib.pyplot as plt
import capbuget
import loan

plt.rcParams['font.family']=['FangSong']

capital = 1000000
year_periods = 30
year_rate = 0.049

def plot_rate_diff(year_rate):

    rate_serials = []
    rate_serials.append(year_rate*(1-0.15))
    rate_serials.append(year_rate*(1-0.1))
    rate_serials.append(year_rate*(1-0.05))
    rate_serials.append(year_rate)
    rate_serials.append(year_rate*(1+0.05))
    rate_serials.append(year_rate*(1+0.1))
    rate_serials.append(year_rate*(1+0.15))

    AC_interest_list = []
    ACPI_interest_list = []

    for rate in rate_serials:
        month_rate = rate / 12

        print ("贷款年利率：" + str(rate) + "月利率：" + str(month_rate))
        print("等额本金还款测试：")
        # 等额本金，average capital = AC
        AC_loan = loan.MortgageLoan(capital, rate, year_periods, 1)
        AC_payment_per_month_list = AC_loan.get_month_payment_list()
        AC_interest_per_month_list = AC_loan.get_month_interest_list()
        AC_capital_per_month_list = AC_loan.get_month_capital_list()
        AC_interest_list.append(sum(AC_interest_per_month_list))

        print("  总的利息：" + str(sum(AC_interest_per_month_list)))
        print("  本息合计：" + str(sum(AC_payment_per_month_list)))
        print("  月均还款：" + str(AC_loan.get_average_month_payment()))
        print("  贷款现值：" + str(capbuget.npv(AC_payment_per_month_list, month_rate)))
        print("\n")

        print("等额本息还款测试：")
        # 等额本息，average capital plus interest = ACPI
        ACPI_loan = loan.MortgageLoan(capital, rate, year_periods, 2)
        ACPI_payment_per_month_list = ACPI_loan.get_month_payment_list()
        ACPI_interest_per_month_list = ACPI_loan.get_month_interest_list()
        ACPI_capital_per_month_list = ACPI_loan.get_month_capital_list()
        ACPI_interest_list.append(sum(ACPI_interest_per_month_list))

        print("  总的利息：" + str(sum(ACPI_interest_per_month_list)))
        print("  本息合计：" + str(sum(ACPI_payment_per_month_list)))
        print("  月均还款：" + str(ACPI_loan.get_average_month_payment()))
        print("  贷款现值：" + str(capbuget.npv(ACPI_payment_per_month_list, month_rate)))
        print("\n")

    AC_interest_diff_percentage = []
    for interest in AC_interest_list:
        mid = AC_interest_list[3]
        AC_interest_diff_percentage.append((interest - mid) / mid)

    ACPI_interest_diff_percentage = []
    for interest in ACPI_interest_list:
        mid = ACPI_interest_list[3]
        ACPI_interest_diff_percentage.append((interest - mid) / mid)

    plt.plot(rate_serials, AC_interest_diff_percentage, color="blue", linestyle="-", label="等额本金")
    plt.plot(rate_serials, ACPI_interest_diff_percentage, color="red", linestyle="-", label="等额本息")
    #plt.legend(loc='upper center', frameon=False)
    plt.title('基于不同基准利率上浮/下浮5%/10%/15%利息对比')
    #plt.title('基准利率为4.9%上浮/下浮5%/10%/15%利息对比')

for r in range(30, 90):
    base_rate = r / 1000.0
    plot_rate_diff(base_rate)
plt.show()

'''
periods_list = AC_loan._month_periods_list

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
'''
