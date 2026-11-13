# Proyecto para la Fase 4 Programación UNAD
 # Sistema para gestionar clientes, servicios y reservas de Software FJ
 # Empezamos importando lo necesario para crear clases abstractas
from abc import ABC, abstractmethod
 # Aquí creo mis propias excepciones, para detectar errores
class DatoInvalidoError(Exception):
     def _init_(self, mensaje):
         super()._init_(mensaje)
class ServicioNoDisponibleError(Exception):
     def _init_(self, mensaje):
         super()._init_(mensaje)
class ReservaIncorrectaError(Exception):
     def _init_(self, mensaje):
         super()._init_(mensaje)
 # Clase abstracta general para todas las entidades
class EntidadGeneral(ABC):
     @abstractmethod
     def mostrar_informacion(self):
         # Este método lo van a usar las demás clases
         pass
