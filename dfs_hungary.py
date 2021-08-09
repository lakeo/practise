# encoding=utf8

class DFSHungary():
    def __init__(self, set_a, set_b, edges, cx, cy, visited):
        self.set_a =  set_a
        self.set_b = set_b
        self.cx = cx
        self.cy = cy
        self.edges = edges
        self.visited = visited
        self.res = 0
        self.M = []

    def max_m(self):
        for i in self.set_a:
            if self.cx[i] != -1:
                continue
            for j in self.set_b:
                self.visited[j] = 0
            self.res += self.path(i)

    def path(self, u):
        for v in self.set_b:
            if not self.edges[u][v] or self.visited[v]:
                continue
            self.visited[v] = 1
            if self.cy[v] == -1:
                self.cx[u], self.cy[v] = v, u
                self.M.append((u, v))
                return 1
            if self.path(self.cy[v]):
                self.M.remove((self.cy[v], v))
                self.M.append((u, v))
                self.cx[u], self.cy[v] = v, u
                return 1
        return 0


if __name__ == '__main__':

    set_A, set_B = ['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H']

    edge = {'A': {'E': 1, 'F': 0, 'G': 1, 'H': 0}, 'B': {'E': 0, 'F': 1, 'G': 0, 'H': 1},

            'C': {'E': 1, 'F': 0, 'G': 0, 'H': 1}, 'D': {'E': 0, 'F': 0, 'G': 1, 'H': 0}}  # 1表示可以匹配，0表示不能匹配

    cx, cy = {'A': -1, 'B': -1, 'C': -1, 'D': -1}, {'E': -1, 'F': -1, 'G': -1, 'H': -1}

    visited = {'E': 0, 'F': 0, 'G': 0, 'H': 0}

    dh = DFSHungary(set_A, set_B, edge, cx, cy, visited)

    dh.max_m()

    print('res', dh.res)

    print('cx', cx)

    print('cy', cy)

    print('visited', visited)
    print('M', dh.M)

