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
type_food = pn.widgets.Select(name="type food", value="-", options=list(set(data['0'])))
country = pn.widgets.Select(name="country", value="-", options=list(set(data['1'])))
clean = pn.widgets.Select(name="clean", value="-", options=list(set(data['2'])))
calories = pn.widgets.Select(name="calories", value="-", options=list(set(data['6'])))
print(type_food)
console.log("Set up widgets!")

pn.Column(type_food).servable(target='type')
pn.Column(country).servable(target='country')
pn.Column(clean).servable(target='clean')
pn.Column(calories).servable(target='calories')

pn.Column(str(clean.value)+str(calories.value)).servable(target='pun')
