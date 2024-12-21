"""
Task: Numerical Solution of Logistic Equation (M7)

This script numerically solves the differential equation P'(t) = P(t)*(1 - P(t)) using the initial condition P(0) = 0.5 over the time interval from t=0 to t=10 seconds. The solution is saved in 'output.txt' at integer time points. The output values must be accurate within 0.000001 units.

Parameters:
    P'(t): Rate of change of P at time t.
    P(t): Value of P at time t.
    dt: Time step for the numerical solution.
    T: Total simulation time in seconds.
"""

import os
import numpy as np 

# Output file path.
filename=os.path.dirname(__file__)+'/output.txt'

def save(outf, P, t): 
    outf.write(f'{int(t)} {P}\n')   # Write time and height to file.

# ODE: P'(t) = P(t)*(1-P(t)), P(0)=0.5.
# using a small dt to achieve the required accuracy.
dt = 0.0001
T = 10.0
steps = int(T/dt)   # number of steps

P = 0.5  # initial condition
t = 0.0

with open(filename, "w") as outf:
    # Save initial state
    save(outf, P, t)
    for i in range(1, steps+1):
        # Euler step
        P = P + dt*P*(1-P)
        t = i*dt
        # Check if time is close to an integer
        if abs(t - round(t)) < 1e-14 and t <= 10:
            save(outf, P, t)

#Test code 
import pandas as pd

data=pd.read_csv(filename, delimiter=' ', names=['t','P'])
P_estim=data['P'].to_numpy()

assert np.abs(P_estim[0]-0.5).max()<=0.00001, 'accuracy error'
assert np.abs(P_estim[3]-0.95257413).max()<=0.00001, 'accuracy error'
assert np.abs(P_estim[10]-0.9999546).max()<=0.00001, 'accuracy error'
