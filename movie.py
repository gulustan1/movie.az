import math

movies = [
    {"id": 1, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": 8.7},
    {"id": 2, "title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8},
    {"id": 3, "title": "The Batman", "genre": "Action", "year": 2022, "rating": 7.9},
    {"id": 4, "title": "Titanic", "genre": "Drama", "year": 1997, "rating": 7.8},
    {"id": 5, "title": "Oppenheimer", "genre": "Biography", "year": 2023, "rating": 8.5},
]

page = 1
page_size = 2

# 1. Sadə səhifələmə testi
start = (page - 1) * page_size
end = start + page_size
page_data = movies[start:end]

# 2. Meta məlumatların hesablanması
total_movies = len(movies)
total_pages = math.ceil(total_movies / page_size)

if page < total_pages:
    next_page = page + 1
else:
    next_page = None

if page > 1:
    prev_page = page - 1
else:
    prev_page = None

# 3. Nəticəni birbaşa ekrana çıxarırıq
result = {
    "page": page,
    "page_size": page_size,
    "next": next_page,
    "prev": prev_page,
    "total_pages": total_pages,
    "data": page_data
}

print(result)