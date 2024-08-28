import re
def prepare_form(f, n_variables):
    rep_val = 5
    for i in range(n_variables):
        f = re.sub(r'x{}\b'.format(i), str(rep_val), f)
        rep_val += 1
    return f
    #return re.findall(r'\d+|[()+*]', f) # useful when u want to pass it to int list

def form_to_intlst(f):
    '''
    0 <- +
    1 <- *
    2 <- neg
    3 <- 0
    4 <- 1
    else -> x>4
    '''
    map_symbols = {
            '+': 0,
            '*': 1,
            '0': 3,
            '1': 4
            }
    intlst = []
    val = f.pop(0)
    while val:
        if val == '(':
            var = f.pop(0)
            f = f[3:]
            intlst.append(2)
            intlst.append(int(var))
        else:
            intlst.append(map_symbols[val] if val in map_symbols.keys() else int(val))
        val = f.pop(0) if f else None
    return intlst

def poly_to_intlst(poly, n_var):
    '''
    Transforms the original string into a int list
    '''
    return form_to_intlst(prepare_form(poly, n_var))

if __name__=="__main__":
    '''
    Ejemplo de uso
    '''
    form = "0+x0*x1+(x0+1)*x1"
    print(form)
    n_variables = 2
    prepared_form = prepare_form(form, n_variables)
    print(prepared_form)
