# 🚀 Numerical Simulations of Motion – Python Project

This project features multiple simulations that model physical systems such as circular motion, spirals, rockets, and harmonic oscillators. The simulations employ numerical integration techniques including Euler's method, Runge-Kutta methods, Leapfrog, and Adams-Bashforth methods. All results are saved to `output.txt` for further analysis or plotting.

---

## 📁 Simulation Scripts

### 🔄 Circular and Spiral Motion

- **`Euler's Circle Simulation.py`**  
  Simulates uniform circular motion using **Euler's method**.  
  ➤ Velocity function: `[-sin(t), cos(t)]`

- **`Circular Motion Simulation.py`**  
  Simulates the same circular motion but with the more accurate **Runge-Kutta 4th order (RK4)** method.

- **`Euler's Spiral Simulation.py`**  
  Models spiral motion where acceleration depends on both position and velocity, using **Euler's method**.

- **`Runge-Kutta Spiral Motion Simulation.py`**  
  More accurate spiral simulation using **RK4**, incorporating position-dependent forces and damping.

- **`adams_bashforth_spiral_simulation.py`**  
  Spiral simulation using **Adams-Bashforth multistep method** (up to 3rd-order). Begins with an Euler step.

---

### 📈 Other Dynamic Systems

- **`Harmonic Oscillator Leapfrog Simulation.py`**  
  Leapfrog integration of a spring-mass system (`F = -kx`), simulating a **harmonic oscillator** over 100 seconds.

- **`Rocket Altitude Simulation.py`**  
  Models rocket flight over 10 seconds where the **engine toggles on/off** every second. Tracks altitude over time.

- **`Numerical Solution of Differential Equation.py`**  
  Solves the logistic growth equation `P'(t) = P(t)(1 - P(t))` from `t=0` to `t=10`.  
  ➤ Uses **Euler's method**, saves results every second.

- **`Numerical Solution of Logistic Equation.py`**  
  Functionally similar to the above, included for practice and accuracy testing.

---

## 🧪 Output Format

All simulations write to a file named **`output.txt`** (overwritten per script). Typical columns include:
- `t`: Time in seconds
- `x`: X-position or value
- `y`: Y-position (where applicable)

---

## ▶️ How to Run

1. Make sure Python 3 and necessary packages (`numpy`, `pandas`, `matplotlib`) are installed.
2. Run any simulation like this:
   ```bash
   python "Euler's Circle Simulation.py"
3. Use the optional plotting code (if enabled) to visualize results.


🧠 Learning Outcomes
Practice implementing common ODE solvers: Euler, RK4, Leapfrog, Adams-Bashforth.

Simulate physical systems like circular or spiral motion, spring-mass dynamics, and rocket flight.

Analyze and validate numerical results using file output and assertions.