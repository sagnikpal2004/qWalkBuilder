import qiskit as qk
from qiskit.circuit.library.standard_gates.x import XGate

import numpy as np

class Coin:
  hadamard = qk.QuantumCircuit(2); hadamard.h([0,1])
  # grover = qk.QuantumCircuit(2)

class Init:
  singleNode = qk.QuantumCircuit(4)
  horizontalLine = qk.QuantumCircuit(4); horizontalLine.h([0,1])
  diagonalLine = qk.QuantumCircuit(4); diagonalLine.h([0,1]); diagonalLine.cx([0,1], [2,3])
  #W = qk.QuantumCircuit(4); W.initialize([0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0], [0,1,2,3], True)
  #EdgesNotCorners = qk.QuantumCircuit(4); EdgesNotCorners.initialize([0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0], [0,1,2,3], True)
  

class Init6:
  maxEigenEntropyInitializer = [ 
   1.98039331e-01+0.01973055j, -3.81324819e-02-0.03968678j,
   9.14349504e-02-0.05772577j, -6.65219460e-02-0.14920015j,
   1.46444890e-01+0.06027131j, -4.12036168e-02+0.02586924j,
   1.36021204e-01+0.02293832j,  2.68038165e-01+0.04295862j,
   5.55996721e-02+0.01948801j,  7.52794732e-02-0.12679261j,
   8.30552033e-03-0.06737816j,  3.17761622e-02+0.02603888j,
   1.74018614e-01-0.03340608j,  1.51248398e-01-0.02618669j,
  -1.86082524e-02+0.04211266j, -1.31456828e-01+0.06568772j,
   5.30941285e-02+0.03756515j, -1.25933282e-01-0.11651575j,
   1.25042298e-01+0.054479j  ,  2.18760861e-02+0.01762044j,
  -2.70003738e-02+0.06038319j, -8.95231381e-02+0.15123338j,
   6.19475955e-02-0.0523341j ,  2.63743531e-02+0.14219617j,
   1.94271967e-02+0.03575628j, -1.70315020e-02-0.00678787j,
   3.84233650e-03-0.10487711j,  6.02771641e-02+0.1002023j,
  -1.30812102e-01+0.04678522j, -5.90283625e-03-0.1350987j,
  -5.43027661e-03-0.07075171j, -8.02321847e-02+0.00080591j,
   5.40726557e-02-0.02397119j, -6.00738683e-02-0.03781652j,
   1.99272588e-01+0.00653483j,  1.39109507e-01-0.0742124j,
  -3.84713187e-02+0.03000728j,  1.29787365e-02-0.0426817j,
   9.53713091e-03-0.02303252j, -1.25032107e-01-0.00072905j,
   8.10878733e-02+0.02464935j, -1.12383906e-01-0.01081598j,
   8.11651592e-02-0.04400814j, -5.55471044e-02-0.00761686j,
  -6.61902396e-02+0.03983244j,  2.83628788e-02+0.08466651j,
  -3.33593956e-02-0.01013517j,  2.93222415e-02-0.04085608j,
   1.29284702e-01-0.21469524j,  1.50480570e-04-0.1154126j,
   5.81387458e-02+0.08197949j, -7.48971723e-02+0.02064233j,
   1.70165066e-01+0.06707509j, -1.30748547e-01+0.02827407j,
   1.06239752e-01+0.13754193j, -5.59914824e-02+0.01530263j,
  -5.20398908e-02-0.03705126j, -4.84034908e-03+0.23883003j,
   1.11861265e-01-0.0185267j , -9.77725965e-02-0.03674129j,
   6.29546519e-02-0.03925193j,  1.08996874e-01+0.18122541j,
   6.42592881e-02+0.00628651j, -3.52173387e-02+0.02563533j,
  ]
  maxEigenEntropy = qk.QuantumCircuit(6)
  maxEigenEntropy.initialize(maxEigenEntropyInitializer, [0,1,2,3,4,5], True)

  minEigenEntropyInitializer = [
 -2.50000000e-01-1.40165657e-15j, -6.76542156e-16+3.63271264e-02j,
  1.38083989e-15-1.53884177e-01j, -1.11803399e-01-2.35922393e-16j,
  5.87785252e-02-1.80901699e-01j, -3.63271264e-02-1.11803399e-01j,
  1.17557050e-01+1.24206201e-15j,  1.53884177e-01-1.11803399e-01j,
  1.11803399e-01+1.23512311e-15j,  1.11803399e-01+2.35922393e-16j,
 -1.06165077e-15+1.53884177e-01j, -5.82867088e-16+1.53884177e-01j,
  5.87785252e-02+1.80901699e-01j, -4.03752616e-16+2.53518600e-16j,
 -1.90211303e-01-9.85322934e-16j,  1.97113220e-16-7.71498972e-16j,
  9.51056516e-02+6.90983006e-02j, -6.38732684e-16+2.26388592e-17j,
  3.10452917e-16-4.33765929e-16j,  1.53884177e-01+1.11803399e-01j,
 -1.23859256e-15+3.63271264e-02j, -1.11803399e-01-1.59594560e-16j,
  4.14598911e-16+3.63271264e-02j, -1.11803399e-01-4.92661467e-16j,
 -9.51056516e-02+6.90983006e-02j,  3.63271264e-02-1.11803399e-01j,
  4.33028456e-16-1.98581914e-16j,  1.26725553e-16-5.82472925e-16j,
  3.74700271e-16-1.53884177e-01j,  2.35922393e-16+3.63271264e-02j,
  6.59194921e-17+3.63271264e-02j,  4.23272528e-16-1.53884177e-01j,
 -1.11803399e-01-1.33226763e-15j, -1.11803399e-01-2.84494650e-16j,
  7.49400542e-16-1.53884177e-01j,  5.27355937e-16-1.53884177e-01j,
 -5.87785252e-02-1.80901699e-01j,  5.29636831e-16-2.83470590e-16j,
  1.90211303e-01+8.32667268e-16j,  6.95229252e-16+7.18647806e-16j,
  2.50000000e-01+0.00000000e+00j,  1.45716772e-16-3.63271264e-02j,
 -8.18789481e-16+1.53884177e-01j,  1.11803399e-01+2.91433544e-16j,
 -5.87785252e-02+1.80901699e-01j,  3.63271264e-02+1.11803399e-01j,
 -1.17557050e-01-4.92661467e-16j, -1.53884177e-01+1.11803399e-01j,
  9.51056516e-02-6.90983006e-02j, -3.63271264e-02+1.11803399e-01j,
  4.13116430e-16-7.15697365e-16j, -2.84101914e-16+1.22690542e-16j,
 -2.70616862e-16+1.53884177e-01j,  2.28983499e-16-3.63271264e-02j,
  4.99600361e-16-3.63271264e-02j, -2.01227923e-16+1.53884177e-01j,
 -9.51056516e-02-6.90983006e-02j,  6.16442777e-16-4.35960122e-17j,
 -2.79116123e-16+4.50672653e-16j, -1.53884177e-01-1.11803399e-01j,
 -2.11636264e-16-3.63271264e-02j,  1.11803399e-01+6.31439345e-16j,
 -9.28077060e-16-3.63271264e-02j,  1.11803399e-01+4.51028104e-16j,
 ]
  minEigenEntropy = qk.QuantumCircuit(6)
  minEigenEntropy.initialize(minEigenEntropyInitializer, [0,1,2,3,4,5], True)


def build16nTQW(time: int, coin: Coin = Coin.hadamard, init: Init = Init.singleNode, init6: Init6 = None) -> qk.QuantumCircuit:
  """ 
  Builds a 16-node Torus Quantum Walk 
      
  Args:
    time (int): number of time steps to run the walk for
    coin (buildQC.Coin): the coin to use for the walk. Defaults to a Hadamard coin
    init (buildQC.Init): the initialization to use for the walk. Defaults to singleNode 
  Returns:  
    qiskit.QuantumCircuit: the quantum circuit for the walk
  """
  coin.name = "coin"
  init.name = "init"
  if init6:
    init6.name = "init6"

  # Quantum circuit setup
  c = qk.QuantumRegister(2, "c")  #control bits
  x = qk.QuantumRegister(2, "x")  #x bits
  y = qk.QuantumRegister(2, "y")  #y bits
  qc = qk.QuantumCircuit(c, x, y)

  # Setup Quantum Walk

  #Initialize
  if not init6:
    qc.append(init, [x[0], x[1], y[0], y[1]])
  else:
    qc.append(init6, [0,1,2,3,4,5])

  for i in range(time):
    qc.append(coin, [c[0], c[1]]) #Coin

    # Shift
    qc.append(XGate().control(3, ctrl_state="000"), [c[0],c[1],x[0], x[1]])
    qc.append(XGate().control(2, ctrl_state= "00"), [c[0],c[1],      x[0]])
    qc.append(XGate().control(3, ctrl_state="110"), [c[0],c[1],x[0], x[1]])
    qc.append(XGate().control(2, ctrl_state= "10"), [c[0],c[1],      x[0]])

    qc.append(XGate().control(3, ctrl_state="001"), [c[0],c[1],y[0], y[1]])
    qc.append(XGate().control(2, ctrl_state= "01"), [c[0],c[1],      y[0]])
    qc.append(XGate().control(3, ctrl_state="111"), [c[0],c[1],y[0], y[1]])
    qc.append(XGate().control(2, ctrl_state= "11"), [c[0],c[1],      y[0]])

  return qc



def printCircuit(qc: qk.QuantumCircuit):
  print(qc.draw(output='text'))
def drawCircuit(qc: qk.QuantumCircuit):
  qc.draw(output='mpl').show()

