import class1
import billing
j=billing.Bill()
i=0
y=0
while i<2:
	x=raw_input("Enter the product:")
	y=y+j.buy(x)
print(y)
