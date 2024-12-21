"""
M9 - Harmonic Oscillator Leapfrog Simulation

This task involves simulating the motion of a mass attached to a spring without considering gravitational force.
The system consists of a mass (m = 2 kg) attached to one end of a spring with a spring constant (k = 3 N/m). 
The origin is set such that when the mass is at x = 0, no force acts on it. If displaced from this position,
the spring exerts a force F = -kx. The simulation runs from t = 0 to t = 100 seconds, with the position recorded every second.

The task is to numerically solve this system using a leapfrog integration method due to its advantages in conserving
energy over long-term simulations and write the output to a file named 'output.txt' with time and position data.

Initial conditions:
- Position (x) = 0.5 meters (indicating initial displacement from equilibrium)
- Velocity (v) = 0 m/s (indicating the mass starts from rest)

The results should be accurate to within 0.1 meters for each timestep.

"""
import os
import numpy as np 

# The output file path
filename = os.path.dirname(__file__) + '/output.txt'

# Constants for the spring-mass system
K = 3  # Spring constant (N/m)
M = 2  # Mass of the object (kg)
T = 100  # Total time for the simulation in seconds

def save(outf, x, t):
    """Function to save the current time and position to the output file."""
    x_i = x[0]  # Current position
    v_i = x[1]  # Current velocity (not used in the output)
    outf.write(f'{int(t)} {x_i}\n')  # Write data as integers

# Simulation parameters
dt = 0.0001  # Time step in seconds
steps = int(T/dt)  # Number of simulation steps

# Initial conditions
pos = 0.5  # Initial position in meters
vel = 0.0  # Initial velocity in m/s

with open(filename, "w") as outf:
    # Save the initial state at t=0
    save(outf, [pos, vel], 0)

    # Leapfrog method initialization for position
    pos_half = pos + 0.5 * dt * vel

    for i in range(1, steps + 1):
        # Calculate the spring force-induced acceleration
        a = -(K / M) * pos_half  # Acceleration due to Hooke's law

        # Update the velocity for the full step
        vel += dt * a

        # Complete the position update
        pos = pos_half + 0.5 * dt * vel

        # Update the position for the next half-step
        pos_half = pos + 0.5 * dt * vel

        # Current time
        t = i * dt
        # Save the output at integer seconds
        if abs(t - round(t)) < 1e-14 and t <= T:
            save(outf, [pos, vel], int(round(t)))


