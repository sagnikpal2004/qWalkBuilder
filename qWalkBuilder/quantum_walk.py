import qiskit as qk
import qiskit_aer as qkA

from .utils.walk_register import RegisterList
from .walk_operators.shiftCoin import ShiftCoin
from .walk_operators.init import Init
from .quantum_circuit import QuantumCircuit


class QuantumWalk:
    """ TODO: Add docstring """

    def __init__(self, shiftCoin, init="uniform"):
        self.qRegs = RegisterList(shiftCoin)

        self.shiftCoin = ShiftCoin(shiftCoin, self.qRegs)
        self.init = Init(init, self.qRegs)


    # TODO: add optimization by caching state at time steps
    def atTime(self, time: int):
        qc = QuantumCircuit(*self.qRegs)
        
        qc.append(self.init, self.qRegs.qubits)
        for i in range(time):
            qc.append(self.shiftCoin, self.qRegs.qubits)

        return qc
    
    # # TODO: Run for a longer time
    # def run(self):
    #     resultViewer = Results()

    #     return resultViewer
    
    def __str__(self):
        return f"QuantumWalk(coin={self.shiftCoin.coin.name}, shift={self.shiftCoin.shift.name}, init={self.init.name})"