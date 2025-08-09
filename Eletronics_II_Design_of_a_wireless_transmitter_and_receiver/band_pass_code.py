import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Define the transfer function coefficients
numerator = [0, 18877.87, 0]
denominator = [1, 18877.87, 3.9e9]  # Example: s^2 + 2s + 1

# Create a transfer function
system = signal.TransferFunction(numerator, denominator)

# Get the poles of the transfer function
poles = system.poles

# Plot the poles in the complex plane
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(np.real(poles), np.imag(poles), s=100, marker='x', color='red', label='Poles')  # Increase marker size to 100
plt.axhline(0, color='black', linewidth=2.0, linestyle='--', label='Real Axis')
plt.axvline(0, color='black', linewidth=2.0, linestyle='--', label='Imaginary Axis')

# Connect poles to the axes with lines
for pole in poles:
    plt.plot([np.real(pole), np.real(pole)], [0, np.imag(pole)], color='red', linestyle='--', linewidth=1.5)
    plt.plot([0, np.real(pole)], [np.imag(pole), np.imag(pole)], color='red', linestyle='--', linewidth=1.5)

    # Add text annotations for pole values
    plt.text(np.real(pole), np.imag(pole), f'({np.real(pole):.2f}, {np.imag(pole):.2f})', ha='right', va='bottom', color='blue')

plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Plot the Bode plot starting at 10^-3 Hz
plt.subplot(1, 2, 2)
frequencies, magnitudes, phases = signal.bode(system, np.logspace(2, 8, 1000))
plt.semilogx(frequencies, magnitudes, label='Magnitude (dB)')
plt.semilogx(frequencies, phases, label='Phase (degrees)')
plt.title('Bode Plot')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB) / Phase (degrees)')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.show()