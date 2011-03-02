import sys

from pyparsing import Word, Suppress
from pyparsing import And, Or
from pyparsing import Literal, QuotedString
from pyparsing import Optional, alphas

# Some Standard tokens that we'll find in
# a BIND configuration.
stmt_term = Suppress(';')
block_start = Suppress('{')
block_term = Suppress('}') + stmt_term

def in_block(expr):
    """
    Sets a config value in a block.

    A block, in this case, is a curly-brace
    delimited chunk of configuration.
    """
    return block_start + expr + block_term

def in_quotes(name):
    """
    Puts a string in between quotes.
    """
    return QuotedString('"').setResultsName(name)

# Zone type, whether it's a master or a slave zone
# that we're loading.
type_ = Suppress('type') + \
    Or((Literal('master'), Literal('slave'))).setResultsName('type_') + stmt_term

# Zone file itself.
file_ = Suppress('file') + in_quotes("file") + stmt_term

# Where we can receive dynamic updates from.
allowed_from = Or((Literal('none'), Word(alphas + '.'))).setResultsName('update_from') + stmt_term

# Dynamic update line
allow = Suppress('allow-update') + in_block(allowed_from)

# Body can be in any order, we're not picky
# so long as they all appear.
body = type_ & file_ & allow

# define a zone configuration stanza
zone = Suppress('zone') + in_quotes("zone") + \
    Optional('IN', default='IN').setResultsName('class_') + in_block(body);

if __name__ == '__main__':
    for z in zone.searchString(open(sys.argv[1]).read(),):
        print("Zone %s(%s) will be loaded from %s as %s" % \
            (z.zone, z.class_, z.file, z.type_))

        # For debugging and example purposes
        print("Parser Scanned: %s" % z)
