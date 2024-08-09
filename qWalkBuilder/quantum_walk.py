from functools import cache

from .utils.register_list import RegisterList
from .operators.shiftcoin import ShiftCoin
from .operators.init import Init
from .operators.circuit import QWalkCircuit


class QuantumWalk:
    """ TODO: Add docstring """

    def __init__(self, shiftCoin, init="uniform", no_cache=False):
        self.qRegs = RegisterList(shiftCoin)

        self.init = Init(init, self.qRegs)
        self.shiftCoin = ShiftCoin(shiftCoin, self.qRegs)

        self.no_cache = no_cache
        if not self.no_cache:
            self._cache = {}


    def atTime(self, time: int):
        if not self.no_cache and time in self._cache:
            return self._cache[time]

        qc = QWalkCircuit(*self.qRegs, metadata={"qWalk": self, "atTime": time})
        qc.append(self.init, self.qRegs.qubits)
        for i in range(time):
            qc.append(self.shiftCoin, self.qRegs.qubits)

        if not self.no_cache:
            self._cache[time] = qc
        return qc
    
    # # TODO: Run for a longer time
    # def run(self):
    #     resultViewer = Results()

    #     return resultViewer


    def __str__(self):
        return f"QuantumWalk(shiftCoin={self.shiftCoin.name}, init={self.init.name})"