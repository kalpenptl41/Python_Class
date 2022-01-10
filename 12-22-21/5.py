def decorator_func(orig_fun):
	def wrapper_fun():
		return orig_fun()
	return wrapper_fun

def display():
	print("Display ran!")


decorated_disp = decorator_func(display)
decorated_disp()
display()