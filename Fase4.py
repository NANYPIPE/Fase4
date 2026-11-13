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
 # Clase Cliente (CONSTRUCTOR _init_ CORREGIDO)
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
     def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
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
     def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
         valor_base = self.horas * self.precio_hora
         valor_descuento = valor_base * descuento
         valor_impuesto = (valor_base - valor_descuento) * impuesto
         valor_final = valor_base - valor_descuento + valor_impuesto
         return valor_final
     def describir_servicio(self):
         return f"Reserva de sala por {self.horas} horas"
 # AlquilerEquipos
class AlquilerEquipos(Servicio):
     def _init_(self, dias: int, precio_dia: float):
         if dias <= 0 or precio_dia <= 0:
             raise DatoInvalidoError("Días y precio diario deben ser mayores a cero")
         self.dias = dias
         self.precio_dia = precio_dia
     def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
         valor_base = self.dias * self.precio_dia
         valor_descuento = valor_base * descuento
         valor_impuesto = (valor_base - valor_descuento) * impuesto
         valor_final = valor_base - valor_descuento + valor_impuesto
         return valor_final
     def describir_servicio(self):
         return f"Alquiler de equipos por {self.dias} días"
 # AsesoriaEspecializada
class AsesoriaEspecializada(Servicio):
     def _init_(self, minutos: int, valor_minuto: float):
         if minutos <= 0 or valor_minuto <= 0:
             raise DatoInvalidoError("Minutos y valor por minuto deben ser mayores a cero")
         self.minutos = minutos
         self.valor_minuto = valor_minuto
     def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
         valor_base = self.minutos * self.valor_minuto
         valor_descuento = valor_base * descuento
         valor_impuesto = (valor_base - valor_descuento) * impuesto
         valor_final = valor_base - valor_descuento + valor_impuesto
         return valor_final
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
     def procesar_reserva(self, descuento: float = 0.0, impuesto: float = 0.0):
         valor_final = self.servicio.calcular_precio(descuento, impuesto)
         print(f"📋 Procesando reserva | Estado: {self.estado}")
         self.cliente.mostrar_informacion()
         print(f"🛠️ {self.servicio.describir_servicio()}")
         print(f"💸 Valor final (descuento + impuesto): ${valor_final:.2f}")
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
 # ---------------- BLOQUE PRINCIPAL – 10 OPERACIONES SIMULADAS ----------------
if __name__ == "_main_":
     print("===== SISTEMA DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS =====")
     operaciones = 0
     r1 = None
     # Operación 1: Creación correcta de cliente
     try:
         c1 = Cliente("María Gómez", "10203040")
         c1.mostrar_informacion()
         registrar_log("Operación 1: Cliente María Gómez creado correctamente")
     except DatoInvalidoError as err:
         registrar_log(f"Error operación 1: {err}")
     finally:
         operaciones += 1
     # Operación 2: Creación inválida cliente (nombre vacío)
     try:
         c2 = Cliente("", "20304050")
     except DatoInvalidoError as err:
         registrar_log(f"Error operación 2: {err}")
     finally:
         operaciones += 1
     # Operación 3: Creación correcta servicio ReservaSalas
     try:
         s1 = ReservaSalas(4, 15000)
         registrar_log("Operación 3: Servicio ReservaSalas creado correctamente")
     except DatoInvalidoError as err:
         registrar_log(f"Error operación 3: {err}")
     finally:
         operaciones += 1
     # Operación 4: Creación inválida servicio (horas negativas)
     try:
         s2 = ReservaSalas(-2, 15000)
     except DatoInvalidoError as err:
         registrar_log(f"Error operación 4: {err}")
     finally:
         operaciones += 1
     # Operación 5: Creación correcta AlquilerEquipos
     try:
         s3 = AlquilerEquipos(3, 80000)
         registrar_log("Operación 5: Servicio AlquilerEquipos creado correctamente")
     except DatoInvalidoError as err:
         registrar_log(f"Error operación 5: {err}")
     finally:
         operaciones += 1
     # Operación 6: Creación correcta AsesoriaEspecializada
     try:
         s4 = AsesoriaEspecializada(60, 2000)
         registrar_log("Operación 6: Servicio AsesoriaEspecializada creado correctamente")
     except DatoInvalidoError as err:
         registrar_log(f"Error operación 6: {err}")
     finally:
         operaciones += 1
     # Operación 7: Crear reserva válida
     try:
         r1 = Reserva(c1, s1, 4)
         r1.procesar_reserva(descuento=0.10, impuesto=0.19)
         registrar_log("Operación 7: Reserva creada correctamente")
     except Exception as err:
         registrar_log(f"Error operación 7: {err}")
     finally:
         operaciones += 1
     # Operación 8: Confirmar reserva
     try:
         if r1 is not None:
             r1.confirmar_reserva()
         else:
             registrar_log("No se puede confirmar, la reserva no fue creada")
     except Exception as err:
         registrar_log(f"Error operación 8: {err}")
     finally:
         operaciones += 1
     # Operación 9: Cancelar reserva
     try:
         if r1 is not None:
             r1.cancelar_reserva()
         else:
             registrar_log("No se puede cancelar, la reserva no fue creada")
     except Exception as err:
         registrar_log(f"Error operación 9: {err}")
     finally:
         operaciones += 1
     # Operación 10: Calcular precio con descuento e impuesto
     try:
         valor_prueba = s3.calcular_precio(descuento=0.15, impuesto=0.19)
         print(f"💸 Prueba cálculo precio AlquilerEquipos: ${valor_prueba:.2f}")
         registrar_log("Operación 10: Cálculo de precio con descuento e impuesto ejecutado")
     except Exception as err:
         registrar_log(f"Error operación 10: {err}")
     finally:
         operaciones += 1
     print(f"\n✅ Finalizado: Se ejecutaron {operaciones} operaciones")
     registrar_log("Ejecución completa del sistema finalizada")
