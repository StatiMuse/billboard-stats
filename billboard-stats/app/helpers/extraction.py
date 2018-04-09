from musicbrainzngs import search_artists, set_useragent

def extract_gender(artist_name):
    set_useragent('Python-urllib', 'any')
    result = next(i for i in search_artists(artist_name)['artist-list'])
    if result:
        return result['gender'] if 'gender' in result else None
    return None 

def extract_genre(song_title):
    pass 


