"""
Módulo biblioteca.

Contiene las clases para gestionar una biblioteca simple y sus libros.
"""


class Biblioteca:
    """Representa una biblioteca que almacena una colección de libros."""

    def __init__(self, name: str) -> None:
        """Inicializa la biblioteca con un nombre y una lista vacía de libros."""
        self.name = name
        self.libros: list[Book] = []

    def addb(self, book: "Book") -> None:
        """Agrega un libro a la biblioteca."""
        self.libros.append(book)

    def show(self) -> None:
        """Muestra en consola la información básica de cada libro."""
        for libro in self.libros:
            print(libro.titulo, libro.autor, libro.indice)


class Book:
    """Representa un libro con estado de disponibilidad para préstamo."""

    def __init__(self, titulo: str, autor: str, indice: int) -> None:
        """Crea un libro con título, autor, índice y estado disponible."""
        self.titulo = titulo
        self.autor = autor
        self.indice = indice
        self.exist = True

    def lend(self) -> bool:
        """Presta el libro si está disponible. Retorna True si se prestó."""
        if self.exist:
            self.exist = False
            return True
        return False

    def back(self) -> None:
        """Devuelve el libro (lo marca como disponible)."""
        self.exist = True
