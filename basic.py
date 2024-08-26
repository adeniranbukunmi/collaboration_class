print("Welcome to collaboration class")

def square(x):
    return x **5
print(square(4))

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
    def __init__(self, payment, details, routine, landing_page, ignition, park, reverse, neutral, drive, drift):
        self.payment=payment
        self.details=details
        self.routine=routine
        self.landing_page=landing_page
        self.ignition=ignition
        self.park=park
        self.reverse=reverse
        self.neutral=neutral
        self.drive=drive
        self.drift=drift

    



# ayodele just join 


# asgodwants just joined


# maimunat just joined..😊✌️

# toluwanimi just joined

# pelumi just joind

# israel just joined

# dave just joined
# it's the end of the month

import time

class Cars:
    def __init__(self):
        pass
    def ignition(self):
        print("Insert the key into the ignition/Press the ignition buttton")
        user = input('').capitalize().lower().strip()
        if user == 'start':
            print("Starting the engine...")
            time.sleep(4) 
            engine_status = "running..."
            if engine_status == "running...":
                print("The engine has started successfully!")
            time.sleep(2)
            print("The car is now ready to drive. Have a safe journey!")

        else: 
            print("Car failed to start!!!") 
mycar = Cars()
mycar.ignition()
  



