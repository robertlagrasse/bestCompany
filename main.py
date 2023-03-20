import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("Best Company")
content = '''
Best co is the best co. Forget the rest, yo.
'''
st.write(content)

st.subheader('Our Team')

col1, empty1, col2, empty2, col3 = st.columns([3,1,3,1,3])

df = pandas.read_csv("data.csv")
first = int(len(df)/3)
second = first * 2

with col1:
    for index, row in df[:first].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(f"{row['role']}")
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[first:second].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(f"{row['role']}")
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[second:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(f"{row['role']}")
        st.image(f"images/{row['image']}")