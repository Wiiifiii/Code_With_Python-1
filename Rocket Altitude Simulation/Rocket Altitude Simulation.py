"""
Task: Rocket Altitude Simulation (M31)

This script simulates the altitude of a rocket as a function of time, under conditions where the rocket's engine alternates between being on and off every second. The rocket's altitude at time intervals from t=0 to t=10 seconds is written to 'output.txt':
    t_i = Time instance, each second from 0 to 10.
    x_i = Altitude at time t_i.
Columns are separated by spaces, and the file contains 11 lines, one for each second including t=0.

Parameters:
    g = Gravitational acceleration (10 m/s^2).
    m = Mass of the rocket (100 kg).
    F = Thrust of the engine (2000 N).
    Altitude error threshold = 0.1 m.

The script utilizes a straightforward integration method to simulate the rocket's motion assuming constant gravitational force and alternating engine thrust.
"""

import os
import numpy as np

filename = os.path.dirname(__file__) + '/output.txt'   # Output file path

def save(outf, x, t):
    """Writes the current time and altitude to the file."""
    outf.write(f'{int(t)} {x:.1f}\n')

# Given constants
m = 100.0  # Mass of the rocket in kg
F = 2000.0  # Thrust of the rocket's engine in N
g = 10.0  # Acceleration due to gravity in m/s^2

# Calculate net accelerations when engine is on and off
a_on = (F / m) - g  # Net acceleration when engine is on
a_off = -g  # Net acceleration when engine is off (only gravity)

# Initial conditions
y = 0.0  # Initial altitude in meters
v = 0.0  # Initial velocity in m/s

with open(filename, 'w') as file:
    # Write initial state at t=0
    save(file, y, 0)

    # Simulate each second from t=1 to t=10
    for t in range(1, 11):
        # Engine on during odd seconds, off during even seconds
        if t % 2 == 1:
            a = a_on
        else:
            a = a_off

        # Update velocity and altitude using basic kinematics
        v += a * 1  # Update velocity with constant acceleration over 1 second
        y += v * 1 + 0.5 * a * (1**2)  # Update position with current velocity and constant acceleration

        # Write the current time and altitude to the file
        save(file, y, t)

print("Simulation complete. Results saved to output.txt.")

# Debugging and validation of output
import pandas as pd

data = pd.read_csv(filename, delimiter=' ', names=['t', 'x'])
print(data)

# Ensuring the data length and value accuracy
assert len(data) == 11, 'Length of data error'
assert np.abs(data.at[0, 'x'] - 0.0) <= 0.1, 'Accuracy error at t=0'
assert np.abs(data.at[1, 'x'] - 5.0) <= 0.1, 'Accuracy error at t=1'
assert np.abs(data.at[10, 'x'] - 50.0) <= 0.1, 'Accuracy error at t=10'
