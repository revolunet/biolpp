#============================================================
#   BioL++ Lexer
#============================================================


import ply.lex as lex


# reserved words
reserved = {
    'seq': 'SEQ',
    'comp': 'COMP',
    'rcomp': 'RCOMP',
    'transc': 'TRANSC',
    'rtransc': 'RTRANSC',
    'compf': 'COMPF',
    'rcompf': 'RCOMPF',
    'transcf': 'TRANSCF',
    'rtranscf': 'RTRANSCF',
    'transl': 'TRANSL',
    'read': 'READ',
    'write': 'WRITE',
    'ctable': 'CTABLE',
    'drawtree': 'DRAW',
    'rna': 'RTYPE',
    'dna': 'DTYPE',
    'print': 'PRINT',
    'hamdis': 'HAMDIS',
    'gccon': 'GCCON',
    'recur': 'RECUR',
    'rnainf': 'RNAINF',
    'rnainf2': 'RNAINF2',
    'orf': 'ORF',
    'protw': 'PROTW',
    'varlist': 'VARLIST',
    'motif': 'MOTIF',
    'punnett': 'PUNNETT',
    'wpunnett': 'WPUNNETT',
    'protinfer': 'PROTINFER'
}

# tokens
tokens = [
    'ID',
    'EQUALS',
    'LPAR',
    'RPAR',
    'STRING',
    'COMMA',
    'INT'
] + list(reserved.values())

# basic regex
t_EQUALS = r'\='
t_LPAR = r'\('
t_RPAR = r'\)'
t_COMMA = r'\,'
t_ignore = " \t"

# regex functions

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_INT(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR: INT overflow.")
        t.value = 0
    return t

def t_STRING(t):
    r'\'(.+?)\''
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error at line %d - unexpected expression '%s' " % (t.lexer.lineno, t.value[0]))
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\#.*'
    pass


# Lexer

lexer = lex.lex()

# Tester

# lexer.input("   bseq abc = btree .read()")
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
