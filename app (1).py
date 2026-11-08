# CIS 211 Lab 4
# Gotham Chess Club NYC: fictional campus club information page.

import streamlit as st

# Club details stored as key-value pairs; the page reads values by key.
club_info = {
    "name": "Gotham Chess Club NYC",
    "day": "Tuesday",
    "time": "5:30 PM - 8:00 PM",
    "location": "Library, Room 3B, Brooklyn",
    "audience": "All students",
}

# Club activities; each item is rendered by the loop below.
activities = [
    "Weekly 1v1s",
    "Instruction in openings, tactics, and endgames",
    "Monthly rapid tournament",
]

# Rating divisions based on Chess.com's self-selected starting levels.
divisions = {
    "New to Chess": "Below 800",
    "Beginner": "800 - 1199",
    "Intermediate": "1200 - 1599",
    "Advanced": "1600 - 1999",
    "Expert": "2000 and above",
}

# Title drawn from the dictionary.
st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")

st.header("About")
# Markdown introduction: ** for bold, * for italic.
st.markdown(
    """
The **Gotham Chess Club NYC** offers students structured study and competitive play.
Members develop *calculation, planning, and analytical reasoning* through regular practice.
"""
)

st.header("Activities")
# Render every activity in the list.
for activity in activities:
    st.markdown(f"- {activity}")

st.header("Divisions")
st.write("Members are grouped by Chess.com rating.")
# Loop through the divisions dictionary; each key is a division name and each value its rating range.
for division, rating_range in divisions.items():
    st.write(f"**{division}:** {rating_range}")

st.header("Meeting Details")
# Labeled dictionary lookups.
st.write(f"**Day:** {club_info['day']}")
st.write(f"**Time:** {club_info['time']}")
st.write(f"**Location:** {club_info['location']}")
st.write(f"**Eligibility:** {club_info['audience']}")

st.header("Before Attending")
# Markdown numbered list and external link.
st.markdown(
    """
1. Learn the movement of each piece.
2. Review basic notation.
3. Arrive on time for timed games.

Practice resource: [Lichess](https://lichess.org)
"""
)
