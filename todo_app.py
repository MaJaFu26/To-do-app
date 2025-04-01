import streamlit as st

st.title("✅ To-Do List with Categories")

# Categories
categories = ["Wintercare", "CCInc"]

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = {cat: [] for cat in categories}

# Select category
selected_category = st.selectbox("Select category", categories)

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("Add"):
    if new_task:
        st.session_state.tasks[selected_category].append({"task": new_task, "done": False})

# Colored headers
if selected_category == "Wintercare":
    st.markdown("### <span style='color:black'>Tasks for Wintercare</span>", unsafe_allow_html=True)
else:
    st.markdown("### <span style='color:red'>Tasks for CCInc</span>", unsafe_allow_html=True)

# Show and update tasks
for i, task in enumerate(st.session_state.tasks[selected_category]):
    is_done = st.checkbox(task["task"], value=task["done"], key=f"{selected_category}_{i}")
    st.session_state.tasks[selected_category][i]["done"] = is_done

# Clear completed tasks
if st.button("Clear completed"):
    st.session_state.tasks[selected_category] = [
        t for t in st.session_state.tasks[selected_category] if not t["done"]
    ]

