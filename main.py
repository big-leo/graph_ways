from queue import Queue
q = Queue()


def find_way_v(graph, start, end, way, ways):
    # print('start: %s -> %s' % (start, graph[start]))
    way = way.copy()
    # if start in way:
    #    return None
    way.append(start)
    if start == end:
        ways.append([start])
    # print('way: %s' % (way,))
    for e in graph[start]:
        if e == end:
            way.append(end)
            ways.append(way)
            continue
        if e in way:
            continue
        find_way_v(graph, e, end, way, ways)


def find_way_h(graph, start, end, way, ways):
    # print('start: %s -> %s' % (start, graph[start]))
    way = way.copy()
    # if start in way:
    #    return None
    way.append(start)
    if start == end:
        ways.append([start])
    # print('way: %s' % (way,))
    for e in graph[start]:
        if e == end:
            way.append(end)
            ways.append(way)
            return way
    for e in graph[start]:
        if e in way:
            continue
        q.put((graph, e, end, way, ways))
        # find_way_h(graph, e, end, way, ways)


def find_short_way(ways):
    short_way = None
    for way in ways:
        if short_way is None or len(way) < len(short_way[0]):
            short_way = [way]
        elif len(way) == len(short_way[0]):
            short_way.append(way)
    # print(q.queue)
    return short_way
