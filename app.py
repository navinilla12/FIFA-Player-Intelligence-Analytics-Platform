import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests

from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

def calculate_fifa_stats(player):

    pace = min(
        int(player.get("top_speed_kmh", 0)),
        99
    )


    shooting = min(
        int(
            (player.get("goals",0) * 15)
            +
            (player.get("expected_goals_xg",0)*10)
        ),
        99
    )


    passing = min(
        int(
            (player.get("pass_accuracy",0))
            +
            (player.get("key_passes",0))
        ),
        99
    )


    dribbling = min(
        int(
            player.get("successful_dribbles",0) * 2
        ),
        99
    )


    defending = min(
        int(
            (
                player.get("tackles",0)
                +
                player.get("interceptions",0)
            )
            /2
        ),
        99
    )


    physical = min(
        int(
            player.get("distance_covered_km",0)
            +
            player.get("accelerations",0)/2
        ),
        99
    )


    return {

        "PAC": pace,

        "SHO": shooting,

        "PAS": passing,

        "DRI": dribbling,

        "DEF": defending,

        "PHY": physical

    }

def find_similar_players(
        df,
        selected_player,
        top_n=5
):


    features = [

        "goals",

        "assists",

        "shots",

        "expected_goals_xg",

        "expected_assists_xa",

        "successful_dribbles",

        "tackles",

        "interceptions",

        "player_rating",

        "performance_score"

    ]


    # keep only columns available in dataset

    available_features = [

        col for col in features

        if col in df.columns

    ]


    player_data = df[
        available_features
    ].fillna(0)



    scaler = StandardScaler()


    scaled_features = scaler.fit_transform(
        player_data
    )


    similarity_matrix = cosine_similarity(
        scaled_features
    )



    player_index = df.index[
        df["player_name"] == selected_player
    ][0]



    similarity_scores = list(
        enumerate(
            similarity_matrix[player_index]
        )
    )


    similarity_scores = sorted(
        similarity_scores,
        key=lambda x:x[1],
        reverse=True
    )



    recommendations = []



    for index, score in similarity_scores[1:top_n+1]:


        recommendations.append(

            {

            "Player":
            df.iloc[index]["player_name"],


            "Team":
            df.iloc[index]["team"],


            "Similarity %":
            round(score*100,2)

            }

        )


    return pd.DataFrame(
        recommendations
    )

def get_player_image(player_name):

    try:

        url = "https://en.wikipedia.org/w/api.php"


        params = {

            "action": "query",

            "format": "json",

            "prop": "pageimages",

            "piprop": "original",

            "titles": player_name

        }


        response = requests.get(
            url,
            params=params
        )


        data = response.json()


        pages = data["query"]["pages"]


        for page in pages.values():

            if "original" in page:

                return page["original"]["source"]


        return None


    except Exception:

        return None
    

country_flags = {

    "France": "🇫🇷",
    "Brazil": "🇧🇷",
    "Argentina": "🇦🇷",
    "Spain": "🇪🇸",
    "Portugal": "🇵🇹",
    "England": "🏴",
    "Germany": "🇩🇪",
    "Italy": "🇮🇹",
    "Netherlands": "🇳🇱",
    "Belgium": "🇧🇪",
    "Croatia": "🇭🇷",
    "Uruguay": "🇺🇾",
    "USA": "🇺🇸",
    "Mexico": "🇲🇽",
    "Japan": "🇯🇵",
    "South Korea": "🇰🇷",
    "Canada": "🇨🇦",
    "Morocco": "🇲🇦",
    "Senegal": "🇸🇳",
    "Nigeria": "🇳🇬"

}

st.set_page_config(
    page_title="FIFA Player Intelligence",
    layout="wide"
)


# Title

st.title(
    "⚽ FIFA World Cup Player Intelligence Dashboard"
)


# Load Data

df = pd.read_csv(
    "data/player_profiles_clustered.csv"
)



# Sidebar Filters

st.sidebar.header(
    "Player Filters"
)


position = st.sidebar.multiselect(
    "Select Position",
    df["position"].unique(),
    default=df["position"].unique()
)


filtered_df = df[
    df["position"].isin(position)
]



# Player Selection

st.sidebar.subheader(
    "Search Player"
)


selected_player = st.sidebar.selectbox(
    "Choose Player",
    filtered_df["player_name"].unique()
)



# Get player data

player = filtered_df[
    filtered_df["player_name"]
    ==
    selected_player
].iloc[0]

country_flag = country_flags.get(
    player["nationality"],
    "🌍"
)

# PLAYER PROFILE CARD

st.subheader(
    "🌟 FIFA Player Card"
)



fifa_stats = calculate_fifa_stats(player)



overall = int(
    player["player_rating"] * 10
)



flag = country_flags.get(
    player["nationality"],
    "🌍"
)



card_col1, card_col2 = st.columns(
    [1,2]
)



with card_col1:


    st.markdown(
        f"""

## {flag}

# {overall}

### {player['player_name']}


**{player['position']}**

**{player['team']}**


---

⚡ PAC : {fifa_stats['PAC']}


🎯 SHO : {fifa_stats['SHO']}


🎮 PAS : {fifa_stats['PAS']}


🌀 DRI : {fifa_stats['DRI']}


🛡 DEF : {fifa_stats['DEF']}


💪 PHY : {fifa_stats['PHY']}


---

🏆 {player['playing_style']}

"""
    )



with card_col2:


    st.markdown(
        f"""

## Player Intelligence


**Nationality**

{flag} {player['nationality']}



**Market Value**

€ {player['market_value_eur']:,}



**Tournament Goals**

{player['goals']}



**Tournament Assists**

{player['assists']}



**Performance Score**

{round(player['performance_score'],2)}


"""
    )


def calculate_fifa_stats(player):

    pace = min(
        int(player["distance_covered_km"] / 2),
        99
    )


    shooting = min(
        int(
            player["goals_per_90"] * 100
        ),
        99
    )


    passing = min(
        int(
            player["assists_per_90"] * 120
        ),
        99
    )


    dribbling = min(
        int(
            player["successful_dribbles"] / 2
        ),
        99
    )


    defending = min(
        int(
            player["defensive_actions_per_90"] * 5
        ),
        99
    )


    physical = min(
        int(
            player["stamina_score"]
        ),
        99
    )


    return {

        "PAC": pace,

        "SHO": shooting,

        "PAS": passing,

        "DRI": dribbling,

        "DEF": defending,

        "PHY": physical

    }

# FIFA ATTRIBUTE RADAR


st.subheader(
    "📊 Player Attribute Radar"
)


categories = [

    "PAC",
    "SHO",
    "PAS",
    "DRI",
    "DEF",
    "PHY"

]


values = [

    fifa_stats["PAC"],
    fifa_stats["SHO"],
    fifa_stats["PAS"],
    fifa_stats["DRI"],
    fifa_stats["DEF"],
    fifa_stats["PHY"]

]


fig_radar = go.Figure()


fig_radar.add_trace(

    go.Scatterpolar(

        r=values,

        theta=categories,

        fill="toself",

        name=player["player_name"]

    )

)



fig_radar.update_layout(

    polar=dict(

        radialaxis=dict(

            visible=True,

            range=[0,100]

        )

    ),

    showlegend=False

)



st.plotly_chart(

    fig_radar,

    use_container_width=True

)

# Player Metrics

c1,c2,c3,c4 = st.columns(4)


c1.metric(
    "Goals",
    player["goals"]
)


c2.metric(
    "Assists",
    player["assists"]
)


c3.metric(
    "Rating",
    round(
        player["player_rating"],
        2
    )
)


c4.metric(
    "Performance",
    round(
        player["performance_score"],
        2
    )
)




# Scatter Plot

st.subheader(
    "Player Playing Style Map"
)



fig = px.scatter(

    filtered_df,

    x="goals_per_90",

    y="assists_per_90",

    color="playing_style",

    hover_name="player_name",

    size="player_rating",

)


st.plotly_chart(
    fig,
    use_container_width=True
)



# Ranking Table

st.subheader(
    "Player Rankings"
)


st.dataframe(

filtered_df[
[
"player_name",
"team",
"position",
"goals",
"assists",
"player_rating",
"playing_style"
]
]

.sort_values(
"player_rating",
ascending=False
)

)

# SIMILAR PLAYER ENGINE

st.subheader(
    "🤖 AI Similar Player Recommendations"
)


similar_players = find_similar_players(
    df,
    selected_player
)


st.dataframe(

    similar_players,

    use_container_width=True

)