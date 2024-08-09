# qWalkBuilder

![LICENSE](https://img.shields.io/github/license/sagnikpal2004/qWalkBuilder)

**qWalkBuilder** is an open-source python library for building and executing well-defined discrete-time quantum walks in [Qiskit](https://github.com/Qiskit/qiskit)

## Installation

To install the `qWalkBuilder` library, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/sagnikpal2004/qWalkBuilder.git
    cd qWalkBuilder
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

4. **Install the `qWalkBuilder` library**:
    ```sh
    pip install .
    ```

## Example Usage
Build a quantum walk with a two-qubit Hadamard coin and a 4x4 node Torus shift operator, initializing from a single node state.\
Measure at time 10 on the Z-basis and print the probabilities for each state
```python
import qWalkBuilder as qWB

qw = qWB.QuantumWalk("H.2", "T.[4,4]", "singleNode")

result = qw.time(10).run("measure_z")
print(f"Probabilities: {result}")
```

## Codes
### Shift
- `16nT`: 4x4 node Torus
### Coin
- `H`: Hadamard
### Init
- `uniform`: Uniform superpositon over all qubits
- `single`: No superposition