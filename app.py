import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import string

# Page settings
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐"
)

# Title
st.title("🔐 Password Strength Analyzer")
st.write(
    "A Python-based tool to analyze password strength "
    "and study password security patterns."
)

st.divider()

# ---------------- PASSWORD CHECKER ----------------

st.header("🔑 Check Your Password")

password = st.text_input(
    "Enter your password:",
    type="password"
)

if password:

    score = 0
    suggestions = []

    # Length
    length = len(password)

    if length >= 8:
        score += 1
    else:
        suggestions.append(
            "Use at least 8 characters."
        )

    # Uppercase
    uppercase = sum(
        char.isupper() for char in password
    )

    if uppercase > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter."
        )

    # Lowercase
    lowercase = sum(
        char.islower() for char in password
    )

    if lowercase > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter."
        )

    # Numbers
    numbers = sum(
        char.isdigit() for char in password
    )

    if numbers > 0:
        score += 1
    else:
        suggestions.append(
            "Add at least one number."
        )

    # Special characters
    special = sum(
        char in string.punctuation for char in password
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

    st.write("Score:", str(score) + "/5")

    st.progress(score / 5)

    # Character analysis
    st.subheader("🔍 Character Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Length",
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

        st.subheader("💡 Improve Your Password")

        for suggestion in suggestions:
            st.write("• " + suggestion)

    else:

        st.success(
            "🎉 Your password meets all basic requirements!"
        )


# ---------------- DATA ANALYSIS ----------------

st.divider()

st.header("📈 IDS Data Analysis")

try:

    data = pd.read_csv("passwords.csv")

    # Calculate password length
    data["length"] = data["password"].str.len()

    # Total
    total = len(data)

    # Count categories
    weak = len(
        data[data["strength"] == "Weak"]
    )

    medium = len(
        data[data["strength"] == "Medium"]
    )

    strong = len(
        data[data["strength"] == "Strong"]
    )

    # Display statistics
    st.subheader("📊 Dataset Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Passwords",
            total
        )

        st.metric(
            "Weak Passwords",
            weak
        )

    with col2:

        st.metric(
            "Medium Passwords",
            medium
        )

        st.metric(
            "Strong Passwords",
            strong
        )

    # Percentages
    st.subheader("📌 Password Percentages")

    weak_percent = (weak / total) * 100
    medium_percent = (medium / total) * 100
    strong_percent = (strong / total) * 100

    st.write(
        "🔴 Weak:",
        round(weak_percent, 2),
        "%"
    )

    st.write(
        "🟠 Medium:",
        round(medium_percent, 2),
        "%"
    )

    st.write(
        "🟢 Strong:",
        round(strong_percent, 2),
        "%"
    )

    # Bar chart
    st.subheader(
        "📊 Strength Distribution"
    )

    chart_data = pd.DataFrame(
        {
            "Strength": [
                "Weak",
                "Medium",
                "Strong"
            ],
            "Number of Passwords": [
                weak,
                medium,
                strong
            ]
        }
    )

    st.bar_chart(
        chart_data.set_index("Strength")
    )

    # Pie chart
    st.subheader(
        "🥧 Password Strength Percentage"
    )

    fig, ax = plt.subplots()

    ax.pie(
        [weak, medium, strong],
        labels=[
            "Weak",
            "Medium",
            "Strong"
        ],
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Password Strength Distribution"
    )

    st.pyplot(fig)

    # Average length
    average_length = data["length"].mean()

    st.subheader(
        "📏 Password Length Analysis"
    )

    st.metric(
        "Average Password Length",
        round(average_length, 2)
    )

    # Length chart
    st.line_chart(
        data["length"]
    )

    # Dataset table
    st.subheader(
        "📋 Sample Dataset"
    )

    st.dataframe(data)

except Exception:

    st.error(
        "Unable to load passwords.csv"
    )


# ---------------- PROJECT INFORMATION ----------------

st.divider()

st.header("🎓 About This Project")

st.write(
    "This project uses Python to analyze password "
    "characteristics and classify passwords as Weak, "
    "Medium, or Strong."
)

st.write(
    "Pandas is used for data analysis and Matplotlib "
    "is used for data visualization."
)

st.write(
    "The project demonstrates basic concepts of "
    "data analysis, classification and visualization."
)

st.caption(
    "🔐 Password Strength Analyzer | "
    "Python + Streamlit | IDS Project"
)