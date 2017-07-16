import csv
class Bill:
	def check_product(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			a=0
			for row in reader:
				if(row['Product']==product):
					a=1
					break
			if a==1:
				return True
			else:
				print("Item not found")
				return False
	def check_quantity(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			a=0
			for row in reader:
				if(row['Product']==product):
					z=row['Quantity']
					a=1
					break
			if a==1:
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
					break
	def red_quantity(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.reader(csvfile)
			lines=[l for l in reader]
			for i in lines:
				if(i[0]==product):
					z=i[2]
					z=int(z)-1
					i[2]=z
					break
		with open('supermarket.csv','w') as csvfile:
			writer=csv.writer(csvfile)
			writer.writerows(lines)
	def buy(self,product):
		b=self.check_product(product)
		if b==True:
			a=self.check_quantity(product)
			if(a==True):
				k=self.ret_price(product)
				self.red_quantity(product)
				return int(k)
