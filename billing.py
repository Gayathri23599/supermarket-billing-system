import csv
class Bill:
	def check_product(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				if(row['Product']==product):
					return True
				else:
					print("Item not found")
					return False
	def check_quantity(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				if(row['Product']==product):
					z=row['Quantity']
					if int(z)!=0:
						return True
					else:
						print("Item out of stock")
						return False
	def ret_price(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				if row['Product']==product:
					return row['Price']
	def red_quantity(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.reader(csvfile)
			lines=[l for l in reader]
			for i in lines:
				if(i[0]==product):
					z=i[2]
					z=int(z)-1
					i[2]=z
		with open('supermarket.csv','w') as csvfile:
			fieldnames=['Product','Price','Quantity','Key']
			writer=csv.writer(csvfile,fieldnames=fieldnames)
			writer.writerows(lines)
	def buy(self,product):
		b=check_product(product)
		if b==True:
			a=check_quantity(product)
			if(a==True):
				k=ret_price(product)
				red_quant()
				return int(k)
