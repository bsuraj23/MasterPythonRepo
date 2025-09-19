#Class Methods in Python
#A class method is a method that is bound to the class and not the instance of the class.
# It can modify a class state that applies across all instances of the class.   
class Sample:
    def __init__(self, color):
        self.color = color  # This car’s color

    # Class method to change the color of the car
    @classmethod
    def change_color(cls, car_instance, new_color):
        car_instance.color = new_color  
        return f"Car color changed to {car_instance.color}"

print(Sample.change_color(my_car, "blue"))  # Change color to blue...see class name was used to call the method    
print(my_car.color)  # Now my_car is blue!      
#Here, change_color is a class method that changes the color of a car instance.