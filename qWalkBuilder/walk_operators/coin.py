import qiskit as qk
import numpy as np


class Coin(qk.QuantumCircuit):
    def __init__(self, coin, qRegs):
        c, x, y = qRegs
        super().__init__(*qRegs)
        
        if coin == "H":
            self.h(c)
        else:
            raise ValueError(f"Invalid coin code: {coin}")
        
        self.name = coin

# TODO: Implement way to convert numpy array to qiskit QuantumCircuit