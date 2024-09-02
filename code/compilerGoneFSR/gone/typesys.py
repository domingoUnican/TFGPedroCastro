# gone/typesys.py
'''
Gone Type System
================
This file implements basic features of the Gone type system.  There is
a lot of flexibility possible here, but the best strategy might be to
not overthink the problem.  At least not at first.  Here are the
minimal basic requirements:

1. Types have names (e.g., IntType, FloatType, 'char')
2. Types have to be comparable. (e.g., int != float).
3. Types support different operators (e.g., +, -, *, /, etc.)

To deal with all this initially, I'd recommend representing types
as simple strings.  Make tables that represent the capabilities
of different types. Make some utility functions that check operators.
KEEP IT SIMPLE. REPEAT. SIMPLE.

'''
class Type:
    name = "type"
    pass

class BoolType(Type):
    name = "bool"
    pass

class FloatType(Type):
    name = "float"
    pass

class IntType(Type):
    name = "int"
    pass
    
class CharType(Type):
    name = "char"
    pass

class StringType(Type):
    name = "string"
    pass

# List of builtin types.  These will get added to the symbol table
builtin_types = [ IntType, FloatType, CharType, BoolType, StringType]

# Dict mapping all valid binary operations to a result type
_supported_binops = {
    # Logical operators
    (BoolType, '&&', BoolType) : BoolType,
    (BoolType, '||', BoolType) : BoolType,
    (BoolType, '==', BoolType) : BoolType,
    (BoolType, '!=', BoolType) : BoolType,
    # Comparison
    (IntType , '<', IntType) : BoolType,
    (IntType , '<=', IntType) : BoolType,
    (IntType, '>', IntType) : BoolType,
    (IntType, '>=', IntType) : BoolType,
    (IntType, '==', IntType) :BoolType,
    (IntType, '!=', IntType) : BoolType,
    (FloatType , '<', FloatType) : BoolType,
    (FloatType , '<=', FloatType) : BoolType,
    (FloatType, '>', FloatType) : BoolType,
    (FloatType, '>=', FloatType) : BoolType,
    (FloatType, '==', FloatType) : BoolType,
    (FloatType, '!=', FloatType) : BoolType,
    # characters are comparable
    (CharType , '<', CharType) : BoolType,
    (CharType , '<=', CharType) : BoolType,
    (CharType, '>', CharType) : BoolType,
    (CharType, '>=', CharType) : BoolType,
    (CharType, '==', CharType) : BoolType,
    (CharType, '!=', CharType) : BoolType,

    # Arithmetics
    (IntType, '+', IntType) : IntType,
    (IntType, '-', IntType) : IntType,
    (IntType , '*', IntType) : IntType,
    (IntType, '/', IntType) : IntType,
    (FloatType, '+', FloatType): FloatType,
    (FloatType, '-', FloatType) : FloatType,
    (FloatType, '*', FloatType): FloatType,
    (FloatType, '/', FloatType) : FloatType
    
    }

# Dict mapping all valid unary operations to result type
_supported_unaryops = {
    # Arithmetics
    ('-', IntType) : IntType,
    ('+', IntType) : IntType,
    ('-', FloatType) : FloatType,
    ('+', FloatType) : FloatType,

    # Logical
    ('!', BoolType) : BoolType
    }
    
def check_binop(left_type, op, right_type):
    ''' 
    Check the validity of a binary operator. 
    '''
    return _supported_binops.get((left_type, op, right_type))

def check_unaryop(op, type):
    '''
    Check the validity of a unary operator. 
    '''
    return _supported_unaryops.get((op, type))

def printType(type):
    strtypes = {None: "None", FloatType: "float", IntType: "int", CharType: "char", BoolType: "bool", 'type': 'type'}
    return strtypes[type]



