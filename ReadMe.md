# Family To-Do Dashboard

## Overview
The **Family To-Do Dashboard** is an interactive web-based application built with **Streamlit**. It allows family members to manage tasks, assign responsibilities, and keep personal notes. The app includes an **interactive calendar view** where tasks and notes are visually displayed, making it easy to track activities.

## Features
1. **Login System**:
   - Secure login for multiple family members.
   - Each user has a unique username and password.

2. **Interactive Calendar**:
   - Displays tasks and notes dynamically using **FullCalendar**.
   - Tasks are shown on their assigned dates.
   - Notes are displayed with their corresponding user.

3. **Task Management**:
   - Parents can assign tasks to children with due dates.
   - Children can view tasks assigned to them.

4. **Notes Section**:
   - Each family member can add and view personal notes.
   - Notes are integrated into the calendar.

5. **Logout Functionality**:
   - Ensures secure session management.

## Technologies Used
- **Python**: Backend logic.
- **Streamlit**: Frontend framework for creating the web app.
- **FullCalendar**: Interactive calendar embedded with custom HTML and JavaScript.

## Installation
Follow these steps to run the app locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up Python Environment**:
   Ensure you have Python installed (version 3.8 or above).
   Install the required dependencies:
   ```bash
   pip install streamlit
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the App**:
   Open the provided local URL (e.g., `http://localhost:8501`) in your web browser.

## Usage
1. **Login**:
   - Enter your username and password to log in. Example credentials:
     - **Parent1**: `parent1123`
     - **Parent2**: `parent2123`
     - **Child1**: `child1123`
     - **Child2**: `child2123`

2. **View Calendar**:
   - Tasks and notes are displayed on the interactive calendar.
   - Use navigation controls to switch between views (monthly, weekly, daily).

3. **Add Tasks**:
   - Parents can assign tasks to children with a description and due date.

4. **Add Notes**:
   - Users can add personal notes that are displayed in the calendar.

5. **Logout**:
   - Click the "Logout" button in the sidebar to end the session.

## Folder Structure
```
.
├── app.py               # Main application script
├── README.md            # Documentation
└── requirements.txt     # Dependencies
```

## Customization
- **Add More Users**:
  Modify the `family_members` and `passwords` variables in the `app.py` file.
- **Persistent Storage**:
  Integrate a database (e.g., SQLite, PostgreSQL) for storing tasks and notes.

## Future Enhancements
- **Color Coding**:
  Differentiate tasks and notes with colors in the calendar.
- **Drag-and-Drop**:
  Allow users to move tasks between dates.
- **Mobile Responsiveness**:
  Optimize layout for smaller screens.
- **Recurring Tasks**:
  Add support for tasks that repeat periodically.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
