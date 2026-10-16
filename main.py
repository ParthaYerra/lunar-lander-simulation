
print("LUNAR LANDER SIMULATION")

# Physical constants
gravity = 1.62
mass = 1000
max_thrust = 3000

# Initial conditions
altitude = 100.0
velocity = -5.0
time = 0.0
dt = 0.1

print("\nControls: Enter throttle from 0 to 100.")
print("Enter -1 to quit the simulation.")

while altitude > 0:
    print(f"\nTime: {time:.1f} s")
    print(f"Altitude: {altitude:.2f} m")
    print(f"Velocity: {velocity:.2f} m/s")

    try:
        throttle = float(input("Throttle (%): "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if throttle == -1:
        print("Simulation ended.")
        break

    if not 0 <= throttle <= 100:
        print("Throttle must be between 0 and 100.")
        continue

    # Calculate acceleration
    thrust = max_thrust * throttle / 100
    acceleration = thrust / mass - gravity

    # Advance physics by 0.1 seconds
    old_altitude = altitude
    velocity += acceleration * dt
    altitude += velocity * dt
    time += dt

    # Detect surface contact
    if altitude <= 0:
        altitude = 0
        print("\nSURFACE CONTACT")
        print(f"Impact velocity: {velocity:.2f} m/s")

        if abs(velocity) <= 3:
            print("SUCCESS: Safe landing!")
        else:
            print("CRASH: Impact speed too high.")
