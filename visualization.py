import pandas as pd

from pathlib import Path

import plotly.express as px



BASE_DIR = Path(__file__).resolve().parent.parent



df = pd.read_csv(
BASE_DIR /
"data" /
"player_profiles_clustered.csv"
)



fig = px.scatter(

df,

x="goals_per_90",

y="assists_per_90",

color="playing_style",

hover_name="player_name",

size="player_rating",

title="FIFA Player Playing Style Clusters"

)



fig.show()