print("welcome to collaboration class")

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
method: ignition(maimunat)
"""
class Cars():
    tyre=4
    engine=1
    bonnet=1
    brake=1
    accelerator=1
    def __init__(self, color, make, model,year, price, engin_type):
        self.color=color
        self.maker=make
        self.model=model
        self.year=year
        self.price=price
        self.engin_type=engin_type

# asgodwants just joined