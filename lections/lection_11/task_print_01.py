class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
        print(f'Создал {self.name = }')

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


user = User('Спенглер')
print(user)
