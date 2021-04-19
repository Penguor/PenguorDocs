from pygments.lexer import RegexLexer
from pygments.token import *

class CustomLexer(RegexLexer):
    name = 'Penguor'
    aliases = ['penguor']
    filenames = ['*.pgr']
    
    tokens = {
        'root': []
    }