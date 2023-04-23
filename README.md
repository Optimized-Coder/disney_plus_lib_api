# Disney Plus Library API

## Introduction
This is a RESTful API that allows you to retrieve information about movies and TV shows available on Disney+. The API is built with Python and Flask and uses a dataset from Kaggle that lists all shows and movies available on Disney+. The dataset was collected from JustWatch in March 2023 and contains data available in the United States.

---
## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.7 or higher
- Flask
- SQLAlchemy

### Installing
Clone this repository to your local machine:
```console
$ git clone https://github.com/Optimized-Coder/disney_plus_lib_api.git
```

Install dependencies:
```console
$ pip install -r requirements.txt
```

Start the server:
```console
$ python app.py
```

---
## API Endpoints
This API provides the following endpoints:

### GET /api/
This endpoint returns all the titles available in the dataset.

### GET /api/title/<title_id>/
This endpoint returns a single title with the specified ID. If the ID is not found, it returns "Title Not Found".

### GET /api/movies/
This endpoint returns all the movies available in the dataset.

### GET /api/shows/
This endpoint returns all the TV shows available in the dataset.

### GET /api/top-20/
This endpoint returns the top 20 titles based on their TMDb rating.

### GET /api/top-100/
This endpoint returns the top 100 titles based on their TMDb rating.

### GET /api/genre/<genre>/
This endpoint returns all the titles in the specified genre.

### GET /api/decade/<decade>/
This endpoint returns all the titles released in the specified decade. The decade parameter should be an integer, e.g. 1980 for the 1980s.

## Conclusion
This API provides easy access to information about Disney+ titles. With the various endpoints available, you can retrieve specific information about movies and TV shows based on your needs. If you have any feedback or suggestions, please feel free to contribute to the project.
