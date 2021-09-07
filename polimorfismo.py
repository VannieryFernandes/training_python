class Super:
 def hello(self):
  print("Olá, sou a superclasse!")
  
class Sub (Super):
 def hello(self,s:str):
  print(f'Olá, sou a subclasse e tenbho {s} reais')

class Subsub (Sub):
 def hello(self,n:int):
  print(f'Olá, sou a subclasse e tenho {n} reais')

teste = Subsub()
teste2 = Sub()
teste2.hello("trinta")
#teste.hello(2)