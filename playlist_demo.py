from ll import Node, LinkedList


def create_playlist() -> LinkedList:
    playlist = LinkedList()

    base_songs = [
        {"name": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours"},
    ]


    for song in base_songs:
        playlist.insert_at_end(Node(song))

    return playlist