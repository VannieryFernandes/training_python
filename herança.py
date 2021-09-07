class Veiculo:
 def __init__(self, tipo, modelo, km):
  self.tipo = tipo
  self.modelo = modelo
  self.km = km
  
class Carro (Veiculo):
 def __init__(self, tipo, modelo, km, portas):
  Veiculo.__init__(self, tipo, modelo, km)
  self.portas = portas
 
 def exibe(self):
  print(self.tipo, "modelo", self.modelo, "com", self.km, 
     "km rodados e", self.portas, "portas.")
  
class Moto (Veiculo):
 def __init__(self, tipo, modelo, km, cilindradas):
  Veiculo.__init__(self, tipo, modelo, km)
  self.cilindradas = cilindradas

 def exibe(self):
    print(self.tipo, "modelo", self.modelo, "com", self.km, 
     "km rodados e", self.cilindradas, " cilindradas.")
 


#palio = Carro("Carro", "Palio", "10000", 2)
#palio.exibe()

cbr = Moto("Moto", "Yamnha", "12000", "50")
cbr.exibe()