from ll import Node
from playlist_demo import create_playlist


def play_song(node: Node) -> None:
    data = node.data

    print("\nReproduciendo:")
    print(f"Canción: {data['name']}")
    print(f"Artista: {data['artist']}")
    print(f"Álbum: {data['album']}")


def run() -> None:
    playlist = create_playlist()
    current = playlist.start

    if current is None:
        return

    while True:
        play_song(current)

        print("\nOpciones:")
        print("1. Siguiente")
        print("2. Anterior")
        print("3. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            if current.next is not None:
                current = current.next
            else:
                print("\nLímite: última canción")

        elif option == "2":
            if current.prev is not None:
                current = current.prev
            else:
                print("\nLímite: primera canción")

        elif option == "3":
            print("\nSaliendo...")
            break

        else:
            print("\nOpción inválida")


if __name__ == "__main__":
    run()