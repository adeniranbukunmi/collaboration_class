import time

print("welcome to collaboration class")

# def square(x):
#     return x **5
# print(square(4))



"""
working on object car
types
method: details(bukunmi)
method: drive(pelumi)
method: drift(boluwatife)
method: park(ayodele)
method: reverse(toluwanimi)
method: payment(maimunat)
method: landing page(Israel)
method: ignition(david)
method: neutral (Emmanuel)

"""
class Cars():
    tyre=4
    engine=1
    bonnet=1
    brake=1
    accelerator=1

    # def __init__(self, color, maker, model,year, price, engin_type):
    #     self.color=color
    #     self.maker=maker
    #     self.model=model
    #     self.year=year
    #     self.price=price
    #     self.engin_type=engin_type

    #     def detail(self):
    #         pass

    # def __init__(self, payment, details, routine, landing_page, ignition, park, reverse, neutral, drive, drift):
    #     self.payment=payment
    #     self.details=details
    #     self.routine=routine
    #     self.landing_page=landing_page
    #     self.ignition=ignition
    #     self.park=park
    #     self.reverse=reverse
    #     self.neutral=neutral
    #     self.drive=drive
    #     self.drift=drift


    def __init__(self):

        self.welcome()

        

    def welcome(self):
        print(f"Welcome to your brand new car")
        print()
        self.ignition_method()


    def ignition_method(self):
        self.ignition = input("Enter start to turn on the car engine: ")
        
        if self.ignition == "start":
            print("Welcome to your new car, the car engine is starting now")
            print()
            self.landing_page()
        else:
            print("You need to press ignition button to start the car") 
            self.ignition_method()

    def landing_page(self):
        car_gears=("Park", "Reverse", "Neutral", "Drive", "Drift")
        for each in car_gears:
            print(each)
        print()
        self.neutral_method()
    
    def neutral_method(self):
        self.neutral = input("Select neutral: ")
        
        if self.neutral =="neutral":
            print("The car is in neutral, please step on the brake")
            self.drive_method()
        else:
            print("This is not neutral")
            self.neutral_method()


    def drive_method(self):
        self.drive = input("Select drive to move the car forward: ")
        
        if self.drive == "drive":
            print("The car is moving forward")
            self.park_method()
        else:
            print("This is not drive")
            self.drive_method()   
    
    def park_method(self):
        self.park = input("Select park to stop the car: ")
        
        if self.park == "park":
            print("Car parked successfully")
            self.reverse_method()
        else:
            print("This is not park")
            self.park_method()
    
        
    def reverse_method(self):
        self.reverse = input("Select reverse: ")
        
        if self.reverse == "reverse":
            print("The car is moving backward")
            self.temporary_park_method()
        else:
            print("This is not reverse")
            self.reverse_method()

    def temporary_park_method(self):
        self.park = input("Select park to stop the car: ")
        
        if self.park == "park":
            print("Car parked successfully")
            self.drift_method()
        else:
            print("This is not park")
            self.temporary_park_method()

        
    def drift_method(self):
        self.drift = input("Select drift mode: ")
        
        if self.drift == "drift":
            print("The car drift mode is successfully activated")
            self.total_park_method()
        else:
            print("This is not drift")
            self.drift_method()

    def total_park_method(self):
        self.total_park = input("Select park: ")

        if self.total_park == "park":
            print("car parked successfully, please turn off your engine")
            print()
            self.ignition_method()
        else:
            print("This is not park")
            self.total_park_method

motocar=Cars()