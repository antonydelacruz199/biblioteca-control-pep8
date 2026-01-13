"""
Librería maestra de gestión de libros (main.py).
"""

from biblioteca import Book, Biblioteca


def main() -> None:
    """Ejecuta una demostración del sistema de biblioteca."""
    objeto_biblioteca = Biblioteca("central")

    book1 = Book("Python", "Guido", 1)
    book2 = Book("Java", "Gosling", 2)

    objeto_biblioteca.addb(book1)
    objeto_biblioteca.addb(book2)

    objeto_biblioteca.show()

    print(f"Primer préstamo de '{book1.titulo}': {book1.lend()}")
    print(f"Segundo préstamo de '{book1.titulo}': {book1.lend()}")
    book1.back()
    print(f"Préstamo después de devolver '{book1.titulo}': {book1.lend()}")


if __name__ == "__main__":
    main()
