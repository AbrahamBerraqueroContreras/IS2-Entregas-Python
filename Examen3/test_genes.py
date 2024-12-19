from Examen3.RedGenetica import *

if __name__ == '__main__':
    rd = RedGenetica.parse('genes.txt','red_genes.txt')
    
    print("El camino más corto desde KRAS hasta PIK3CA es:")
    
    camino = dfs(rd, rd.genes_por_nombre['KRAS'], rd.genes_por_nombre['PIK3CA'])
    print(camino)
    
    g_camino = rd.subgraph(camino)
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.nombre}", lambda_arista=lambda e: e.conexion)