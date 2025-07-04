User Data Access Using Public API (Python + Requests)
This project is a Python script that demonstrates how to fetch and display random user data from a public REST API using the requests library.

It connects to the free API endpoint:

https://api.freeapi.app/api/v1/public/randomusers/user/random

And retrieves key user information such as:

    Name (Title, First, Last)

    Username

    Password

    Profile Picture (Thumbnail URL)

This script shows how to:

    Make an HTTP GET request

    Handle JSON responses

    Safely access nested data in the API response

    Implement basic error handling with try/except

Features:

     Fetches random user data

     Parses and prints user info clearly

   Handles API connection or data errors
   
   Easy to extend into a GUI or web app
