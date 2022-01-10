class Emp:
	def __init__(self, ID, First, Last, Age, Pay):
		self.ID = ID
		self.First = First
		self.Last = Last
		self.Age = Age
		self.Pay = Pay
		self.Email = First + "." + Last + "@company.com"

Emp_1 = Emp(1, "John", "Day", 38, 60000)
Emp_2 = Emp(2, "Richie", "Rich", 33, 80000)
Emp_3 = Emp(3, "Jigs", "Patel", 38, 100000)

print(Emp_1.First)
print(Emp_2.Email)
print(f"{Emp_3.First} {Emp_3.Last}")