# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G, with_labels=False, node_size=5, width=0.3, alpha=0.5)
        plt.show()




# Driver code
G = GraphVisualization()

# circuit.V('input', 1, circuit.gnd, 10 @ u_V)
# circuit.R(1, 1, 2, 2 @ u_kΩ)
# circuit.R(2, 1, 3, 1 @ u_kΩ)
# circuit.R(3, 2, circuit.gnd, 1 @ u_kΩ)
# circuit.R(4, 3, circuit.gnd, 2 @ u_kΩ)
# circuit.R(5, 3, 2, 2 @ u_kΩ)

G.addEdge(1, 0)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(2, 0)
G.addEdge(3, 0)
G.addEdge(3, 2)
G.visualize()