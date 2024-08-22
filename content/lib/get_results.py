from qiskit import transpile
from qiskit_aer import AerSimulator

def get_results(qc, shots=1000):

    backend = AerSimulator
    transpiled_circuit = transpile(qc, backend)
    result = backend.run(transpiled_circuit, shots=shots).result()   
    counts = result.get_counts()   
    return counts