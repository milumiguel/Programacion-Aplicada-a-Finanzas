#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:56:33 2023

@author: milu
"""

class Myarray_1():
    """ En esta clase las matrices estan indexadas con 'lenguaje matematico',
    es decir, si queremos hablar del primer elemento de la matriz, este va a
    tener coordenadas (1,1). Las funciones tienen esto en cuenta.
    Toma como argumentos una lista 'elems' de los elementos que conforman
    la matriz, una cantidad de filas r y columnas c, y un booleano by_row que 
    indica si la matriz recorre su lista de elementos fila por fila (en cuyo 
    caso devuelve 'True') o columna por columna ('False')
    
    Funciones disponibles:
        - get_pos(self,j,k): encuentra la posicion de un elemento en la lista
                            elems dadas sus coordenadas (j,k).
        -get_coords(self,m): encuentra las coordenadas de un elemento dentro
                                de la matriz dada su posicion m.
        - switch(self): devuelve otra instancia de clase con la misma matriz 
                        pero alterando la lista elems y el valor de by_row.
        - __eq__(self,otra): redefinicion del 'magic method' __eq__ para que
                            compare que dos matrices tengan los mismos elems,
                            mismo numero de filas y columnas y mismo by_row
                            (en lugar de comparar el hash).
        - get_row(self,j): devuelve una lista que representa una fila j en la 
                            matriz con la que se llame a la clase. 
        - get_col(self,k): devuelve una lista que representa una columna k en 
                            la matriz con la que se llame a la clase. 
        - get_elem(self,j,k): toma como argumento el numero de fila y de 
                                columna y a partir de eso devuelve el elemento 
                                que se encuentra en esas coordenadas.
        - my_print(self): recibe una lista que contiene una matriz de rxc 
                            y la devuelve en formato matricial.
        - del_row(self,j):  devuelve un objeto de la clase habiendo eliminando 
                            una fila j.
        - del_col(self,k):  devuelve un objeto de la clase habiendo eliminando 
                            una columna k.
        - swap_rows(self,j,k): devuelve un objeto de la clase habiendo
                                intercambiado los lugares de las filas j y k
        - swap_cols(self,l,m): devuelve un objeto de la clase habiendo
                               intercambiado los lugares de las columnas l y m
        -scale_row(self,j,x):  devuelve un objeto de la misma clase con la fila j 
                            multiplicada por el factor x.
        - scale_col(self,k,x): devuelve un objeto de la misma clase con la  
                               columna k multiplicada por el factor x.
        - transpose(self): devuelve un elemento de la clase, pero con la matriz 
                            transpuesta. 
        - flip_rows(self): devuelve una copia del elemento de la clase, pero 
                                reflejado especularmente en sus filas. 
        - flip_cols(self): devuelve una copia del elemento de la clase, pero 
                            reflejado especularmente en sus columnas. 
        - det(self): devuelve el determinante de cualquier matriz
                     cuadrada, y lo computa recursivamente a partir del teorema 
                     de Laplace.                    
        - add(self,b): efectua la operacion de suma entre matriz (self) y b,
                        que puede ser: matriz, lista o tupla.       
        - sub(self,b): efectua la operacion de resta entre matriz (self) y b,
                        que puede ser: matriz, lista o tupla.
        - mul(self.x): efectua la operacion de multiplicacion entre matriz 
                        (self) y un escalar x.
        - rprod(self,b): Efectua la operacion de multiplicacion entre matriz 
                        (self) y b, que puede ser: matriz, lista o tupla. Esta
                        version es 'por derecha' asi que multiplica self * b
        -lprod(self,b): Efectua la operacion de multiplicacion entre matriz 
                        (self) y b, que puede ser: matriz, lista o tupla. Esta
                        version es 'por izquierda' asi que multiplica b * self
        - identidad(n,del_row=None, swap_row=None): Funcion generadora de 
                                                    matriz identidad tomando
                                                    el numero de filas y 
                                                    columnas dadas (es el 
                                                    mismo, por eso n).
                                                    @staticmethod
                                                    
        - power(self,n): Efectua la operacion de potenciacion por un escalar n.
        
        - del_row_2(self,j): nueva version de del_row aprovechando identidad 
                            y rprod.
        - del_col_2(self,k): nueva version de del_col aprovechando identidad 
                            y lprod.
        - swap_rows_2(self,j,k): nueva version de swap_rows aprovechando 
                                identidad y rprod.
        - swap_cols_2(self,l,m): nueva version de swap_cols aprovechando 
                                identidad y lprod.
        
        """
    
    def __init__(self, elems, r, c, by_row= True):
        """ Al inicializar la clase se toma como parametro una lista "elems"
        que representa a la matriz, un integer r que representa el numero de 
        filas y uno c que representa el numero de columnas. Ademas, un booleano
        "by_row"  que nos indica si esa lista va a ser recorrida por fila 
        (el booleano devuelve True) o por columnas (devuelve False)."""
        
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row       
            
    def get_pos(self, j, k,):
        """ Esta funcion toma como argumentos la fila y la columna de un elem
        especifico dentro de la matriz (sus coordenadas) y devuelve su posicion
        dentro de la lista que representa a la matriz.""" 
        
        """ Ojo! el indice de las filas y columnas va a incluir el 0, entonces
        para que me devuelva valores en lenguaje matematico la fila que entra
        va a ser en python la siguiente a la objetivo (si yo quiero la fila 1
        en python es la 0) por eso al entrar a la funcion se le resta 1 a la
        fila y la columna ingresada.
        
        Funcionamiento: con self.by_row = True al multiplicar la fila 
        correspondiente al elem (j) por la cantidad de columnas que hay en la 
        matriz me posiciono en el primer elemento (indice 0) de la fila que 
        quiero. Luego sumo k para moverme sobre la fila hacia la columna que
        quiero. Cuando recorro por columnas es al reves.""" 
   
        #para hablar en 'lenguaje matematico' uso j-1 y k-1
        return ((j-1) * self.c + (k-1)) +1 if self.by_row else ((k-1) * self.r + (j-1)) +1
    
    def get_coords(self, m):
        """ Funcion inversa a get_pos. Recibe como parámetro una posición m 
        en la lista de elementos elems de la matriz y devuelve en forma de 
        tupla las coordenadas de fila y columna correspondientes en la matriz 
        en formato (j, k). Hay que tener el mismo cuidado con los indices ya 
        que empiezan con 0, por eso la funcion devuelva j+1 y k+1, porque
        queremos que la fila 1 sea la primera, no la segunda.
        
        El funcionamiento sigue la misma logica que antes: si recorro por 
        filas divido la posicion del elem en la lista por el numero de columnas
        que tiene la matriz y me posiciono en la fila objetivo. Con el modulo
        puedo moverme sobre la fila objetivo hacia la columna objetivo.
        """
        return (((m-1) // self.c)+1, ((m-1) % self.c)+1) if self.by_row else (((m-1) % self.r)+1, ((m-1) // self.r)+1)

    def switch(self):
        """ Esta funcion devuelve un objeto con la misma matriz descripta
        por la lista elems pero alterando elems y la manera en la que se 
        recorre la matriz, es decir, si by_row era True, esta funcion devuelve 
        una nueva instancia de la clase donde se recorre por columnas y 
        viceversa. La lista elems va a ser distinta pero esta instancia de 
        clase nueva en realidad es otra version de la misma matriz original.""" 

        elems_2 = []
        k = 0
        # caso donde se recorre la matriz por filas         
        if self.by_row:
            for i in range(self.c):
                elems_2 += self.elems[k::self.c]
                k += 1
            by_row2 = False
       
        # por columnas            
        else:
            for i in range(self.r):
                elems_2 += self.elems[k::self.r]
                k += 1
            by_row2 = True
        
        return Myarray_1(elems_2, self.r, self.c, by_row2)    
    
    def __eq__(self, otra):
        """ Esta funcion se encarga de verificar si dos objetos de la clase 
        tienen la misma matriz de elementos y si tienen el mismo número de 
        filas y columnas. Primero, el método compara si el número de filas y 
        columnas de los dos objetos son iguales. Si no lo son, devuelve False 
        inmediatamente, ya que las dos matrices son diferentes por definición.

        Si tienen el mismo número de filas y columnas, entonces el método 
        sigue comparando elemento por elemento. Si encuentra dos elementos 
        que son diferentes, devuelve False inmediatamente, ya que las dos 
        matrices son diferentes. Si termina de recorrer todos los elementos 
        sin encontrar ninguna diferencia, entonces devuelve True, lo que 
        significa que las dos matrices son iguales.
        
        Tuve que crear esta funcion porque Python utiliza una comparación 
        'por defecto' (en el metodo especial __eq__ original) que compara los 
        objetos por referencia, es decir, si son el mismo objeto en memoria 
        (mismo hash), yo solo quiero ver si son iguales en terminos de 
        elementos, filas, columnas y forma de recorrerla.""" 
        
        return self.elems == otra.elems and self.r == otra.r and self.c == otra.c and self.by_row == otra.by_row
                 
    def get_row(self, j):
        """ Esta funcion toma como argumento un numero de fila y devuelve una
        lista que representa esa fila en la matriz con la que se llame a la 
        clase. 
        Funcionamiento: primero le restamos 1 a j para poder utilizar lenguaje
        matematico. 
        Luego, si la matriz se recorre por filas, la funcion devuelve la lista 
        (matriz) original pero desde el primer elemento de la fila objetivo j 
        (llegamos multiplicando la fila objetivo por el numero de columnas que 
        tenga la matriz) hasta la suma de los elementos recorridos hasta el 
        primero + la cantidad de columnas.
        Si se recorre por columnas, el primer elemento de la fila j se va a 
        encontrar con el indice j en la lista elems! entonces agarro la lista
        original desde ese elemento hasta el final dando tantos 'saltos' 
        como cantidad de columnas tenga la matriz.""" 
        
        return (self.elems[self.c * (j-1): self.c * (j-1) + self.c]) if self.by_row else (self.elems[(j-1)::self.r])


    def get_col(self, k):
        """ Esta funcion (analoga a get_row) toma como argumento un numero de 
        columna y devuelve una lista que representa esa col en la matriz con 
        la que se llame a la clase. 
        Funcionamiento: primero le restamos 1 a k para poder utilizar lenguaje
        matematico. 
        Luego, si la matriz es recorrida por filas basta con recorrer la lista
        de elementos desde el numero de columnas hasta el final (es como en 
        get_row en el caso donde se recorre por columnas) dando 'saltos' como
        cantidad de columnas en la matriz. 
        Si se recorre por columnas, la funcion devuelve la lista (matriz) 
        original pero desde el primer elemento de la columna objetivo k 
        (llegamos multiplicando la columna objetivo por el numero de columnas 
        que tenga la matriz) hasta la suma de los elementos recorridos hasta el 
        primero + la cantidad de filas.""" 
        
        return (self.elems[(k-1)::self.c]) if self.by_row else (self.elems[self.r * (k-1): self.r * (k-1) + self.c])

    def get_elem(self, j, k):
        """ Esta funcion toma como argumento el numero de fila y de columna y
        a partir de eso devuelve el elemento que se encuentra en esas 
        coordenadas.
        Funcionamiento: aprovecho la funcion get_pos que ya tenia definida
        arriba para que insertando las coordenadas j y k me devuelva la 
        posicion del elemento en la matriz. Luego la funcion utiliza esa
        posicion como indice en la fila self.elems y lo devuelve.
        Sin embargo, self.elems es una lista que por default esta escrito como
        si se fuera fila por fila, entonces cuando estemos en un caso donde
        se recorre por columnas, llamamos a otra funcion ya definida (swtich)."""
 
        return (self.elems[self.get_pos(j,k)-1]) if self.by_row else (self.switch().elems[self.get_pos(k,j)-1])
        
    def my_print(self):
        """"La función myprint recibe una lista que contiene una matriz de rxc 
        y la devuelve en formato matricial."""
        if self.by_row:
            print('\n')
            for k in range(1,self.r+1):
                print(self.get_row(k))
            print('\n')
            return None
        else:
            print('\n')
            for k in range(1,self.r+1):
                print(self.get_row(k))
            print('\n')
            return None
        
    def del_row(self, j):
        """ Esta funcion toma como argumento un numero de fila j y devuelve
        un objeto de la clase habiendo eliminando esa fila j en términos
        matemáticos (es decir, se resta 1 al número de fila)."""
        
        j-= 1  # para hablar en 'lenguaje matematico'
        
        # caso donde se recorre por filas
        if self.by_row:
            elems_2 = self.elems.copy() # para no cambiar la lista de la matriz original
            del elems_2[j*self.c:(j+1)*self.c]
            return Myarray_1(elems_2, self.r-1, self.c, self.by_row)
        # caso donde se recorre por columnas
        else:
            elems_nuevos = self.switch().elems
            elems_aux = elems_nuevos.copy()
            del elems_aux[j*self.c:(j+1)*self.c]
            k = 0
            elems_2 = []
            for i in range(self.c):
                elems_2 += elems_aux[k::self.c]
                k +=1
            return Myarray_1(elems_2, self.r, self.c-1, self.by_row)
                
        
              
    def del_col(self, k):
        """ Esta funcion (que es analoga a del_row) toma un argumento k que 
        representa el índice de la columna a eliminar. El objetivo de la 
        función es crear una nueva instancia de la clase que contenga todos 
        los elementos de la matriz original, excepto la columna k."""
        
        k -= 1   # ajusto indices para hablar en 'lenguaje matematico'
        
       # caso donde se recorre por filas
        if self.by_row:
           
            elems_2 = []
            for j in range(self.r): # recorro por filas
                for i in range(self.c): # recorro por columnas
                    if i != k:
                        elems_2.append(self.elems[j * self.c + i])
            return Myarray_1(elems_2, self.r, self.c-1, self.by_row)
        
       # caso donde se recorre por columnas
        else:
            elems_2 = self.elems.copy() # para no cambiar la lista de la matriz original
            print(elems_2)
            del elems_2[k*self.r:(k+1)*self.r]
            print(elems_2)
            return Myarray_1(elems_2, self.r, self.c-1, self.by_row)


                   
    def swap_rows(self, j, k):
        """ Esta funcion toma como argumento 2 filas j y k para devolver un 
        objeto de la clase con estas filas intercambiadas.
        Funcionamiento: La funcion itera sobre las filas de la matriz original 
        con range(self.r). Si la fila actual es igual a j, se agregan los 
        elementos de la fila k a elems_2 (porque la idea es intercambiarlas).
        Si la fila actual es igual a k, se agregan los elementos de la fila j.
        Si la fila actual no es ni j ni k, se agregan los elementos de la fila 
        actual a elems_2 (porque son las que quiero que queden iguales y en
        el orden original."""
        
        if self.by_row:
            j -= 1
            k -= 1 # ajusto indices para hablar en 'lenguaje matematico'
            elems_2 = []
    
            if j == k: # caso donde se pide intercambiar por la misma fila
                elems_2 = self.elems
            
            else:   # puede pasar que j<k o j>k
                j, k = k, j    # de cualquier manera, las intercambio
        
            for i in range(self.r): # recorro por filas
            
                    if i == j: # fila actual es j
                        for x in range(self.c): # recorro por columnas
                            elems_2.append(self.elems[k * self.c + x])
                            
                    elif i == k: # fila actual es k
                            for x in range(self.c):
                                elems_2.append(self.elems[j * self.c + x])
                                
                    else: # fila actual no es de las que quiero intercambiar
                            for x in range(self.c):
                                elems_2.append(self.elems[i * self.c + x])
            
            return Myarray_1(elems_2, self.r, self.c, self.by_row) 
        else:
            return self.swap_cols(j, k)
    
    def swap_cols(self,l,m):
        """Esta funcion (analoga a swap_rows) toma como argumento 2 columnas
        l y m para devolver un objeto de la clase con las estas columnas 
        intercambiadas.
        Funcionamiento: Si l == m significa que se están intercambiando la 
        misma columna consigo misma y retorna la matriz original (una instancia
        de la clase con los mismos elementos y dimensiones que la matriz 
        original). Si l y m son distintos, se intercambian usando la misma 
        técnica que en swap_rows: se recorre cada fila y se agregan los 
        elementos correspondientes de la columna l a la lista elems_2 si es 
        necesario, y los elementos de la columna m si es necesario. Los 
        elementos de las otras columnas se agregan como estaban. La matriz 
        resultante se crea a partir de elems_2 y se devuelve como una instancia 
        de la clase Myarray_1.""" 
        
        l -= 1
        m -= 1 # ajusto indices para hablar en 'lenguaje matematico'
      
        elems_2 = []
          
        if l == m: # caso donde se pide intercambiar por la misma columna
            elems_2 = self.elems
              
        else:   # o bien l<m o m>l
            l, m = m, l   
          
            for i in range(self.r): # recorro filas
                for k in range(self.c): # recorro columnas
                    if k == l:
                        elems_2.append(self.elems[i * self.c + m])
                    elif k == m:
                        elems_2.append(self.elems[i * self.c + l])
                    else:
                        elems_2.append(self.elems[i * self.c + k])
            return Myarray_1(elems_2, self.r, self.c, self.by_row)        

        
        
    def scale_row(self, j, x):
        """Esta función toma como argumento la fila j y el factor x para
        devolver un objeto de la misma clase con la fila j multiplicada por x.
        Funcionamiento: la funcion itera  sobre todas las filas de la matriz. 
        Si la fila i (la actual en el loop) es igual a la fila j, entonces 
        itera sobre todas las columnas de la fila j y multiplica cada elemento 
        por x, y agrega el resultado a la lista elems_2. Si la fila i no es 
        igual a la fila j, simplemente agregamos todos los elementos de la fila 
        i a la lista elems_2. La funcion retorna una instancia de Myarray_1 
        con la nueva lista de elementos."""
        
        j -= 1 # ajusto indice para hablar en 'lenguaje matematico'
        
        elems_2 = []

        for i in range(self.r): # recorro filas
            if i == j:
                for l in range(self.c): # recorro columnas
                    elems_2.append(x * self.elems[j * self.c + l])
                    
            else:   # si son != no quiero multiplicarla por x
                for l in range(self.c):
                    elems_2.append(self.elems[i * self.c + l])

        return Myarray_1(elems_2, self.r, self.c, self.by_row)
    
    def scale_col(self, k, y):
        """Esta función (analoga a scale_row) toma como argumento la columna k 
        y el factor x para devolver un objeto de la misma clase con la columna 
        k multiplicada por x.       
        Funcionamiento: En lugar de iterar sobre las filas y multiplicar los 
        elementos de una fila, se itera sobre las columnas y se multiplican los 
        elementos de una columna. En el loop, si la columna actual es la 
        columna k, se multiplica cada elemento por el escalar y y se agrega a 
        la nueva lista de elementos elems_2. Si no es la columna k, simplemente 
        se agrega el elemento actual a elems_2. Finalmente, se crea un nuevo 
        objeto de la clase con los elementos actualizados y se retorna."""
       
        k -= 1 # ajusto indice para hablar en 'lenguaje matematico'
        
        elems_2 = []
        
        for i in range(self.r): # recorro filas
            for j in range(self.c): # recorro columnas
                if j == k:
                    elems_2.append(self.elems[i * self.c + j] * y)
                else: # otras columnas (no las multiplico)
                    elems_2.append(self.elems[i * self.c + j])
                    
        return Myarray_1(elems_2, self.r, self.c, self.by_row)        
        
    def transpose(self):
        """ Esta funcion devuelve un elemento de la clase, pero con la matriz 
        transpuesta. 
        Funcionamiento: separo el caso donde se recorre por filas (by_row=True)
        y donde se recorre por columnas. En donde se recorra por filas me paro
        en el primer elemento de la matriz y recorro 'saltando' (uso el step
        de [start:stop:step]) por la cantidad de columnas. Ahi estoy agarrando 
        cada columna y agregandosela (con +=) a la nueva lista elems_2. En el
        caso donde se recorre por columnas es la misma logica pero el salto es
        la cantidad de filas.
        Notar que en el return se le asigna self.c (# de columnas original) 
        al numero de filas nuevo y self.r (# de filas original) al numero de 
        columnas nuevo."""
        
        elems_2 = []   
        
        if self.by_row:
            k = 0
            for i in range(self.c):
                elems_2 += self.elems[k::self.c]
                k += 1
                
        else:
            k = 0
            for i in range(self.r):
                elems_2 += self.elems[k::self.r]
                k += 1
                
        return Myarray_1(elems_2, self.c, self.r, self.by_row) # cambio numero de columnas x numero de filas
    
    def flip_rows(self):
        """ Esta funcion devuelve una copia del elemento de la clase, pero 
        reflejado especularmente en sus filas. 
        Funcionamiento: primero la funcion define una lista vacia elems_2 para 
        despues recorrer las filas e ir agregandolas en el orden nuevo. Para 
        reflejarlas especularmente simplemente puse que la primera fila en esta
        nueva lista de elementos sea la ultima (para hacer eso uso la funcion 
        ya definida llamada get_row y le pido que me devuelva la fila con el 
        numero self.r que va a ser la ultima). Despues, en cada iteracion ese 
        numero de fila se va restando (con el k-= 1) y funciona porque se van a
        ir intercambiando las de las puntas (si las filas son impares, la del
        medio va a quedar en su lugar) Pero basicamente es pasar de que las 
        filas sean (por ejemplo en una matriz 4x4): 1,2,3,4 a 4,3,2,1
        En el caso de que la matriz se recorra por columnas la transpongo."""
        
        elems_2 = []
        k = self.r
        for i in range(self.r):
            elems_2 += self.get_row(k)
            k -=1
            
        # caso donde se recorre la matriz por filas        
        if self.by_row:
            flip = Myarray_1(elems_2, self.r, self.c, self.by_row)
       
        # por columnas        
        else:
            flip =  Myarray_1(elems_2, self.r, self.c, self.by_row).transpose()
                
        return flip       
        
    def flip_cols(self):
        """ Esta funcion devuelve una copia del elemento de la clase, pero 
        reflejado especularmente en sus columnas. 
        Funcionamiento: analogo a flip_rows; primero la funcion define una 
        lista vacia elems_2 para despues recorrer las columnas e ir 
        agregandolas en el orden nuevo. Para reflejarlas especularmente 
        simplemente puse que la primera columna en esta nueva lista de 
        elementos sea la ultima (para hacer eso uso la funcion ya definida 
        llamada get_col y le pido que me devuelva la columna con el numero 
        self.c que va a ser la ultima). Despues, en cada iteracion ese numero 
        de columna se va restando (con el k-= 1) y funciona porque se van a ir 
        intercambiando las de las puntas (si las columnas son impares, la del 
        medio va a quedar en su lugar) Pero basicamente es pasar de que las 
        columnas sean (por ejemplo en una matriz 4x4): 1,2,3,4 a 4,3,2,1.
        En el caso de que la matriz se recorra por filas la traspongo."""
        
        elems_2 = []
        k = self.c
        for i in range(self.c):
            elems_2 += self.get_col(k)
            k -=1
            
        # caso donde se recorre la matriz por filas        
        if self.by_row:
            flip =  Myarray_1(elems_2, self.r, self.c, self.by_row).transpose()       
       
        # por columnas        
        else:
            flip = Myarray_1(elems_2, self.r, self.c, self.by_row)
                
        return flip
    
    def det(self):
        """ Esta funcion devuelve el determinante de cualquier matriz
        cuadrada, y lo computa recursivamente a partir del teorema de Laplace. 
        Funcionamiento: primero chequea si la matriz es cuadrada (self.r == 
        self.c: mismo # de filas y columnas), de lo contrario se imprime error.
        Despues comprueba si la matriz es una matriz de 1x1 o 2x2 porque si es
        de 1x1 su det es el elemento unico que conforma a la matriz y si es
        2x2 se puede calcular el det facilmente con la resta entre el producto 
        de la primera diagonal y el producto de la segunda (estos 2 casos 
        constituyen los casos base)
        Si no se cumple ninguno de los dos casos base, la funcion calcula el 
        determinante recursivamente usando las funciones del_row y del_col
        para crear matrices auxiliares (itera a través de la primera fila de 
        la matriz y se construyen las aux_matrix eliminando la primera fila y 
        la columna correspondiente a cada elemento de la primera fila).
        Usa Laplace para cada uno de los elementos de la primera fila, 
        multiplicando cada elemento por su correspondiente cofactor y la
        submatriz auxiliar resultante. Finalmente, se suman todos los resultados 
        y se devuelve el resultado como el determinante de la matriz 
        original. """
        
        if self.by_row:
            # chequeo si es cuadrada
            if self.r != self.c:
                raise ValueError("Error, la matriz no es cuadrada: su determinante no esta definido.")
                
            # casos base
            elif self.r == 1: 
                det = self.get_elem(1, 1)
          
            elif self.r == 2: 
                det = self.get_elem(1, 1) * self.get_elem(2, 2) - self.get_elem(1, 2) * self.get_elem(2, 1)
          
            # caso recursivo
            else:
                det = 0
                for j in range(1, self.c+1):
                    aux_matrix = self.del_row(1).del_col(j)
                    det += ((-1) ** (j+1)) * self.get_elem(1, j) * aux_matrix.det() # formula teorema de Laplace
        else:
            det = self.switch().det()
            self.switch()
        return det
    
    def add(self, b):
        """ Esta funcion efectua la operacion de suma.
        Funcionamiento: chequea el tipo de los objetos que quiero sumar, 
        sabiendo que self es una matriz de la clase, chequea b. Si ambos son
        instancias de la clase irera por sus elementos y devuelve una nueva
        matriz con cada elemento del mismo indice sumados (en el caso de que
        tengan misma cantidad de filas y columnas y pueda hacerse). Si b es una
        lista o tupla, """
        
        
        if isinstance(b,Myarray_1): # caso donde b es una instancia de la clase Myarray_1
           if self.r == b.r and self.c == b.c: # chequeo si la cantidad de filas y columnas de la matriz self son iguales a las de b
               elems_2 = []
               for k in range(len(b.elems)):
                   elems_2.append(self.elems[k] + b.elems[k]) # sumo elememto x elemento
               a = Myarray_1(elems_2, self.r, self.c, self.by_row) 
           else:
               raise ValueError("Error. Las matrices no tienen misma cantidad de filas y columnas.")
        
        elif isinstance(b,list) or isinstance(b,tuple): # caso donde es una lista o tupla 
           if self.r == len(b) and self.c == len(b[0]): # chequeo que tenga misma cantidad de elementos que las filas y columnas de self
               elems_2 = []
               for i in range(len(self.elems)):
                   elems_2.append(self.elems[i] + b[i//self.c][i%self.c])
               a = Myarray_1(elems_2, self.r, self.c, self.by_row)
           else:
               raise ValueError("Error.")
        else:
           elems_2 = []
           for i in range(len(self.elems)):
                   elems_2.append(self.elems[i] + b)
           a = Myarray_1(elems_2, self.r, self.c, self.by_row)
        return a
           
    def sub(self, b):
        """ Esta funcion efectua la operacion de resta.
        Funcionamiento: analogo a add. """
        if isinstance(b,Myarray_1): # chequeo si b es una instancia de la clase
           if self.r == b.r and self.c == b.c: # chequeo que tenga misma cantidad de filas y columnas que self
               elems_2 = []
               for i in range(len(self.elems)):
                   elems_2.append(self.elems[i] - b.elems[i])
               a = Myarray_1(elems_2, self.r, self.c, self.by_row)
           else: 
               raise ValueError ("Error. Las matrices no tienen misma cantidad de filas y columnas.")
        elif isinstance(b,list) or isinstance(b,tuple): # chequeo si b es una lista o tupla
           if self.r == len(b) and self.c == len(b[0]): # chequeo que tenga misma cantidad de elementos que las filas y columnas de self
               elems_2 = []
               for i in range(len(self.elems)):
                   elems_2.append(self.elems[i] - b[i//self.c][i%self.c])
               a = Myarray_1(elems_2, self.r, self.c, self.by_row)
           else:
               raise ValueError("Error.")
        else: 
           elems_2 = []
           for i in range(len(self.elems)):
                   elems_2.append(self.elems[i] - b)
           a = Myarray_1(elems_2, self.r, self.c, self.by_row)
        return a
    
    def mul(self,x):
        """ Esta funcion multiplica elemento a elemento de la matriz self por
        un escalar x.
        El funcionamiento es analogo a las funciones de suma y resta pero ahora
        al recorrer cada elemento lo multiplicamos. Hace los mismos chequeos 
        sobre el type del factor x."""
        
        if isinstance(x,Myarray_1): # le pregunta si es de tipo Myarray_1
            if self.r != x.r or self.c != x.c:
                raise ValueError("Error. Las matrices no tienen misma cantidad de filas y columnas.")
                elems_2 = None
        elif isinstance(x,(int,float)): # le pregunta si es de tipo int o float
                elems_2 = [i * x for i in self.elems]
        else:
                raise ValueError("Error. el type de x no es multiplicable por una matriz.")
        return Myarray_1(elems_2, self.r, self.c, self.by_row)
   
   
    def rprod(self, b):
        """ Esta funcion efectua la operacion de multiplicacion entre matriz 
        (self) y b, que puede ser: matriz, lista o tupla. Esta version es 
        'por derecha' asi que multiplica self*b (el producto de matrices no es 
        conmutativo).""" 
        a = Myarray_1([], 0, 0, self.by_row)
        if type(b) == Myarray_1:
           if self.c == b.r:
               elems_2 = []
               for i in range(self.r):
                   for j in range(b.c):
                       suma = 0
                       for k in range(self.c):
                           suma += self.elems[i*self.c + k] * b.elems[k*b.c + j]
                       elems_2.append(suma)
               a = Myarray_1(elems_2, self.r, b.c, self.by_row)
           else:
               print("Error")
        elif type(b) == list or type(b) == tuple:
           if self.c == len(b):
               elems_2 = []
               for i in range(self.r):
                   for j in range(len(b[0])):
                       sum = 0
                       for k in range(self.c):
                           sum += self.elems[i*self.c + k] * b[k][j]
                       elems_2.append(sum)
               a = Myarray_1(elems_2, self.r, len(b[0]), self.by_row)
           else:
               print("Error")
        else:
           print("Error")
        return a
            
    def lprod(self, b):
        """ Esta funcion efectua la operacion de multiplicacion entre matriz 
        (self) y b, que puede ser: matriz, lista o tupla. Esta version es 
        'por izquierda' asi que multiplica b*self (el producto de matrices no 
        es conmutativo).""" 
        a = Myarray_1([], 0, 0, self.by_row)
        if type(b) == Myarray_1:
           if self.r == b.c:
               elems_2 = []
               for i in range(b.r):
                   for j in range(self.c):
                       sum = 0
                       for k in range(self.r):
                           sum += b.elems[i*b.c + k] * self.elems[k*self.c + j]
                       elems_2.append(sum)
               a = Myarray_1(elems_2, b.r, self.c, self.by_row)
           else:
               print("Error")
        elif type(b) == list or type(b) == tuple:
           if self.r == len(b[0]):
               elems_2 = []
               for i in range(len(b)):
                   for j in range(self.c):
                       sum = 0
                       for k in range(self.r):
                           sum += b[i][k] * self.elems[k*self.c + j]
                       elems_2.append(sum)
               a = Myarray_1(elems_2, len(b), self.c, self.by_row)
           else:
               print("Error")
        else:
           print("Error")
        return a
    
    @staticmethod
    def identidad(n,del_row=None, swap_rows=None):
        """ Esta funcion genera la matriz identidad tomando
            el numero de filas y columnas dadas. 
            Recordemos que la matriz identidad es una matriz cuadrada donde 
            todos sus elementos son ceros (0) menos los elementos de la 
            diagonal principal que son unos (1).
            n es el numero tanto de columnas como filas (aprovecho que la 
            matriz debe ser cuadrada)
            ! Ver funciones del_row_2, del_col_2, swap_rows_2 y swap_cols_2 para
            entender la necesidad de los argumentos del_row y swap_rows."""
        elems_2=[1]
        if del_row is None:
            a = 0
            for i in range(n):
               elems_2 += n*[0]+[1]
        else:
            a = 1
            for i in range(n):
                if i != (del_row-1) and i!= del_row:
                    elems_2 += n*[0]+[1]
                elif i == del_row:
                    elems_2+= (n+1) * [0]+ [1]
        return Myarray_1(elems_2, n-a, n,by_row=True).swap_rows(*swap_rows) if swap_rows is not None else Myarray_1(elems_2, n-a, n,by_row=True)
    
    """Las siguientes funciones son reversiones usando las funciones nuevas"""
    def del_row_2(self,j):
        matriz_identidad = self.identidad(self.r,j-1)
        
        nueva = matriz_identidad.rprod(self)
        return nueva
    
    def del_col_2(self,k):
        matriz_identidad = self.identidad(self.c,k-1)
        print((matriz_identidad).my_print())
        matriz_identidad = matriz_identidad.transpose()
        print((matriz_identidad).my_print())
        nueva = matriz_identidad.lprod(self)
        return nueva
    
    def swap_rows_2(self,j,k):
        matriz_identidad = self.identidad(self.r, swap_rows=(j,k))
        nueva = matriz_identidad.rprod(self)
        return nueva
    
    def swap_cols_2(self,l,m):
        matriz_identidad = self.identidad(self.c, swap_rows=(m,l)).transpose()
        nueva = matriz_identidad.lprod(self)
        return nueva

    
    #%%
if __name__ == 'main':
    
        
    # TESTER
    
    # ej 4x4:
        
    #    1 2 3 4 
    #    5 6 7 8
    #    9 8 7 6
    #    5 4 3 2
    
    #    1 5 9 5
    #    2 6 8 4
    #    3 7 7 3
    #    4 8 6 2
    
    
    #   [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2] --> by_row = True !!!esto es self.elems
    #   [1,5,9,5,2,6,8,4,3,7,7,3,4,8,6,2] --> by_row = False  
    
    matrix = Myarray_1([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2], 4, 4, by_row=True)  
    matrix_2 = Myarray_1([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 4, 4, by_row=True)        
        
    print(matrix.get_pos(1,2))
    print(matrix.get_coords(12))
    print(matrix.switch().switch() == matrix ) # --> me devuelve True
    print((matrix.switch()).my_print())
    print(matrix.get_row(1)) 
    print(matrix.get_col(3))
    print(matrix.get_elem(2,1))
    print((matrix.del_row(2)).my_print())
    print((matrix.del_col(4)).my_print())
    print((matrix.swap_rows(3,4)).my_print())
    print((matrix.swap_cols(3,4)).my_print())
    print(matrix.scale_row(2,2).my_print())
    print(matrix.scale_col(2,2).my_print())
    print((matrix.transpose()).my_print())
    print((matrix.transpose().elems)) 
    print(matrix.my_print())  
    print((matrix.flip_rows(2,3)).my_print())    
    print((matrix.flip_cols(2,3)).my_print())
    print(matrix.det())  
    
    
    print((matrix.add(matrix_2)).my_print())
    print((matrix.sub(matrix_2)).my_print())
    print((matrix.mul(2)).my_print())
    print((matrix.rprod(matrix_2)).my_print())
    print((matrix.lprod(matrix_2)).my_print())
    print(((matrix.identidad(5)).my_print()))
    print((matrix.del_row_2(3)).my_print())
    print((matrix.del_col_2(1)).my_print()) # me esta funcionando mal
    print(((matrix.swap_rows_2(1,2)).my_print())) 
    print(((matrix.swap_cols_2(1,2)).my_print())) 
    
    
    
    
#%%

class Myarray_2():
    """ En esta clase las matrices estan indexadas con 'lenguaje matematico',
    es decir, si queremos hablar de el primer elemento de la matriz, este va a
    tener coordenadas (1,1). Las funciones tienen esto en cuenta.
    Toma como argumentos una lista de listas 'elems' que contiene cada fila o
    columna separada en sublistas, la cantidad de filas r y de columnas c, y
    un booleano by_row que indica si la matriz recorre su lista de elementos
    fila por fila (en cuyo caso devuelve 'True') o columna por columna ('False')"""
    
    def __init__(self, elems, r, c, by_row= True):
        """ Al inicializar la clase se toma como parametro una lista "elems"
        que representa a la matriz, un integer r que representa el numero de 
        filas y uno c que representa el numero de columnas. Ademas, un booleano
        "by_row"  que nos indica si esa lista va a ser recorrida por fila 
        (el booleano devuelve True) o por columnas (devuelve False)."""
        
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
    def my_print(self):
         print('\n')
         for k in range(1,self.r+1):
             print(self.get_row(k))
         print('\n')
         return None
     
    def switch(self):
        """ Esta funcion devuelve un objeto con la misma matriz descripta
        por la lista elems pero alterando elems y la manera en la que se 
        recorre la matriz."""

    def __eq__(self, otra):
        """ Esta funcion se encarga de verificar si dos objetos de la clase 
        tienen la misma matriz de elementos y si tienen el mismo número de 
        filas y columnas. Primero, el método compara si el número de filas y 
        columnas de los dos objetos son iguales. Si no lo son, devuelve False 
        inmediatamente, ya que las dos matrices son diferentes por definición.

        Si tienen el mismo número de filas y columnas, entonces el método 
        sigue comparando elemento por elemento. Si encuentra dos elementos 
        que son diferentes, devuelve False inmediatamente, ya que las dos 
        matrices son diferentes. Si termina de recorrer todos los elementos 
        sin encontrar ninguna diferencia, entonces devuelve True, lo que 
        significa que las dos matrices son iguales.
        
        Tuve que crear esta funcion porque Python utiliza una comparación 
        'por defecto' (en el metodo especial __eq__ original) que compara los 
        objetos por referencia, es decir, si son el mismo objeto en memoria 
        (mismo hash), yo solo quiero ver si son iguales en terminos de 
        elementos, filas, columnas y forma de recorrerla.""" 
        
        return self.elems == otra.elems and self.r == otra.r and self.c == otra.c and self.by_row == otra.by_row 
    
    def get_pos(self, j, k):
        """ Esta funcion toma como argumentos la fila y la columna de un elem
        especifico dentro de la matriz (sus coordenadas) y devuelve su posicion
        dentro de la lista que representa a la matriz.
        (en lenguaje matematico) """
        
        return self.c * (j-1) + (k-1) +1 if self.by_row else self.r * (k-1) + (j-1)+1
    
    def get_coords(self, m):
        """ Funcion inversa a get_pos. Recibe como parámetro una posición m 
        en la lista de elementos elems de la matriz (en lenguaje matematico!) 
        y devuelve en forma de tupla las coordenadas de fila y columna 
        correspondientes en la matriz en formato (j, k). """
        
        return (((m-1) // self.c)+1, ((m-1) % self.c)+1) if self.by_row else (((m-1) % self.r)+1, ((m-1) // self.r)+1)

    
    def get_elem(self, j, k):
         """ Esta funcion toma como argumento el numero de fila y de columna y
         a partir de eso devuelve el elemento que se encuentra en esas 
         coordenadas.
         Funcionamiento: aprovecho la el concepto de lista de listas y utilizo
         los parametros j y k (a los dos les resto 1 para tener indices en 
        lenguaje matematico) para buscar al elemento con ese indice dentro de 
        la lista elems. Si el booleano devuelve True, busco la lista de la fila
        y luego adentro de ella la columna, sino al reves."""
         
         return self.elems[j-1][k-1] if self.by_row else self.elems[k-1][j-1]      
     
    def get_row(self, j):
        """ Esta funcion toma como argumento un numero de fila y devuelve una
        lista que representa esa fila en la matriz con la que se llame a la 
        clase. 
        Funcionamiento: aprovechando la funcion get_elem esta funcion busca 
        cada elemento de la fila j iterando por las columnas."""   
        
        return [self.get_elem(j,k) for k in range(1, self.c+1)] # list comprehension    

    def get_col(self, k):
        """ Esta funcion toma como argumento un numero de fila y devuelve una
        lista que representa esa fila en la matriz con la que se llame a la 
        clase. 
        Funcionamiento: analoga a get_row., usando get_elem.""" 

        return [self.get_elem(j,k) for j in range(1,self.r+1)]
    
    def del_row(self,j):
        """Esta funcion toma como argumento una fila j y devuelve una nueva 
        instancia de la clase que contenga todos los elementos de la matriz 
        original, excepto la fila j."""
        print(self.elems)
        elems_2 = self.elems[:]
        print(self.elems)
        if self.by_row:
            elems_2.pop(j-1)
            print(self.elems)
        else:
            for i in range (self.c):
                elems_2[i].pop(j-1)
            print(self.elems)
        
        return  Myarray_2(elems_2, self.r-1, self.c, self.by_row)  
        print(self.elems)    
        
    def del_col(self,k):
        """Esta funcion toma como argumento una columna k y devuelve una nueva 
        instancia de la clase que contenga todos los elementos de la matriz 
        original, excepto la columna k."""
        print(self.elems)
        elems_3 = self.elems[:]
        print(elems_3)
        
        if self.by_row == False:
            elems_3.pop(k-1)
            print(elems_3)
            
        else:
            for i in range (self.r):
                elems_3[i].pop(k-1)
            
        return  Myarray_2(elems_3, self.r, self.c-1, self.by_row)
        print(self.elems)      

    
    
    
    
    

#%%

#if __name__ == 'main':
    
matrix = Myarray_2([[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]], 4, 4, by_row=False) 

    #    1 2 3 4 
    #    5 6 7 8
    #    9 8 7 6
    #    5 4 3 2
    
matrix_2 = Myarray_2([[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]], 4, 4, by_row=False) 
    
    #    1 5 9 5
    #    2 6 8 4
    #    3 7 7 3
    #    4 8 6 2
    
    #print((matrix.switch()).my_print())
    #print(matrix.elems)
   # print(matrix.my_print())#
   # print((matrix.switch()).my_print())
    #print((matrix.switch()).elems)
    #print(((matrix.switch()).switch()) == matrix )


    #print((matrix.switch().my_print()))
    #print(matrix.get_row(3))
    #print(matrix.get_coords())
    #print(matrix.get_elem(3,4))

    #print((matrix.del_row_2(3)).my_print())
    #print((matrix.swap_rows(3,4)).my_print())
    
 # ---
#print(matrix.get_pos(1,4))  # funciona
#print(matrix.get_coords(5)) # funciona
#print(matrix.get_elem(4,3)) # funciona
#print(matrix.get_row(3))    # funciona
#print(matrix.get_col(2))    # funciona
#print((matrix.del_row(2)).my_print()) # funciona solo con Trye
#print((matrix.del_col(2)).my_print())  # funciona solo con False




















 