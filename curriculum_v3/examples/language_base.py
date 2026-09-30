class ProgrammingLanguage:
    def __init__(self, name, year_created, paradigms):
        self.name = name
        self.year_created = year_created
        self.paradigms = list(paradigms)

    def add_paradigms(self, paradigm):
        self.paradigms.append(paradigm)

    def __str__(self):
        description = f"Language[{self.name}]"
        description += f", Year created[{self.year_created}]"
        description += f", Paradigms{self.paradigms}"
        return description
