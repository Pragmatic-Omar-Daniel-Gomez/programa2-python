
# PROGRAMA DE INVENTARIO
# FASE 5 EVALUACION FINAL 
# ESTUDIANTE OMAR DANIEL GOMEZ 

#CREAR UNA MATRIZ CON LA LISTA DE LOS PRODUCTOS 
# CADA FILA DE LA MATRIZ CONTIENE LOS SIGUIENTES CAMPOS: CODIGO, NOMBRE, STOCK ACTUAL, STOCK MINIMO

inventario = [
    ["001", "Aceite de aguacate", 5,15],
    ["002", "Aceite de coco", 10,20],
    ["003", "Aceite de oliva", 8,12],
    ["004", "Aceite de girasol", 10,10],
    ["005", "Aceite de almendra", 2,8]
]
# FUNCION PARA MOSTRAR EL INVENTARIO
def mostrar_inventario(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo-stock_actual
    else:
        cantidad = 0
    return cantidad

#MOSTRAR LOS RESULTADOS
print ("="*50)
print ("INVENTARIO DE PRODUCTOS ")
print ("="*50)
print (f"{'ARTICULO' :<20}{'CANT A PEDIR ' :<20}")
print ("="*50)

#RECORRER LA MATRIZ PARA MOSTRAR LOS PRODUCTOS QUE NECESITAN REABASTECER

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    # LLAMAR A LA FUNCION PARA CALCULAR LA CANTIDAD A REABASTECER
    cantidad_reabastecer = mostrar_inventario(stock_actual, stock_minimo)
  
    
    if cantidad_reabastecer > 0:
        print (f"{nombre :<20}{cantidad_reabastecer :<20} UNIDADES A REABASTECER")
    else:
        print (f"{nombre :<20}{cantidad_reabastecer :<20} STOCK OK")
print ("INVENTARIO FINALIZADO ")        

        

    
        