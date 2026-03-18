from ll import Node, LinkedList


def create_playlist() -> LinkedList:
    playlist = LinkedList()

    base_songs = [
        {"name": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours"},
        {"name": "Shape of You", "artist": "Ed Sheeran", "album": "Divide"},
        {"name": "Levitating", "artist": "Dua Lipa", "album": "Future Nostalgia"},
        {"name": "Peaches", "artist": "Justin Bieber", "album": "Justice"},
        {"name": "Save Your Tears", "artist": "The Weeknd", "album": "After Hours"},
        {"name": "HUMBLE.", "artist": "Kendrick Lamar", "album": "DAMN."},
        {"name": "God's Plan", "artist": "Drake", "album": "Scorpion"},
        {"name": "Bad Guy", "artist": "Billie Eilish", "album": "WWAFAWDWG"},
        {"name": "Stay", "artist": "The Kid LAROI", "album": "F*CK LOVE"},
        {"name": "As It Was", "artist": "Harry Styles", "album": "Harry's House"},
    ]

    songs = base_songs * 5

    for song in songs:
        playlist.insert_at_end(Node(song))

    return playlist