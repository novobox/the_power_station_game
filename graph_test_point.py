from classes.PowPoint import PowPoint

pointA = PowPoint(0,0)
pointB = PowPoint(0,1)
pointC = PowPoint(1,1)
pointD = PowPoint(1,2)
pointE = PowPoint(2,2)
pointF = PowPoint(2,3)

graph = {pointA: [pointB, pointE, pointC],
         pointB: [pointC, pointD],
         pointC: [pointD],
         pointD: [pointC],
         pointE: [pointF],
         pointF: [pointC]}

    
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def display_points(path):
    points = []
    for point in path:
        points.append((point.posX, point.posY))
    return points

print("-------------------------------")
print("PATH pointA and pointD")
print(display_points(find_path(graph, pointA, pointD)))

print("-------------------------------")
print("ALL PATH point A and pointD")
paths=find_all_paths(graph, pointA, pointD)
for path in paths:
    print(display_points(path))

print("-------------------------------")
print("SHORTEST PATH point A and pointD")
print(display_points(find_shortest_path(graph, pointA, pointD)))

print("-------------------------------")
print("SHORTEST PATH point A and pointE")
print(display_points(find_shortest_path(graph, pointA, pointE)))
