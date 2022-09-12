
from collections import defaultdict
class Grafica:
    """Clase que representa a una gráfica. Los id's de los nodos que
    pertenezcan a estas gráficas comenzarán desde 0.
    
    Atributos:
    nombre -- nombre de la gráfica
    nodos -- una lista con los nodos que conforman la gráfica
    """
    class Nodo:
        """Clase interna que representa a un nodo.

        Atributos:
        id -- número que identifica al nodo
        vecinos -- lista con los id's de los vecinos del nodo
        """
        def __init__(self, id, vecinos):
            self.id = id
            #lista de nodos vecinos
            self.vecinos = vecinos 
            #raise NotImplementedError('Constructor de Nodo no implementado')"""

        def __str__(self):
            nodo_str = str(self.id)
            return f'Yo soy el nodo {nodo_str}'
            #raise NotImplementedError('__str__ de Nodo no implementado')"""

    def __init__(self, adyacencias, nombre='sin nombre'):
        """Constructor de una gráfica.
        
        Atributos:
        adyacencias -- lista de listas, cada elemento adyacencias[i] es una 
                       lista de los ids a los que el nodo i es adyacente.
        """
        self.nombre = nombre
        self.nodos = [] 
        i = 0 
        for adyacencias_nodo in adyacencias:
            # Creamos el i-esimo nodo y lo agregamos a la lista
            nodo_aux = self.Nodo(i, adyacencias_nodo)
            self.nodos.append(nodo_aux)
            i += 1

    def __str__(self):
        """Representación en cadena de la gráfica."""
        grafica_str = '\n'.join([str(nodo) for nodo in self.nodos])
        #             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Usamos la función 'join' y una lista por comprensión para crear  
        # 'grafica_str', cadena que tendra todas las cadenas de los nodos
        # unidas con saltos de línea

        return f'Gráfica {self.nombre}\n' + grafica_str


    def bfs(self):
        """Algoritmo BFS.
        
        Regresa:
        Una cadena de enteros de la forma '0,3,8,10,2' que indica el orden en 
        el que su algoritmo recorrió la gráfica.
        NOTA: deben usar el nodo en self.nodes[0] como raíz de sus recorridos.
        """
        #creamos un arreglo para marcar todos los nodos como no visitados.
        #notita: visistados maraca el nodo en la posición i como visitado(true)
        visitados = [False] * (len(self.nodos)) #en la pagina lo hacen con un +1

        #creamos una cola para poner los nodos que vamos recorriendo
        queue = [] 
        nodo_inicial = self.nodos[0]

        queue.append(nodo_inicial)
        visitados[0] = True
        imprimir = ""
        num_visit = len(self.nodos)
        while queue:
 
            # Obten el vertice en el fondo e imprimelo.
            nodo_actual = queue.pop(0)
            num_visit = num_visit -1
            if num_visit > 0:
                imprimir += str(nodo_actual.id) + ","
                
            else:
                imprimir += str(nodo_actual.id)
                
 
            
            for vecino in nodo_actual.vecinos :
                if visitados[vecino] == False:
                    nodo_vecino = self.nodos[vecino]
                    queue.append(nodo_vecino)
                    visitados[vecino] = True

        return (imprimir)
 
# ------------------ MAIN --------------------------
def prueba_grafica(g, res_esperado):
    """Método auxiliar para facilitar las pruebas de su BFS."""
    print('Probando ' + str(g))
    print(f'BFS_ESPERADO : {g.bfs()}\nBFS_RESULTADO: {res_esperado}')
    if g.bfs() == res_esperado:
        print('Resultado correcto!')
    else:
        print('Resultado incorrecto :(')

adyacencias = [[1, 2], [0, 3, 4], [0], [1, 4], [1, 3]]
resultado_esperado = '0,1,2,3,4'
g = Grafica(adyacencias, 'A')
prueba_grafica(g, resultado_esperado)
