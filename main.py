class Pilha:
  """Esta classe representa uma pilha."""

  def __init__(self):
      self.items = []

  def __repr__(self):
      return "[" + " -> ".join(map(str, self.items)) + "]"

  def insere(self, novo_dado):
      """Insere um elemento no topo da pilha."""
      self.items.append(novo_dado)

  def remove(self):
      """Remove o elemento que está no topo da pilha."""
      if not self.esta_vazia():
          return self.items.pop()

  def topo(self):
      """Retorna o elemento do topo da pilha."""
      if not self.esta_vazia():
          return self.items[-1]

  def esta_vazia(self):
      """Verifica se a pilha está vazia."""
      return len(self.items) == 0


tabela_analise = {
  "S": {"a": "aA", "b": "", "$": ""},
  "A": {"a": "", "b": "bB", "$": "ϵ"},
  "B": {"a": "aA", "b": "bS", "$": ""}
}


def analise_sintatica(palavra):
  pilha = Pilha()
  pilha.insere("$")
  pilha.insere("S")
  i = 0
  while pilha:
      if i >= len(palavra):# A análise falha se a palavra acabar antes da pilha
          return False  
      #verifica se o topo da pilha é terminal
      if pilha.topo() == 'a' or pilha.topo() == 'b': 
          if pilha.topo() == palavra[i]:
              pilha.remove()
              i += 1
      #verifica se o topo da pilha é não-terminal
      elif pilha.topo() == 'S' or pilha.topo() == 'A' or pilha.topo() == 'B':
          #verifica na tabela de análise se existe uma produção
          producao = tabela_analise[pilha.topo()].get(palavra[i], None)
         #Se não há produção definida para o símbolo, a palavra não pertence à linguagem
          if producao is None:
              return False  
          elif producao == 'ϵ': # Se a produção for 'ϵ' apenas removemos A da pilha
              pilha.remove()
          #Se não existe produção na tabela, a palavra não pertence à linguagem
          elif producao == "":
              return False
          else:
              pilha.remove()
              for simbolo in reversed(producao):
                  pilha.insere(simbolo)
      elif pilha.topo() == "$":
          if palavra[i] == "$":
              return True
      else:
          return False
  return False


#recebe a palavra e cocatena com $ no fim
palavra = input("Insira a cadeia a ser avaliada: ") + "$"
    
if analise_sintatica(palavra):
  print("A palavra %s pertence à linguagem." % palavra)
else:
  print("A palavra %s não pertence à linguagem." % palavra)

  
