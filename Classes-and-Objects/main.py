class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.track = score
        pass

        def __change_name__(self):
            print(self.name)

        def __change_age__(self):
            print(self.age)

        def __add_track__(self):
            print(self.tracks)

        def __get_score__(self):
            print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
