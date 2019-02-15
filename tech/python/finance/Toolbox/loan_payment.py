###############################################
# 贷款本金： 100 0000
# 名义年利率： 4.9%
# 贷款期限：30年（360个月）
###############################################
total_capital = 1000000.0
year_rate = 0.049
rate_per_month = year_rate / 12

# 等额本金
capital_per_month = total_capital / 30 / 12

periods_list = []
capital_permonth_list = []
interest_per_month_list = []
total_payment_per_month_list = []

for k in range(30*12):
    past_months_number = k + 1
    periods_list.append(past_months_number)

    interest = (total_capital - k*capital_per_month)*rate_per_month
    interest_per_month_list.append(interest)

    total_payment = capital_per_month + interest
    total_payment_per_month_list.append(total_payment)

    print(str(past_months_number) + " " + str(capital_per_month) + " " + str(interest) + " " + str(total_payment) + "\n\n")

print("支付的总利息：" + str(sum(interest_per_month_list)))
print("支付的利息和本金：" + str(sum(total_payment_per_month_list)))

#print(periods_list)
#print(interest_per_month_list)
#print(capital_per_month_list)
#print(total_payment_per_month_list)

# 等额本息
