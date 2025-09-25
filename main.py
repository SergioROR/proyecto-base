from clases.operaciones import Operaciones

def main():
    op = Operaciones()
    op.leerNumeros()
    op.sumar()
    op.mostrarResultado()

    op.restar()
    op.mostrarResultado()

    op.multiplicar()
    op.mostrarResultado()

    op.dividir()
    op.mostrarResultado()
    
    #Realiza las pruebas con las nuevas operaciones
    

if __name__ == "__main__":
    main()
    
    
