import qiskit as qk


class Init(qk.QuantumCircuit):
    def __init__(self, init, qRegs):
        c, x, y = qRegs
        super().__init__(*qRegs)

        if init == "uniform":
            self.h(qRegs.qubits)
        elif init == "single":
            pass
        else:
            raise ValueError(f"Invalid init code: {init}")
        
        self.name = init