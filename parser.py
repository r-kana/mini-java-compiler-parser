
EPSILON = 'ε'

STACK = []

PRODUCTION_RULES = [
  'aABb',
  'c',
  EPSILON,
  'd',
  EPSILON
]

NON_TERMINAL_TOKENS = [
  'S',
  'A',
  'B'
]

TERMINAL_TOKENS = [
  'a',
  'b',
  'c',
  'd',
  '$'
]

START_TOKEN = 'S'

PARSING_TABLE = {
  'a': {
    'S': 1,
    'A': 0,
    'B': 0
  },
  'b': {
    'S': 0,
    'A': 3,
    'B': 5
  },
  'c': {
    'S': 0,
    'A': 2,
    'B': 0
  },
  'd': {
    'S': 0,
    'A': 3,
    'B': 4
  },
  '$': {
    'S': 0,
    'A': 0,
    'B': 0
  }
}

def stack_top (stack):
  return stack[len(stack) - 1]


def is_terminal_token (token):
  return token in TERMINAL_TOKENS


def is_non_terminal_token (token):
  return token in NON_TERMINAL_TOKENS

def get_production(input_symbol, stack_token):
  rule_index = PARSING_TABLE[input_symbol][stack_token] - 1
  if (rule_index >= 0):
    return PRODUCTION_RULES[ rule_index ]
  else:
    return None


def initialize_stack():
  STACK.append('$')
  STACK.append(START_TOKEN)


def append_production(production):
  for i in range(len(production)):
    STACK.append(production[i])


def parser (input):
  initialize_stack()
  cursor = 0
  end_of_input = input[cursor] == '$'
  
  while(not end_of_input):
    print(STACK)
    stack_token = stack_top(STACK)
    
    if (is_terminal_token(stack_token)):
      if (stack_token == input[cursor]):
        print(STACK.pop())
        cursor += 1
      else:
        end_of_input = True
        print("ERRO: erro de sintaxe. Simbolo não corresponde a token terminal")
        
    elif (is_non_terminal_token(stack_token)):
      production = get_production(input[cursor], stack_token)
      if (production is None) :
        end_of_input = True
        print("ERRO: erro de sintaxe. Não existe produção para simbolo")
      else:
        print(STACK.pop())
        if (production != EPSILON):      
          append_production(production[::-1])
          
    else:
      end_of_input = True
      print("ERRO: símbolo inválido.")
      
    end_of_input = input[cursor] == '$'
parser('adb$') 
    