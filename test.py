#!/usr/bin/env python3.4
from main import find_way_h, find_way_v, find_short_way, q


graph = {'A': ['B', 'D'],
         'B': ['E', 'D'],
         'C': ['A'],
         'D': ['E', 'F'],
         'E': ['C'],
         'F': ['B']}


def test_way(graph, start, end):
    print('test %s->%s' % (start, end))

    v_ways = []
    find_way_v(graph, start, end, [], v_ways)
    short_v_ways = find_short_way(v_ways)

    h_ways = []
    find_way_h(graph, start, end, [], h_ways)
    while h_ways == []:
        find_way_h(*(q.get()))
    short_h_ways = find_short_way(h_ways)

    if v_ways == h_ways:
        print('%s' % (v_ways,))
    else:
        print('\nvertical: %s' % (v_ways,))
        print('horisontal: %s' % (h_ways,))
    if short_v_ways == short_h_ways:
        print('short: %s' % (short_v_ways))
    else:
        print('short v: %s' % (short_v_ways))
        print('short h: %s' % (short_h_ways))


if __name__ == '__main__':
    # test_way(graph, 'A', 'F')
    # list(map(test_way, 'A', graph.keys()))
    for key1 in graph:
       for key2 in graph:
           test_way(graph, key1, key2)