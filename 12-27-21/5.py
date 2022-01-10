class Emp:
	
	Increment_Amt = 1.05

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
		self.Pay = self.Pay * self.Increment_Amt

Emp_1 = Emp(1, "John", "Day", 28, 60000)

print(Emp_1.Pay)
Emp_1.Increment()
print(Emp_1.Pay)
print(int(Emp_1.Pay))