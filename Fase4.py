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
 # 1. Clase hija ReservaSalas
class ReservaSalas(Servicio):
     def _init_(self, horas: float, precio_hora: float):
         self.horas = horas
         self.precio_hora = precio_hora
     def calcular_precio(self):
         return self.horas * self.precio_hora
 # 2. Clase hija AlquilerEquipos
class AlquilerEquipos(Servicio):
     def _init_(self, dias: int, precio_dia: float):
         self.dias = dias
         self.precio_dia = precio_dia
     def calcular_precio(self):
         return self.dias * self.precio_dia
 # 3. Clase hija AsesoriaEspecializada
class AsesoriaEspecializada(Servicio):
     def _init_(self, minutos: int, valor_minuto: float):
         self.minutos = minutos
         self.valor_minuto = valor_minuto
     def calcular_precio(self):
         return self.minutos * self.valor_minuto
