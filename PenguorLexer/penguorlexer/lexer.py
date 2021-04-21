from pygments.lexer import RegexLexer
from pygments.token import *


class PenguorLexer(RegexLexer):
    name = 'Penguor'
    aliases = ['penguor']
    filenames = ['*.pgr']

    tokens = {
        'root': [
            (r'[A-Za-z_]\w*(?=\()', Name.Function),
            (r'(?<=system)\s+[A-Za-z_]\w*', Name.Class),
            (r'(?<=data)\s+[A-Za-z_]\w*', Name.Class),
            (r'(?<=type)\s+[A-Za-z_]\w*', Name.Class),
            (r'//.*?$', Comment.Single),
            
        ]
    }
