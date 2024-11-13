customer_credit = input("if bad credit input 'true' else input 'false': ").strip().lower()

good_credit = ['false']
bad_credit = ['true']

house_price = 1000000

#good_credit = False
#bad_credit = False

if customer_credit in good_credit:
    print("Put down 10%")

elif customer_credit in bad_credit:
    print("Put down 20%")

else:
    print("Nothing for you!")