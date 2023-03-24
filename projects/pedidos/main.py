##
from class_pedidos import Pedido

##
def main():

    miPedido = Pedido() 
    miPedido.mensaje_inicio()
    
    opcion = None
    while opcion != 0:
        opcion = int(input("______ MENU ______\n[ 1 ] => Buscar\n[ 2 ] => Agregar\n[ 3 ] => Pedidos\n[ 4 ] => Conteo rápido\n[ 5 ] => Actualizar pedido\n[ 6 ] => Eliminar (posicion)\n[ 7 ] => Eliminar (no. orden)\n[ 0 ] => salir\n>>>>>>>> "))

        if opcion==0:
            continue

        elif opcion==1:
            miPedido.search()

        elif opcion==2:
            miPedido.create_pedido()
        
        elif opcion==3:
            miPedido.get_pedidos()

        elif opcion==4:
            num_filas = miPedido.numero_filas_db()
            print(f"\nExisten: {num_filas} registros.\n")

        elif opcion==5:
            miPedido.update()

        elif opcion==6:
            miPedido.delete_por_posicion()

        elif opcion==7:
            miPedido.delete_por_numero()

        else:
            print("\n¡Opción Incorrecta!\n")

    miPedido.mensaje_final()


###
if __name__ == '__main__':
    main()