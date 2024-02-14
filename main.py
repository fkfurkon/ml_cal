import panel as pn
import pandas as pd

from js import console
from pyodide_http import patch_all
patch_all()

pn.extension(design='material')

csv_file = ("https://raw.githubusercontent.com/fkfurkon/ml_cal/main/data.csv")
data = pd.read_csv(csv_file)
console.log("Downloaded data")

# Panel Widgets
variable_widget = pn.widgets.Select(name="variable", value="Temperaturessss", options=list(set(data['0'])))
print(variable_widget)
console.log("Set up widgets!")

def test():
    test = Element("test").element.value
    consloe.log(test)

def tt():
    print(variable_widget)
# Servable App
pn.Column(variable_widget).servable(target='panel')
