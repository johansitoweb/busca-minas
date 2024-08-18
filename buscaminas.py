import random  

def buscaminas():  
    def crear_tablero(tamano, minas):  
        tablero = [[' ' for _ in range(tamano)] for _ in range(tamano)]  
        posiciones = random.sample(range(tamano * tamano), minas)  
        
        for pos in posiciones:  
            fila = pos // tamano  
            col = pos % tamano  
            tablero[fila][col] = '*'  
        
        return tablero  

    def mostrar_tablero(tablero):  
        for fila in tablero:  
            print(' '.join(fila))  
    
    tamano = 5  
    minas = 5  
    tablero = crear_tablero(tamano, minas)  
    
    print("¡Bienvenido al Buscaminas!")  
    mostrar_tablero(tablero)  

# Ejecuta el juego  
buscaminas()