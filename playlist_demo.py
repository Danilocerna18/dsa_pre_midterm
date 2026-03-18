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
        {"name": "Medallo", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Imposible Remix", "artist": "Blessd", "album": "Single"},
        {"name": "Quien TV Remix", "artist": "Blessd", "album": "Single"},
        {"name": "Tendencia Global", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Instagram", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Hace Tiempo", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Dime", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "AP", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Te Canto Bajito", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Mujeriego", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Ojitos Rojos", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Antioquia", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Si Sabe", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Pa Olvidar", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "Aguardiente", "artist": "Blessd", "album": "Hecho en Medellín"},
        {"name": "GTA", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Palabras Sobran", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Sisas Nada", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Bendecido", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Deportivo", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "La 1", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Casi Algo", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Dos Problemas", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Tussi Code", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Carita de Ángel", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Envigado", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Yogurcito", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "Mirame", "artist": "Blessd", "album": "Siempre Blessd"},
        {"name": "La Curiosidad Remix", "artist": "Blessd", "album": "Single"},
        {"name": "Ojitos Azules", "artist": "Blessd", "album": "Single"},
        {"name": "Tamo Bien", "artist": "Blessd", "album": "Single"},
        {"name": "El Mensaje", "artist": "Blessd", "album": "Single"},
        {"name": "Tu Me Prefieres a Mi", "artist": "Blessd", "album": "Single"},
        {"name": "Pintas", "artist": "Blessd", "album": "Single"},
        {"name": "Melo", "artist": "Blessd", "album": "Single"},
        {"name": "Ferrari", "artist": "Blessd", "album": "Single"},
        {"name": "Bandido", "artist": "Blessd", "album": "Single"},
        {"name": "No Se Equivoca", "artist": "Blessd", "album": "Single"},
        {"name": "Tu Perfume", "artist": "Blessd", "album": "Single"},
        {"name": "Quien Diria", "artist": "Blessd", "album": "Single"},
        {"name": "Como Antes", "artist": "Blessd", "album": "Single"},
        {"name": "No Fue Suficiente", "artist": "Blessd", "album": "Single"},
        {"name": "Amor y Plata", "artist": "Blessd", "album": "Single"},
        {"name": "Una Noche Mas", "artist": "Blessd", "album": "Single"},
        {"name": "Malvada", "artist": "Blessd", "album": "Single"},
        {"name": "Cual Es Esa", "artist": "Blessd", "album": "Single"},
        {"name": "Pa Las Girlas", "artist": "Blessd", "album": "Single"},
        {"name": "La Baby", "artist": "Blessd", "album": "Single"},
        {"name": "Frikitona", "artist": "Blessd", "album": "Single"},
        {"name": "No Me Supera", "artist": "Blessd", "album": "Single"},
    ]


    for song in base_songs:
        playlist.insert_at_end(Node(song))

    return playlist