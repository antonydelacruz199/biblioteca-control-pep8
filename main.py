"""
Librería maestra de gestión de libros (main.py).
"""

from biblioteca import Book, Biblioteca


def main() -> None:
    """Ejecuta una demostración del sistema de biblioteca."""
    objetoBiblioteca = Biblioteca("central")

    book1 = Book("Python", "Guido", 1)
    book2 = Book("Java", "Gosling", 2)

    objetoBiblioteca.addb(book1)
    objetoBiblioteca.addb(book2)

    objetoBiblioteca.show()

    print(book1.prest())
    print(book1.prest())
    book1.ret()
    print(book1.prest())

if __name__ == "__main__":
    main()
