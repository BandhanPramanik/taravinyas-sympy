# SPDX-License-Identifier: BSD-3-Clause
from evaluate_truth_table import find_minterms
from sympy import symbols
from sympy.logic import *
from sympy.logic.boolalg import *

# change this
cs, cl, cr1, cr0, s, l, n, r, v, a = symbols('cs,cl,cr1,cr0,s,l,n,r,v,a')
minterms = [0, 1, 2, 6, 3, 7, 8, 16, 20, 32] # just add everything that's possible
variables = [s,l, n, r, v, a]

dontcare_minterms = list(set(range(2**len(variables))) - set(minterms))
expr = SOPform(variables, minterms)
dontcare_expr = SOPform(variables, dontcare_minterms)

# change this
output = [i for i in range(len(minterms))]
length = len(minterms).bit_length()
minterms_d = find_minterms(output, minterms, length)
sop_d = []
for i in minterms_d:
    sop_d.append(SOPform(variables, i))
for i, final_expr in enumerate(sop_d):
    print("D" + str(i) + " =", simplify_logic(final_expr,dontcare=dontcare_expr, force=True))

# change this and write ALL the states that are allowed for a set of variables. AND has been used for restriction
coarse = expr & (
        (~r | ~cr1 | cr0) &
        (~s | cs) &
        (~l | cl) &
        (~r | cr0) &
        (~(~s & ~l & ~n & r & v) | (cr1 & cr0)) &
        (~(~s & l & ~n & r & ~v & ~a) | (~cr1 & cr0)) &
        Exclusive(s, l, n, (v | a))
        )
invalid_all = Not(coarse)
invalid_all = simplify_logic(invalid_all, force=True)
print("Invalid =", invalid_all)


