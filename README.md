# Electronics I & II - Academic Projects

This repository contains academic projects from Electronics I and Electronics II courses at NOVA University.

Eletronics I project focus on operational amplifier design 

Eletronics II projects focus on a wireless communication system.

## Project Structure

```
├── Eletronics_I_final_OPAMP_schematic.asc    # Electronics I: Discrete Op-Amp Design
├── OPAMP_circuit.png                         # Op-Amp Circuit Visualization
├── Eletronics_II_Design_of_a_wireless_transmitter_and_receiver/
│   ├── wireless_circuit.jpeg                 # Wireless Circuit Design
│   ├── band_pass_code.py                     # Band-Pass Filter Analysis
│   ├── low_pass_code.py                      # Low-Pass Filter Analysis
│   └── circuito_completo_certo.log           # Circuit Simulation Results
└── README.md                                 # This file
```

## Electronics I Project: Discrete Operational Amplifier

### Overview
This project implements a **discrete operational amplifier** using individual transistors, resistors, and capacitors instead of an integrated circuit op-amp. The design serves as an educational tool for understanding operational amplifier principles at the component level.

### Key Features
- **Multi-stage Design**: Three-stage op-amp architecture
  - Input stage: Differential amplifier (Q1A, Q1B, Q1C)
  - Intermediate stage: Voltage amplification (Q2)
  - Output stage: Push-pull configuration (Q3, Q4)
- **Dual Power Supply**: ±6V operation
- **Multiple Output Stages**: vo1, vo2, vo for different gain measurements
- **LED Indicator**: Status indication (DLED)
- **Comprehensive Analysis**: Automatic gain calculations and measurements

### Circuit Components
- **Transistors**: BC547C (NPN), BC557C (PNP), BD139 (NPN), DB140 (PNP)
- **Resistors**: Various values for biasing and gain control
- **Capacitors**: 470μF output coupling capacitor
- **Power Supply**: Dual ±6V supply
- **Load**: 8Ω resistive load

### Simulation Features
The LTspice schematic includes automatic measurements for:
- Input/output peak-to-peak voltages
- Stage-by-stage gain analysis (V1, V2, V3)
- Total system gain calculation
- Transient analysis over 40ms

### Files
- `Eletronics_I_final_OPAMP_schematic.asc`: Complete LTspice schematic
- `OPAMP_circuit.png`: Circuit visualization

---

## Electronics II Project: Wireless Transmitter and Receiver Design

### Overview
This project focuses on **wireless communication system** with emphasis on **filter design and signal processing**. The system includes both band-pass and low-pass filters for signal conditioning.

### Key Features
- **Band-Pass Filter**: Second-order filter for frequency selection
- **Low-Pass Filter**: Second-order filter for signal smoothing
- **Signal Analysis**: Pole-zero plots and Bode diagrams
- **Wireless Circuit Design**: Complete transmitter/receiver system

### Filter Specifications

#### Band-Pass Filter
- **Transfer Function**: `H(s) = 18877.87s / (s² + 18877.87s + 3.9e9)`
- **Center Frequency**: ~31.2 kHz
- **Purpose**: Frequency selection for wireless communication

#### Low-Pass Filter
- **Transfer Function**: `H(s) = 7.7759e7 / (s² + 12453.2s + 7.7759e7)`
- **Cutoff Frequency**: Determined by damping coefficient
- **Purpose**: Signal smoothing and noise reduction

### Analysis Tools

#### `band_pass_code.py`
- **Pole-Zero Analysis**: Visualizes system poles in complex plane
- **Bode Plot**: Magnitude and phase response (100 Hz - 100 MHz)
- **Transfer Function**: `18877.87s / (s² + 18877.87s + 3.9e9)`

#### `low_pass_code.py`
- **Pole-Zero Analysis**: System stability analysis
- **Bode Plot**: Frequency response (0.1 Hz - 1 GHz)
- **Transfer Function**: `7.7759e7 / (s² + 12453.2s + 7.7759e7)`

### Files
- `wireless_circuit.jpeg`: Complete wireless system design
- `band_pass_code.py`: Band-pass filter analysis and visualization
- `low_pass_code.py`: Low-pass filter analysis and visualization
- `circuito_completo_certo.log`: LTspice simulation results

---

## Technical Requirements

### Software Dependencies
- **LTspice XVII**: Circuit simulation and analysis
- **Python 3.x**: Signal processing and analysis
- **Required Python Packages**:
  ```bash
  pip install matplotlib numpy scipy
  ```

---

## Key Results

### Electronics I - Op-Amp Performance
- **Gain Stages**: Multiple amplification stages for high overall gain
- **Bandwidth**: Wide frequency response for audio applications
- **Stability**: Stable operation with proper biasing

### Electronics II - Filter Performance
- **Band-Pass Filter**: Selective frequency response around 31.2 kHz
- **Low-Pass Filter**: Smooth signal processing with controlled cutoff
- **System Integration**: Complete wireless communication chain

---

## 🤝 Contributors

### For eletronics I:

- [Rodrigo Luz](https://www.linkedin.com/in/rodrigo-luz-43977b24a/)
- [Pedro Domingão](https://www.linkedin.com/in/pedro-gabriel-00088127b/)
- [Tiago Monteiro](https://www.linkedin.com/in/tiago-monteiro-/)

### For eletronics II:

- [Moacir Diniz](https://www.linkedin.com/in/moacirdiniz/)
- Filipa Correia
- [Tiago Monteiro](https://www.linkedin.com/in/tiago-monteiro-/)