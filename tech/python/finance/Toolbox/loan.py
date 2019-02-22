import numpy as np

class PaymentMethod():
    AC   = 1 # average capital
    ACPI = 2 # average capital plus interest

class MortgageLoan(object):
    def __init__(self, capital, period_rate, periods, payment_method):
        self._capital = capital
        self._period_rate = period_rate
        self._periods = periods
        self._periods_list = [k for k in range(1, self._periods + 1)]
        self._payment_method = payment_method

        self.AC_capital_per_month_list = [self._capital / self._periods] * self._periods
        self.AC_interest_per_month_list = []
        self.AC_payment_per_month_list = []

        self.ACPI_payment_per_month = (self._capital * self._period_rate * ((1 + self._period_rate)**self._periods)) / ((1 + self._period_rate)**self._periods - 1)
        self.ACPI_payment_per_month_list = [self.ACPI_payment_per_month] * self._periods
        self.ACPI_capital_per_month_list = []
        self.ACPI_interest_per_month_list = []

        AC_capital_per_month = self._capital / self._periods
        ACPI_paid_capital = 0

        for k in range(self._periods):
            AC_interest = (self._capital - k * AC_capital_per_month) * self._period_rate
            self.AC_interest_per_month_list.append(AC_interest)
            self.AC_payment_per_month_list.append(AC_capital_per_month + AC_interest)

            ACPI_interest = (self._capital - ACPI_paid_capital) * self._period_rate
            ACPI_capital = self.ACPI_payment_per_month - ACPI_interest
            self.ACPI_interest_per_month_list.append(ACPI_interest)
            self.ACPI_capital_per_month_list.append(ACPI_capital)
            ACPI_paid_capital += (ACPI_capital)


    def display(self):
        print (str(self))

    def __str__(self):
        return ("MortgageLoan(capital=%d, year_rate=%f, periods=%d)" % (self.__capital, self.__year_rate, self._periods))

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
