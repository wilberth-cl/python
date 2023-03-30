###
from operator import itemgetter

###
class Pedido():
    #constructor
    def __init__(self, numpedido=0, articulo='', pedidos=0):
        #atributos de clase, parametros
        self.numpedido = numpedido
        self.articulo = articulo
        self.pedidos = self.numero_filas_db()

    def mensaje_inicio(self):
        return print("\n==== Bienvenido a Pedido ====\n")
    
    def mensaje_final(self):
        return print("\n==== ¡hasta pronto! ====\n")

    def numero_filas_db(self):
        num_filas = 0
        with open('pedidosdb.txt','r') as archivo:
            num_filas = sum(1 for fila in archivo)
        return num_filas
        
    def conecxion_read(self):
        lista_filas_db = []
        with open('pedidosdb.txt','r') as archivo:
            filas = archivo.readlines()
            for fila_db in filas:
                fila_db_formateada = fila_db.split('-')
                lista_filas_db.append(fila_db_formateada)
        return lista_filas_db

    def show_pedidos(self, lista_filas):
        if lista_filas:
            encabezado = "{:>15} {:>15}".format("Número","Artículo")
            print('')
            print('_' * 40)
            print(encabezado)
            print("-" * 40)
            for fila in lista_filas:
                fila_formateada = "{:>15} {:>15}".format(fila[0], fila[1])
                print(fila_formateada)
            print('-' * 40)
            print('')
        else:
            print("\nLista vacía\n")

    ##
    def get_pedidos(self):
        lista_filas = self.conecxion_read()
        lista_filas.sort(key=itemgetter(0))
        self.show_pedidos(lista_filas)

    def create_pedido(self):
        num_pedido = self.pedidos+1
        print("\n===== Nuevo Pedido =====")
        print(f"Pedido aprox => {num_pedido}")
        articulo = input("Artículo => ").lower()
        with open('pedidosdb.txt','a') as archivo:
            nueva_fila = str(f"{num_pedido}-{articulo}\n")
            archivo.write(nueva_fila)
        print('')

    # en cuenta, datatype de la primera columna:
    # si es, int solo buscara valores int
    # si es, str solo buscara valores str
    def search(self):
        palabra = str(input("\nBuscar:\n>>>>>>>> "))
        lista_filas = self.conecxion_read()
        coincidencias = []
        for fila in lista_filas:
            if palabra in fila:
                coincidencias.append(fila)    
        self.show_pedidos(coincidencias)      

    def delete_por_posicion(self):
        pedido = int(input("\nNúmero de posición:\n>>>>>>>> "))
        with open('pedidosdb.txt','r') as archivo:
            filas_db = archivo.readlines()        
        del filas_db[pedido-1]
        with open('pedidosdb.txt','w') as archivo:
            archivo.writelines(filas_db)
        print(f"----> Pedido: {pedido}, eliminado\n")

    def delete_por_numero(self):
        pedido = input("\nNúmero de pedido:\n>>>>>>>>> ")
        with open('pedidosdb.txt','r') as archivo:
            filas_db = archivo.readlines()
        index = None
        for i, fila in enumerate(filas_db):
            if pedido in fila:
                index = i
                break
        if index is not None:
            del filas_db[index]
            with open('pedidosdb.txt','w') as archivo:
                archivo.writelines(filas_db)
        print(f"----> Pedido: {pedido}, eliminado\n")

    def update(self):
        pedido = input("\nNúmero de pedido\n>>>>>>>>> ")
        with open('pedidosdb.txt','r') as archivo:
            filas_db = archivo.readlines()  
        coincidencia = []
        for i, fila in enumerate(filas_db):
            if pedido in fila:
                index = i
                coincidencia.append(fila.split('-'))
                
                self.show_pedidos(coincidencia)

        num_pedido = index+1
        print(f"Pedido aprox => {num_pedido}")
        articulo = input("\nArtículo >>>>>>>>>").lower()
        nuevo_pedido = str(f"{num_pedido}-{articulo}\n")
        filas_db[index] = nuevo_pedido
        with open('pedidosdb.txt','w') as archivo:
            archivo.writelines(filas_db)
        print('')

        
            

