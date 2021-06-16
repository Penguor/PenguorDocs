from pygments.lexer import RegexLexer
from pygments.token import *


class PenguorLexer(RegexLexer):
    name = 'Penguor'
    aliases = ['penguor']
    filenames = ['*.pgr']

    tokens = {
        'root': [
            #keywords
            
            # builtin types
            (r'(?<!\w)(i8|i16|i32|i64|u8|u16|u32|u64|f32|f64|char|str|bool|void)(?!\w)', Keyword.Type),

            (r'(?<!\w)(true|false|null)(?!\w)', Keyword.Constant),
            (r'(?<!\w)(return|if|else|while|do|for|switch|case|default)(?!\w)', Keyword.Reserved),
            
            # names
            (r'[A-Za-z_]\w*\s*(?=\()', Name.Function),
            (r'(?<=system)\s+[A-Za-z_]\w*', Name.Class),
            (r'(?<=data)\s+[A-Za-z_]\w*', Name.Class),
            (r'(?<=type)\s+[A-Za-z_]\w*', Name.Class),
            
            # comments
            (r'//.*?$', Comment.Single),
            (r'/\*.*\*/', Comment.Multiline),
            
            # numbers
            (r'(?<![A-Za-z])(\d*\.\d+|\d+\.\d+)', Number.Float),
            (r'(?<![A-Za-z\.\d])\d+(?!\.)', Number.Integer),
            (r'0h[0-9A-Fa-f]+', Number.Hex),
            (r'0b[01]+', Number.Bin),
            (r'0o[0-7]+', Number.Oct),
            (r'0x[0-9A-Za-z]+', Number),
            
            # strings
            (r"'.'", String.Char),
            (r'"(.*?)"', String.Double)
        ]
    }
