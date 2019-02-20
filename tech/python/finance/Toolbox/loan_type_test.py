import numpy as np
import matplotlib.pyplot as plt
import capbuget
import loan

plt.rcParams['font.family']=['FangSong']

plt.xlabel('投资收益率 [%]')
plt.ylabel('金额 [元]')
plt.title('等额本息在不同房贷利率[3.0%-7.0%]、不同投资收益率[3.0%-9.0%]下相对等额本金的对比')

for r in range(30,71):
    year_rate = r / 1000.0
    year_rate_label = str(year_rate*100) + "%"
    #loan = Loan(1000000, year_rate, 30)
    #loan_diff_list = loan.get_diff()

    AC_loan = loan.MortgageLoan(1000000, year_rate, 30, 1)
    ACPI_loan = loan.MortgageLoan(1000000, year_rate, 30, 2)
    loan_diff_list =  np.array(AC_loan.get_month_payment_list()) - np.array(ACPI_loan.get_month_payment_list())

    discount_year_rate_list = [r/10.0 for r in range(30, 91)]
    discount_month_rate_list = [r/12000.0 for r in range(30, 91)]

    NPV_list = [capbuget.npv(loan_diff_list, v) for v in discount_month_rate_list]

    plt.plot(discount_year_rate_list, NPV_list, color="blue", linestyle="-", label=year_rate_label)
    #plt.legend(loc='best')

plt.show()
