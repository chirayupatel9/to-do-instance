import streamlit as st
from datetime import date, datetime
from collections import defaultdict
import json

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user" not in st.session_state:
    st.session_state["user"] = None
if "tasks" not in st.session_state:
    st.session_state["tasks"] = defaultdict(list)
if "notes" not in st.session_state:
    st.session_state["notes"] = defaultdict(str)

# Mock family members
family_members = ["Parent1", "Parent2", "Child1", "Child2"]
passwords = {member: f"{member.lower()}123" for member in family_members}

# Login Page
def login_page():
    st.title("Family To-Do Dashboard")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username in passwords and passwords[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")

# Dashboard Page
def dashboard():
    st.title(f"Welcome, {st.session_state['user']}!")
    
    # Sidebar: Display family members and their notes
    st.sidebar.title("Family Members")
    for member in family_members:
        st.sidebar.subheader(member)
        if st.session_state["notes"][member]:
            st.sidebar.write(f"**Note:** {st.session_state['notes'][member]}")
        else:
            st.sidebar.write("No notes yet.")
    st.sidebar.markdown("---")
    st.sidebar.button("Logout", on_click=logout)

    # Layout
    col1, col2 = st.columns([2, 1])

    # Calendar View
    with col1:
        st.subheader("Calendar View")
        show_calendar()

    # Task and Note Management
    with col2:
        st.subheader("Manage Tasks and Notes")
        if st.session_state["user"] in ["Parent1", "Parent2"]:  # Parents can assign tasks
            assign_tasks()
        else:  # Children can view their tasks
            view_tasks()

        # Notes Section
        st.subheader("Notes")
        add_notes()

# Assign Tasks (Parents Only)
def assign_tasks():
    selected_child = st.selectbox("Select Child", [m for m in family_members if "Child" in m])
    new_task = st.text_input("Task Description")
    task_date = st.date_input("Task Date", value=date.today())
    if st.button("Add Task"):
        if new_task:
            st.session_state["tasks"][selected_child].append({"task": new_task, "date": task_date})
            st.success(f"Task added for {selected_child} on {task_date}!")
        else:
            st.warning("Task cannot be empty.")

# View Tasks (Children)
def view_tasks():
    st.write("Your Tasks:")
    user_tasks = st.session_state["tasks"][st.session_state["user"]]
    if user_tasks:
        for task in user_tasks:
            st.write(f"- {task['task']} (Due: {task['date']})")
    else:
        st.write("No tasks assigned yet.")

# Add Notes
def add_notes():
    new_note = st.text_area(f"Add a note for {st.session_state['user']}")
    if st.button("Save Note"):
        st.session_state["notes"][st.session_state["user"]] = new_note
        st.success("Note saved!")

# Show Calendar
def show_calendar():
    """Render the interactive calendar using FullCalendar."""
    events = prepare_events()
    calendar_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/fullcalendar@5.11.0/main.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/fullcalendar@5.11.0/main.min.js"></script>
        <style>
            #calendar {{
                max-width: 90%;
                margin: auto;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <div id="calendar"></div>
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var calendarEl = document.getElementById('calendar');
                var calendar = new FullCalendar.Calendar(calendarEl, {{
                    initialView: 'dayGridMonth',
                    headerToolbar: {{
                        left: 'prev,next today',
                        center: 'title',
                        right: 'dayGridMonth,timeGridWeek,timeGridDay'
                    }},
                    events: {json.dumps(events)}
                }});
                calendar.render();
            }});
        </script>
    </body>
    </html>
    """
    st.components.v1.html(calendar_html, height=600, scrolling=True)

# Prepare Events for Calendar
def prepare_events():
    """Combine tasks and notes into calendar events."""
    events = []
    
    # Add tasks to calendar
    for member, tasks in st.session_state["tasks"].items():
        for task in tasks:
            events.append({
                "title": f"Task: {task['task']} ({member})",
                "start": task["date"].isoformat(),
                "allDay": True
            })

    # Add notes to calendar
    for member, note in st.session_state["notes"].items():
        if note:
            events.append({
                "title": f"Note: {note} ({member})",
                "start": date.today().isoformat(),
                "allDay": True
            })

    return events

# Logout Function
def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None

# Main App
if st.session_state["logged_in"]:
    dashboard()
else:
    login_page()
