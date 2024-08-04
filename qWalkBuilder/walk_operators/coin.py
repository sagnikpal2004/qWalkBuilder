import qiskit as qk
import numpy as np

class Coin(qk.QuantumCircuit):
    def __init__(self, quantumWalk, coin):
        if isinstance(coin, str):
            self.stringMap(coin)
        elif isinstance(coin, qk.QuantumCircuit):
            self = coin
        # elif isinstance(coin, np.ndarray):
        #     self = qk.QuantumCircuit(coin)
        else:
            raise TypeError()

    def stringMap(self, coin):
        coin, count = coin.split('.')

        super().__init__(count)
        if coin in ['H', 'hadamard']:
            self.h(range(count))
            self.name = "H"

# TODO: Implement way to convert numpy array to qiskit QuantumCircuit