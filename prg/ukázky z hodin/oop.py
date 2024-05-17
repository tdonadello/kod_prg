class Student():
    def __init__(self, name, school, colour):
        self.name = name
        self.school = school
        self.fav_colour = colour
    def speak(self, pozdrav):
        print(f"{pozdrav}, my favorite colour is {self.fav_colour}")


class Zak(Student):
    def __init__(self, name, school, colour):
        super().__init__(name, school, colour)

hvezdon = Student("Hvězdoň", "Třebešín", "red")

print(hvezdon.fav_colour)
hvezdon.speak("Hello")


rehor = Student("Řehoř", "Úžlabina", "blue")
rehor.speak("Hi")


ida = Zak("Ida", "Nějaké základka", "modrá")
ida.speak("Dobrý den")