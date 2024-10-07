from graphs_jjarek import sp

def test_dijkstra():
    graph = {
        0: {1: 4, 2: 1},
        1: {3: 1},
        2: {1: 2, 3: 5},
        3: {}
    }
    dist, path = sp.dijkstra(graph, 0)
    assert dist == {0: 0, 2: 1, 1: 3, 3: 4}, "Distance is incorrect"
    assert path == {1: [0, 2, 1], 3: [0, 2, 1, 3]}, "Path is incorrect"
