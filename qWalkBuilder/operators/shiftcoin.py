from qiskit.circuit.library.standard_gates.x import XGate

from . import Operator


class ShiftCoin(Operator):

    def __init__(self, shiftCoin, qRegs):
        shift, coin = shiftCoin.split(".")

        self.coin = Coin(coin, qRegs)
        self.shift = Shift(shift, qRegs)

        super().__init__(*qRegs, name=shiftCoin)
        self.append(self.coin, self.qubits)
        self.append(self.shift, self.qubits)


class Shift(Operator):
    def __init__(self, shift, qRegs):
        c, x, y = qRegs
        super().__init__(*qRegs, name=shift)

        if shift == "16nT":
            self.append(XGate().control(3, ctrl_state="000"), [c[0],c[1],x[0], x[1]])
            self.append(XGate().control(2, ctrl_state= "00"), [c[0],c[1],      x[0]])
            self.append(XGate().control(3, ctrl_state="110"), [c[0],c[1],x[0], x[1]])
            self.append(XGate().control(2, ctrl_state= "10"), [c[0],c[1],      x[0]])

            self.append(XGate().control(3, ctrl_state="001"), [c[0],c[1],y[0], y[1]])
            self.append(XGate().control(2, ctrl_state= "01"), [c[0],c[1],      y[0]])
            self.append(XGate().control(3, ctrl_state="111"), [c[0],c[1],y[0], y[1]])
            self.append(XGate().control(2, ctrl_state= "11"), [c[0],c[1],      y[0]])
        
        else:
            raise ValueError(f"Invalid shift code: {shift}")
        
    
class Coin(Operator):
    def __init__(self, coin, qRegs):
        c, x, y = qRegs
        super().__init__(*qRegs, name=coin)
        
        if coin == "H":
            self.h(c)
        else:
            raise ValueError(f"Invalid coin code: {coin}")