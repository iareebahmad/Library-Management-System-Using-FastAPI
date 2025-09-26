#backend.py
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Streamlit to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

BOOKS = [
    {"Name":"Before The Coffee Gets Cold","Author":"Toshikazu kawaguchi","Genre":"Magical Realism"},
    {"Name":"The Silent Patient","Author":"Alex Michaelides","Genre":"Psychological Thriller"}
]

# API Endpoints
# 1. Get all books
@app.get("/books")
async def get_books():
    return BOOKS

# 2. Add New Book
@app.post("/books")
async def add_book(new_book=Body()):
    for book in BOOKS:          # Check if the book already exists
        if book.get("Name").casefold() == new_book.get("Name").casefold():
            return {"message":"Book Already Exists in Library!"}
    BOOKS.append(new_book)
    return {"message":"Book has been Added!", "book":new_book}

# 3. Delete a Book
@app.delete("/books/{book_title}")
async def del_book(book_title :str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("Name").casefold() == book_title.casefold():
            rem = BOOKS.pop(i)
            return {"message":"Book Deleted Successfully!", "book":rem}


# 4. Find a book whether it exist in lib or not
@app.get("/books/find/{book_name}")
async def find_book(book_name :str):
    for book in BOOKS:
        if book.get("Name").casefold() == book_name.casefold():
            return {"message":"Yup! You have this book"}
    return {"message":"Nope! You don't have this book!"}