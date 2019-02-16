import numpy as np
import matplotlib.pyplot as plt
import capital

plt.rcParams['font.family']=['FangSong']

class Loan(object):
    def __init__(self, capital, year_rate, year_periods):
        self.__capital = capital
        self.__year_rate = year_rate
        self.__year_periods = year_periods
        self.__month_rate = year_rate / 12
        self.__periods = year_periods * 12
        self.periods_list = [k for k in range(1, self.__periods+1)]

        # 等额本金，average capital = AC
        self.AC_capital_per_month = capital / self.__periods
        self.AC_capital_per_month_list = [self.AC_capital_per_month] * self.__periods
        self.AC_interest_per_month_list = []
        self.AC_payment_per_month_list = []

        # 等额本息，average capital plus interest = ACPI
        self.ACPI_payment_per_month = (capital * self.__month_rate * ((1 + self.__month_rate)**self.__periods)) / ((1 + self.__month_rate)**self.__periods - 1)
        self.ACPI_payment_per_month_list = [self.ACPI_payment_per_month] * self.__periods
        self.ACPI_interest_per_month_list = []
        self.ACPI_capital_per_month_list = []
        self.ACPI_paid_capital = 0.0

    def display(self):
        print (str(self))

    def __str__(self):
        return ("Loan(capital=%d, year_rate=%f, year_periods=%d)" % (self.__capital, self.__year_rate, self.__year_periods))

    def calc(self):
        for k in range(30*12):
            AC_interest = (self.__capital - k*self.AC_capital_per_month) * self.__month_rate
            self.AC_interest_per_month_list.append(AC_interest)
            self.AC_payment_per_month_list.append(self.AC_capital_per_month + AC_interest)

            ACPI_interest = (self.__capital - self.ACPI_paid_capital) * self.__month_rate
            ACPI_capital = self.ACPI_payment_per_month - ACPI_interest
            self.ACPI_interest_per_month_list.append(ACPI_interest)
            self.ACPI_capital_per_month_list.append(ACPI_capital)
            self.ACPI_paid_capital += (ACPI_capital)

    def get_diff(self):
        # 计算两种还款方式的差异
        self.calc()
        NP_AC_payment_per_month_list = np.array(self.AC_payment_per_month_list)
        NP_ACPI_payment_per_month_list = np.array(self.ACPI_payment_per_month_list)
        NP_payment_diff_per_month = NP_AC_payment_per_month_list - NP_ACPI_payment_per_month_list

        return NP_payment_diff_per_month.tolist()

loan = Loan(1000000, 0.049, 30)
loan_diff_list = loan.get_diff()

discount_year_rate_list = [r/1000.0 for r in range(30, 91)]
discount_month_rate_list = [r/12000.0 for r in range(30, 91)]

#print("折现率：\n")
#print(discount_month_rate_list)
#print("差异值：\n")
#print(loan_diff_list)
#print(capital.npv(loan_diff_list, 0.03/12))

NPV_list = [capital.npv(loan_diff_list, v) for v in discount_month_rate_list]

plt.plot(discount_year_rate_list, NPV_list, color="blue", linestyle="-", label="假定折现率")
plt.legend(loc='upper center', frameon=False)
plt.xlabel('百分比 [%]')
plt.ylabel('金额 [元]')
plt.title('房贷利率4.9%下不同还款方式对比')
plt.show()
