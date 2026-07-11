import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


DATA_PATH = BASE_DIR / "data" / "players_cleaned.csv"



df = pd.read_csv(DATA_PATH)



# Aggregate player statistics

player_profiles = df.groupby(
    [
        "player_id",
        "player_name",
        "nationality",
        "team",
        "position"
    ]
).agg({

    "age":"first",

    "market_value_eur":"first",

    "goals":"sum",

    "assists":"sum",

    "shots":"sum",

    "expected_goals_xg":"sum",

    "expected_assists_xa":"sum",

    "successful_passes":"sum",

    "key_passes":"sum",

    "dribbles_attempted":"sum",

    "successful_dribbles":"sum",

    "tackles":"sum",

    "interceptions":"sum",

    "player_rating":"mean",

    "performance_score":"mean",

    "distance_covered_km":"sum",

    "goals_per_90":"mean",

    "assists_per_90":"mean",

    "defensive_actions_per_90":"mean"


}).reset_index()



OUTPUT = BASE_DIR / "data" / "player_profiles.csv"



player_profiles.to_csv(
    OUTPUT,
    index=False
)


print(player_profiles.head())

print("\nPlayer Profiles Created")

print(player_profiles.shape)