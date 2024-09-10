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

    def __init__(self, color, maker, model,year, price, engin_type):
        self.color=color
        self.maker=maker
        self.model=model
        self.year=year
        self.price=price
        self.engin_type=engin_type

        def detail(self):
            pass

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

    







# Maimunat just joined..😊✌️

# toluwanimi just joined

# pelumi just joind

# Israel just joined


    def reverse(self):
        self.gear = 'reverse'
        self.brake = 'engaged'
        self.clutch = 'engaged'

        if self.brake == 'engaged':
            if self.clutch == 'engaged' and self.gear == 'reverse':
                self.accelerator = 'engaged'
                print ('car is in reverse')
