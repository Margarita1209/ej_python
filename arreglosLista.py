def orden_burbuja(lista):# ordenar lista de arreglo

    for i in range(len(lista)):

        for j in range(0, len(lista) - i - 1):

            if lista[j] > lista[j+1]:
                temporal = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temporal
            print(lista[j])
          #  print(lista[j+1])
       # print(lista[i])
        print("valor de la variable temporal " , int(temporal))
        print(lista[j+1])   

    return lista

print(orden_burbuja([5,8,4,1,2,6])) 


def encontrar_duplicados(lista):

    elementos_lista = []
    duplicados = []

    for elemento in lista:

        if elemento in elementos_lista:
            duplicados.append(elemento)
            print("valor del nombre que se repite", elemento) 
        else:
            elementos_lista.append(elemento)
      
    print("valor del nombre que no se repiten",elementos_lista) 

    return duplicados


lista=["ana", "paco", "paco", "emilio", "javier", "ana"]
print(encontrar_duplicados(lista), "son nombres que se repiten de la lista") # ["paco", "ana"]


def aplanar_lista(lista):

    nueva_lista = []

    for elemento in lista:

        if type(elemento) is list:
            nueva_lista.extend(elemento)
        else:
            nueva_lista.append(elemento)

    return nueva_lista


print(aplanar_lista([2, 3, 4, [3, 2]])) # [2, 3, 4, 3, 2]
print(aplanar_lista([2, 3, 4, [[2]]])) # [2, 3, 4. [2]]

def tri_pascal(cantidad_filas):

    triangulo = []

    for n_fila in range(cantidad_filas):

        fila = []

        for posicion in range(n_fila+1):

            if posicion == 0 or posicion == n_fila:
                fila.append(1)
            else:
                valor = triangulo[n_fila-1][posicion-1] + triangulo[n_fila-1][posicion]
                fila.append(valor)

        triangulo.append(fila)
    return triangulo
cantidad_filas=input("ingrese cantidad de Filas \n")
print(tri_pascal(int(cantidad_filas)))
