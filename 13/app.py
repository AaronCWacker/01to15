import streamlit as st

# Define Roles and their Descriptions
roles = {
    "1. Coder": "💻 Creates short python code functions to solve tasks.",
    "2. Humanities Expert": "📚 Focuses on arts, literature, history, and other humanities subjects.",
    "3. Analyst": "🤔 Analyzes situations and provides logical solutions.",
    "4. Roleplay Expert": "🎭 Specialized in mimicking behaviors or characters.",
    "5. Mathematician": "➗ Solves mathematical problems with precision.",
    "6. STEM Expert": "🔬 Specialized in Science, Technology, Engineering, and Mathematics tasks.",
    "7. Extraction Expert": "🔍 Strictly sticks to facts and extracts concise information.",
    "8. Drafter": "📝 Exhibits expertise in generating textual content and narratives.",
}

# Streamlit UI
st.title("AI Role Selector - CHARMSED 🤖✨")
st.markdown("""
### Harness the power of AI with the CHARMSED framework. 
#### This suite of roles brings together a comprehensive set of AI capabilities, tailored for diverse tasks:

- **C**oder 💻: Craft pythonic solutions with precision.
- **H**umanities Expert 📚: Dive deep into arts, literature, and history.
- **A**nalyst 🤔: Derive insights through logical reasoning.
- **R**oleplay Expert 🎭: Mimic behaviors or adopt personas for engaging interactions.
- **M**athematician ➗: Crunch numbers and solve mathematical enigmas.
- **S**TEM Expert 🔬: Navigate through the realms of Science, Technology, Engineering, and Mathematics.
- **E**xtraction Expert 🔍: Extract concise information with a laser-focus.
- **D**rafter 📝: Generate textual content and narratives with flair.

Empower your tasks with the perfect AI role and unleash the magic of CHARMSED!
""")

# Dropdown to select role
selected_role = st.selectbox("Select AI Role:", list(roles.keys()))

# Display the description of the selected role
st.write(roles[selected_role])

# Switch to choose between two models
model = st.radio("Choose Model:", ["model_1", "model_2"])

# Text area for user input
user_input = st.text_area("Provide your task/question:")

# Button to execute
if st.button("Execute"):
    # Here, you would add code to get the AI response based on the selected role and model.
    # For now, just echoing the user input.
    st.write(f"You said: {user_input}")
