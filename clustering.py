import pandas as pd

from pathlib import Path

from sklearn.preprocessing import StandardScaler

from sklearn.cluster import KMeans



BASE_DIR = Path(__file__).resolve().parent.parent



DATA = BASE_DIR / "data" / "player_profiles.csv"



df = pd.read_csv(DATA)



# Features for clustering


features = [

"goals_per_90",

"assists_per_90",

"player_rating",

"performance_score",

"key_passes",

"successful_dribbles",

"tackles",

"interceptions",

"distance_covered_km"

]



X = df[features]



# Scaling

scaler = StandardScaler()


X_scaled = scaler.fit_transform(X)



# KMeans


kmeans = KMeans(

    n_clusters=5,

    random_state=42

)



df["cluster"] = kmeans.fit_predict(
    X_scaled
)



# Give football meanings


cluster_names = {

0:"Elite Attackers",

1:"Creative Playmakers",

2:"Defensive Specialists",

3:"Box-to-Box Midfielders",

4:"Balanced Players"

}



df["playing_style"] = (

df["cluster"]

.map(cluster_names)

)



OUTPUT = BASE_DIR / "data" / "player_profiles_clustered.csv"



df.to_csv(
    OUTPUT,
    index=False
)



print(df[
[
"player_name",
"playing_style"
]
].head(20))


print("\nClustering Completed")