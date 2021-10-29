class Converter:
	def __init__(self,c=0,f=0,k=0):
		self.c = c
		self.f = f
		self.k = k

	def CeltoFar(self):
		self.f = (self.c * (9/5)) + 32
		if self.f <= -22:
			print (self.f, 'degree F, Very cold if you are outside in this temperature, unbearable to most')
		elif self.f < 32:
			print(self.f, 'degree F, Very cold still but bearable if in lots of warm clothes')
		elif self.f >= 32 and self.f < 39.2:
			print(self.f, 'degree F, Cold! Typical coldest average temperature for UK in winter')
		elif self.f >= 39.2 and self.f < 50:
			print(self.f, 'degree F, Cold! Water has its smallest volume at this temperature')
		elif self.f >= 50 and self.f < 77:
			print(self.f, 'degree F, Cold to Warm!')
		elif self.f >= 77 and self.f < 86:
			print(self.f, 'degree F, Warm to Hot! Typical maximum temperature for British summer')
		elif self.f >= 86 and self.f < 98.6:
			print(self.f, 'degree F, Feeling hot! Typical temperature for hotter countries')
		elif self.f >= 98.6 and self.f < 122:
			print(self.f, 'degree F, Very hot! If you are outside in this temperature you will feel hot, but more so if humidity is high. If your internal body temperature reaches this level you are in danger of death')
		elif self.f >= 122 and self.f < 140:
			print(self.f, 'degree F, Extremely hot! Not many places get this high in temperature, and this heat you would need to find shade, drink water and stay cool.')
		elif self.f >= 140 and self.f < 194:
			print(self.f, 'degree F, Too hot to live in! Most bacteria die at this temperature')
		else:
			print(self.f, 'degree F, Too hot to live in! Humans cannot survive such high temperatures')

	def FartoCel(self):
		self.c = (self.f - 32) * 5/9
		if self.c <= -30:
			print (self.c, 'degree C, Very cold if you are outside in this temperature, unbearable to most')
		elif self.c < 0:
			print(self.c, 'degree C, Very cold still but bearable if in lots of warm clothes')
		elif self.c >= 0 and self.c < 4:
			print(self.c, 'degree C, Cold! Typical coldest average temperature for UK in winter')
		elif self.c >= 4 and self.c < 10:
			print(self.c, 'degree C, Cold! Water has its smallest volume at this temperature')
		elif self.c >= 10 and self.c < 25:
			print(self.c, 'degree C, Cold to Warm!')
		elif self.c >= 25 and self.c < 30:
			print(self.c, 'degree C, Warm to Hot! Typical maximum temperature for British summer')
		elif self.c >= 30 and self.c < 37:
			print(self.c, 'degree C, Feeling hot! Typical temperature for hotter countries')
		elif self.c >= 37 and self.c < 50:
			print(self.c, 'degree C, Very hot! If you are outside in this temperature you will feel hot, but more so if humidity is high. If your internal body temperature reaches this level you are in danger of death')
		elif self.c >= 50 and self.c < 60:
			print(self.c, 'degree C, Extremely hot! Not many places get this high in temperature, and this heat you would need to find shade, drink water and stay cool.')
		elif self.c >= 60 and self.c < 90:
			print(self.c, 'degree C, Too hot to live in! Most bacteria die at this temperature')
		else:
			print(self.c, 'degree C, Too hot to live in! Humans cannot survive such high temperatures')

	def CeltoKel(self):
		self.k = self.c + 273.15
		if self.k <= 243.15:
			print (self.k, 'K, Very cold if you are outside in this temperature, unbearable to most')
		elif self.k < 273.15:
			print(self.k, 'K, Very cold still but bearable if in lots of warm clothes')
		elif self.k >= 273.15 and self.k < 277.15:
			print(self.k, 'K, Cold! Typical coldest average temperature for UK in winter')
		elif self.k >= 277.15 and self.k < 283.15:
			print(self.k, 'K, Cold! Water has its smallest volume at this temperature')
		elif self.k >= 283.15 and self.k < 298.15:
			print(self.k, 'K, Cold to Warm!')
		elif self.k >= 298.15 and self.k < 303.15:
			print(self.k, 'K, Warm to Hot! Typical maximum temperature for British summer')
		elif self.k >= 303.15 and self.k < 310.15:
			print(self.k, 'K, Feeling hot! Typical temperature for hotter countries')
		elif self.k >= 310.15 and self.k < 323.15:
			print(self.k, 'K, Very hot! If you are outside in this temperature you will feel hot, but more so if humidity is high. If your internal body temperature reaches this level you are in danger of death')
		elif self.k >= 323.15 and self.k < 333.15:
			print(self.k, 'K, Extremely hot! Not many places get this high in temperature, and this heat you would need to find shade, drink water and stay cool.')
		elif self.k >= 333.15 and self.k < 363.15:
			print(self.k, 'K, Too hot to live in! Most bacteria die at this temperature')
		else:
			print(self.k, 'K, Too hot to live in! Humans cannot survive such high temperatures')

	def FartoKel(self):
		self.k = (self.f - 32) * 5/9 + 273.15
		if self.k <= 243.15:
			print (self.k, 'K, Very cold if you are outside in this temperature, unbearable to most')
		elif self.k < 273.15:
			print(self.k, 'K, Very cold still but bearable if in lots of warm clothes')
		elif self.k >= 273.15 and self.k < 277.15:
			print(self.k, 'K, Cold! Typical coldest average temperature for UK in winter')
		elif self.k >= 277.15 and self.k < 283.15:
			print(self.k, 'K, Cold! Water has its smallest volume at this temperature')
		elif self.k >= 283.15 and self.k < 298.15:
			print(self.k, 'K, Cold to Warm!')
		elif self.k >= 298.15 and self.k < 303.15:
			print(self.k, 'K, Warm to Hot! Typical maximum temperature for British summer')
		elif self.k >= 303.15 and self.k < 310.15:
			print(self.k, 'K, Feeling hot! Typical temperature for hotter countries')
		elif self.k >= 310.15 and self.k < 323.15:
			print(self.k, 'K, Very hot! If you are outside in this temperature you will feel hot, but more so if humidity is high. If your internal body temperature reaches this level you are in danger of death')
		elif self.k >= 323.15 and self.k < 333.15:
			print(self.k, 'K, Extremely hot! Not many places get this high in temperature, and this heat you would need to find shade, drink water and stay cool.')
		elif self.k >= 333.15 and self.k < 363.15:
			print(self.k, 'K, Too hot to live in! Most bacteria die at this temperature')
		else:
			print(self.k, 'K, Too hot to live in! Humans cannot survive such high temperatures')

	def KeltoCel(self):
		self.c = self.k - 273.15
		if self.c <= -30:
			print (self.c, 'degree C, Very cold if you are outside in this temperature, unbearable to most')
		elif self.c < 0:
			print(self.c, 'degree C, Very cold still but bearable if in lots of warm clothes')
		elif self.c >= 0 and self.c < 4:
			print(self.c, 'degree C, Cold! Typical coldest average temperature for UK in winter')
		elif self.c >= 4 and self.c < 10:
			print(self.c, 'degree C, Cold! Water has its smallest volume at this temperature')
		elif self.c >= 10 and self.c < 25:
			print(self.c, 'degree C, Cold to Warm!')
		elif self.c >= 25 and self.c < 30:
			print(self.c, 'degree C, Warm to Hot! Typical maximum temperature for British summer')
		elif self.c >= 30 and self.c < 37:
			print(self.c, 'degree C, Feeling hot! Typical temperature for hotter countries')
		elif self.c >= 37 and self.c < 50:
			print(self.c, 'degree C, Very hot! If you are outside in this temperature you will feel hot, but more so if humidity is high. If your internal body temperature reaches this level you are in danger of death')
		elif self.c >= 50 and self.c < 60:
			print(self.c, 'degree C, Extremely hot! Not many places get this high in temperature, and this heat you would need to find shade, drink water and stay cool.')
		elif self.c >= 60 and self.c < 90:
			print(self.c, 'degree C, Too hot to live in! Most bacteria die at this temperature')
		else:
			print(self.c, 'degree C, Too hot to live in! Humans cannot survive such high temperatures')

	def KeltoFar(self):
		self.f = (self.k - 273.15) * 9/5 + 32
		if self.f <= -22:
			print (self.f, 'degree F, Very cold if you are outside in this temperature, unbearable to most')
		elif self.f < 32:
			print(self.f, 'degree F, Very cold still but bearable if in lots of warm clothes')
		elif self.f >= 32 and self.f < 39.2:
			print(self.f, 'degree F, Cold! Typical coldest average temperature for UK in winter')
		elif self.f >= 39.2 and self.f < 50:
			print(self.f, 'degree F, Cold! Water has its smallest volume at this temperature')
		elif self.f >= 50 and self.f < 77:
			print(self.f, 'degree F, Cold to Warm!')
		elif self.f >= 77 and self.f < 86:
			print(self.f, 'degree F, Warm to Hot! Typical maximum temperature for British summer')
		elif self.f >= 86 and self.f < 98.6:
			print(self.f, 'degree F, Feeling hot! Typical temperature for hotter countries')
		elif self.f >= 98.6 and self.f < 122:
			print(self.f, 'degree F, Very hot! If you are outside in this temperature you will feel hot, but more so if humidity is high. If your internal body temperature reaches this level you are in danger of death')
		elif self.f >= 122 and self.f < 140:
			print(self.f, 'degree F, Extremely hot! Not many places get this high in temperature, and this heat you would need to find shade, drink water and stay cool.')
		elif self.f >= 140 and self.f < 194:
			print(self.f, 'degree F, Too hot to live in! Most bacteria die at this temperature')
		else:
			print(self.f, 'degree F, Too hot to live in! Humans cannot survive such high temperatures')

cft = Converter(-30)
cft.CeltoFar()

fct = Converter(0,32)
fct.FartoCel()

ckt = Converter(80)
ckt.CeltoKel()

fkt = Converter(0,300)
fkt.FartoKel()

kct = Converter(0,0,250)
kct.KeltoCel()

kft = Converter(0,0,77)
kft.KeltoFar()
