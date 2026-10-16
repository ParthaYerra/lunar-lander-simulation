
import matplotlib.pyplot as plt

# Physical constants
gravity = 1.62
mass = 1000.0
max_thrust = 3000.0
dt = 0.1

# Initial conditions
altitude = 100.0
velocity = -5.0
time = 0.0

# Store data for graphs
times = [time]
altitudes = [altitude]
velocities = [velocity]
throttles = [0.0]

print("AUTONOMOUS LUNAR LANDER")
print("-----------------------")

while altitude > 0 and time < 300:
    # Set a safe target descent speed
    target_velocity = -min(5.0, max(0.5, altitude * 0.15))

    # Feedback controller
    desired_acceleration = 0.8 * (target_velocity - velocity)

    required_thrust = mass * (gravity + desired_acceleration)
    throttle = 100 * required_thrust / max_thrust
    throttle = max(0.0, min(100.0, throttle))

    # Calculate acceleration
    thrust = max_thrust * throttle / 100
    acceleration = thrust / mass - gravity

    # Update motion
    old_altitude = altitude
    velocity += acceleration * dt
    altitude += velocity * dt
    time += dt

    # Handle surface contact
    if altitude <= 0:
        fraction = old_altitude / (old_altitude - altitude)
        impact_velocity = velocity
        altitude = 0
        time -= dt * (1 - fraction)

        times.append(time)
        altitudes.append(altitude)
        velocities.append(impact_velocity)
        throttles.append(throttle)
        break

    # Record each simulation step
    times.append(time)
    altitudes.append(altitude)
    velocities.append(velocity)
    throttles.append(throttle)

print("\n--- LANDING REPORT ---")
print(f"Flight time: {time:.1f} seconds")

if altitude == 0:
    print(f"Impact velocity: {impact_velocity:.2f} m/s")

    if abs(impact_velocity) <= 3:
        print("SUCCESS: Safe landing!")
    else:
        print("CRASH: Impact speed too high.")
else:
    print("Simulation stopped before landing.")

# Create three engineering graphs
fig, axes = plt.subplots(3, 1, figsize=(9, 10))

axes[0].plot(times, altitudes)
axes[0].set_title("Lander Altitude vs. Time")
axes[0].set_ylabel("Altitude (m)")
axes[0].grid(True)

axes[1].plot(times, velocities)
axes[1].set_title("Lander Velocity vs. Time")
axes[1].set_ylabel("Velocity (m/s)")
axes[1].grid(True)

axes[2].plot(times, throttles)
axes[2].set_title("Engine Throttle vs. Time")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Throttle (%)")
axes[2].grid(True)

plt.tight_layout()
plt.savefig("landing_analysis.png", dpi=150)
print("\nGraph saved as landing_analysis.png")

plt.show()
