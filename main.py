
print("Lunar Lander Engineering Project")
print("Python is working!")

gravity = 1.62
mass = 1000
thrust = 2000

acceleration = thrust / mass - gravity

print("Lunar gravity:", gravity, "m/s^2")
print("Spacecraft mass:", mass, "kg")
print("Engine thrust:", thrust, "N")
print("Net acceleration:", round(acceleration, 2), "m/s^2")
