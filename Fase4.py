# Proyecto para la Fase 4 Programación UNAD
# Sistema para gestionar clientes, servicios y reservas de Software FJ
from abc import ABC, abstractmethod
 # Excepciones personalizadas
class DatoInvalidoError(Exception):
     def _init_(self, mensaje):
         super()._init_(mensaje)
class ServicioNoDisponibleError(Exception):
     def _init_(self, mensaje):
         super()._init_(mensaje)
class ReservaIncorrectaError(Exception):
     def _init_(self, mensaje):
         super()._init_(mensaje)
 # Clase abstracta general EntidadGeneral
class EntidadGeneral(ABC):
     @abstractmethod
     def mostrar_informacion(self):
         pass
 # Clase Cliente (hereda de EntidadGeneral)
class Cliente(EntidadGeneral):
     def _init_(self, nombre: str, identificacion: str):
         self._nombre = nombre
         self._identificacion = identificacion
         if not nombre.strip() or not identificacion.strip():
             raise DatoInvalidoError("Nombre o identificación no pueden estar vacíos")
     def get_nombre(self):
         return self._nombre
     def set_nombre(self, nombre: str):
         if not nombre.strip():
             raise DatoInvalidoError("El nombre no puede estar vacío")
         self._nombre = nombre
     def get_identificacion(self):
         return self._identificacion
     def set_identificacion(self, identificacion: str):
         if not identificacion.strip():
             raise DatoInvalidoError("La identificación no puede estar vacía")
         self._identificacion = identificacion
     def mostrar_informacion(self):
         print(f"Cliente: {self._nombre}, Identificación: {self._identificacion}")
 # Clase abstracta Servicio
class Servicio(ABC):
     @abstractmethod
     def calcular_precio(self):
         pass
