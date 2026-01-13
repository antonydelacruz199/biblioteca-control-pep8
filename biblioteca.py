class Biblioteca:
 def __init__(self,name):
  self.name = name
  self.libros = []

 def addb(self,book):
  self.libros.append(book)

 def show(self):
  for libro in self.libros:
   print(libro.titulo,libro.autor,libro.indice)

class Book:
 def __init__(self,titulo,autor,indice):
  self.titulo = titulo
  self.autor = autor
  self.indice = indice
  self.exist = True

 def lend(self):
  if self.exist == True:
   self.exist = False
   return True
  else:
   return False

 def back(self):
  self.exist = True
