class Medienbibliothek:
    def __init__(self):
        self._title = 0

    def Movie(self, title):
        if -1 < title <= 2:
            self._title = title




#0 = "The Godfather"
#1 = "The Shawshank Redemption"
#2 = "Schindler's List"

meine_filme = Medienbibliothek()
meine_filme.Movie(1)
print(meine_filme.film_name())
Medienbibliothek.Movie(2)
print(meine_filme.film_name())
