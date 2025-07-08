import numpy as np
import matplotlib.pyplot as plt

# Define the discrete time range
n = np.arange(-10, 21)  # from -10 to 20

# Unit Step: u[n]
u = np.where(n >= 0, 1, 0)

# Ramp: r[n] = n * u[n]
r = n * u

# Exponential: x[n] = a^n * u[n]
a = 0.9  # Try a = 1.1 for growing exponential
exp_signal = (a ** n) * u

# Sine: x[n] = sin(ωn)
omega = np.pi / 4
sine_signal = np.sin(omega * n)

# Cosine: x[n] = cos(ωn)
cos_signal = np.cos(omega * n)

# Plotting all signals
fig, axs = plt.subplots(5, 1, figsize=(10, 12))
signal_list = [u, r, exp_signal, sine_signal, cos_signal]
titles = ['Unit Step', 'Ramp', f'Exponential (a = {a})', f'Sine (ω = π/4)', f'Cosine (ω = π/4)']

for i, ax in enumerate(axs):
    ax.stem(n, signal_list[i])  # removed deprecated argument
    ax.set_title(titles[i])
    ax.set_xlabel('n')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

plt.tight_layout()
plt.show()
