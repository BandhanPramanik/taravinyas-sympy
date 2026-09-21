from sympy import symbols
from sympy.logic import *
from sympy.logic.boolalg import *
cs, cl, cr1, cr0, s, l, n, r, v, a = symbols('cs,cl,cr1,cr0,s,l,n,r,v,a')
minterms = [0, 1, 2, 6, 3, 7, 8, 16, 20, 32] # just add everything that's possible
variables = [s,l, n, r, v, a]
expr = SOPform(variables, minterms)
coarse = ~((s & ~cs) | (l & ~cl) | (r & ~cr0) | ((~s & ~l & ~n & r & v) & (~cr1 & cr0)) | ((~s & l & ~n & r & ~v & ~a) & (cr1 & cr0)))
invalid_all = Nand(expr, coarse)
dontcares = simplify_logic(invalid_all, force=True)
print("Invalid =", dontcares)
minterms_d3 = [{s: 1}]
minterms_d2 = [{v: 1, a: 1}, {n: 1}, {l: 1, r: 0}]
minterms_d1 = [{v: 1, a: 0}, {n: 1}, {l:1, r: 0}]
minterms_d0 = [{v:0, a:1}, {r:1, v:1}, {l:1, r: 0}, {s: 1}]
sop_d3 = SOPform(variables, minterms_d3)
sop_d2 = SOPform(variables, minterms_d2)
sop_d1 = SOPform(variables, minterms_d1)
sop_d0 = SOPform(variables, minterms_d0)
print("D3 =", simplify_logic(sop_d3, dontcare=dontcares))
print("D2 =", simplify_logic(sop_d2, dontcare=dontcares))
print("D1 =", simplify_logic(sop_d1, dontcare=dontcares))
print("D0 =", simplify_logic(sop_d0, dontcare=dontcares))

