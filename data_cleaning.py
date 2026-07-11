import pandas as pd
from pathlib import Path


# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Dataset location
DATA_PATH = BASE_DIR / "data" / "players.csv"


# Load data
df = pd.read_csv(DATA_PATH)


print("Dataset Shape:")
print(df.shape)


# Standardize column names

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
)


# Remove duplicates

df.drop_duplicates(inplace=True)


# Handle missing values

df.fillna(0, inplace=True)



# FEATURE ENGINEERING


# Goals per 90

df["goals_per_90"] = (
    df["goals"] /
    df["minutes_played"].replace(0,1)
) * 90



# Assists per 90

df["assists_per_90"] = (
    df["assists"] /
    df["minutes_played"].replace(0,1)
) * 90



# Expected goal efficiency

df["xg_efficiency"] = (
    df["goals"] /
    df["expected_goals_xg"].replace(0,1)
)



# Passing contribution

df["passes_per_90"] = (
    df["successful_passes"] /
    df["minutes_played"].replace(0,1)
) * 90



# Defensive contribution

df["defensive_actions_per_90"] = (
    df["defensive_actions"] /
    df["minutes_played"].replace(0,1)
) * 90



# Save cleaned file

OUTPUT = BASE_DIR / "data" / "players_cleaned.csv"


df.to_csv(
    OUTPUT,
    index=False
)



print("\nCleaning Completed")
print("Saved:")
print(OUTPUT)