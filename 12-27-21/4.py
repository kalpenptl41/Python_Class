class Emp:
	def __init__(self, ID, First, Last, Age, Pay):
		self.ID = ID
		self.First = First
		self.Last = Last
		self.Age = Age
		self.Pay = Pay
		self.Email = First + "." + Last + "@company.com"

	def Fullname(self):
		return f"{self.First} {self.Last}"

	def Increment(self):
		self.Pay = self.Pay * 1.05

Emp_1 = Emp(1, "John", "Day", 28, 60000)
Emp_2 = Emp(2, "Richie", "Rich", 33, 80000)
Emp_3 = Emp(3, "Jigs", "Patel", 38, 100000)
Emp_4 = Emp(4, "Deep", "Pal", 36, 20000)

print(Emp_1.First)
print(Emp_2.Email)
print(Emp_3.Fullname())
print(Emp.Fullname(Emp_4))

print(Emp_3.Pay)
Emp_3.Increment()
print(Emp_3.Pay)
print(int(Emp_3.Pay))