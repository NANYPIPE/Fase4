# ============================================================
# PROYECTO FASE 4 UNAD: SISTEMA DE GESTIÓN DE CLIENTES,
# SERVICIOS Y RESERVAS
# ============================================================
from abc import ABC, abstractmethod
import datetime


# ==============================================
# Excepciones personalizadas
# ==============================================
class DatoInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class ServicioNoDisponibleError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class ReservaIncorrectaError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


# ==============================================
# Clase abstracta EntidadGeneral
# ==============================================
class EntidadGeneral(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass


# ==============================================
# Clase Cliente
# ==============================================
class Cliente(EntidadGeneral):
    def __init__(self, nombre: str, identificacion: str):
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


# ==============================================
# Clase abstracta Servicio
# ==============================================
class Servicio(ABC):
    @abstractmethod
    def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


# ==============================================
# Servicio: Reserva de Salas
# ==============================================
class ReservaSalas(Servicio):
    def __init__(self, horas: float, precio_hora: float):
        if horas <= 0 or precio_hora <= 0:
            raise DatoInvalidoError("Horas y precio por hora deben ser mayores a cero")
        self.horas = horas
        self.precio_hora = precio_hora

    def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
        valor_base = self.horas * self.precio_hora
        valor_descuento = valor_base * descuento
        valor_impuesto = (valor_base - valor_descuento) * impuesto
        return valor_base - valor_descuento + valor_impuesto

    def describir_servicio(self):
        return f"Reserva de sala por {self.horas} horas"


# ==============================================
# Servicio: Alquiler de Equipos
# ==============================================
class AlquilerEquipos(Servicio):
    def __init__(self, dias: int, precio_dia: float):
        if dias <= 0 or precio_dia <= 0:
            raise DatoInvalidoError("Días y precio diario deben ser mayores a cero")
        self.dias = dias
        self.precio_dia = precio_dia

    def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
        valor_base = self.dias * self.precio_dia
        valor_descuento = valor_base * descuento
        valor_impuesto = (valor_base - valor_descuento) * impuesto
        return valor_base - valor_descuento + valor_impuesto

    def describir_servicio(self):
        return f"Alquiler de equipos por {self.dias} días"


# ==============================================
# Servicio: Asesoría Especializada
# ==============================================
class AsesoriaEspecializada(Servicio):
    def __init__(self, minutos: int, valor_minuto: float):
        if minutos <= 0 or valor_minuto <= 0:
            raise DatoInvalidoError("Minutos y valor por minuto deben ser mayores a cero")
        self.minutos = minutos
        self.valor_minuto = valor_minuto

    def calcular_precio(self, descuento: float = 0.0, impuesto: float = 0.0):
        valor_base = self.minutos * self.valor_minuto
        valor_descuento = valor_base * descuento
        valor_impuesto = (valor_base - valor_descuento) * impuesto
        return valor_base - valor_descuento + valor_impuesto

    def describir_servicio(self):
        return f"Asesoría especializada de {self.minutos} minutos"


# ==============================================
# Clase Reserva
# ==============================================
class Reserva:
    def __init__(self, cliente: Cliente, servicio: Servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = 0
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
        print(f"\n📋 Procesando reserva | Estado: {self.estado}")
        self.cliente.mostrar_informacion()
        print(f"🛠️ {self.servicio.describir_servicio()}")
        print(f"💸 Valor final (descuento + impuesto): ${valor_final:.2f}")


# ==============================================
# Función para registrar eventos en log.txt
# ==============================================
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


# ============================================================
# MENÚ INTERACTIVO - El usuario elige qué hacer
# ============================================================
def menu_principal():
    """
    Menú interactivo que permite al usuario elegir qué operación realizar.
    Corrige la observación del tutor sobre la falta de interacción.
    """
    clientes = []
    servicios = []
    reservas = []

    while True:
        print("\n" + "=" * 55)
        print("   SISTEMA DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS")
        print("=" * 55)
        print("1. Crear cliente")
        print("2. Crear servicio")
        print("3. Crear reserva")
        print("4. Confirmar reserva")
        print("5. Cancelar reserva")
        print("6. Procesar reserva (calcular precio)")
        print("7. Ver clientes")
        print("8. Ver servicios")
        print("9. Ver reservas")
        print("10. Salir")
        print("=" * 55)

        opcion = input("Elija una opción (1-10): ").strip()

        # ----- OPCIÓN 1: CREAR CLIENTE -----
        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del cliente: ").strip()
                identificacion = input("Ingrese la identificación: ").strip()
                cliente = Cliente(nombre, identificacion)
                clientes.append(cliente)
                registrar_log(f"Cliente creado: {nombre} ({identificacion})")
                print("✅ Cliente creado exitosamente.")
            except DatoInvalidoError as e:
                registrar_log(f"Error al crear cliente: {e}")
                print(f"❌ Error: {e}")

        # ----- OPCIÓN 2: CREAR SERVICIO -----
        elif opcion == "2":
            print("\nTipos de servicio:")
            print("  1. Reserva de salas")
            print("  2. Alquiler de equipos")
            print("  3. Asesoría especializada")
            tipo = input("Elija el tipo de servicio (1-3): ").strip()

            try:
                if tipo == "1":
                    horas = float(input("Ingrese las horas: "))
                    precio_hora = float(input("Ingrese el precio por hora: "))
                    servicio = ReservaSalas(horas, precio_hora)
                    servicios.append(servicio)
                    registrar_log(f"Servicio creado: ReservaSalas ({horas} horas)")
                    print("✅ Servicio de reserva de salas creado.")

                elif tipo == "2":
                    dias = int(input("Ingrese los días: "))
                    precio_dia = float(input("Ingrese el precio por día: "))
                    servicio = AlquilerEquipos(dias, precio_dia)
                    servicios.append(servicio)
                    registrar_log(f"Servicio creado: AlquilerEquipos ({dias} días)")
                    print("✅ Servicio de alquiler de equipos creado.")

                elif tipo == "3":
                    minutos = int(input("Ingrese los minutos: "))
                    valor_minuto = float(input("Ingrese el valor por minuto: "))
                    servicio = AsesoriaEspecializada(minutos, valor_minuto)
                    servicios.append(servicio)
                    registrar_log(f"Servicio creado: AsesoriaEspecializada ({minutos} minutos)")
                    print("✅ Servicio de asesoría creado.")

                else:
                    print("❌ Opción inválida.")
            except ValueError:
                print("❌ Error: debe ingresar valores numéricos válidos.")
            except DatoInvalidoError as e:
                registrar_log(f"Error al crear servicio: {e}")
                print(f"❌ Error: {e}")

        # ----- OPCIÓN 3: CREAR RESERVA -----
        elif opcion == "3":
            if not clientes or not servicios:
                print("❌ Debe crear al menos un cliente y un servicio primero.")
                continue

            print("\nClientes disponibles:")
            for i, c in enumerate(clientes, 1):
                print(f"  {i}. {c.get_nombre()} ({c.get_identificacion()})")
            try:
                idx_cliente = int(input("Elija el cliente (número): ")) - 1
                if idx_cliente < 0 or idx_cliente >= len(clientes):
                    print("❌ Cliente inválido.")
                    continue

                print("\nServicios disponibles:")
                for i, s in enumerate(servicios, 1):
                    print(f"  {i}. {s.describir_servicio()}")
                idx_servicio = int(input("Elija el servicio (número): ")) - 1
                if idx_servicio < 0 or idx_servicio >= len(servicios):
                    print("❌ Servicio inválido.")
                    continue

                reserva = Reserva(clientes[idx_cliente], servicios[idx_servicio])
                reservas.append(reserva)
                registrar_log(f"Reserva creada para {clientes[idx_cliente].get_nombre()}")
                print("✅ Reserva creada exitosamente.")
            except ValueError:
                print("❌ Error: debe ingresar valores numéricos válidos.")

        # ----- OPCIÓN 4: CONFIRMAR RESERVA -----
        elif opcion == "4":
            if not reservas:
                print("❌ No hay reservas para confirmar.")
                continue
            print("\nReservas disponibles:")
            for i, r in enumerate(reservas, 1):
                print(f"  {i}. {r.cliente.get_nombre()} - {r.servicio.describir_servicio()} [{r.estado}]")
            try:
                idx = int(input("Elija la reserva (número): ")) - 1
                if 0 <= idx < len(reservas):
                    reservas[idx].confirmar_reserva()
                else:
                    print("❌ Reserva inválida.")
            except ValueError:
                print("❌ Error: debe ingresar un número válido.")

        # ----- OPCIÓN 5: CANCELAR RESERVA -----
        elif opcion == "5":
            if not reservas:
                print("❌ No hay reservas para cancelar.")
                continue
            print("\nReservas disponibles:")
            for i, r in enumerate(reservas, 1):
                print(f"  {i}. {r.cliente.get_nombre()} - {r.servicio.describir_servicio()} [{r.estado}]")
            try:
                idx = int(input("Elija la reserva (número): ")) - 1
                if 0 <= idx < len(reservas):
                    reservas[idx].cancelar_reserva()
                else:
                    print("❌ Reserva inválida.")
            except ValueError:
                print("❌ Error: debe ingresar un número válido.")

        # ----- OPCIÓN 6: PROCESAR RESERVA -----
        elif opcion == "6":
            if not reservas:
                print("❌ No hay reservas para procesar.")
                continue
            print("\nReservas disponibles:")
            for i, r in enumerate(reservas, 1):
                print(f"  {i}. {r.cliente.get_nombre()} - {r.servicio.describir_servicio()} [{r.estado}]")
            try:
                idx = int(input("Elija la reserva (número): ")) - 1
                if 0 <= idx < len(reservas):
                    descuento = float(input("Ingrese descuento (0-1): ") or 0)
                    impuesto = float(input("Ingrese impuesto (0-1): ") or 0)
                    reservas[idx].procesar_reserva(descuento, impuesto)
                else:
                    print("❌ Reserva inválida.")
            except ValueError:
                print("❌ Error: debe ingresar valores numéricos válidos.")

        # ----- OPCIÓN 7: VER CLIENTES -----
        elif opcion == "7":
            if not clientes:
                print("❌ No hay clientes registrados.")
            else:
                print("\n📋 Clientes registrados:")
                for c in clientes:
                    c.mostrar_informacion()

        # ----- OPCIÓN 8: VER SERVICIOS -----
        elif opcion == "8":
            if not servicios:
                print("❌ No hay servicios registrados.")
            else:
                print("\n📋 Servicios registrados:")
                for s in servicios:
                    print(f"  - {s.describir_servicio()}")

        # ----- OPCIÓN 9: VER RESERVAS -----
        elif opcion == "9":
            if not reservas:
                print("❌ No hay reservas registradas.")
            else:
                print("\n📋 Reservas registradas:")
                for i, r in enumerate(reservas, 1):
                    print(f"  {i}. Cliente: {r.cliente.get_nombre()} | "
                          f"Servicio: {r.servicio.describir_servicio()} | "
                          f"Estado: {r.estado}")

        # ----- OPCIÓN 10: SALIR -----
        elif opcion == "10":
            print("\n👋 Saliendo del sistema... ¡Hasta luego!")
            registrar_log("Sistema cerrado por el usuario.")
            break

        else:
            print("❌ Opción inválida. Por favor, elija una opción del 1 al 10.")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    menu_principal()
