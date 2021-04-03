from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from Agent import CarModel
import random

def wegen():
    pass

def auto_visualisatie(agent):
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())
    return {"Shape": "rect", "w": 0.5,"h": 40, "Filled": "true", "Layer": 0, "Color": color, "stroke_color": "#00FF00" }

grid = CanvasGrid(auto_visualisatie, 100, 1, 500, 500) # 100x1 grid in 500x500 pixels

x = {"height": 100,
    "width": 100}

server = ModularServer(CarModel(100, 100, 100),
                       [grid],
                       "#naam",
                       x)

server.port = 8521  # The default
server.launch()