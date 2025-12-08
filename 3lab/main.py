

if __name__ == "__main__":
    pass
def find_path(graph, start, end):
    steps = []
    
    def dfs(node, path, dist):
        path = path + [node]
        steps.append(f"Текущий путь: {path}, Промежуточное минимальное расстояние: {dist}")
        
        if node == end:
            return path, dist
        
        best = None, float('inf')
        
        for n, w in graph.get(node, []):
            if n not in path:
                steps.append(f"Пробуем маршрут {node}->{n}")
                p, d = dfs(n, path, dist + w)
                if d < best[1]:
                    best = p, d
        
        return best
    
    path, dist = dfs(start, [], 0)
    return path, dist, steps

# Пример
g = {0:[(1,4),(2,1)], 1:[(3,1)], 2:[(1,2),(3,5)], 3:[(4,3)]}
path, dist, steps = find_path(g, 0, 4)

print(f"Кратчайший путь: {path}, длина: {dist}")
for s in steps:
    print(s)
# Ваш код здесь
