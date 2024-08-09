from . import Operator

# TODO: add support for qk.quantum_info.StateVector and qk.QuantumCircuit.set_statevector
class Init(Operator):
    def __init__(self, init, qRegs):
        c, x, y = qRegs
        super().__init__(*qRegs, name=init)

        if init == "uniform":
            self.h(qRegs.qubits)
        elif init == "single":
            pass
        else:
            raise ValueError(f"Invalid init code: {init}")