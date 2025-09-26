#app.py
import streamlit as st
import requests

BASE_URL = "http://library-management-system-using-fastapi-production.up.railway.app"

# Title and Configuration
st.title("FastAPI Library Management System")
st.set_page_config(layout="centered")
st.subheader("Keep a Track of Your Books!")

# Sidebar and Logo
with st.sidebar:
    st.image("lib.png")
    st.markdown("---")
    st.markdown("### Features")
    st.markdown("""
    - View Books
    - Add New Books
    - Delete a Book
    - Find a Book
    """)

# 1. Get all books
with st.expander("📚 View All Books"):
    if st.button("Show Books", key="show_books"):
        response = requests.get(f"{BASE_URL}/books")
        books = response.json()
        st.table(books)

# 2. Add New Book
with st.expander("🆕 Add a New Book"):
    name = st.text_input("Book Name", key="add_name")
    author = st.text_input("Author", key="add_author")
    genre = st.text_input("Genre", key="add_genre")

    if st.button("Add Book", key="add_book"):
        if name and author and genre:
            new_book = {"Name": name,"Author":author,"Genre":genre}
            response = requests.post(f"{BASE_URL}/books", json = new_book)
            st.success(response.json()["message"])
        else:
            st.error("Please fill all the fields")

# 3. Delete a Book
with st.expander("🗑️ Delete a Book"):
    book_to_del = st.text_input("Name of the Book to be Deleted", key="delete_name")

    if st.button("Delete Book", key="delete_book"):
        if book_to_del:
            response = requests.delete(f"{BASE_URL}/books/{book_to_del}")
            st.success(response.json()["message"])
        else:
            st.error("Enter the Name of the Book To Be Deleted")
# 4. Find a Book
with st.expander("🧐 Find a Book"):
    find_book = st.text_input("Enter the Name of the Book to be Searched", key="find_name")

    if st.button("Find Book", key="book_find"):
        response = requests.get(f"{BASE_URL}/books/find/{find_book}")
        result = response.json()
        st.info(result["message"])
st.markdown("---")
st.markdown('<p style="text-align:center;">Made ❤️ by Areeb</p>', unsafe_allow_html = True)