class MyClass:
    # Class attribute
    class_variable = "I am a class variable"
    
    def __init__(self, instance_variable):
        # Instance attribute
        self.instance_variable = instance_variable
    
    def greet(self):
        print(f"Hello! My instance variable is {self.instance_variable}")

# Creating an instance of MyClass   
my_object = MyClass("I am an instance variable")

# Accessing class and instance attributes
print(MyClass.class_variable)  # Output: I am a class variable
print(my_object.instance_variable)  # Output: I am an instance variable


# Creating an object (instance) of MyClass
obj = MyClass("instance value")
obj.greet()  # Output: Hello! My instance variable is instance value
