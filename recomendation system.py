
item_features = {
    0: ['Action', 'Adventure'],
    1: ['Drama', 'Romance'],
    2: ['Comedy'],
    3: ['Action', 'Sci-Fi'],
    4: ['Mystery',],
    5: ['Thriller','Crime']
}


liked_genres = ['Action', 'Adventure','Romance']
#liked_genres1 = ['Crime','Drama']


recommended_items = []
for item_id, genres in item_features.items():
    if any(genre in genres for genre in liked_genres):
        recommended_items.append(item_id)

print(f"Recommended items for user based on liked genres: {recommended_items}")
