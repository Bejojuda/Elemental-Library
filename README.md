# Elemental Library

## Usage

The API's endpoints documentation can be accessed through:
```
http://127.0.0.1:8000/
```

The project allows creation of Users for authentication, Books, BookUnits, Authors and Rentals.

A Book has none, one or many authors, and can have multiple BooksUnits.

A Rental has a BookUnit, as well as the rental and return dates, and the User information.

To populate the database use:
```
python manage.py populate
```
