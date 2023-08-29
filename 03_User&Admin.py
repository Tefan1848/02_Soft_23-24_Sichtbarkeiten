class User():
    def __init__(self) -> None:
        self._username = "User"
        self.__password = "1234"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise ValueError("Passwort muss ein String sein!")
        elif len(password) < 1:
            raise ValueError("Passwort must not be empty!")
        self.__password = password

    def check_password(self, password: str) -> bool:
        if password == self.__password:
            return True
        return False

    def print_username(self):
        print(self._username)

user = User()
print(user.check_password("1234"))
user.print_username()

class Admin(User):
    def __init__(self) -> None:
        super().__init__()

    def change_username(self, username : str):
        if not isinstance(username, str):
            raise ValueError("Username muss ein String sein!")
        elif len(username) < 1:
            raise ValueError("Username must not be empty!")
        self._username = username

admin = Admin()
admin.change_username("Admin")
admin.print_username()

