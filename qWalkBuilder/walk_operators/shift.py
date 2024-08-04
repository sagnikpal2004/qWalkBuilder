import qiskit as qk


class Shift(qk.QuantumCircuit):
    def __init__(self, quantumWalk, shift):
        if isinstance(shift, str):
            self.stringMap(shift)
        elif isinstance(shift, qk.QuantumCircuit):
            self = shift
        else:
            raise TypeError()
        
    def stringMap(self, shiftStr):
        shift_code, count = shiftStr.split('.')
        
        super().__init__(int(count))
        if shift_code in ['T', 'torus']:
            if count == "[4,4]":
                pass