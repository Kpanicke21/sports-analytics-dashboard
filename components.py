import streamlit as st


def player_card(player):
    """
    Display a compact NBA player card.
    """

    st.subheader(f"🏀 {player['player_name']}")

    st.caption(
        f"{player['team']} • {player['position']}"
    )

    st.write(
        f"**Age:** {player['age_completed_years']}  |  "
        f"**Experience:** {player['experience']} years"
    )

    st.divider()

    # -------------------------
    # Basic Stats
    # -------------------------

    st.markdown("### 📊 Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Points", int(player["points"]))
        st.metric("Rebounds", int(player["rebounds"]))
        st.metric("Assists", int(player["assists"]))

    with col2:
        st.metric("Steals", int(player["steals"]))
        st.metric("Blocks", int(player["blocks"]))

    st.divider()

    # -------------------------
    # Shooting
    # -------------------------

    st.markdown("### 🎯 Shooting")

    col3, col4 = st.columns(2)

    with col3:
        st.metric("FG%", f"{player['fg_pct']}%")
        st.metric("2PT%", f"{player['two_pct']}%")

    with col4:
        st.metric("3PT%", f"{player['three_pct']}%")
        st.metric("FT%", f"{player['ft_pct']}%")