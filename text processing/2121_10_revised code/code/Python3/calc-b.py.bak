import sys
import operator
from pyparsing import nums, oneOf, Word
from pyparsing import ParseException

# Map math operations to callable functions within
# the operator module.
op_map = {
    '*': operator.mul,
    '+': operator.add,
    '/': operator.div,
    '-': operator.sub
}

def to_i(s, loc, toks):
    """Translate to int"""
    return int(toks[0])

# define grammar
MATH_GRAMMAR = Word(nums).setResultsName('first_term').setParseAction(to_i) + \
    oneOf('+ - / *').setResultsName('op') + \
    Word(nums).setResultsName('second_term').setParseAction(to_i)

def handle_line(line):
    """
    Parse a newly read line.
    """
    result = MATH_GRAMMAR.parseString(line)
    return op_map[result.op](result.first_term, 
        result.second_term)

while True:
    try:
        print handle_line(raw_input('> '))
    except ParseException, e:
        print >>sys.stderr, \
            "Syntax err at position %d: %s" % (e.col, e.line)

