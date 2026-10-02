import streamlit as st
import ollama

st.set_page_config(
    page_title="ServiceNow Interview Buddy",
    page_icon="🚀"
)

st.title("🚀 ServiceNow Interview Buddy")

st.write(
    "Generate ServiceNow interview questions using Local AI"
)

role = st.selectbox(
    "Role",
    [
        "Administrator",
        "Developer",
        "Consultant",
        "Architect"
    ]
)

experience = st.slider(
    "Years of Experience",
    0,
    20,
    5
)

if st.button("Generate Questions"):

    prompt = f"""
    You are an expert ServiceNow interviewer.

    Generate 5 interview questions.

    Candidate Role: {role}
    Experience: {experience}

    Include:
    - Technical questions
    - Scenario based questions
    - Best practices

    Return only numbered questions.
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    st.subheader("Generated Questions")

    st.write(
        response["message"]["content"]
    )