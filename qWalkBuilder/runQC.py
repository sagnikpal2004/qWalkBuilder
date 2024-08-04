import qiskit as qk
import qiskit_aer as qka

import numpy as np

def getUnitaryMatrix(qc: qk.QuantumCircuit):
  backend = qka.Aer.get_backend('unitary_simulator')
  t_qc = qk.transpile(qc, backend)
  job = backend.run(t_qc)
  
  return job.result().get_unitary()

def getStateVector(qc: qk.QuantumCircuit):
  backend = qka.Aer.get_backend('statevector_simulator')
  t_qc = qk.transpile(qc, backend)
  job = backend.run(t_qc)

  return job.result().get_statevector()

def qasm_simulator(qc: qk.QuantumCircuit, shots: int = 4096):
  qc.measure_all()

  backend = qka.Aer.get_backend('qasm_simulator')
  t_qc = qk.transpile(qc, backend)
  job = backend.run(t_qc, shots=shots)

  result_dict = dict(job.result().get_counts())
  result_dict = {key: value / shots for key, value in result_dict.items()}
  return result_dict


def basis_measurement(qc: qk.QuantumCircuit, basisList: list[list[complex]]):
  curState = getStateVector(qc)

  resultProbs = []
  for basis in basisList:
    curProb = np.abs(np.dot(basis, curState))**2
    resultProbs.append(curProb)
  return resultProbs

import qWalkBuilder.buildQC as buildQC
def eigenBasis_measurement(qc: qk.QuantumCircuit, coin: buildQC.Coin = buildQC.Coin.hadamard):
  shiftCoinQC = buildQC.build16nTQW(1, coin)
  shiftCoin = getUnitaryMatrix(shiftCoinQC).data
  eigenVectors = np.linalg.eig(shiftCoin)[1].T

  return basis_measurement(qc, eigenVectors)

def z_measurement(qc: qk.QuantumCircuit):
  zBasis = np.eye(64)
  return basis_measurement(qc, zBasis)


import csv
def writeToCSV(filename: str, time: int, data: list[float]):
  with open(filename, mode="a", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow([time] + data)

# def run16nTQW(time: int, coin=buildQC.hadamardCoin, init=buildQC.singleNodeInit, runQC=qasm_simulator):
#   results = []
#   for i in range(time):
#     qc = buildQC.build16nTQW(1, coin, init)
#     results.append(runQC(qc))
#     initUnitary = getUnitaryMatrix(qc)
  
#   filename = f"16nT.{coin.name}.{basis}"