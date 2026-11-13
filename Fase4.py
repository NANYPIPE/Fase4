# Proyecto Fase 4 UNAD: Sistema Gestión Clientes, Servicios y Reservas
from abc import ABC, abstractmethod
import datetime
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
 # Clase abstracta EntidadGeneral
class EntidadGeneral(ABC):
     @abstractmethod
     def mostrar_informacion(self):
         pass
 # Clase Cliente
class Cliente(EntidadGeneral):
     def _init_(self, nombre: str, identificacion: str):
         if not nombre.strip() or not identificacion.strip():
             raise DatoInvalidoError("Nombre o identificación no pueden estar vacíos")
         self._nombre = nombre
         self._identificacion = identificacion
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
     @abstractmethod
     def describir_servicio(self):
         pass
 # ReservaSalas
class ReservaSalas(Servicio):
     def _init_(self, horas: float, precio_hora: float):
         if horas <= 0 or precio_hora <= 0:
             raise DatoInvalidoError("Horas y precio por hora deben ser mayores a cero")
         self.horas = horas
         self.precio_hora = precio_hora
     def calcular_precio(self):
         return self.horas * self.precio_hora
     def describir_servicio(self):
         return f"Reserva de sala por {self.horas} horas"
 # AlquilerEquipos
class AlquilerEquipos(Servicio):
     def _init_(self, dias: int, precio_dia: float):
         if dias <= 0 or precio_dia <= 0:
             raise DatoInvalidoError("Días y precio diario deben ser mayores a cero")
         self.dias = dias
         self.precio_dia = precio_dia
     def calcular_precio(self):
         return self.dias * self.precio_dia
     def describir_servicio(self):
         return f"Alquiler de equipos por {self.dias} días"
 # AsesoriaEspecializada
class AsesoriaEspecializada(Servicio):
     def _init_(self, minutos: int, valor_minuto: float):
         if minutos <= 0 or valor_minuto <= 0:
             raise DatoInvalidoError("Minutos y valor por minuto deben ser mayores a cero")
         self.minutos = minutos
         self.valor_minuto = valor_minuto
     def calcular_precio(self):
         return self.minutos * self.valor_minuto
     def describir_servicio(self):
         return f"Asesoría especializada de {self.minutos} minutos"
 # Clase Reserva
class Reserva:
     def _init_(self, cliente: Cliente, servicio: Servicio, duracion: float):
         self.cliente = cliente
         self.servicio = servicio
         self.duracion = duracion
         self.estado = "Pendiente"
     def confirmar_reserva(self):
         self.estado = "Confirmada"
         mensaje = f"Reserva confirmada para cliente: {self.cliente.get_nombre()}"
         registrar_log(mensaje)
         print("✅ Reserva confirmada")
     def cancelar_reserva(self):
         self.estado = "Cancelada"
         mensaje = f"Reserva cancelada para cliente: {self.cliente.get_nombre()}"
         registrar_log(mensaje)
         print("❌ Reserva cancelada")
     def procesar_reserva(self):
         valor = self.servicio.calcular_precio()
         print(f"📋 Procesando reserva | Estado: {self.estado}")
         self.cliente.mostrar_informacion()
         print(f"🛠️ {self.servicio.describir_servicio()}")
         print(f"💸 Valor base: ${valor:.2f}")
 # Función para registrar eventos y errores en el archivo log.txt
def registrar_log(mensaje: str):
     """Guarda eventos relevantes y errores dentro del archivo log.txt"""
     fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     registro = f"[{fecha_hora}] {mensaje}\n"
     try:
         with open("log.txt", "a", encoding="utf-8") as archivo_log:
             archivo_log.write(registro)
         print(f"📝 Log registrado: {mensaje}")
     except Exception as e:
         print(f"❌ Error al escribir el log: {e}")
