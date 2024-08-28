import pdb
import re
from collections import deque

'''
TODO: cambiar el sequence por initial state, y luego pasar otro parametro que sea la longitud total de la sequencia.
Parameters
---------
sequence -> initial sequence
'''
def verify_mfsr(sequence, minimal_recurrence, n_coefficients):
    m = n_coefficients
    len_seq = len(sequence)
    original_sequence = deque(sequence[:m]) # original_seq = coeficients

    i = m 
    while i < len_seq:
        copy_min_recur = minimal_recurrence
        for j in range(m):
            replace_value = original_sequence[-1-j]
            copy_min_recur = re.sub(r'x{}\b'.format(j), str(replace_value), copy_min_recur)
        res = eval(copy_min_recur) % 2
        original_sequence.append(res)
        i += 1
    return list(original_sequence)

'''
Parameters
----------
poly : string -> logic function/polynomio
values : list[int]

Returns
-------
the value of the function with those parameters
'''
def logic_poly_executer(poly, values):
    for i, v in enumerate(values):
        poly = re.sub(r'x{}\b'.format(i), str(v), poly)
    print(poly)
    print(values)
    return eval(poly)%2

        


