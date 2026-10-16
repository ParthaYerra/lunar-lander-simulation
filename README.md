# Lunar Lander Simulation
### An Autonomous Spacecraft Landing System Built with Python

A physics-based lunar lander simulation that models spacecraft descent under lunar gravity and tests an autonomous controller designed to achieve safe landings. This project combines physics, feedback control, experimental testing, and real-time visualization to explore the engineering challenges of landing a spacecraft on the Moon.

## Project Demo

[**Watch the Lunar Lander Simulation Demo**](https://drive.google.com/file/d/13Pb-Veq__2Dti88rI7XadPvTPSBrozQ_/view?usp=drive_link)

The demo showcases the autonomous spacecraft descent, real-time flight telemetry, and throttle-responsive thruster effects.


## Project Features

- **Lunar Physics Model:** Simulates vertical motion under lunar gravity of 1.62 m/s².
- **Autonomous Landing Controller:** Adjusts engine thrust based on altitude and vertical velocity.
- **Real-Time Visualization:** Displays the spacecraft, lunar terrain, telemetry, and throttle-responsive engine flames.
- **Experimental Testing:** Tests different initial altitudes and descent velocities to evaluate landing performance.
- **Performance Analysis:** Tracks flight time, impact velocity, and whether each landing meets the safety criterion.

## How It Works

### 1. Physics Model

The simulation calculates the spacecraft's vertical acceleration using the relationship between engine thrust, spacecraft mass, and lunar gravity.

\[
a=(T/m)-g
\]

Where:

- \(a\) = vertical acceleration (m/s²)
- \(T\) = engine thrust (N)
- \(m\) = spacecraft mass (kg)
- \(g\) = lunar gravitational acceleration (1.62 m/s²)

The model uses a spacecraft mass of 1,000 kg and a maximum engine thrust of 3,000 N. Velocity and altitude are updated throughout the descent.

### 2. Autonomous Landing Controller

The controller uses feedback from the spacecraft's current velocity and altitude to determine the thrust required for a controlled descent. It calculates a target descent velocity, estimates the necessary thrust, and adjusts throttle within the engine's limits.

The goal is to reduce descent speed before touchdown. However, the controller cannot guarantee a safe landing under every initial condition because the engine has a finite thrust capacity.

### 3. Landing Evaluation

For this project, a landing is classified as safe when the absolute vertical impact velocity is no greater than 3.0 m/s. Faster impacts are classified as crashes.

## Experimental Results

The following tests evaluate how different starting conditions affect landing performance.

| Starting Altitude | Initial Velocity | Flight Time | Impact Velocity | Outcome |
|---:|---:|---:|---:|---|
| 100 m | −5 m/s | 31.9 s | −0.50 m/s | Safe |
| 150 m | −8 m/s | 41.1 s | −0.50 m/s | Safe |
| 150 m | −12 m/s | 38.2 s | −0.50 m/s | Safe |
| 50 m | −12 m/s | 7.1 s | −2.07 m/s | Safe |
| 50 m | −15 m/s | 4.1 s | −9.20 m/s | Crash |
| 50 m | −20 m/s | 2.8 s | −16.14 m/s | Crash |

*Negative velocity indicates downward motion.*

### What the Experiments Show

The tests demonstrate that the controller can achieve safe landings under several initial conditions. However, the low-altitude, high-speed tests show that limited engine thrust can prevent the spacecraft from slowing down sufficiently before impact.

These results highlight an important engineering trade-off: a control system must account for both the spacecraft's current motion and the amount of time and thrust available to correct it.

## Technology Stack

- **Python:** Physics calculations and control logic
- **Pygame:** Real-time visual simulation and interface
- **Matplotlib:** Flight-performance graphs and analysis

## Getting Started

### Requirements

Install Python 3.13 and the required libraries.

```bash
py -3.13 -m pip install pygame matplotlib
```

### Run the Project

Clone the repository:

```bash
git clone https://github.com/ParthaYerra/lunar-lander-simulation.git
cd lunar-lander-simulation
```

Run the basic physics model:

```bash
py -3.13 main.py
```

Run the autonomous landing controller and generate performance graphs:

```bash
py -3.13 autopilot.py
```

Launch the visual simulation:

```bash
py -3.13 visual_lander.py
```

Press **R** to restart the visual simulation or **Esc** to exit.

## Project Structure

```text
lunar-lander-simulation/
├── main.py               # Basic physics calculations
├── autopilot.py          # Autonomous landing controller
├── visual_lander.py      # Interactive visual simulation
├── landing_analysis.png  # Flight-performance graphs
└── README.md             # Project documentation
```

## Limitations and Future Improvements

The current model focuses on vertical motion and does not simulate the full complexity of a real lunar landing. It excludes horizontal movement, changing spacecraft mass, terrain collision geometry, and other environmental effects.

Potential improvements include refining the feedback controller, testing a wider range of initial conditions, expanding the physics model, and improving the realism of the spacecraft visualization.

## Learning Outcomes

This project provided practical experience with physics modeling, feedback control, Python programming, data visualization, and experimental evaluation. Testing both successful and unsuccessful landings helped identify the limitations of the controller and showed how simulation can be used to evaluate engineering decisions.

---

**Author:** Partha Yerra  
**Repository:** [lunar-lander-simulation](https://github.com/ParthaYerra/lunar-lander-simulation)
