from typing import ClassVar


class Ponto:
  def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z

class Vetor:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

class Segmento:
  def __init__(self,p1 : Ponto,p2 :Ponto):
    self.p1 = p1
    self.p2 = p2

class Reta:
  def __init__(self,p : Ponto, vetorDiretor : Vetor):
    self.ponto = p
    self.vetorDiretor = vetorDiretor

class Plano:
  def __init__(self,p : Ponto, vetorNormal : Vetor ):
    self.ponto = Ponto 
    self.vetorNormal = vetorNormal

class Esfera:
  def __init__(self,centro : Ponto , raio):
    self.centro = centro
    self.raio =raio

class Triangulo:
  def __init__(self,p1 : Ponto , p2 : Ponto, p3 : Ponto):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3

class Base:
  def __ini__(self,v1 :Vetor,v2 :Vetor ,v3 :Vetor):
    self.v1 : v1
    self.v2 : v2
    self.v3 : v3
