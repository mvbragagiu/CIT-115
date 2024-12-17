# Mihaela Bragagiu
#November 10 2024
#CIT-115 - Python
#Planetary surface gravity calculator

#Planet surface gravity constants
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

#inputs
sUserName = str(input("What is your name: "))
fUserWeight = float(input("What is your weight: "))

#outputs

print(sUserName + " here are your weights on our Solar System's planets:")
print("Weight on Mercury: ","{:.2f}".format(MERCURY * fUserWeight).center(20))
print("Weight on Venus:   ","{:.2f}".format(VENUS * fUserWeight).center(20))
print("Weight on our Moon:","{:.2f}".format(MOON * fUserWeight).center(20))
print("Weight on Mars:    ","{:.2f}".format(MARS * fUserWeight).center(20))
print("Weight on Jupiter: ","{:.2f}".format(JUPITER * fUserWeight).center(20))
print("Weight on Saturn:  ","{:.2f}".format(SATURN * fUserWeight).center(20))
print("Weight on Uranus:  ","{:.2f}".format(URANUS * fUserWeight).center(20))
print("Weight on Neptune: ","{:.2f}".format(NEPTUNE * fUserWeight).center(20))
print("Weight on Pluto:   ","{:.2f}".format(PLUTO * fUserWeight).center(20))


