class Student:
    # initializing class intances
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

# change student's name, accept a new name as an argument.
    def change_name(self, new_name):
        Bob.name = new_name

# change student's age, accept a new age as an argument.
    def change_age(self, new_age):
        Bob.age = new_age

# Add a new item to student's tracks, accept a new track as an argument.
    def add_track(self, new_track):
        (Bob.tracks).append(new_track)

# Return student’s score.
    def get_score(self):
        return self.score

# checking results on IDE
    def __str__(self):
        return f"{self.name} is {self.age} years old, enrolled in {self.tracks} tracks, with current score of {self.score}"


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Testing initial results
print(Bob)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

# Testing final results
print(Bob)
