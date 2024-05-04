import random
import string


def get_text(filename):
    try:
        file = open(filename, encoding='utf8')
    except OSError:
        return None
    else:
        text = file.read()
    finally:
        if file in locals():
            file.close()
    text = ' '.join(text.split())
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation + "“”"))
    text = text.split()
    return text


def get_graph(text):
    graph = dict()
    for prev_vertex, next_vertex in zip(text, text[1:]):
        if prev_vertex in graph:
            adjacent_verticies = adjacent(graph, prev_vertex)
            if next_vertex in adjacent_verticies:
                index = get_edge(adjacent_verticies, next_vertex)
                graph[prev_vertex][index] = increment_weight(graph, prev_vertex, index)
            else:
                graph[prev_vertex].append((next_vertex, 1))
        else:
            graph[prev_vertex] = [(next_vertex, 1)]
    return graph


def compose(graph, length):
    text = list()
    vertex = random.choice(list(graph.keys()))
    while length > 0:
        text.append(vertex)
        adjacent_verticies = adjacent(graph, vertex)
        adjacent_weights = weights(graph, vertex)
        vertex = random.choices(adjacent_verticies, adjacent_weights)[0]
        length -= 1
    return ' '.join(text)


def adjacent(graph, vertex):
    return list(item[0] for item in graph[vertex])


def weights(graph, vertex):
    return list(item[1] for item in graph[vertex])


def get_edge(adjacent_verticies, vertex):
    return adjacent_verticies.index(vertex)


def increment_weight(graph, vertex, index):
    return (graph[vertex][index][0], graph[vertex][index][1] + 1)


text = get_text('alice.txt')
graph = get_graph(text)
composed = compose(graph, 100)
print(composed)
