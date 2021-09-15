class kettle(object):
	power_source = "electricity"

	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False

	def switch_on(self):
		self.on = True


kenwood = kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.switch_on()
print(kenwood.on)

kenwood.price = 12.75
print(kenwood.price)

hamilton = kettle("Hamilton", 14.55)
print(hamilton.make)
print(hamilton.price)
print("Models: {0.make} = {0.price} , {1.make} = {1.price} ".format(kenwood,hamilton))
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# kettle.switch_on(kenwood)
print(kenwood.on)

print('*'*80)

# print(kenwood.power)
# print(hamilton.power)
print("Switch to atomic power")
kettle.power_source = "atomic power"
print("kenwood to gas")
kenwood.power_source = "gas"
print("hamilton to green energy")
hamilton.power_source = "green energy"
print(kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

