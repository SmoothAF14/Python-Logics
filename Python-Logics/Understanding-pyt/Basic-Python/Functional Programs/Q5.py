import math

t = float(input("Enter temperature (Fahrenheit): "))
v = float(input("Enter wind speed (mph): "))

if abs(t) > 50 or v > 120 or v < 3:
    print("Invalid input range for wind chill formula.")
else:
    wind_chill = 35.74 + 0.6215*t + (0.4275*t - 35.75) * math.pow(v, 0.16)
    print("Wind Chill =", wind_chill)