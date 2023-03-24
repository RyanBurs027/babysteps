house_price = 1000000
good_credit = False
down_pay1 = (10 / 100 ) * house_price
down_pay2 = (20 / 100 ) * house_price
print("Price of a house is $1M.")
if good_credit:
    print("they need to put down " f'{down_pay1}')
else:
    print("they need to put down " f'{down_pay2}')


if good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f"Down payment should be: ${down_payment}")