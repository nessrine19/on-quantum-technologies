from qiskit import transpile
from qiskit_aer import AerSimulator

def get_statevector(circuit):
    simulator = AerSimulator()
    transpiled_circuit = transpile(circuit, simulator)
    result = simulator.run(transpiled_circuit).result()
    statevector=result.get_statevector(circuit)
    precision = 3
    current_quantum_state = [round(val, precision) for val in statevector]
    
    return current_quantum_state