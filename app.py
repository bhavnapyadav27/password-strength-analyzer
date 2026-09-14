import streamlit as st
import string

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐"
)

st.title("🔐 Password Strength Analyzer")
st.write("Check the strength of your password.")

password = st.text_input(
    "Enter your password:",
    type="password"
)

if password:

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Display analysis
    st.subheader("📊 Password Analysis")

    st.write("Password Length:", len(password))
    st.write("Score:", str(score) + "/5")

    # Determine strength
    if score <= 2:
        strength = "🔴 Weak"
    elif score <= 4:
        strength = "🟠 Medium"
    else:
        strength = "🟢 Strong"

    st.subheader("Strength: " + strength)

    # Progress bar
    st.progress(score / 5)

    # Suggestions
    if suggestions:
        st.subheader("💡 Suggestions")

        for suggestion in suggestions:
            st.write("• " + suggestion)
    else:
        st.success(
            "🎉 Excellent! Your password meets all basic requirements."
        )