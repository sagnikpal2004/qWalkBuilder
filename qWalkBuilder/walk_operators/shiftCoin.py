import qiskit as qk

from .shift import Shift
from .coin import Coin

class ShiftCoin(qk.QuantumCircuit):

    def __init__(self, shiftCoin, qRegs):
        shift, coin = shiftCoin.split(".")

        self.coin = Coin(coin, qRegs)
        self.shift = Shift(shift, qRegs)

        super().__init__(*qRegs)
        self.append(self.coin, self.qubits)
        self.append(self.shift, self.qubits)

    
    def getEigen(self):
        pass