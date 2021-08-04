# encoding=utf8

def _dfs(n, in_degree, g):
    res = [n]
    for k in g[n]:
        in_degree[k] -= 1
        if in_degree[k] == 0:
            res.extend(_dfs(k, in_degree, g))
    return res


def dfs(g):
    in_degree = {i: 0 for i in g.keys()}
    for k, v in g.items():
        for n in v:
            in_degree[n] += 1
    res = []
    queue = []
    for i, v in in_degree.items():
        if v == 0:
            queue.append(i)
    for i in queue:
        res.extend(_dfs(i, in_degree, g))
    return res


def sort(g):
    in_degree = {i: 0 for i in g.keys()}
    res = []
    for k, v in g.items():
        for n in v:
            in_degree[n] += 1
    queue = []
    for i, v in in_degree.items():
        if v == 0:
            queue.append(i)

    while queue:
        q = queue.pop(0)
        res.append(q)
        for n in g[q]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)
    if len(res) == len(in_degree):
        return res
    return []


G = {
    'a': 'bf',
    'b': 'cdf',
    'c': 'd',
    'd': 'ef',
    'e': 'f',
    'f': ''
}

print(sort(G))
print(dfs(G))
