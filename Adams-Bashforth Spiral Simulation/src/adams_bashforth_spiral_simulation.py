"""
Task: Adams-Bashforth Spiral Simulation (M05)

This script simulates the motion of an object under a specific force field using the Adams-Bashforth 2nd order method. It writes the object's (x, y) coordinates at each timestep to a file named 'output.txt':
    t_i = Time instance, starting at 0 and ending at n*Dt.
    x_i = x-coordinate at time t_i.
    y_i = y-coordinate at time t_i.
Columns are separated by spaces, and the file contains n+1 lines, one for each timestep including the initial condition.

Parameters:
    Dt = Time step for the simulation.
    n = Number of timesteps to simulate.

This script uses an initial Euler step followed by the Adams-Bashforth method to approximate the trajectory based on the object's dynamics.
"""
import numpy as np
import os

filename=os.path.dirname(__file__)+'/output.txt' # the output file path
def save(outf, x, t):
    x_i=x[0]
    y_i=x[1]
    outf.write(f'{t} {x_i} {y_i}\n')    # Write the time, x, and y coordinates to the file.

def ab_spiral(Dt, n):
    # Initial conditions: X = [x, y, vx, vy]
    X = np.array([1.0, 0.0, 0.0, 1.0], dtype=float) # Initial position and velocity

    def acceleration(x, y, vx, vy): # Function to calculate acceleration based on position and velocity.
        r = np.sqrt(x*x + y*y) # The radial distance from the origin, calculated using the Pythagorean theorem.
        if r == 0:
            # In case of extremely unlikely scenario of returning to origin, avoid division by zero:
            r = 1e-12 
        ax = (-1.25 / r)*x - 0.3*vx # Compute the acceleration in the x direction.
        ay = (-1.25 / r)*y - 0.3*vy # Compute the acceleration in the y direction.
        return ax, ay

    def f(X):
        x, y, vx, vy = X    # Unpack the position and velocity values.
        ax, ay = acceleration(x, y, vx, vy) # Compute the acceleration values.
        return np.array([vx, vy, ax, ay], dtype=float)  # Return the acceleration values.

    times = [i*Dt for i in range(n+1)]  # Create a list of time values from 0 to n*Dt.
    f_list = []

    with open(filename, "w") as out:
        # Write initial condition line
        out.write(f"{times[0]} {X[0]} {X[1]}\n")

        for i in range(1, n+1): # Loop over the time steps.
            current_f = f(X)    # Compute the current f-value.
            f_list.append(current_f)    # Append the current f-value to the list.

            # If we have fewer than 2 f-values, use Euler method
            if len(f_list) < 2:
                X = X + Dt*current_f
            else:
                # Use AB2 once we have at least 2 f-values
                fk = f_list[-1]    # f(X_k)
                fkm1 = f_list[-2]  # f(X_{k-1})
                X = X + (Dt/2)*(3*fk - fkm1)

            # Write a line for this step
            out.write(f"{times[i]:.8f} {X[0]:.8f} {X[1]:.8f}\n")
# Test code
if __name__=='__main__':
    import pandas as pd
    from matplotlib import pyplot as plt

    show_figure=False

    if show_figure:
        N=100
        dt=10/N
        ab_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=1000
        dt=10/N
        ab_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=10000
        dt=10/N
        ab_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        plt.legend()
        plt.show()

    N=100
    dt=10/N
    ab_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

    inaccurate_values=np.array([[4.3, 0.3348311043562908, -0.10543010657264017],
                                 [6.7,  -0.025926510426994766, -0.2557111932731299]])

    accurate_values=np.array([[4.3,  0.33590747680361643, -0.08836541262642196],
                              [6.7,  -0.019781308150982085, -0.2621123367635826]])

    assert len(data)==N+1, 'length of data error'
    assert len(data.columns)==3, 'columns number error'

    eps=0.0001
    assert abs(data['t'].min()-0)<eps
    assert abs(data['t'].max()-N*dt)<eps

    def compare_xy(data, t, x, y):
        d=data.loc[(t-eps<data['t']) & (data['t']<t+eps)]
        dx = float(d['x'].iloc[0])
        dy = float(d['y'].iloc[0])
        return abs(dx-x), abs(dy-y)

    for t, x, y in inaccurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps

    N=10000
    dt=10/N
    ab_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
    for t, x, y in accurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps



# if __name__ == '__main__':
#     import matplotlib.pyplot as plt

#     # Optional visualization
#     dt = 0.01
#     N = 100
#     ab_spiral(dt, N)
#     data = np.loadtxt(filename)
#     plt.plot(data[:, 1], data[:, 2])
#     plt.xlabel('X position')
#     plt.ylabel('Y position')
#     plt.title('Adams-Bashforth Spiral Motion')
#     plt.show()
