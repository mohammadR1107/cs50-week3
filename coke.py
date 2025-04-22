amount_due=50
while amount_due>0:
    print(f"amount due: {amount_due}")
    pyment=int(input('insert coin: '))
    if pyment in [25,10,5]:
        amount_due-=pyment
    else:
        continue
print(f"change owed: {abs(amount_due)}")
