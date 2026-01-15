import streamlit as st
import pandas as pd

st.title("Любими неща - класна анкета")

# Инициализация на данните
if "colors" not in st.session_state:
    st.session_state.grades = {
        "Слаб (2)": 0,
        "Среден (3)": 0,
        "Добър (4)": 0,
        "Мн. Добър (5)": 0,
        "Отличен (6)": 0
    }

if "sports" not in st.session_state:
    st.session_state.students = {
        "Salih": 0,
        "Rado": 0,
        "Nasko": 0,
        "Mitko": 0
    }

st.subheader("Избери любими неща")

grades = st.selectbox("Оценка:", list(st.session_state.grades.keys()))
students = st.selectbox("Ученик:", list(st.session_state.students.keys()))

if st.button("Запази избора"):
    st.session_state.grades[grades] += 1
    st.session_state.students[students] += 1
    st.success("Изборът е записан!")

st.divider()

st.subheader("Резултати")


st.write("Любими цветове")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(grades_df)


st.write("Любими спортове")
students_df = pd.DataFrame.from_dict(
    st.session_state.students, orient="index", columns=["Брой"]
)
st.bar_chart(students_df)
