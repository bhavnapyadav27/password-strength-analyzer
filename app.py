import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import string

# Page settings
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Password Strength Analyzer")
st.write(
    "Analyze your password strength using Python "
    "and basic data analysis."
)

st.divider()

# Password input
password = st.text_input(
    "🔑 Enter your password:",
    type="password"
)

if password:

    score = 0
    suggestions = []

    # Password length
    length = len(password)

    if length >= 8:
        score += 1
    else:
        suggestions.append(
            "Use at least 8 characters."
        )

    # Uppercase
    uppercase = sum(
        1 for char in password if char.isupper()
    )

    if uppercase > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter."
        )

    # Lowercase
    lowercase = sum(
        1 for char in password if char.islower()
    )

    if lowercase > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter."
        )

    # Numbers
    numbers = sum(
        1 for char in password if char.isdigit()
    )

    if numbers > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one number."
        )

    # Special characters
    special = sum(
        1 for char in password
        if char in string.punctuation
    )

    if special > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one special character."
        )

    # Strength
    if score <= 2:
        strength = "Weak"
        st.error("🔴 Password Strength: WEAK")

    elif score <= 4:
        strength = "Medium"
        st.warning("🟠 Password Strength: MEDIUM")

    else:
        strength = "Strong"
        st.success("🟢 Password Strength: STRONG")

    # Score
    st.subheader("📊 Strength Score")

    st.write(
        f"Your score is **{score}/5**"
    )

    st.progress(score / 5)

    st.divider()

    # Character analysis
    st.subheader("🔍 Character Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Password Length",
            length
        )

        st.metric(
            "Uppercase",
            uppercase
        )

        st.metric(
            "Lowercase",
            lowercase
        )

    with col2:
        st.metric(
            "Numbers",
            numbers
        )

        st.metric(
            "Special Characters",
            special
        )

    # Suggestions
    if suggestions:

        st.subheader("💡 Suggestions")

        for suggestion in suggestions:
            st.write("• " + suggestion)

    else:

        st.success(
            "🎉 Excellent! Your password satisfies "
            "all basic security requirements."
        )


# Dataset analysis
st.divider()

st.header("📈 IDS Data Analysis")

try:

    data = pd.read_csv("passwords.csv")

    # Calculate length
    data["length"] = data["password"].str.len()

    # Total passwords
    total = len(data)

    st.metric(
        "Total Sample Passwords",
        total
    )

    # Strength distribution
    strength_count = data["strength"].value_counts()

    st.subheader(
        "📊 Password Strength Distribution"
    )

    st.bar_chart(strength_count)

    # Pie chart
    st.subheader(
        "🥧 Strength Distribution"
    )

    fig, ax = plt.subplots()

    ax.pie(
        strength_count.values,
        labels=strength_count.index,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Password Strength Distribution"
    )

    st.pyplot(fig)

    # Average length
    average_length = data["length"].mean()

    st.metric(
        "Average Password Length",
        round(average_length, 2)
    )

    # Length analysis
    st.subheader(
        "📏 Password Length Analysis"
    )

    st.line_chart(data["length"])

    # Dataset
    st.subheader(
        "📋 Sample Dataset"
    )

    st.dataframe(data)

except Exception:

    st.error(
        "Unable to load the password dataset."
    )

# Footer
st.divider()

st.caption(
    "🔐 Password Strength Analyzer | "
    "Python + Streamlit | IDS Project"
)