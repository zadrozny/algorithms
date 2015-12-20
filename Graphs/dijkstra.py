#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Graph in example on https://en.m.wikipedia.org/wiki/Dijkstra's_algorithm

N = {
    1: {2: 7, 3: 9, 6: 14}, # Node 1
    2: {3: 10, 4: 15},      # 2
    3: {4: 11, 6: 2},       # 3
    4: {5: 6},              # 4
    5: {},                  # 5
    6: {5: 9}               # 6
}



def dijkstra(graph, origin, destination, distances=[0], paths=['_']):
    if distances == [0]:
        distances.extend([float('inf') for i in range(len(graph) - 1)])

    if paths == ['_']:
        paths = ([str(origin) for i in range(len(graph))])

    if origin == destination:
        path, distance = paths[destination - 1], distances[destination - 1]
        return path, distance

    else:
        cumulative_distance = distances[origin - 1]  # Distance from origin

        adjacent = sorted(graph[origin].items(), key=lambda x: x[1])

        for edge in adjacent:
            neighbor = edge[0]
            distance_neighbor = graph[origin][neighbor]

            if cumulative_distance+distance_neighbor < distances[neighbor - 1]:
                distances[neighbor - 1] = cumulative_distance+distance_neighbor
                paths[neighbor - 1] = str(paths[origin -1])+str(neighbor)


        return dijkstra(graph, adjacent[0][0], destination, distances, paths)

print dijkstra(N, 1, 5)    


