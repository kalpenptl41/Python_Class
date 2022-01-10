class City:
	
	def __init__(self, name, size, county, literacy):
		self.name = name
		self.size = size
		self.county = county
		self.literacy = literacy

Sugarland = City("Sugarland", 100, "Fort Bend", 99)
Houston	=	City("Houston", 200, "Harries", 89)

print(Sugarland)