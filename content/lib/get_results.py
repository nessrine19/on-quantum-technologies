# from qiskit import Aer
from qiskit_aer import Aer

def get_results(qc, shots=1000):

    backend = Aer.get_backend('statevector_simulator')
    result = backend.run(qc.decompose(reps=6), shots=shots).result()   
    counts = result.get_counts()   
    return counts