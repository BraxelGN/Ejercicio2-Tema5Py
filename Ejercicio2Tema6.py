class Alumno:
  def __init__(self,nombre,nota):
    self.nombre = nombre
    self.nota = int(nota)
  def Aprobo (nota):
    if nota>=7:
      print("Aprobo con: ",nota)
    elif nota<7:
      print("Desaprobo con: ",nota)
  def MostrarNombre(self,nombre):
    print("Nombre: ",nombre)
  def MostrarNota(self,nota):
    Alumno.Aprobo(nota)
    return nota


alumno= Alumno("Pedro",7)
alumno.MostrarNombre(alumno.nombre)
alumno.MostrarNota(alumno.nota)

alumno= Alumno("Julian",5)
alumno.MostrarNombre(alumno.nombre)
alumno.MostrarNota(alumno.nota)
