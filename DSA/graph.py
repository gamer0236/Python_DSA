class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("graph dict :",self.graph_dict)

    def get_path(self,start,end,path = []):
        path = path + [start]

        if start == end:
            return[path]

        if start not in self.graph_dict:
            return []
        
        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths

routes = [
    ("mumbai","paris"),
    ("mumbai","dubai"),
    ("paris","dubai"),
    ("paris","newyork"),
    ("dubai","newyork"),
    ("newyork","toronto"),
]


route_graph = Graph(routes)

d = {
    "mumbai":["paris","dubai"]
}
print(route_graph.get_path('mumbai',"newyork"))
        