import numpy as np
import qiskit as qk
import qWalkBuilder.runQC as runQC

def getEigenValues(qc: qk.QuantumCircuit) -> np.ndarray:
  unitaryMatrix = runQC.getUnitaryMatrix(qc)
  return np.linalg.eigvals(unitaryMatrix)

def getEigenProbabilities(qc: qk.QuantumCircuit, round: int = 12) -> np.ndarray:
  eigenValues = getEigenValues(qc)
  eigenValues = np.round(eigenValues, round)
  uniqueElements, elementCounts = np.unique(eigenValues, return_counts=True)
  return elementCounts / np.sum(elementCounts)

def getEigenEntropy(qc: qk.QuantumCircuit, round: int = 12) -> float:
  eigenProbabilities = getEigenProbabilities(qc, round)
  return calcEntropy(eigenProbabilities)

def calcEntropy(probabilities: list[float]) -> float:
  probabilities = [p for p in probabilities if p != 0]
  
  if not np.isclose(np.sum(probabilities), 1.0):
    raise ValueError("Probabilities must sum to 1")
  return -np.sum(probabilities * np.log2(probabilities))