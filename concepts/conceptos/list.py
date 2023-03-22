print( dir(list) )
print()

#Declarar Listas
lb = list( ("uno",2,"tres","cuatro") )
print( lb )

lc = list( range(0, 10) )
print( lc )

ld = [ "uno", 2,"3",True,[1, "dos", False] ]
print( ld ) 

print()

la = ["uno","dos","tres","cuatro","cinco"]
print( la )

print( len( la ) )
print( la[2] )
print( 'tres' in la )

print( la )
#Reemplaza Items
la[1] = "tres"
print( la )

#Agrega Item al ultimo lugar
la.append( "seis" )
print( la )

#Inserta Item en lugar definido
la.insert( len( la ), "siete" )
print( la )
la.insert(2,"cero")
print( la )

#Inserta Items al ultimo lugar en forma de Tuplas o Listas 
la.append( ("ocho","nueve") )
la.append( ["ocho","nueve"] )

#Inserta Multiples Items al ultimo lugar en forma individual
la.extend( ("ocho","nueve") )
print( la )

#Elimina el ultimo item
la.pop()
print( la )

#Elimina un item definido
la.remove('cero')
print(la)

#Elimina por Index
la.pop(1)
print(la)

#Ordenar
#print( la.sort() )

#Extraer Index
print( la.index("cinco") )	

print( la.count("ocho") )

#valia lista
la.clear()
print(la)

