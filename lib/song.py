class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name=None, artist=None, genre=None):
        if name is not None and artist is not None and genre is not None:
            self.name = name
            self.artist = artist
            self.genre = genre
            Song.count += 1
            Song.genres.add(genre)
            Song.artists.add(artist)
            Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
            Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1