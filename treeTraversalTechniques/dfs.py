g={'0':['1','2'],
        '1':['0','3','4'],
        '2':['0'],
        '3':['1'],
        '4':['2','3']}
def dfs(g,start,v=None):
    if v is None:
        v=set()
    v.add(start)
    print(start)
    for next in g[start]-v:
        dfs(g,next,v)
    return v
dfs(g,'0')
