import re
import random
import string
import streamlit as st


def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback


def suggest_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title("🔐 Password Strength Meter")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")

if st.button("Submit"):
    st.write("You have successfully logged in")
    if email and password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for tip in feedback:
                st.write(tip)

        if score < 4:
            st.info("🔑 Suggested Strong Password: ")
            st.code(suggest_strong_password())
    else:
        st.warning("⚠️ Please fill both email and password fields.")