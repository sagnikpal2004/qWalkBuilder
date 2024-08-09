import qiskit as qk


class RegisterList(list[qk.QuantumRegister]):
    def __init__(self, shift):
        shift = shift.split(".")[0]

        if shift == "16nT":
            self.coinRegs = [
                qk.QuantumRegister(2, "c")
            ]
            self.shiftRegs = [
                qk.QuantumRegister(2, "x"),
                qk.QuantumRegister(2, "y")
            ]

        else:
            raise ValueError(f"Invalid shift code: {shift}")
        
        self.extend(self.coinRegs)
        self.extend(self.shiftRegs)

    @property
    def num_qubits(self):
        return sum(reg.size for reg in self)
    
    @property
    def qubits(self):
        return [q for reg in self for q in reg]