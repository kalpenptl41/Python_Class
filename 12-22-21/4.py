def outer_func():
	message = "Good morning"

	def inner_func():
		return message

	return inner_func
	
new_var = outer_func()
print(new_var())