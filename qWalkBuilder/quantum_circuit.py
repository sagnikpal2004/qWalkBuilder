import qiskit as qk
import qiskit_aer as qka
import numpy as np

from .utils import Result


class QuantumCircuit(qk.QuantumCircuit):
    
    def run(self, operation: str, **kwargs):
        if operation == "measure_basis":
            result = self.measure_basis(**kwargs)
        # elif operation == "measure_eigen":
        #     result = self.measure_eigen()
        elif operation == "measure_z":
            result = self.measure_z()
        else:
            raise ValueError()

        return Result(result)


    def measure_basis(self, basisList: list[list[complex]]):
        if basisList is None:
            raise ValueError()
        if len(basisList) != 2**self.num_qubits:
            raise ValueError()
        if any(len(basis) != 2**self.num_qubits for basis in basisList):
            raise ValueError()

        curState = self.getStateVector()

        resultProbs = []
        for basis in basisList:
            curProb = np.abs(np.dot(basis, curState))**2
            resultProbs.append(curProb)
        return resultProbs
    
    # TODO: Get shiftCoin unitary
    # def measure_eigen(self):
    #     shiftCoin =
    #     eigenVectors = np.linalg.eig(shiftCoin)[1].T

    #     return self.measure_basis(eigenVectors)
    
    def measure_z(self):
        zBasis = np.eye(2**self.num_qubits)
        return self.measure_basis(zBasis)


    def getUnitary(self):
        backend = qka.Aer.get_backend('unitary_simulator')
        t_qc = qk.transpile(self, backend)
        job = backend.run(t_qc)
        
        return job.result().get_unitary()
    
    def getState(self):
        backend = qka.Aer.get_backend('statevector_simulator')
        t_qc = qk.transpile(self, backend)
        job = backend.run(t_qc)

        return job.result().get_statevector()
    
    def simulate_qasm(self, shots: int = 4096):
        self.measure_all()

        backend = qka.Aer.get_backend('qasm_simulator')
        t_qc = qk.transpile(self, backend)
        job = backend.run(t_qc, shots=shots)

        result_dict = dict(job.result().get_counts())
        result_dict = {key: value / shots for key, value in result_dict.items()}
        return result_dict