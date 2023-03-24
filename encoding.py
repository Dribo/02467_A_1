import numpy as np
import json
from networkx.readwrite import json_graph


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


def save_json(filename, graph):
    g = graph
    g_json = json_graph.node_link_data(g)
    json.dump(g_json,open(filename,'w'),indent=2, cls=NpEncoder)


def read_json_file(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return json_graph.node_link_graph(js_graph)