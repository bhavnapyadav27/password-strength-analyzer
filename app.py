import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import string

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐"
)

# -------------------------------
# TITLE
# -------------------------------

st.title("🔐 Password Strength Analyzer")
st.write("Analyze your password and understand its strength.")

# -------------------------------
# PASSWORD CHECKER
# -------------------------------

password = st.text_input(
    "Enter your password:",
    type="password"
)

if password:

    score = 0
    suggestions = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Number
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Special character
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    # -------------------------------
    # DISPLAY RESULTS
    # -------------------------------

    st.subheader("📊 Password Analysis")

    st.write("Password Length:", len(password))
    st.write("Score:", str(score) + "/5")

    if strength == "Weak":
        st.error("🔴 Strength: Weak")

    elif strength == "Medium":
        st.warning("🟠 Strength: Medium")

    else:
        st.success("🟢 Strength: Strong")

    st.progress(score / 5)

    # Suggestions

    if suggestions:

        st.subheader("💡 Suggestions")

        for suggestion in suggestions:
            st.write("•", suggestion)

    else:

        st.success(
            "🎉 Excellent! Your password meets all basic requirements."
        )


# -------------------------------
# DATASET ANALYSIS
# -------------------------------

st.divider()

st.header("📈 Dataset Analysis")

try:

    data = pd.read_csv("passwords.csv")

    # Total passwords

    total = len(data)

    st.write("Total Sample Passwords:", total)

    # Strength count

    strength_count = data["strength"].value_counts()

    st.subheader("Password Strength Distribution")

    st.bar_chart(strength_count)

    # Average length

    data["length"] = data["password"].str.len()

    average_length = data["length"].mean()

    st.write(
        "Average Password Length:",
        round(average_length, 2)
    )

    # Length chart

    st.subheader("Password Length Analysis")

    st.line_chart(data["length"])

    # Dataset table

    st.subheader("Sample Dataset")

    st.dataframe(data)

except Exception as e:

    st.error("Dataset could not be loaded.")