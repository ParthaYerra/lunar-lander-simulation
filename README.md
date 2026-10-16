# Lunar Lander Simulation

## Overview
This project simulates a spacecraft landing on the Moon using Python. It models lunar gravity, spacecraft thrust, altitude, and velocity. An autonomous feedback controller adjusts engine throttle to achieve a controlled landing.

## Physics Model
The simulation uses lunar gravity of 1.62 m/s² and a spacecraft mass of 1,000 kg. The engine produces a maximum thrust of 3,000 N.

Net acceleration is calculated using:

**Acceleration = (Thrust / Mass) − Lunar Gravity**

The simulation updates velocity and altitude at 0.1-second intervals.

## Autonomous Control
The autopilot calculates a target descent velocity based on the current altitude. It then adjusts engine throttle according to the difference between the target velocity and the actual velocity.

## Initial Test Results

| Initial Altitude | Initial Velocity | Flight Time | Impact Velocity | Result |
|---|---|---|---|---|
| 100 m | −5 m/s | 31.9 s | −0.50 m/s | Safe |
| 150 m | −8 m/s | 41.1 s | −0.50 m/s | Safe |
| 150 m | −12 m/s | 38.2 s | −0.50 m/s | Safe |

A landing is classified as safe when the absolute impact velocity is no greater than 3 m/s.

## Tools
- Python
- Matplotlib
- Git and GitHub

## Limitations and Future Improvements
This is a simplified physics model. It assumes constant spacecraft mass and does not model fuel consumption or variable engine performance. Future improvements could include fuel constraints, randomized starting conditions, and more advanced control algorithms.
