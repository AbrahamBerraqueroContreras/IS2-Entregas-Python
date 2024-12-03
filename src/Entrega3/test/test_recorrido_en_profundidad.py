from Entrega3.tipos.red_social import *

if __name__ == '__main__':
    raiz = '../'
    rrss = Red_social.parse(raiz+'usuarios.txt', raiz+'relaciones.txt', es_dirigido=False)
    
    inicio:str = '25143909I'
    destino:str = '76929765H'
    
    camino = dfs(rrss, rrss.usuarios_dni[inicio], rrss.usuarios_dni[destino])
    if len(camino) == 0:
        print(f'No hay conexión directa entre {inicio} y {destino}')
    else:
        print(f'El camino más corto desde {inicio} hasta {destino} es: {camino}')
        g_camino = rrss.subgraph(camino)
        g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)