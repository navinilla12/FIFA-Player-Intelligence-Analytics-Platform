# ⚽ FIFA Player Intelligence Analytics Platform

## 🚀 Overview

The FIFA Player Intelligence Analytics Platform is an end-to-end football analytics application that combines data science, machine learning, and interactive visualization to analyze player performance and discover playing styles.

The platform transforms raw football statistics into actionable scouting insights through player profiling, clustering, similarity modeling, and interactive dashboards.


## 🎯 Business Problem

Football clubs analyze thousands of player statistics to identify talent, compare performance, and discover players with similar playing styles.

This project answers:

- Which players have similar performance profiles?
- What playing styles exist among football players?
- How can data-driven insights support scouting decisions?


# 🛠️ Technologies Used

## Programming
- Python

## Data Analysis
- Pandas
- NumPy

## Machine Learning
- Scikit-learn
- K-Means Clustering
- Cosine Similarity

## Visualization
- Plotly
- Matplotlib
- Seaborn

## Application
- Streamlit


# 📊 Key Features

## 1. FIFA Player Card Generator

Creates an interactive FIFA-inspired player card containing:

- Overall rating
- Pace
- Shooting
- Passing
- Dribbling
- Defense
- Physical attributes
- Nationality
- Team information


## 2. Player Performance Dashboard

Interactive analysis of:

- Goals
- Assists
- Expected goals (xG)
- Passing efficiency
- Defensive contribution
- Player ratings


## 3. Playing Style Classification

Applied K-Means clustering to group players into performance categories:

Examples:

- Elite Attackers
- Creative Midfielders
- Defensive Specialists
- Balanced Players


## 4. Player Similarity Recommendation Engine

Uses machine learning similarity modeling to identify comparable players based on:

- Offensive output
- Passing ability
- Defensive contribution
- Overall performance


# 🏗️ Project Architecture


Raw Football Data

↓

Data Cleaning

↓

Feature Engineering

↓

Machine Learning Models

↓

Player Intelligence Dashboard

↓

Scouting Insights


# 📸 Dashboard Preview


## FIFA Player Card

![FIFA Card](<img width="960" height="600" alt="Screenshot 2026-07-11 171402" src="https://github.com/user-attachments/assets/4f59d0e0-320e-4dd0-bdf7-73530c555e8c" />
)


## Player Analytics Dashboard

![Dashboard](<img width="960" height="600" alt="Screenshot 2026-07-11 171434" src="https://github.com/user-attachments/assets/2c61de45-d347-4939-b608-ab804cc045a3" />
)


## Player Attribute Radar

![Radar](<img width="960" height="600" alt="Screenshot 2026-07-11 171420" src="https://github.com/user-attachments/assets/9f77df72-af1a-4c74-a0d6-45fa786ecd77" />
)


## Similar Player Recommendation

![Similarity](<img width="960" height="600" alt="Screenshot 2026-07-11 171443" src="https://github.com/user-attachments/assets/3d634e95-655f-47b9-9982-27aee91d2577" />
)


# ⚙️ Installation


Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/FIFA-Player-Intelligence-Analytics-Platform.git

#Install dependencies
pip install pandas seaborn matplotlib streamlit

#Run application
streamlit run app.py
```

# 📈 Machine Learning Approach
- Feature Engineering

Created performance metrics using:

1. Goals per 90 minutes
2. Assists per 90 minutes
3. Shooting efficiency
4. Passing accuracy
5. Defensive contribution

- Player Clustering
Algorithm:
K-Means Clustering

Purpose:
Identify player archetypes based on performance characteristics.

- Similarity Modeling
Algorithm:
Cosine Similarity

Purpose:
Recommend players with comparable playing styles.


# 💡 Future Improvements

- Real-time football API integration
- Player market value prediction
- AI-generated scouting reports
- Team strategy analysis
- Live World Cup match analytics


# 👩‍💻 Author

Vaishnavi Surnilla

MS Information Technology
University of Cincinnati
