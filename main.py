import class1
import billing
j=class1.Product()
k=billing.Bill()
x=raw_input("Press 1:To alter the stock list 2:To buy:")
if x=='1':
	y=raw_input("Press 1:to add 2:to update price 3:to update quantity 4:display all the products 5:search 6:delete")
	if(y=='1'):
		j.add()
	elif y=='2':
		po=raw_input("Enter the product:")
		pr=raw_input("Enter the new price:")
		j.update_price(po,pr)
	elif y=='3':
		p=raw_input("Enter the product:")
		q=raw_input("Enter the quantity:")
		j.update_quantity(p,q)
	elif y=='4':
		j.display()
	elif y=='5':
		s=raw_input("Enter the product to search:")
		j.search(s)
	else:
		k=raw_input("Enter the key of product to be deleted:")
		j.delete(k)
else:
	op='y'
	i=0
	amt=0
	lines=[]
	line1=[]
	while op!='n':
		pd=raw_input("Enter the product:")
		qn=raw_input("Enter the quantity:")
		if k.buy(pd,qn)!=0:
			lines.append(pd)
			line1.append(qn)
			i=i+1
		amt=amt+(int(qn)*k.buy(pd,qn))
		op=raw_input("Do you want to continue shopping:y or n?")
	if i!=0:
		print("BILL:")
		loop=0
		while loop<i:
			print(lines[loop],line1[loop],k.ret_price(lines[loop]))
			loop=loop+1		
		print("Total:",amt)

		
