import itertools, time, re

def formula(f):
  if f: 
    value = f.pop()
    if value == 0:
      return f'{formula(f)} + {formula(f)}'
    elif value == 1:
      return f'{formula(f)} * {formula(f)}'
    elif value == 2:
      return f'(1 + {formula(f)})'
    else:
      return f'x{value-3}'
  else:
    return "S"

def evaluation(f, values):
    '''
    mucho mas lento esto que la recursividad, probablemente por las busquedas de las expresiones
    regulares
    '''
    for i, v in enumerate(values):
        f = re.sub(r'x{}\b'.format(i), str(v), f)
    return eval(f) % 2
  
def calc_all_form_results(num_variables, num_op):
    tiempo = time.time()
    all_eval = set()
    for t in itertools.product(range(num_variables + 3), repeat=num_op):
        string = formula(list(t))
        if 'S' not in string:
            result = []
            for values in itertools.product([0, 1], repeat=num_variables):
                result.append(evaluation(string, values))
            all_eval.add(tuple(result))
    return time.time() - tiempo, len(all_eval)
