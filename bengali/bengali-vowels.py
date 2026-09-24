# SPDX-License-Identifier: BSD-3-Clause
# TODO: the entire thing; bengali consonants aren't complete yet
from evaluate_truth_table import find_minterms
from sympy import symbols
from sympy.logic import *
from sympy.logic.boolalg import *

# change this
vi, h, m = symbols('vi, h, m')
variables = [h, m]
minterms = [0, 1, 2]

dontcare_minterms = list(set(range(2**len(variables))) - set(minterms))
expr = SOPform(variables, minterms)
dontcare_expr = SOPform(variables, dontcare_minterms)

# change this
output = [i for i in range(len(minterms))]

length = len(minterms).bit_length()
minterms_s = find_minterms(output, minterms, length)
sop_s = []
for i in minterms_s:
    sop_s.append(SOPform(variables, i))
for i, final_expr in enumerate(sop_s):
    print("S" + str(i) + " =", simplify_logic(final_expr, dontcare=dontcare_expr))

# change this
coarse = expr & ~(h & ~vi)

invalid_all = Not(coarse)
invalid_all = simplify_logic(invalid_all)
print("Invalid =", invalid_all)


