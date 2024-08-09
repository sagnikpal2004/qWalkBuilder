import qiskit as qk
import qiskit_aer as qka
import numpy as np


# TODO: Implement way to convert numpy array to qiskit QuantumCircuit
class Operator(qk.QuantumCircuit):
    
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
    
    def getEigen(self):
        unitary = self.getUnitary()

        x = np.linalg.eig(unitary)
        return x[0], x[1].T