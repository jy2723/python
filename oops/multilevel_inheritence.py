

class Class1:
	def m(self):
		print("In Class1") 
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")
  	
class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		Class2.m(self)
		Class3.m(self)
		Class1.m(self)

obj = Class4()
obj.m()
obj1 = Class3()
obj1.m()