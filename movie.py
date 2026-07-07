import math
movies = [
    {"id": 1, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": 8.7},
    {"id": 2, "title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8},
    {"id": 3, "title": "The Batman", "genre": "Action", "year": 2022, "rating": 7.9},
    {"id": 4, "title": "Titanic", "genre": "Drama", "year": 1997, "rating": 7.8},
    {"id": 5, "title": "Oppenheimer", "genre": "Biography", "year": 2023, "rating": 8.5},
]
def get_movies(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return movies[start_index:end_index]

def get_movies_with_meta(page,page_size):
    total_movies = len(movies)
    total_pages = math.ceil(total_movies / page_size)
    paginated_movies = get_movies(page, page_size)

    if page < total_pages:
        next_page = page + 1
    else:
        next_page = None     
     if page > 1:
        prev_page = page - 1
    else:
        prev_page = None

return {
        "page": page,
        "page_size": page_size,
        "next": next_page,
        "prev": prev_page,
        "total_pages": total_pages,
        "data": page_data
    }
if __name__ == "__main__":
    print("Sadə Səhifələmə (Səhifə 1, Ölçü 2)")
    print(get_movies(1, 2))
    
    print("\n Meta Məlumatla Səhifələmə (Səhifə 1, Ölçü 2)")
    print(get_movies_with_meta(1, 2))
    