import csv
class Product:	
	def add(self):
		with open('supermarket.csv','a+') as csvfile:
			writer=csv.writer(csvfile)
			x=raw_input("Enter the product:")
			y=raw_input("Enter the price:")
			z=raw_input("Enter the quantity:")
			reader=csv.reader(csvfile)
			fields=[l for l in reader]
			for i in fields:
				k=i[3]
			k=int(k)+1
			lines=[x,y,z,k]
			writer.writerow(lines)
	def update_price(self,product,new_price):
		with open('supermarket.csv') as csvfile:
			reader=csv.reader(csvfile)
			lines=[l for l in reader]
			for i in lines:
				for j in i:
					if(j==product):
						i[1]=new_price
		with open('supermarket.csv','w') as csvfile:
			writer=csv.writer(csvfile)
			writer.writerows(lines)
	def update_quantity(self,product,new_quantity):
		with open('supermarket.csv') as csvfile:
			reader=csv.reader(csvfile)
			lines=[l for l in reader]
			for i in lines:
				for j in i:
					if(j==product):
						i[2]=new_quantity
		with open('supermarket.csv','w') as csvfile:
			writer=csv.writer(csvfile)
			writer.writerows(lines)
	def display(self):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				print(row['Product'])
	def search(self,product):
		with open('supermarket.csv') as csvfile:
			reader=csv.DictReader(csvfile)
			a=0
			for row in reader:
				if(row['Product']==product):
					a=1
					print(row)
					break
			if(a!=1):
				print("Item not found")
	def delete(self,key):
		with open('supermarket.csv') as inp:
			reader=csv.reader(inp)
			a=0
			lines=[l for l in reader]
			for i in lines:
				a=a+1
				if i[3]==key:
					del lines[a-1:a]
					break
		with open('supermarket.csv','w') as out:
			writer=csv.writer(out)
			writer.writerows(lines)
			
			
	
