from math import pi
from math import pow

PI = pi
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    #returns volume of cylinder assuming cm
    def volumeOfCylinder(self):
        #V = PI*(r^2)*h
        rSquared = pow(self.radius, 2)
        volume = (PI)*(rSquared)*(self.height)
        return volume

    #returns volume of cylinder in kg assuming cm
    def weightOfCylinder(self):
        #Convert volume in cm^3 to dm^3
        #1 dm^3 = 1L = 1kg
        RATIO_CM3_DM3 = 1/1000
        volume = self.volumeOfCylinder()
        weight = volume * RATIO_CM3_DM3
        return weight