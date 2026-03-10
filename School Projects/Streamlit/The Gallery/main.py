import streamlit as st # type: ignore
from datetime import datetime, date, time
import pandas as pd
import uuid

st.set_page_config(page_title="The Gallery", page_icon="TheGallery.png", layout="wide")

if 'ToDo' not in st.session_state:
    st.session_state.ToDo = []
    
if 'notes' not in st.session_state or isinstance(st.session_state.notes, str):
    st.session_state.notes = []
    
if 'habits' not in st.session_state:
    st.session_state.habits = []

if 'schedule_df' not in st.session_state:
    times = [
        "01:00 AM", "02:00 AM", "03:00 AM", "04:00 AM", "05:00 AM", "06:00 AM", "07:00 AM", "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", 
        "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM", "08:00 PM", "09:00 PM", "10:00 PM", "11:00 PM", "12:00 AM",
    ]
    st.session_state.schedule_df = pd.DataFrame({
        "Time": times,
        "Monday": [""] * len(times),
        "Tuesday": [""] * len(times),
        "Wednesday": [""] * len(times),
        "Thursday": [""] * len(times),
        "Friday": [""] * len(times),
        "Saturday": [""] * len(times)
    })

if 'flashcards' not in st.session_state:
    st.session_state.flashcards = []

if 'flashcard_index' not in st.session_state:
    st.session_state.flashcard_index = 0

if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

# SIDEBAR
st.sidebar.title("Navigation")

st.sidebar.divider()
current_page = st.sidebar.radio("Pick a page:", ["Welcome", "Student Gallery"])

if 'coffee_count' not in st.session_state:
    st.session_state.coffee_count = 3

def add_coffee():
    st.session_state.coffee_count += 1

def reset_coffee():
    st.session_state.coffee_count = 0


# HOMEPAGE
if current_page == "Welcome":
    
    col1, col2, col3 = st.columns([3,3,1.8])

    with col2:
        st.image("TheGallery.png", width=100)

    st.title("Welcome to The Gallery")
    st.write("A personal Student Hub")

    tab_welcome, tab_about = st.tabs(["Home", "About"])
    
    #WELCOME
    with tab_welcome:

        st.header("Lian Andrew R. Arellano | ICS-01-401-A")

        st.write("""
        Welcome to your new digital headquarters. Being a student is a lot to handle, so I built 
        The Gallery to keep the important stuff in one place. Whether you're here to dump some brain notes, 
        check off your to-do list, or grind through flashcards, this hub is designed to 
        help you stay focused and finish strong. Let’s get to work!""")
        
        col1, col2, col3 = st.columns(3)

        if 'ToDo' in st.session_state:
            tasks_done = len([t for t in st.session_state.ToDo if t['is_done']])
            tasks_left = len([t for t in st.session_state.ToDo if not t['is_done']])
        else:
            tasks_done, tasks_left = 0, 0
        
        col1.metric("Tasks Finished", tasks_done)
        col2.metric("Tasks Left", tasks_left)
        col3.metric("Coffee Consumed", f"{st.session_state.coffee_count} cups")
        
        btn_col1, btn_col2, spacer = col3.columns([2, 8, 3])
        btn_col1.button("Add", on_click=add_coffee)
        btn_col2.button("Reset", on_click=reset_coffee)
        
        st.divider()
        
        if st.button("I need motivation!"):
            st.balloons()

    #ABOUT        
    with tab_about:
            st.subheader("About This App")
            st.write("Assignment 5: Exploring API Documentation for Streamlit UI Components")

            st.subheader("What the app does (Use-case)")
            st.write("""
            The Gallery is an all-in-one personal academic dashboard designed to centralize and manage a student's workflow. 
            It functions as a digital planner that tracks tasks, monitors habits, and facilitates active recall studying.
                    
            **Side Note about The Development:** This project was developed with the assistance of AI, which served as a real-time tutor. 
            I used it to break down multiple complex documentation, troubleshoot state management logic, and explore 
            the best practices for Streamlit’s UI components. I truly enjoyed the process of following through with the AI's guidance; 
            it turned coding this assignment into an interactive learning experience where I felt like I was building *with* a mentor rather 
            than just following a rubric.
            """)

            st.subheader("Who the target user is?")
            st.write("""
            The primary target user is a university or college student who wants a distraction-free, unified hub to 
            organize their coursework, balance personal habits, and actively study without needing to switch between 
            multiple different productivity apps.
            """)

            st.subheader("Inputs collected")
            st.write("""
            - **Text & Data Entry**: Task titles, note content, and flashcard questions/answers.
            - **Time & Scheduling**: Deadlines via date pickers and drop-downs, and schedule blocks via the interactive data editor.
            - **Categorization**: Subject selections and view-mode toggles via radio buttons and select boxes.
            - **Metrics**: Habit goals via number inputs and task urgency via a dynamic select slider.
            """)

            st.subheader("Outputs shown")
            st.write("""
            - **Visual Progress**: Progress bars for habits, to-do lists, and flashcard study sessions.
            - **Dynamic Data**: A master timeline that automatically merges regular classes with active task deadlines.
            - **File Generation**: Downloadable .txt files for saved digital notes.
            - **Dashboard Metrics**: Real-time counters for coffee consumption, study proficiency, and task completion.
            """)

            with st.expander("My UI Component Documentation"):
                st.write("""
                * **st.set_page_config**: I used this to set the browser tab title and a wide layout for better data visibility.
                * **st.sidebar & st.radio**: I implemented these to create a clean navigation system that separates the 'About' section from the workspace.
                * **st.columns**: I utilized these to align my dashboard metrics and images side-by-side for a professional look.
                * **st.tabs**: I used tabs to organize the 'Student Gallery' into distinct functional areas like Tasks, Habits, and Notes.
                * **st.expander**: I hid my input forms inside expanders to keep the UI clean while still allowing quick access to data entry.
                * **st.form & st.form_submit_button**: I grouped inputs into forms to ensure the app only refreshes once the user is ready to save.
                * **st.text_input / st.text_area**: I used these to collect everything from short task titles to long-form digital notes.
                * **st.date_input & st.selectbox**: These allowed me to capture precise deadlines and categorical data like subjects.
                * **st.select_slider**: I used this to let users 'feel' the urgency of a task by sliding from 'Chill' to 'Urgent.'
                * **st.data_editor**: I implemented this advanced component to allow users to type directly into their class schedule like a spreadsheet.
                * **st.download_button**: I added this to allow users to export their digital notes as text files for offline use.
                * **st.progress**: I used visual progress bars to give immediate feedback on study sessions and habit completion.
                * **st.metric**: I chose this to highlight key statistics on the home page, giving the app a true dashboard feel.
                * **st.toast**: I used non-intrusive 'toasts' to confirm when data has been successfully saved.
                * **st.balloons**: I added this as a fun interactive element for when the user needs a boost of motivation.
                """)
                
# STUDENT GALLERY
elif current_page == "Student Gallery":
        
        col1, col2, col3 = st.columns([3,3,1.8])

        with col2:
            st.image("StudentGallery.png", width=120)

        st.title("Student Gallery")
        
        # Tabs
        tab_todo, tab_habits, tab_notes, tab_schedule, tab_flashcards = st.tabs(["To-Do List", "Habits", "Notes", "Schedule", "Flash Cards"])
        
        # TODOLIST
        with tab_todo:
            st.header("Things I need to do")

        # Add new task
            with st.expander("Add Something To-Do", expanded=False):
                with st.container():
                    with st.form("add_task_form"):
                        title = st.text_input("Title", placeholder="Read chapter 4")
                        description = st.text_area("Description", placeholder="Summarize key points...")
                        
                        col1, col2, col3, = st.columns([3,2,1.8])

                        with col2:
                            st.write("Deadline")
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            deadline_date = st.date_input("Date", value=date.today())
                        with col2:
                            hour = st.selectbox("Hour", options=list(range(1, 13)))
                        with col3:
                            minute = st.selectbox("Minute", options=[f"{m:02d}" for m in range(0, 60)])
                        with col4:
                            ampm = st.selectbox("AM/PM", options=["AM", "PM"])

                        subject = st.selectbox("Subject", options=[
                            "Personal",
                            "Information Management",
                            "Data Structures and Algorithms",
                            "Object-Oriented Programming",
                            "Platform Technologies",
                            "Web Systems and Technologies",
                            "Physical Activities Towards Health and Fitness I",
                        ])

                        urgency = st.select_slider(
                            "How urgent is this?", 
                            options=["Chill", "Normal", "Important", "URGENT"]
                        )

                        submitted = st.form_submit_button("Add to list")
                        
                        if submitted:
                            if title.strip():
                                if ampm == "AM":
                                    hour_24 = 0 if hour == 12 else hour
                                else:
                                    hour_24 = 12 if hour == 12 else hour + 12
                                
                                deadline = datetime.combine(deadline_date, time(hour=hour_24, minute=int(minute)))

                                st.session_state.ToDo.append({
                                    "id": str(uuid.uuid4()),
                                    "title": title.strip(),
                                    "description": description.strip(),
                                    "deadline": deadline,
                                    "subject": subject,
                                    "urgency": urgency,
                                    "is_done": False
                                })
                                st.toast("Added it to the list!")
                                st.rerun()
                            else:
                                st.error("Please enter a title for your task!")

            st.divider()

            # Display Tasks
            if len(st.session_state.ToDo) == 0:
                st.info("Nothing to do yet. Time to relax!")
            else:
                completed_count = 0

                for i, item in enumerate(st.session_state.ToDo):
                    check_col, delete_col = st.columns([0.85, 0.15])

                    with check_col:
                        is_checked = st.checkbox(
                            f"**{item['title']}** - {item['subject']} ({item['urgency']}) \n\n"
                            f"Deadline: {item['deadline'].strftime('%b %d, %Y at %I:%M %p')} \n\n"
                            f"*{item['description']}*",
                            value=item['is_done'],
                            key=f"check_{item['id']}"
                        )
                        
                        if is_checked != item['is_done']:
                            st.session_state.ToDo[i]['is_done'] = is_checked
                            st.rerun()
                        
                        if item['is_done']:
                            completed_count += 1

                    with delete_col:
                        if st.button("Delete", key=f"del_{item['id']}"):
                            st.session_state.ToDo = [
                                t for t in st.session_state.ToDo
                                if t["id"] != item["id"]
                            ]
                            st.rerun()

                st.write("### How am I doing today?")
                total_tasks = len(st.session_state.ToDo)
                progress = completed_count / total_tasks if total_tasks > 0 else 0
                st.progress(progress, text=f"{completed_count} done out of {total_tasks}")


        # HABITS
        with tab_habits: 
            st.header("Daily Habits")
            
            with st.expander("Create a New Habit", expanded=False):        
                with st.form("add_habit_form", clear_on_submit=True):
                    habit_name = st.text_input("Habit Name", placeholder="Drink water")
                    habit_goal = st.number_input("Goal (times per day)", min_value=1, value=1)
                    submitted = st.form_submit_button("Add Habit")

                    if submitted:
                        if habit_name.strip():
                            st.session_state.habits.append({
                                "name": habit_name.strip(),
                                "goal": habit_goal,
                                "progress": 0
                            })
                            st.toast(f"Habit '{habit_name}' added!")
                            st.rerun() 
                        else:
                            st.error("Please enter a habit name!")

            st.divider()

            # Display habits
            if not st.session_state.habits:
                st.info("No habits yet. Add one above!")
            else:
                for i, habit in enumerate(st.session_state.habits):

                    col_name, col_progress, col_btn_add, col_btn_sub, col_delete = st.columns([2, 2, 0.5, 0.5, 1])

                    with col_name:
                        st.write(f"**{habit['name']}**")

                    with col_progress:
                        progress_val = min(habit['progress'] / habit['goal'], 1.0)
                        st.progress(progress_val, text=f"{habit['progress']} / {habit['goal']}")

                    with col_btn_add:
                        if st.button("+", key=f"inc_{i}"):
                            if habit['progress'] < habit['goal']:
                                habit['progress'] += 1
                                st.rerun()
                                
                    with col_btn_sub:
                        if st.button("-", key=f"dec_{i}"):
                            if habit['progress'] > 0:
                                habit['progress'] -= 1
                                st.rerun()

                    with col_delete:
                        if st.button("Delete", key=f"del_{i}"):
                            st.session_state.habits.pop(i)
                            st.rerun()

        # NOTES
            with tab_notes:
                st.header("Brain Dump & Notes")
                
                # ADD A NEW NOTES
                with st.expander("Create a New Note", expanded=False):
                    with st.form("new_note_form", clear_on_submit=True):
                        new_title = st.text_input("Title of Notes", placeholder="Chapter 5 Summary")
                        new_subject = st.selectbox("Subject", options=[
                            "Personal", "Information Management", "Data Structures and Algorithms", 
                            "Object-Oriented Programming", "Platform Technologies", 
                            "Web Systems and Technologies", "Physical Activities Towards Health and Fitness I"
                        ])
                        new_content = st.text_area("Notes", placeholder="Type your notes here...", height=150)
                        submit_note = st.form_submit_button("Save Note")

                        if submit_note:
                            if new_title.strip():
                                st.session_state.notes.append({
                                    "id": str(uuid.uuid4()),
                                    "title": new_title.strip(),
                                    "subject": new_subject,
                                    "content": new_content
                                })
                                st.toast("Note saved!")
                                st.rerun()
                            else:
                                st.error("Please give your note a title!")

                st.divider()

                # DISPLAY AND EDIT EXISTING NOTES
                if not st.session_state.notes:
                    st.info("No notes yet. Create one above!")
                else:
                    for i, note in enumerate(st.session_state.notes):
                        with st.expander(f"{note['title']} - {note['subject']}", expanded=False):
                            
                            edit_title = st.text_input("Edit Title", value=note['title'], key=f"title_{note['id']}")
                            edit_subject = st.text_input("Edit Subject", value=note['subject'], key=f"subj_{note['id']}") 
                            edit_content = st.text_area("Edit Notes", value=note['content'], height=200, key=f"content_{note['id']}")

                            col1, col2, col3 = st.columns([1, 0.62, 10])
                            
                            with col1:
                                if st.button("Save Changes", key=f"save_{note['id']}"):
                                    st.session_state.notes[i]['title'] = edit_title
                                    st.session_state.notes[i]['subject'] = edit_subject
                                    st.session_state.notes[i]['content'] = edit_content
                                    st.toast("Changes saved!")
                                    st.rerun()
                                    
                            with col2:
                                if st.button("Delete", key=f"del_note_{note['id']}"):
                                    st.session_state.notes.pop(i)
                                    st.rerun()
                                    
                            with col3:
                                st.download_button(
                                    label="Download",
                                    data=f"TITLE: {note['title']}\nSUBJECT: {note['subject']}\n\n{note['content']}",
                                    file_name=f"{note['title'].replace(' ', '_')}.txt",
                                    mime="text/plain",
                                    key=f"dl_{note['id']}"
                                )

        # SCHEDULE
                with tab_schedule:
                    st.header("Class Schedule")
                    
                    view_mode = st.radio(
                        "View Mode", 
                        ["Edit Class Schedule", "Master Timeline (Classes + Tasks)"], 
                        horizontal=True
                    )
                    
                    if view_mode == "Edit Class Schedule":
                        st.write("Double-click any empty cell to type in your class. Your changes save automatically.")
                        st.session_state.schedule_df = st.data_editor(
                            st.session_state.schedule_df,
                            use_container_width=True,
                            hide_index=True,
                            column_config={
                                "Time": st.column_config.TextColumn("Time", disabled=True)
                            }
                        )
                    
                    else:
                        st.write("This combines your regular classes with your active To-Do deadlines.")
                        
                        display_df = st.session_state.schedule_df.copy()
                        
                        active_tasks = [t for t in st.session_state.ToDo if not t['is_done']]
                        
                        for task in active_tasks:
                            day_of_week = task['deadline'].strftime('%A')
                            hour_str = task['deadline'].strftime('%I:00 %p')
                            
                            if day_of_week in display_df.columns and hour_str in display_df['Time'].values:
                                row_idx = display_df.index[display_df['Time'] == hour_str].tolist()[0]
                                existing_text = display_df.at[row_idx, day_of_week]
                                
                                task_text = f"DUE: {task['title']}"
                                
                                if existing_text.strip():
                                    display_df.at[row_idx, day_of_week] = existing_text + "\n\n" + task_text
                                else:
                                    display_df.at[row_idx, day_of_week] = task_text
                                    
                        st.dataframe(display_df, use_container_width=True, hide_index=True)
                        
                    st.divider()
                    
                    st.write("### Upcoming Deadlines")
                    active_tasks = [t for t in st.session_state.ToDo if not t['is_done']]
                    
                    if not active_tasks:
                        st.info("No pending tasks! Enjoy your free time.")
                    else:
                        active_tasks = sorted(active_tasks, key=lambda x: x['deadline'])
                        for task in active_tasks:
                            st.write(f"**{task['deadline'].strftime('%A, %b %d at %I:%M %p')}** — {task['title']} *({task['subject']})*")

        # FLASHCARDS
                    with tab_flashcards:
                        st.header("Active Recall Studio")
                        
                        total_cards = len(st.session_state.flashcards)
                        mastered_cards = sum(1 for card in st.session_state.flashcards if card['proficiency'] == 'Mastered')
                        learning_cards = total_cards - mastered_cards
                        
                        stat_col1, stat_col2, stat_col3 = st.columns(3)
                        stat_col1.metric("Total Cards", total_cards)
                        stat_col2.metric("Learning", learning_cards)
                        stat_col3.metric("Mastered", mastered_cards)
                        
                        with st.expander("Add New Flashcard", expanded=False):
                            with st.form("add_flashcard_form", clear_on_submit=True):
                                new_q = st.text_input("Question / Concept", placeholder="What is the primary function of a CPU?")
                                new_a = st.text_area("Answer", placeholder="To execute instructions comprising a computer program.")
                                subject = st.selectbox("Subject", options=[
                                    "Information Management",
                                    "Data Structures and Algorithms",
                                    "Object-Oriented Programming",
                                    "Platform Technologies",
                                    "Web Systems and Technologies",
                                    "Physical Activities Towards Health and Fitness I",
                                ])
                                
                                if st.form_submit_button("Add to Deck"):
                                    if new_q.strip() and new_a.strip():
                                        st.session_state.flashcards.append({
                                            "id": str(uuid.uuid4()),
                                            "question": new_q.strip(),
                                            "answer": new_a.strip(),
                                            "subject": subject,
                                            "proficiency": "New"
                                        })
                                        st.toast("Card added to your deck.")
                                        st.rerun()
                                    else:
                                        st.error("Both a question and an answer are required.")
                        
                        st.divider()
                        
                        if total_cards == 0:
                            st.info("Your deck is empty. Add some flashcards above to begin your study session.")
                        else:
                            st.write("### Study Session")
                            
                            if st.session_state.flashcard_index >= total_cards:
                                st.session_state.flashcard_index = 0
                                
                            current_card = st.session_state.flashcards[st.session_state.flashcard_index]
                            
                            progress = (st.session_state.flashcard_index + 1) / total_cards
                            st.progress(progress, text=f"Card {st.session_state.flashcard_index + 1} of {total_cards}")
                            
                            # Card Display
                            with st.container(border=True):
                                st.caption(f"Subject: {current_card['subject']} | Current Status: {current_card['proficiency']}")
                                st.subheader(current_card['question'])
                                
                                if st.session_state.show_answer:
                                    st.divider()
                                    st.write("**Answer:**")
                                    st.info(current_card['answer'])
                                    
                                    st.write("How well did you know this?")
                                    col1, col2, col3 = st.columns(3)
                                    
                                    with col1:
                                        if st.button("Needs Review", use_container_width=True):
                                            st.session_state.flashcards[st.session_state.flashcard_index]['proficiency'] = "Learning"
                                            st.session_state.show_answer = False
                                            st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % total_cards
                                            st.rerun()
                                    with col2:
                                        if st.button("Got It", use_container_width=True):
                                            st.session_state.flashcards[st.session_state.flashcard_index]['proficiency'] = "Mastered"
                                            st.session_state.show_answer = False
                                            st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % total_cards
                                            st.rerun()
                                    with col3:
                                        if st.button("Hide Answer", use_container_width=True):
                                            st.session_state.show_answer = False
                                            st.rerun()
                                else:
                                    st.write("")
                                    if st.button("Reveal Answer", type="primary", use_container_width=True):
                                        st.session_state.show_answer = True
                                        st.rerun()
                            
                            col_prev, col_spacer, col_next = st.columns([1, 2, 1])
                            with col_prev:
                                if st.button("Previous", use_container_width=True):
                                    st.session_state.flashcard_index = (st.session_state.flashcard_index - 1) % total_cards
                                    st.session_state.show_answer = False
                                    st.rerun()
                            with col_next:
                                if st.button("Skip", use_container_width=True):
                                    st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % total_cards
                                    st.session_state.show_answer = False
                                    st.rerun()