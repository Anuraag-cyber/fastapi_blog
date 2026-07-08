from fastapi import FastAPI
# Import the FastAPI class to create the application.

from fastapi.responses import HTMLResponse
# Import HTMLResponse to return HTML instead of JSON.


app = FastAPI()
# Create a FastAPI application.


posts = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]
# Dummy data stored as a Python list of dictionaries.


@app.get("/", response_class=HTMLResponse, include_in_schema=True)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=True)
# Two GET routes mapped to the same function. Returns HTML and hides these routes from Swagger docs.

def home():
    return f"<h1>{posts[0]['title']}</h1>"
# Returns the title of the first post as an HTML heading.


@app.get("/api/posts")
# Creates a GET API endpoint for '/api/posts'.

def get_posts():
    return posts
# Returns the Python list. FastAPI automatically converts it to JSON.