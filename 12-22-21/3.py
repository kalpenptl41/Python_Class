def square(x):
	return x*x

def cube(x):
	return x*x*x

def my_func(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

print(my_func(square, [1,2,3]))
print(my_func(cube, [1,2,3]))