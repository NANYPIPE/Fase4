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
     # Clase Cliente (hereda de EntidadGeneral)
class Cliente(EntidadGeneral):
     def _init_(self, nombre: str, identificacion: str):
         # Encapsulación: atributos protegidos
         self._nombre = nombre
         self._identificacion = identificacion
         # Validación robusta (lanza error si está vacío)
         if not nombre.strip() or not identificacion.strip():
             raise DatoInvalidoError("Nombre o identificación no pueden estar vacíos")
     # Método para consultar el nombre
     def get_nombre(self):
         return self._nombre
     # Método para cambiar el nombre con validación
     def set_nombre(self, nombre: str):
         if not nombre.strip():
             raise DatoInvalidoError("El nombre no puede estar vacío")
         self._nombre = nombre
     # Método para consultar identificación
     def get_identificacion(self):
         return self._identificacion
     # Método para cambiar identificación con validación
     def set_identificacion(self, identificacion: str):
         if not identificacion.strip():
             raise DatoInvalidoError("La identificación no puede estar vacía")
         self._identificacion = identificacion
     # Sobrescribimos el método abstracto
     def mostrar_informacion(self):
         print(f"Cliente: {self._nombre}, Identificación: {self._identificacion}")
