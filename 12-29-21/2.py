class Emp:
	
	Increment_Amt = 1.05
	Num_of_emp = 0

	def __init__(self, ID, First, Last, Age, Pay):
		self.ID = ID
		self.First = First
		self.Last = Last
		self.Age = Age
		self.Pay = Pay
		self.Email = First + "." + Last + "@company.com"

		Emp.Num_of_emp += 1

	def Fullname(self):
		return f"{self.First} {self.Last}"

	def Increment(self):
		self.Pay = self.Pay * self.Increment_Amt

	def set_raise_amt(amount):
		Emp.Increment_Amt = amount

Emp_1 = Emp(1, "John", "Day", 28, 60000)

print(Emp_1.Pay)
print(Emp.Num_of_emp)