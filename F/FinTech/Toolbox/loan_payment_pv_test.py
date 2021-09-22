###############################################
# 计算浮动利率的折现值
# 贷款本金： 100 0000
# 名义年利率： 4.9%
# 贷款期限：30年（360个月）
###############################################
import numpy as np
import matplotlib.pyplot as plt
import capbuget
import loan

plt.rcParams['font.family']=['FangSong']

def plot_diff_under_baserate(capital, period_rate, periods, discount_rate = 0.049/12):
    rate_serials = [period_rate*(1-0.20), period_rate*(1-0.15), period_rate*(1-0.1), period_rate*(1-0.05), period_rate, period_rate*(1+0.05), period_rate*(1+0.1), period_rate*(1+0.15), period_rate*(1+0.20)]
    AC_interest_list = []
    ACPI_interest_list = []

    for rate in rate_serials:
        print ("贷款年利率：" + str(rate*12) + "月利率：" + str(rate))
        # 等额本金，average capital = AC
        AC_loan = loan.MortgageLoan(capital, rate, periods, 1)
        AC_payment_per_month_list = AC_loan.get_month_payment_list()
        AC_interest_per_month_list = AC_loan.get_month_interest_list()
        AC_capital_per_month_list = AC_loan.get_month_capital_list()
        AC_interest_list.append(sum(AC_interest_per_month_list))

        print("  AC总的利息：" + str(sum(AC_interest_per_month_list)))
        print("  AC本息合计：" + str(sum(AC_payment_per_month_list)))
        print("  AC月均还款：" + str(AC_loan.get_average_month_payment()))
        print("  AC贷款现值：" + str(capbuget.pv(AC_payment_per_month_list, discount_rate)))
        print("\n")

        # 等额本息，average capital plus interest = ACPI
        ACPI_loan = loan.MortgageLoan(capital, rate, periods, 2)
        ACPI_payment_per_month_list = ACPI_loan.get_month_payment_list()
        ACPI_interest_per_month_list = ACPI_loan.get_month_interest_list()
        ACPI_capital_per_month_list = ACPI_loan.get_month_capital_list()
        ACPI_interest_list.append(sum(ACPI_interest_per_month_list))

        print("  ACPI总的利息：" + str(sum(ACPI_interest_per_month_list)))
        print("  ACPI本息合计：" + str(sum(ACPI_payment_per_month_list)))
        print("  ACPI月均还款：" + str(ACPI_loan.get_average_month_payment()))
        print("  ACPI贷款现值：" + str(capbuget.pv(ACPI_payment_per_month_list, discount_rate)))
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
    plt.show()

def plot_diff_under_floatrate(capital, period_rate, periods):
    AC_loan = loan.MortgageLoan(capital, period_rate, periods, 1)
    AC_payment_per_month_list = AC_loan.get_month_payment_list()
    AC_payment_under_diff_floatrate_list = []

    ACPI_loan = loan.MortgageLoan(capital, period_rate, periods, 2)
    ACPI_payment_per_month_list = ACPI_loan.get_month_payment_list()
    ACPI_payment_under_diff_floatrate_list = []

    # 适用浮动利率进行折现
    rate_serials = [period_rate*(1-0.15), period_rate*(1-0.1), period_rate*(1-0.05), period_rate, period_rate*(1+0.05), period_rate*(1+0.1), period_rate*(1+0.15)]
    for discount_rate in rate_serials:
        print ("贷款年利率：" + str(period_rate*12) + "折现年利率：" + str(discount_rate*12))
        pv = capbuget.pv(AC_payment_per_month_list, discount_rate)
        print("  AC贷款现值：" + str(pv))
        AC_payment_under_diff_floatrate_list.append(pv)

        pv = capbuget.pv(ACPI_payment_per_month_list, discount_rate)
        print("  ACPI贷款现值：" + str(capbuget.pv(ACPI_payment_per_month_list, discount_rate)))
        ACPI_payment_under_diff_floatrate_list.append(pv)


capital = 1000000
year_periods = 30
year_rate = 0.049

periods = year_periods * 12
period_rate = year_rate / 12

plot_diff_under_baserate(capital, period_rate, periods)
#plot_diff_under_floatrate(capital, period_rate, periods)
