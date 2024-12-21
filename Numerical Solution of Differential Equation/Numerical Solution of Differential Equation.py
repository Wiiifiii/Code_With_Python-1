"""
Task: Numerical Solution of Differential Equation (M8)

This script numerically solves the differential equation P'(t) = P(t)*(1 - P(t)) using the initial condition P(0) = 0.5 over the time interval from t=0 to t=10 seconds. The solution is saved in 'output.txt' at integer time points. The output values must be accurate within 0.000001 units.

Parameters:
    P'(t): Rate of change of P at time t.
    P(t): Value of P at time t.
    dt: Time step for the numerical solution.
    T: Total simulation time in seconds.
"""

import os
import numpy as np 

filename = os.path.join(os.path.dirname(__file__), 'output.txt')  # Path to output file

def save(outf, P, t):
    """Writes the current time and value of P to the output file."""
    outf.write(f'{int(t)} {P:.6f}\n')  # Save time as integer and P with six decimal places

# Initial condition and parameters
P = 0.5  # P at t=0
dt = 0.0001  # Time step
T = 10.0  # Total time
steps = int(T / dt)  # Number of steps

with open(filename, "w") as outf:
    save(outf, P, 0)  # Save the initial state
    
    for i in range(1, steps + 1):
        # Euler method to update P
        P += dt * P * (1 - P)
        t = i * dt
        
        # Check if the current time is close to an integer
        if abs(t - round(t)) < 1e-14 and t <= T:
            save(outf, P, t)

# Debugging and validation
import pandas as pd

data = pd.read_csv(filename, delimiter=' ', names=['t', 'P'])
P_estim = data['P'].to_numpy()

# Assertions to check the accuracy of the simulation at specific times
assert np.abs(P_estim[0] - 0.5) <= 0.000001, 'Accuracy error at t=0'
assert np.abs(P_estim[int(1/dt)] - 0.95257413) <= 0.000001, 'Accuracy error at t=1'
assert np.abs(P_estim[int(10/dt)] - 0.9999546) <= 0.000001, 'Accuracy error at t=10'
