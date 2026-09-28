import streamlit as st

from data_loader import load_data, filter_data, get_player
from charts import league_leaders_chart, comparison_chart
from components import player_card

st.set_page_config(
    page_title="NBA Analytics Dashboard",
    page_icon="🏀",
    layout="wide",
)

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

df = load_data()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("⚙️ Dashboard Filters")

positions = ["All"] + sorted(df["position"].dropna().unique())
teams = ["All"] + sorted(df["team"].dropna().unique())

selected_position = st.sidebar.selectbox(
    "Position",
    positions,
)

selected_team = st.sidebar.selectbox(
    "Team",
    teams,
)

minimum_points = st.sidebar.slider(
    "Minimum Points",
    min_value=0,
    max_value=int(df["points"].max()),
    value=0,
)

filtered_df = filter_data(
    df,
    position=selected_position,
    team=selected_team,
    minimum_points=minimum_points,
)

if filtered_df.empty:
    st.warning("No players match the selected filters.")
    st.stop()

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🏀 NBA Analytics Dashboard")

st.markdown(
    """
Interactive NBA analytics dashboard built with **Python, Pandas, Streamlit, and Plotly**.
"""
)

st.divider()

# ----------------------------------------------------
# League Leaders
# ----------------------------------------------------

st.subheader("🏆 League Leaders")

leader_category = st.selectbox(
    "Statistic",
    [
        "Points",
        "Rebounds",
        "Assists",
        "Blocks",
        "Steals",
    ],
)

st.plotly_chart(
    league_leaders_chart(
        filtered_df,
        leader_category,
    ),
    use_container_width=True,
)

st.divider()

# ----------------------------------------------------
# Compare Players
# ----------------------------------------------------

st.subheader("⚔️ Compare Players")

players = sorted(filtered_df["player_name"].unique())

left_select, right_select = st.columns(2)

with left_select:

    player_one_name = st.selectbox(
        "Player 1",
        players,
        key="player_one",
    )

with right_select:

    default_index = 1 if len(players) > 1 else 0

    player_two_name = st.selectbox(
        "Player 2",
        players,
        index=default_index,
        key="player_two",
    )

player_one = get_player(filtered_df, player_one_name)
player_two = get_player(filtered_df, player_two_name)

st.plotly_chart(
    comparison_chart(
        player_one,
        player_two,
    ),
    use_container_width=True,
)

st.divider()

# ----------------------------------------------------
# Player Cards
# ----------------------------------------------------

left_card, right_card = st.columns(2)

with left_card:
    player_card(player_one)

with right_card:
    player_card(player_two)