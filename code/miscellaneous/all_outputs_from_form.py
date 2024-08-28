'''
Test to understand in depth patterns in logic formulas results
From a string representing a formula returns all
possible outputs from a formula
Autor: Pedro Castro
'''
import re
import sys
import itertools
from common.termcolor import GREEN, RED, ENDCOLOR

def logic_function(fn, inputs):
    for i, bool_input in enumerate(inputs):
        fn = re.sub(r'x{}\b'.format(i), str(bool_input), fn)
    return eval(fn) % 2



if __name__=="__main__":
    logic_formula = sys.argv[1]
    num_variables = int(sys.argv[2])
    for i in itertools.product([1, 0], repeat = num_variables):
        print(f"{GREEN}{i} {ENDCOLOR}-> {RED}{logic_function(logic_formula, i)}{ENDCOLOR}")
