import networkx as nx
import matplotlib.pyplot as plt
import random

class MyGraph:
    nedges = 10
    graph = None

    def __init__(self, molecule):
        self.molecule = molecule

    def generate_graph(self):
        # https://networkx.github.io/documentation/latest/reference.html
        # https://networkx.github.io/documentation/latest/reference/generators.html
        self.graph = nx.Graph()
        for u,v,wt in self.generate_edges():
            self.graph.add_edge(u, v, weight=wt)

    def generate_edges(self):
        # returns [(node0, node1, edge_weight)]
        if self.molecule == "alpha":
            print("using alpha pinene")
            return self.alpha_pinene_edges()
        elif self.molecule == "beta":
            print("using beta pinene")
            return self.beta_pinene_edges()
        else:
            print("using random edges")
            return [(random.randint(0,6), random.randint(0,6), 1) for _ in range(self.nedges)]

    def alpha_pinene_edges(self):
        # (node0, node1, edge_weight)
        return [(1,3,1),
                (2,3,1),
                (3,4,1),
                (3,6,1),
                (4,5,1),
                (4,10,1),
                (5,7,1),
                (6,9,1),
                (6,10,1),
                (7,8,2),
                (8,9,1)]

    def beta_pinene_edges(self):
        # (node0, node1, edge_weight)
        return [(1,3,1),
                (2,3,1),
                (3,4,1),
                (3,6,1),
                (4,5,1),
                (4,10,1),
                (5,7,1),
                (6,9,1),
                (6,10,1),
                (7,8,1),
                (8,9,2)]

    def draw(self):
        # pos is: {node_id: numpy.ndarray(np.float64)}
        # where the ndarray is a the 2-d position of node_id
        region=330 # for pylab 2x2 subplot layout
        plt.subplots_adjust(left=0,right=1,bottom=0,top=0.95,wspace=0.01,hspace=0.01)
        for i in range(9):
            region+=1
            plt.subplot(region)
            self.generate_graph()
            self.pos = nx.spring_layout(self.graph, iterations=500, fixed=[10])
            nx.draw(self.graph, self.pos)
            nx.draw_networkx_labels(self.graph, self.pos)
        filename = "{}.png".format(self.molecule)
        print("saving to {}".format(filename))
        plt.savefig(filename)

G = MyGraph("alpha")
#G = MyGraph("beta")
G.draw()
