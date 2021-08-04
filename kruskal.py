# encoding=utf8

max_value = None
row0 = [0,7,max_value,max_value,max_value,5]
row1 = [7,0,9,max_value,3,max_value]
row2 = [max_value,9,0,6,max_value,max_value]
row3 = [max_value,max_value,6,0,8,10]
row4 = [max_value,3,max_value,8,0,4]
row5 = [5,max_value,max_value,10,4,0]

maps = [row0, row1, row2,row3, row4, row5]


class Graph:
    def __init__(self, maps):
        self.maps = maps
        self.node_num = self.get_node_num()
        self.edge_num = self.get_edge_num()

    def get_node_num(self):
        return len(self.maps)

    def get_edge_num(self):
        cnt = 0
        for r in self.maps:
            for i in r:
                if i != max_value:
                    cnt += 1
        return cnt // 2

    def kruskal(self):
        edges = []
        for i in range(self.node_num):
            for j in range(i, self.node_num):
                if self.maps[i][j] != max_value:
                    edges.append([i, j, self.maps[i][j]])
        edges.sort(key=lambda a: a[2])
        groups = [[i] for i in range(self.node_num)]
        res = []
        for e in edges:
            i, j = e[0], e[1]
            for g in range(len(groups)):
                if i in groups[g]:
                    m = g
                if j in groups[g]:
                    n = g
            if m != n:
                groups[m] += groups[n]
                groups[n] = []
                res.append(e)
        return res

    def prim(self):
        res = []
        u = [0]
        v = [i for i in range(1, self.node_num)]

        while v:
            value = 0
            edge = None
            for i in u:
                for j in v:
                    if self.maps[i][j] == max_value:
                        continue
                    if not value:
                        edge = [i, j]
                        value = self.maps[i][j]
                    elif self.maps[i][j] <= value:
                        edge = [i, j]
                        value = self.maps[i][j]
            u.append(edge[1])
            v.remove(edge[1])
            res.append(edge)
        return res


g = Graph(maps)
print(maps)
print(g.kruskal())
print(g.prim())
