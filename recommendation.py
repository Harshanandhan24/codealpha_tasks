movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr Bean", "The Mask", "Hangover"],
    "horror": ["Conjuring", "Annabelle", "Insidious"]
}

genre = input("Enter movie genre: ").lower()

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print(movie)
else:
    print("Genre not found.")