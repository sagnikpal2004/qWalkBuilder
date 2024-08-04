import qiskit as qk
import qiskit_aer as qka
import numpy as np


class QuantumCircuit(qk.QuantumCircuit):
    def run(self):
        pass


    def basis_measurement(self, basisList: list[list[complex]]):
        curState = self.getStateVector()

        resultProbs = []
        for basis in basisList:
            curProb = np.abs(np.dot(basis, curState))**2
            resultProbs.append(curProb)
        return resultProbs
    
    # TODO: Get shiftCoin unitary
    # def eigenBasis_measurement(self):
    #     shiftCoin =
    #     eigenVectors = np.linalg.eig(shiftCoin)[1].T

    #     return self.basis_measurement(eigenVectors)
    
    def z_measurement(self):
        zBasis = np.eye(2**self.num_qubits)
        return self.basis_measurement(zBasis)


    def getUnitaryMatrix(self):
        backend = qka.Aer.get_backend('unitary_simulator')
        t_qc = qk.transpile(self, backend)
        job = backend.run(t_qc)
        
        return job.result().get_unitary()
    
    def getStateVector(self):
        backend = qka.Aer.get_backend('statevector_simulator')
        t_qc = qk.transpile(self, backend)
        job = backend.run(t_qc)

        return job.result().get_statevector()
    
    def qasm_simulator(self, shots: int = 4096):
        self.measure_all()

        backend = qka.Aer.get_backend('qasm_simulator')
        t_qc = qk.transpile(self, backend)
        job = backend.run(t_qc, shots=shots)

        result_dict = dict(job.result().get_counts())
        result_dict = {key: value / shots for key, value in result_dict.items()}
        return result_dict