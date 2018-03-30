from musicbrainzngs import search_artists, set_useragent

def extract_gender(artist_name):
    set_useragent('Python-urllib', 'any')
    return next(i['gender'] for i in search_artists(artist_name)['artist-list'])

def extract_genre(song_title):
    pass 


