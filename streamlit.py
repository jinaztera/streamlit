import streamlit as st

view = [100, 150, 30]
view

st.write("# Youtube view")

# st.bar_chart(view)
#
# st.bar_chart(view)

#헤더 및 텍스트
st.title('My Streamlit App')
st.header('A Header')
st.subheader('A Subheader')
st.text('Some text here.')

#마크다운
st.markdown('**Bold text** and _italic text_ using Markdown.')

# 위젯 (텍스트 입력, 슬라이더 및 확인란)
user_input = st.text_input('Enter some text:')
number = st.slider('Choose a number:', min_value=1, max_value=10)
checkbox = st.checkbox('Check me')

user_input = st.text_input("Enter your name:")
st.write(f"Hello, {user_input}!")

number = st.slider("Choose a number", min_value=1, max_value=100)
st.write(f"You chose the number {number}.")

# 상호작용 및 데이터 처리 추가
if st.button('Run function'):
    st.write('Function executed!')



# 데이터 표시
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
st.dataframe(data)
st.line_chart(data)


# 파일 업로드
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    content = uploaded_file.read()
    st.write(content)


# import time
#
# @st.cache
# def slow_function(x):
#     time.sleep(5)  # Simulating a slow function
#     return x * 2
#
# result = slow_function(10)
# st.write(f"Result: {result}")

# 열
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column 1 content")

with col2:
    st.write("Column 2 content")

with col3:
    st.write("Column 3 content")

# 확장기
expander = st.expander("Click to expand")
expander.write("This content is hidden until the expander is clicked.")
expander.write("This content is hidden until the expander is clicked.")

st.sidebar.title("My Sidebar 1")
st.sidebar.write("Sidebar 1")
st.sidebar.write("Sidebar 2")
st.sidebar.write("Sidebar 3")
st.sidebar.title("My Sidebar 2")
st.sidebar.write("Sidebar 1")
st.sidebar.write("Sidebar 2")
st.sidebar.write("Sidebar 3")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")

if st.button("Increment counter"):
    st.session_state.counter += 1