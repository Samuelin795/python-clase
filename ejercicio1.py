datos = [5,10,25,7,33,20,6,7,10,2,4]
for i in datos:
    if datos.count(7)>2:
        i = "false"
    elif datos.count(7)>1:
        i = "true"
    else:
        i = "false"
print(datos)
print(i)