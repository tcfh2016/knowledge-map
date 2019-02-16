###############################################
# 贷款本金： 100 0000
# 名义年利率： 4.9%
# 贷款期限：30年（360个月）
###############################################
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family']=['FangSong']

capital = 1000000.0
year_rate = 0.049
month_rate = year_rate / 12
periods = 30 * 12
periods_list = [k for k in range(1, 30*12+1)]

# 等额本金，average capital = AC
AC_capital_per_month = capital / periods
AC_capital_per_month_list = [AC_capital_per_month] * periods
AC_interest_per_month_list = []
AC_payment_per_month_list = []

# 等额本息，average capital plus interest = ACPI
# 等额本息
ACPI_payment_per_month = (capital * month_rate * ((1 + month_rate)**periods)) / ((1 + month_rate)**periods - 1)
ACPI_payment_per_month_list = [ACPI_payment_per_month] * periods
ACPI_interest_per_month_list = []
ACPI_capital_per_month_list = []
ACPI_paid_capital = 0.0

for k in range(30*12):
    AC_interest = (capital - k*AC_capital_per_month) * month_rate
    AC_interest_per_month_list.append(AC_interest)
    AC_payment_per_month_list.append(AC_capital_per_month + AC_interest)

    #print(str(past_months_number) + " " + str(capital_per_month) + " " + str(interest) + " " + str(total_payment) + "\n")
    ACPI_interest = (capital - ACPI_paid_capital) * month_rate
    ACPI_capital = ACPI_payment_per_month - ACPI_interest
    ACPI_interest_per_month_list.append(ACPI_interest)
    ACPI_capital_per_month_list.append(ACPI_capital)
    ACPI_paid_capital += (ACPI_capital)

# 计算两种还款方式的差异
NP_AC_payment_per_month_list = np.array(AC_payment_per_month_list)
NP_ACPI_payment_per_month_list = np.array(ACPI_payment_per_month_list)
NP_payment_diff_per_month = NP_AC_payment_per_month_list - NP_ACPI_payment_per_month_list


print("NPV：" + str(NPV(NP_payment_diff_per_month, month_rate)))

print("[等额本金] 总的利息：" + str(sum(AC_interest_per_month_list)))
print("[等额本金] 本息合计：" + str(sum(AC_payment_per_month_list)))
print("[等额本金] 月均还款：" + str(np.mean(AC_payment_per_month_list)))

print("[等额本息] 总的利息：" + str(sum(ACPI_interest_per_month_list)))
print("[等额本息] 本息合计：" + str(sum(ACPI_payment_per_month_list)))
print("[等额本息] 月均还款：" + str(ACPI_payment_per_month))

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

#print(periods_list)
#print(interest_per_month_list)
#print(capital_per_month_list)
#print(total_payment_per_month_list)

# 等额本息
