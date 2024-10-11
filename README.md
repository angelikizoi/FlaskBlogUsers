# Flask Blog Application

A simple Flask blog application that allows users to register, log in, create blog posts, and comment on posts. Admin users can manage posts
(create, edit, delete), while registered users can leave comments on blog posts.

This project is based on and inspired by the **100 Days of Code: The Complete Python Pro Bootcamp for 2023** 
course by Angela Yu. The course provides an excellent introduction to Python and was the foundation for this game. 
You can check out the course on [Udemy](https://www.udemy.com/course/100-days-of-code/?couponCode=ST14MT101024#reviews).
## Features
- User registration and login
- Admin-only access to post creation, editing, and deletion
- Rich-text blog post creation using CKEditor
- Gravatar integration for user profile images
- Commenting system for blog posts
- Secure password hashing using Werkzeug
- Database setup with SQLAlchemy
- Environment-based configuration using `python-dotenv`

## Requirements
Make sure you have the following installed:
- Python 3.6+
- Flask and other dependencies (see `requirements.txt`)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/angelikizoi/FlaskBlogUsers.git
cd FlaskBlogUsers
```

### 2. Set Up a Virtual Environment
You can set up a virtual environment to manage your dependencies.

For **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

For **macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all the necessary dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File
In the root directory of your project, create a `.env` file to store environment variables such as `FLASK_KEY` and `DB_URI`.

Example `.env` file:
```bash
FLASK_KEY=your-secret-flask-key
DB_URI=sqlite:///posts.db  # Use your preferred DB URI, or leave this for local SQLite
```

### 5. Initialize the Database
Before running the application, ensure the database is set up:
1. Open a Python shell:
   ```bash
   flask shell
   ```
2. In the shell, run the following command to create the database tables:
   ```python
   from app import db
   db.create_all()
   ```

### 6. Run the Application
To start the Flask server, run the following command:
```bash
flask run
```
By default, the app will be accessible at `http://127.0.0.1:5000/`.

## Project Structure

```bash
FlaskBlog/
├── main.py              # Main Flask application
├── forms.py            # WTForms for handling forms like registration, login, post creation
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (not uploaded to GitHub)
├── templates/          # HTML templates for rendering the pages
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── post.html
│   ├── make-post.html
│   ├── ...
├── static/             # Static files like CSS, JS, images
├── venv/               # Virtual environment (not uploaded to GitHub)
└── README.md           # Project README file
```

## Routes Overview

- **`/`**: Displays all blog posts.
- **`/register`**: Allows new users to register.
- **`/login`**: Allows existing users to log in.
- **`/logout`**: Logs out the current user.
- **`/new-post`**: Admin-only route for creating a new blog post.
- **`/edit-post/<post_id>`**: Admin-only route for editing a blog post.
- **`/delete/<post_id>`**: Admin-only route for deleting a blog post.
- **`/post/<post_id>`**: Displays a specific post along with the comment section.
- **`/about`**: Information about the blog.
- **`/contact`**: Contact information page.

## Environment Variables

The application uses environment variables to manage sensitive configurations. These variables should be stored in a `.env` file, and the `python-dotenv` package is used to load them. Key variables:
- `FLASK_KEY`: The secret key for Flask session management.
- `DB_URI`: The URI of the database. For local development, this can be SQLite (e.g., `sqlite:///posts.db`). For production, use PostgreSQL or another database.

## Running Tests
If you have tests set up, you can run them using:
```bash
python -m unittest discover
```

## Deployment
To deploy this application:
1. Ensure you have a production-ready database set up (such as PostgreSQL).
2. Configure the `DB_URI` environment variable accordingly.
3. Use a WSGI server like **gunicorn** to run the app in production.

Example with gunicorn:
```bash
gunicorn app:app
```
