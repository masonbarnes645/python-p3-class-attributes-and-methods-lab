class Song:
    count = 0
    genres = []
    artists = []
    artist_count={}
    genre_count={}
    
    
    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.genre = genre
        self.artist = artist
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)
        # type(self).add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls,genre):
            if genre not in cls.genres:
                cls.genres.append(genre)
                cls.genre_count[genre] = 1
            else:
                cls.genre_count[genre] += 1
                 
        
    @classmethod
    def add_to_artists(cls,artist):
            if artist not in cls.artists:
                cls.artists.append(artist)
                cls.artist_count[artist] = 1
            else:
                cls.artist_count[artist] += 1
                

                 





