import json
import pandas as pd
from scipy.stats import entropy
from matplotlib import pyplot as plt
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation
import networkx as nx
import numpy as np


class Result(list[float]):
    def __init__(self, result: list[float], metadata={}):
        if any(not (0 <= prob <= 1) for prob in result):
            raise ValueError()
        super().__init__(result)

        self.metadata = metadata

    def getEntropy(self):
        return entropy(self)
    
    def __str__(self):
        return f"{self.metadata['circuit']}.run({self.metadata['run']})\n" + str(np.around(self, 5))


#TODO: Feature where walk runs live on the csv file, and plt updates live
class Results(pd.DataFrame):
    def __init__(self, results: list[list[float]], metadata, filename):
        self.metadata = metadata
        # if not filename:
        #     filename = "./qWalk_cache/{shiftCode}.{coinCode}.{basisCode}.{initCode}.csv".format(**metadata) # TODO: fix this
        self.filename = filename

        super().__init__([Result(result, metadata={**metadata, "atTime": t}) for t, result in enumerate(results)])

#     def append(self, result: list[float]):
#         with open(self.filename, 'a') as file:
#             writer = csv.writer(file)
#             writer.writerow(result)

#         super().append(Result(result))


#     @classmethod
#     def load_csv(cls, filename: str):
#         with open(filename, 'r') as file:
#             reader = csv.reader(file)

#             metadata = json.loads(next(reader)[0])
#             results = [result for result in reader]
#         return cls(results, filename, metadata)


#     def view(self, type: str, interval: int):
#         if type == "entropy":
#             plot = self.plot_entropy
#         if type == "graph":
#             plot = self.plot_graph
#         else:
#             raise ValueError()
        
#         animation = FuncAnimation(plt.gcf(), plot, interval=1000)
#         plt.show()

#     # TODO: add a range param for the x-axis
#     def plot_entropy(self):
#         entropies = [result.getEntropy() for result in self]
#         range = list(range(len(entropies)))

#         plt.xlabel("time")
#         plt.ylabel("Entropy")
#         plt.plot(range, entropies)

#     def plot_graph(self):
#         if self.metadata["shiftCode"] == "16nT":
#             if self.metadata["basisCode"] == "Z":
#                 nodeLabels = {(i,j): f"{i:02b} {j:02b}" for i in range(4) for j in range(4)}
#                 edgeLabels = {(i,j,k): f"{k:02b} {i:02b} {j:02b}" for k in range(4) for i in range(4) for j in range(4)}
#             else:
#                 raise NotImplementedError()
            
#             pos = {(i,j): (i,j) for i in range(4) for j in range(4)}
#             cmap = plt.get_cmap('inferno')

#             def atTime(time: int):
#                 result = self[time]

#                 probsEdges = { edge: result[i] for i, edge in enumerate(edgeLabels.values()) }
#                 probs = { node: sum(probsEdges[edge] for edge in edgeLabels.values() if edge.endswith(node)) for node in nodeLabels.values() }

#                 nodeColors = [cmap(value) for value in probs.values()]
#                 edgeColors = [cmap(probsEdges[edge]) for edge in edgeLabels.values()]
#                 edgeWidths = [10 * probsEdges[edge] for edge in edgeLabels.values()]
#                 pos = {(i,j): (i,j) for i in range(4) for j in range(4)}
#                 graph = nx.grid_2d_graph(4,4, periodic=True, create_using=nx.DiGraph)

#                 def edgeGenerator():
#                     edges = []
#                     for key in edgeLabels.keys():
#                         ogNode = key[:2]
#                         x,y,c = key
#                         if c == 0: x = (x - 1) % 4
#                         if c == 1: y = (y - 1) % 4
#                         if c == 2: x = (x + 1) % 4
#                         if c == 3: y = (y + 1) % 4
#                         edges.append((ogNode, (x,y)))
#                     return edges
#                 graph.edges = edgeGenerator

#                 nx.draw(graph, pos, labels=nodeLabels, node_size=1500, node_color=nodeColors, edge_color=edgeColors, width=edgeWidths)

#             return atTime

#         else:
#             raise NotImplementedError()
