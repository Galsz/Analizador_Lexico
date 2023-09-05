import os 
import string

os.system('cls')

def __init__(self):
    self.operadores = [':=', '==', '<<', '<=', '>>', '>=', '&&', '||']
    self.operadores_matematicos = ['+', '-', '/', '*', '^']


arquivo_e = open('Files/programa.txt', 'rb')
arquivo_s = open('Files/resp_lex.txt', 'wb')

lines = arquivo_e.readlines()


for line in lines: 
    linedeco = line.decode('UTF-8')
    line = linedeco.split()

   
    print(line)


