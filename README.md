# Movie API Challenge (movie.az)

This repository contains the solution for the Movie API Challenge, covering Python backend pagination, MongoDB queries, and ES6 JavaScript syntax.

## 📁 Project Structure

movie.az/
│
├── movie.py                  # Part A: Python backend and pagination logic
├── movie_database.mongodb.js # Part B: MongoDB queries for CRUD operations
└── review.js                 # Part C: JavaScript ES6 features review  
    
    Features & Implementation
Part A: Backend (Python)
Implemented pagination logic using Python's list slicing and math utilities:
get_movies(page, page_size): Returns a sliced sublist of movies for the requested page.
get_movies_with_meta(page, page_size): Generates structured metadata containing current page, page size, next page, previous page, total pages, and the data payload.

    Discussion: The Deletion Issue in Offset Pagination
When using simple offset-based pagination, deleting a record alters the index positions of subsequent items. If a user moves to the next page after a deletion occurs, items shift forward into the previous page's index range, causing the user to skip an item.
Part B: MongoDB Queries
Includes standard MongoDB shell queries for CRUD management on the movies collection:
Document insertion (insertOne)
Content filtering (find with $gte and exact match constraints)
Document updates (updateOne with $set)
Document removal (deleteOne)
Document counting (countDocuments)
Sorting query responses (sort in descending order)
Part C: ES6 Review (JavaScript)
Demonstrates foundational modern JavaScript (ES6+) specifications:
Spread Operator (...): Used to clone and append data immutably into arrays.
Arrow Functions (=>): Used as a clean syntax within array filtering methods.
Template Literals (`): Employed for readable string interpolation without complex concatenation.