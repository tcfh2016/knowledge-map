import numpy as np

class PaymentMethod():
    AC   = 1 # average capital
    ACPI = 2 # average capital plus interest

class MortgageLoan(object):
    def __init__(self, capital, year_rate, year_periods, payment_method):
        self._capital = capital
        self._year_rate = year_rate
        self._year_periods = year_periods
        self._month_rate = year_rate / 12
        self._month_periods = year_periods * 12
        self._month_periods_list = [k for k in range(1, self._month_periods + 1)]
        self._payment_method = payment_method

        self.AC_capital_per_month_list = [self._capital / self._month_periods] * self._month_periods
        self.AC_interest_per_month_list = []
        self.AC_payment_per_month_list = []

        self.ACPI_payment_per_month = (self._capital * self._month_rate * ((1 + self._month_rate)**self._month_periods)) / ((1 + self._month_rate)**self._month_periods - 1)
        self.ACPI_payment_per_month_list = [self.ACPI_payment_per_month] * self._month_periods
        self.ACPI_capital_per_month_list = []
        self.ACPI_interest_per_month_list = []

        AC_capital_per_month = self._capital / self._month_periods
        ACPI_paid_capital = 0

        for k in range(self._month_periods):
            AC_interest = (self._capital - k * AC_capital_per_month) * self._month_rate
            self.AC_interest_per_month_list.append(AC_interest)
            self.AC_payment_per_month_list.append(AC_capital_per_month + AC_interest)

            ACPI_interest = (self._capital - ACPI_paid_capital) * self._month_rate
            ACPI_capital = self.ACPI_payment_per_month - ACPI_interest
            self.ACPI_interest_per_month_list.append(ACPI_interest)
            self.ACPI_capital_per_month_list.append(ACPI_capital)
            ACPI_paid_capital += (ACPI_capital)

    def get_average_month_payment(self):
        if (self._payment_method == PaymentMethod.AC):
            return np.mean(self.AC_payment_per_month_list)
        elif (self._payment_method == PaymentMethod.ACPI):
            return self.ACPI_payment_per_month

    def get_month_payment_list(self):
        if (self._payment_method == PaymentMethod.AC):
            return self.AC_payment_per_month_list
        elif (self._payment_method == PaymentMethod.ACPI):
            return self.ACPI_payment_per_month_list

    def get_month_interest_list(self):
        if (self._payment_method == PaymentMethod.AC):
            return self.AC_interest_per_month_list
        elif (self._payment_method == PaymentMethod.ACPI):
            return self.ACPI_interest_per_month_list

    def get_month_capital_list(self):
        if (self._payment_method == PaymentMethod.AC):
            return self.AC_capital_per_month_list
        elif (self._payment_method == PaymentMethod.ACPI):
            return self.ACPI_capital_per_month_list

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

#print("折现率：\n")
#print(discount_month_rate_list)
#print("差异值：\n")
#print(loan_diff_list)
#print(capital.npv(loan_diff_list, 0.03/12))
