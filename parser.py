from parse_tree import TreeNode

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

ROOT = TreeNode(None, "root")

def stack_top (stack):
  return stack[len(stack) - 1]


def is_terminal_symbol (token):
  return token in TERMINAL_TOKENS


def is_non_terminal_symboll (token):
  return token in NON_TERMINAL_TOKENS

def get_production(input_symbol, stack_symbol):
  rule_index = PARSING_TABLE[input_symbol][stack_symbol] - 1
  if (rule_index >= 0):
    return PRODUCTION_RULES[rule_index]
  else:
    return None


def initialize_stack():
  STACK.append('$')
  STACK.append(START_TOKEN)


def append_production(production):
  for i in range(len(production)):
    STACK.append(production[i])
    
def print_parse_tree(root, level =0):
  tab = ""
  for i in range(level):
    tab += " "
    
  if (root.children_count != 0):
    print(f"{tab}{root.token}: {'{'}")
    level += 1
    for child in root.children:
      print_parse_tree(child, level)
    print(f"{tab}{'}'}")
  else:
    print(f"{tab}{root.token}")
  


def parser (input):
  initialize_stack()
  cursor = 0
  end_of_input = input[cursor] == '$'
  ROOT.children_count = 1
  parent_stack = [ROOT]
  
  while(not end_of_input):
    print(STACK)
    stack_symbol = stack_top(STACK)
    
    if (is_terminal_symbol(stack_symbol)):
      if (stack_symbol == input[cursor]):
        tree_node = TreeNode(parent_stack[-1], STACK.pop())
        parent_stack[-1].children.append(tree_node)
        print(tree_node.token)
        
        if (parent_stack[-1].is_complete()):
          parent_stack.pop()
        
        cursor += 1
      else:
        end_of_input = True
        print("ERRO: erro de sintaxe. Sem correspondencia com simbolo terminal")
        
    elif (is_non_terminal_symboll(stack_symbol)):
      production = get_production(input[cursor], stack_symbol)
      if (production is None) :
        end_of_input = True
        print("ERRO: erro de sintaxe. Não existe produção possível")
      else:
        tree_node = TreeNode(parent_stack[-1], STACK.pop())
        print(tree_node.token)
        parent_stack[-1].children.append(tree_node)
        
        if (parent_stack[-1].is_complete()):
          parent_stack.pop()
          
        parent_stack.append(tree_node)
        
        if (production != EPSILON):  
          tree_node.append_children(production)    
          append_production(production[::-1])
        else:
          tree_node.children.append(TreeNode(tree_node, EPSILON))
          tree_node.children_count += 1
          parent_stack.pop()
      
    end_of_input = input[cursor] == '$'
    
    
parser('adb$') 
print_parse_tree(ROOT)
    