import tkinter as tk
from random import randrange

class TaTeTi:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tres en línea")
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugador_actual = "X" if randrange(2) == 0 else "O"

        for fila in range(3):
            for columna in range(3):
                boton = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                  command=lambda f=fila, c=columna: self.realizar_movimiento(f, c))
                boton.grid(row=fila, column=columna)

    def realizar_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = self.jugador_actual
            self.actualizar_texto_boton(fila, columna)
            if self.verificar_ganador():
                self.mostrar_ganador()
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
                if self.jugador_actual == "O":
                    self.realizar_movimiento_aleatorio()

    def actualizar_texto_boton(self, fila, columna):
        boton = self.root.grid_slaves(row=fila, column=columna)[0]
        boton.config(text=self.tablero[fila][columna], state=tk.DISABLED)

    def verificar_ganador(self):
        for i in range(3):
            if all(self.tablero[i][j] == self.jugador_actual for j in range(3)) or \
               all(self.tablero[j][i] == self.jugador_actual for j in range(3)):
                return True
        return self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == self.jugador_actual or \
               self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == self.jugador_actual

    def mostrar_ganador(self):
        etiqueta_ganador = tk.Label(self.root, text=f"¡{self.jugador_actual} gana!", font=("Arial", 16))
        etiqueta_ganador.grid(row=3, columnspan=3)

    def realizar_movimiento_aleatorio(self):
        celdas_vacias = [(f, c) for f in range(3) for c in range(3) if self.tablero[f][c] == " "]
        if celdas_vacias:
            fila, columna = celdas_vacias[randrange(len(celdas_vacias))]
            self.realizar_movimiento(fila, columna)

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    juego = TaTeTi()
    juego.ejecutar()
