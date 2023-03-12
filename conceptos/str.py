mystr="Wilberth fRanciso, wistfer"

#Funciones para un Tipo STR
print( dir(mystr) )

print()

print( "Mi nombre es: " + mystr )
print( f"Mi nombre es: {mystr}" )
print( "Mi nombre es: {0}".format(mystr) )

print()

print( mystr.upper() )
print( mystr.lower() )
print( mystr.startswith("wil") )
print( mystr.replace("fRan", "frank") )

print()

print( mystr.split(",") )
print( mystr.split("i") )

print()

print( mystr[15] )
print( mystr[-1] )

print()

print( mystr.count(" ") )
print( mystr.count("r") )
print( mystr.count("R") )

print()

print( len(mystr) )
print( mystr.index(" ") )
print( mystr.find(" ") )

print()

print( mystr.isnumeric() )
print( mystr.isalpha() )
