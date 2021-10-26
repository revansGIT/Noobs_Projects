class Product():
	def __init__(self,p_id,name,price,quantity):
		self.id = p_id
		self.name = name
		self.price = price
		self.quantity = quantity

	def updatePrice(self,new_orice):
		if new_price > 0:
			self.price = new_orice
		else:
			print("Error! Cannot update price to lower than or equal to zero")

	def updateQuantity(self,new_quantity,is_incriment):
		if is_incriment is True:
			self.quantity += new_quantity
		elif (self.quantity - new_quantity) >= 0:
			self.quantity -= new_quantity
		else:
			print("Error! cannot reduce further!")

	def getQuantity(self):
		print("Quantity of "+self.name, "is:", self.quantity)

	def viewProduct(self):
		print("\n#############"+"\nProduct ID: "+str(self.id)+"\nName: "+self.name+"\nPrice: "+str(self.price)+"\nQuantity: "+str(self.quantity)+"\n#############")

class Inventory:
	def __init__(self):
		self.list_product = []
	
	def add_product(self,p_id):
		self.list_product.append(p_id)

	def remove_product(self,p_id):
		if p_id in self.list_product:
			self.list_product.remove(p_id)
		else:
			print("Error! Product is not in the cart/inventory")

	def viewInventory(self):
		print("Total item in cart/inventory:",self.list_product)



p1 = Product(1, "Water", '12tk', 1)
p2 = Product(2, "Bread", '30tk', 1)
print(p1.getQuantity())
print(p2.getQuantity())
p1.updateQuantity(2,True)
p1.viewProduct()
p2.viewProduct()

inv = Inventory()
inv.add_product(1)
inv.add_product(2)
inv.viewInventory()
inv.remove_product(2)
inv.viewInventory()