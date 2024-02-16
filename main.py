import panel as pn
import pandas as pd

from js import console
from pyodide_http import patch_all
patch_all()
pn.extension(design='material')


# image_path = "img_0.jpg"
# image_pane = pn.pane.PNG(image_path, width=300, height=300)
csv_file = ("https://raw.githubusercontent.com/fkfurkon/ml_cal/main/data.csv")
data = pd.read_csv(csv_file)
console.log("Downloaded data")

# Panel Widgets
type_food = pn.widgets.Select(name="type food", value="-", options=list(set(data['0'])))
country = pn.widgets.Select(name="country", value="-", options=list(set(data['1'])))
clean = pn.widgets.Select(name="clean", value="-", options=list(set(data['2'])))
calories = pn.widgets.Select(name="calories", value="-", options=list(set(data['6'])))
console.log("Set up widgets!")

pn.Column(type_food).servable(target='type')
pn.Column(country).servable(target='country')
pn.Column(clean).servable(target='clean')
pn.Column(calories).servable(target='calories')

def callback(new):
    return f'Amplitude is: {type_food.value+country.value+clean.value+calories.value}'

submit = pn.widgets.Button(name='Submit', icon='caret-right', button_type='primary')
pn.Row(submit, pn.bind(callback, submit)).servable(target='pun')

# -----------------------------------
