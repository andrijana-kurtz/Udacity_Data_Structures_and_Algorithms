from heapq import heappush, heappop, heapify
from math import sqrt

def calc_euc_dist(a, b, intersections):
    a = intersections[a]
    b = intersections[b]
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

class PathIsec:
    def __init__(self, no):
        self.no = no
        self.previous = None
        self.cost_g = 0
        self.cost_h = 0

    def __lt__(self, other):
        return (self.cost_g + self.cost_h) < (other.cost_g + other.cost_h)

def shortest_path(M,start,goal):
    intersections = M.intersections
    roads = M.roads
    explored = set()
    frontier = list()
    heapify(frontier)

    start_isec = PathIsec(start)
    start_isec.cost_h += calc_euc_dist(start, goal, intersections)
    heappush(frontier, start_isec)
    
    while len(explored) < len(intersections):
        #print(f'\nstart state: {[[n.no, n.cost_g, n.cost_h] for n in frontier]}')
        isec = heappop(frontier)
        if isec.no == goal:
            break
        #print(f'Popped: {isec.no=} {isec.cost=}')

        for road in roads[isec.no]:
            if road in explored:
                continue
            conn_isec = PathIsec(road)
            # total distance to previous intersection (isec)
            conn_isec.cost_g += isec.cost_g
            # g - distance from previous intersection (isec) to connected intersection (conn_isec)
            conn_isec.cost_g += calc_euc_dist(isec.no, road, intersections)
            # h - heuristic distance (approx) from connected intersection (conn_isec) to goal
            conn_isec.cost_h += calc_euc_dist(road, goal, intersections)
            conn_isec.previous = isec
            heappush(frontier, conn_isec)

        explored.add(isec.no)
        #print(f'end state: {[[n.no, n.cost] for n in frontier]}')

    path_length = 0
    result = []
    while isec:
        if isec.previous: 
            path_length += calc_euc_dist(isec.no, isec.previous.no, intersections)
        result.append(isec.no)
        isec = isec.previous
    #print(f'{path_length=}')
    #print(f'direct_path={calc_euc_dist(start, goal, intersections)}')
    return result[::-1]
