house_price = 1000000
good_credit = False

if good_credit:
    print('You need to put down 10% downpayment')
    down_pay = house_price * (10/100)
else:
    print('You need to put down 20% downpayment')
    down_pay = house_price * (20/100)
print(f'Down Payment: {down_pay}')
    
    
    