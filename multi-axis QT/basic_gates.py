import sympy as sp
from sympy.physics.quantum import TensorProduct

# Symbolic variables
a, b = sp.symbols('a b')
input_q = sp.Matrix([[a], [b]])
ket_0 = sp.Matrix([[1], [0]])
ket_1 = sp.Matrix([[0], [1]])

# Define gates symbolically
I = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
H = (1/sp.sqrt(2)) * sp.Matrix([[1, 1], [1, -1]])
S = sp.Matrix([[1, 0], [0, sp.I]])
S_dg = sp.Matrix([[1, 0], [0, -sp.I]])
sqrt_X = (1/2) * sp.Matrix([[1 + sp.I, 1 - sp.I],
                            [1 - sp.I, 1 + sp.I]])
sqrt_X_dg = (1/2) * sp.Matrix([[1 - sp.I, 1 + sp.I],
                               [1 + sp.I, 1 - sp.I]])
CNOT = sp.Matrix([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])

# Expand Gate Matrix to 3 qubits
HII = TensorProduct(H, I, I)    # (H ⊗ I ⊗ I)
CNOT_I = TensorProduct(CNOT, I) # (CNOT ⊗ I)
I_CNOT = TensorProduct(I, CNOT) # (I ⊗ CNOT)
IHI = TensorProduct(I, H, I)    # (I ⊗ H ⊗ I)

inputs_3q = TensorProduct(input_q, ket_0, ket_0)
state_before_AB_entangle  =  I_CNOT * IHI * inputs_3q
state_before_measurement = HII * CNOT_I * state_before_AB_entangle
# sp.pprint(state_before_measurement, use_unicode=True)