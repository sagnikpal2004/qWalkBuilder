import qiskit as qk
import qiskit_aer as qkA

from .walk_operators import Coin, Shift, Init
from .quantum_circuit import QuantumCircuit


class QuantumWalk:
    def __init__(self, coin="H.2", shift="T.[4,4]", init="singleNode"):
        self.coin = Coin(coin)
        self.shift = Shift(shift)
        self.init = Init(init)

    def time(self, time: int):
        c = self.coin.qubits
        v = self.shift.qubits
        qc = QuantumCircuit(c+v)
        
        # Append quantum walk operators
        qc.append(self.init, c+v)
        for i in range(time):
            qc.append(self.coin, c)
            qc.append(self.shift, c+v)

        return qc
    
    def __str__(self):
        return f"QuantumWalk(
            coin={self.coin}, 
            shift={self.shift}, 
            init={self.init},
        )"