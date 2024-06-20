import pickle
import sys
import os
import random

class TicketSystem:
    def __init__(self):
        self.tickets = {}
        self.ticket_counter = 0

    def alta_ticket(self):
        nombre = input("Ingrese el nombre del solicitante: ")
        sector = input("Ingrese el sector: ")
        asunto = input("Ingrese el asunto: ")
        problema = input("Ingrese el problema: ")

        self.ticket_counter += 1
        numero_ticket = random.randint(1000, 9999)
        self.tickets[numero_ticket] = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema,
        }

        print(f"\nTicket creado con éxito. Número de ticket: {numero_ticket}")
        print("¡Por favor, acuérdate de este número!\n")

        self.menu_principal()

    def leer_ticket(self):
        numero_ticket = int(input("Ingrese el número de ticket: "))
        if numero_ticket in self.tickets:
            ticket = self.tickets[numero_ticket]
            print("\nDetalles del ticket:")
            print(f"Nombre: {ticket['nombre']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Problema: {ticket['problema']}\n")
        else:
            print("\nTicket no encontrado. Por favor, verifica el número.\n")

        self.menu_principal()

    def menu_principal(self):
        print("¡Hola! Bienvenido/a al sistema de tickets.")
        print("Menú Principal:")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")
        if opcion == "1":
            self.alta_ticket()
        elif opcion == "2":
            self.leer_ticket()
        elif opcion == "3":
            confirmacion = input("¿Estás seguro de que deseas salir? (Sí/No): ")
            if confirmacion.lower() == "sí":
                print("¡Hasta luego!")
                sys.exit()
            else:
                self.menu_principal()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")
            self.menu_principal()

if __name__ == "__main__":
    ticket_system = TicketSystem()
    ticket_system.menu_principal()
