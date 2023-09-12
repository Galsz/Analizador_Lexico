import os 
import re

os.system('cls')

tokens = [
    ('PALAVRAS_RESERVADAS', r'DEFINICOES|FIM|INICIO|LEIA|IF|ELSE|PRINT'),
    ('VAR_INT', r'varINT[A-Za-z0-9_]{1,12}'),
    ('VAR_FLT', r'varFLT[A-Za-z0-9_]{1,12}'),
    ('OPERADOR_MAT', r'[+\-/*^]'),
    ('OPERADOR_LOGICOS', r':=|==|<<|<=|>>|>=|&&|\|\|'),
    ('INICIO_ESTRUTURA', r':'),
    ('TERMINO_ESTRUTURA', r';')
]


token_maps = {
    'PALAVRAS_RESERVADAS': {},
    'VAR_INT': {},
    'VAR_FLT': {},
    'OPERADOR_MAT': {},
    'OPERADOR_LOGICOS': {},
    'INICIO_ESTRUTURA': {},
    'TERMINO_ESTRUTURA': {}
}

def tokenize(code):
    tokens_found = []
    errors = []
    input_string = code.strip()  

    while input_string:
        matched = False
        for token_type, pattern in tokens:
            match = re.match(pattern, input_string)
            if match:
                value = match.group(0)
                if value not in token_maps[token_type]:
                    token_maps[token_type][value] = len(token_maps[token_type]) + 1
                tokens_found.append((token_type, token_maps[token_type][value]))
                input_string = input_string[len(value):].strip()
                matched = True
                break
        
        if not matched:
            error_match = re.match(r'\S+', input_string)
            if error_match:
                error_value = error_match.group(0)
                errors.append(error_value)
                input_string = input_string[len(error_value):].strip()

    return tokens_found, errors

def analyze_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    tokens, errors = tokenize(source_code)

    with open('Files\\resp_lex.txt', 'w') as f:
        token_line = 1

        for token_type, value in tokens:
            f.write(f"{token_line}. {token_type}: {value}\n")
            token_line += 1
        
        if errors:
            f.write("\n")
            for error in errors:
                f.write(f"{token_line}. ERRO: {error}\n")
                token_line += 1

input_file = 'Files\\programa.txt'
analyze_file(input_file)