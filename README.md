# LITReview Platform Documentation

## Overview

LITReview is a web-based application designed for sharing and reviewing literary works. 
It provides a platform where users can follow each other, share tickets (requests for reviews), 
and write reviews on literary works. The application is built with Django, a high-level Python 
web framework that encourages rapid development and clean, pragmatic design

## Features

- User Authentication: Users can sign up, log in, and log out of the application. Authentication 
  is required to access most parts of the application.
- Ticket Management: Users can create, update, and delete tickets. Each ticket represents a request 
  for a review of a literary work and includes details such as the title, description, and an 
  optional image.
- Review Management: Users can create, update, and delete reviews. Each review is linked to a specific 
  ticket and includes a rating, headline, and body text.
- User Follow System: Users can follow and unfollow other users. This system allows users to see 
  tickets and reviews from users they are interested in.
- Home Page Feed: The home page displays a feed of tickets and reviews from the user and the users 
  they follow, sorted by creation time.

## Installation

1. Clone the repository:

   Clone the LITReview repository to your local machine using Git.

2. Set up a Virtual Environment:

   It's recommended to use a virtual environment for Python projects. You can create one using 
   python -m venv venv and activate it with source venv/bin/activate on Unix/Linux or venv\Scripts\activate on Windows.

3. Install Dependencies

   Install all required dependencies by running pip install -r requirements.txt in the root directory 
   of the project.

4. Migrate the Database

   Apply migrations to create the database schema with python manage.py migrate.

5. Run the server

   Start the Django development server with python manage.py runserver. Access the application 
   by navigating to http://localhost:8080 in your web browser.

## Usage

- Navigating the Application: After logging in, users are redirected to the home page, which 
  displays a feed of tickets and reviews.
- Creating Tickets and Reviews: Use the "Create" buttons for tickets and reviews in the navigation 
  bar to share new content.
- Following Users: Navigate to the "Follow Users" section to follow other users. You can view a 
  list of users you follow and also unfollow them from there.
- Viewing and Updating Content: Each ticket and review has its detail view, where you can read 
  more about it or update and delete your content.
- Logging Out: You can log out using the "Logout" button in the navigation bar.

## Development

The application is structured around Django's Model-View-Template (MVT) architecture. Here is a 
brief overview of the key components:

- Models: Defined in models.py files, they represent the application's data structure.
- Views: Defined in views.py files, they handle the logic and control flow of the application.
- Templates: Located in the templates directory, they define the HTML structure and presentation 
  of the application.
- Forms: Defined in forms.py files, they handle form rendering and validation.
- URLs: Configuration is found in urls.py, routing the URLs to their respective views.
