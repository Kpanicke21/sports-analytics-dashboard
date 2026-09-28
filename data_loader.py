from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/nba_player_stats.csv")


def load_data():
    """
    Load and prepare the NBA dataset.
    """

    df = pd.read_csv(DATA_PATH)

    # ------------------------
    # Derived statistics
    # ------------------------

    df["rebounds"] = (
        df["offensive_rebounds"]
        + df["defensive_rebounds"]
    )

    df["points"] = (
        df["one_point_made"]
        + (df["two_point_made"] * 2)
        + (df["three_point_made"] * 3)
    )

    # ------------------------
    # Shooting Percentages
    # ------------------------

    df["ft_pct"] = (
        df["one_point_made"]
        / df["one_point_attempted"].replace(0, 1)
        * 100
    ).round(1)

    df["two_pct"] = (
        df["two_point_made"]
        / df["two_point_attempted"].replace(0, 1)
        * 100
    ).round(1)

    df["three_pct"] = (
        df["three_point_made"]
        / df["three_point_attempted"].replace(0, 1)
        * 100
    ).round(1)

    df["fg_pct"] = (
        (
            df["two_point_made"]
            + df["three_point_made"]
        )
        /
        (
            df["two_point_attempted"]
            + df["three_point_attempted"]
        ).replace(0, 1)
        * 100
    ).round(1)

    df = df.sort_values("player_name")

    return df


def filter_data(
    df,
    position="All",
    team="All",
    minimum_points=0,
):
    filtered = df.copy()

    if position != "All":
        filtered = filtered[
            filtered["position"] == position
        ]

    if team != "All":
        filtered = filtered[
            filtered["team"] == team
        ]

    filtered = filtered[
        filtered["points"] >= minimum_points
    ]

    return filtered


def get_player(df, player_name):
    player = df[
        df["player_name"].str.lower()
        == player_name.lower()
    ]

    if player.empty:
        return None

    return player.iloc[0]