import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# Team Colors
# ----------------------------------------------------

TEAM_COLORS = {
    "Los Angeles Lakers": "#552583",
    "Golden State Warriors": "#1D428A",
    "Boston Celtics": "#007A33",
    "Chicago Bulls": "#CE1141",
    "New York Knicks": "#F58426",
    "Philadelphia 76ers": "#006BB6",
    "Dallas Mavericks": "#00538C",
    "Denver Nuggets": "#0E2240",
    "Milwaukee Bucks": "#00471B",
    "Phoenix Suns": "#1D1160",
}


# ----------------------------------------------------
# League Leaders Chart
# ----------------------------------------------------

STAT_COLUMNS = {
    "Points": "points",
    "Rebounds": "rebounds",
    "Assists": "assists",
    "Steals": "steals",
    "Blocks": "blocks",
}


def league_leaders_chart(df, stat_name):
    """
    Interactive league leaders chart.
    """

    column = STAT_COLUMNS[stat_name]

    leaders = (
        df.sort_values(column, ascending=False)
        .head(10)
        .sort_values(column)
    )

    fig = px.bar(
        leaders,
        x=column,
        y="player_name",
        orientation="h",
        color=column,
        color_continuous_scale="oranges",
        text=column,
        labels={
            "player_name": "Player",
            column: stat_name,
        },
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_dark",
        title=f"Top 10 {stat_name}",
        height=550,
        coloraxis_showscale=False,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig


# ----------------------------------------------------
# Player Comparison
# ----------------------------------------------------

def comparison_chart(player_one, player_two):
    """
    Compare two players.
    """

    comparison = pd.DataFrame(
        {
            "Statistic": [
                "Points",
                "Rebounds",
                "Assists",
                "Steals",
                "Blocks",
            ],
            player_one["player_name"]: [
                player_one["points"],
                player_one["rebounds"],
                player_one["assists"],
                player_one["steals"],
                player_one["blocks"],
            ],
            player_two["player_name"]: [
                player_two["points"],
                player_two["rebounds"],
                player_two["assists"],
                player_two["steals"],
                player_two["blocks"],
            ],
        }
    )

    comparison = comparison.melt(
        id_vars="Statistic",
        var_name="Player",
        value_name="Value",
    )

    colors = {
        player_one["player_name"]:
            TEAM_COLORS.get(
                player_one["team"],
                "#F97316",
            ),
        player_two["player_name"]:
            TEAM_COLORS.get(
                player_two["team"],
                "#A3A3A3",
            ),
    }

    fig = px.bar(
        comparison,
        x="Statistic",
        y="Value",
        color="Player",
        barmode="group",
        color_discrete_map=colors,
    )

    fig.update_layout(
        template="plotly_dark",
        title="Player Comparison",
        height=500,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig