
# Lunar Lander: Feedback-Controlled Autopilot

gravity = 1.62
mass = 1000.0
max_thrust = 3000.0
dt = 0.1

altitude = 100.0
velocity = -5.0  # Negative means descending
time = 0.0

print("AUTONOMOUS LUNAR LANDER")
print("-----------------------")

while altitude > 0 and time < 300:
    # Aim to descend more slowly as the surface approaches.
    target_velocity = -min(5.0, max(0.5, altitude * 0.15))

    # Feedback controller: correct the difference from target speed.
    desired_acceleration = 0.8 * (target_velocity - velocity)

    # Convert desired acceleration to required throttle.
    required_thrust = mass * (gravity + desired_acceleration)
    throttle = 100 * required_thrust / max_thrust
    throttle = max(0.0, min(100.0, throttle))

    # Update the physics.
    acceleration = (max_thrust * throttle / 100) / mass - gravity
    old_altitude = altitude
    velocity += acceleration * dt
    altitude += velocity * dt
    time += dt

    # Detect contact and estimate impact velocity.
    if altitude <= 0:
        fraction = old_altitude / (old_altitude - altitude)
        impact_velocity = velocity
        altitude = 0

        print("\nSURFACE CONTACT")
        print(f"Flight time: {time - dt + fraction * dt:.1f} seconds")
        print(f"Impact velocity: {impact_velocity:.2f} m/s")

        if abs(impact_velocity) <= 3:
            print("SUCCESS: Safe landing!")
        else:
            print("CRASH: Impact speed too high.")

if altitude > 0:
    print("\nSimulation stopped: time limit reached.")
    print(f"Altitude remaining: {altitude:.2f} m")
    print(f"Velocity: {velocity:.2f} m/s")
