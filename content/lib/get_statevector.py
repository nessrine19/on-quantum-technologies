from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit_aer import Aer

def get_statevector(circuit):
    simulator = Aer.get_backend('statevector_simulator')
    result = simulator.run(circuit.decompose(reps=6)).result()
    statevector=result.get_statevector(circuit)
    precision = 3
    current_quantum_state = [round(val, precision) for val in statevector]
    
    return current_quantum_state