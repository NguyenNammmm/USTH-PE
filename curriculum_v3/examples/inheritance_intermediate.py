from language_base import ProgrammingLanguage


class C(ProgrammingLanguage):
    def __init__(self, name, year_created, paradigms, std_version):
        super().__init__(name, year_created, paradigms)
        self.std_version = std_version

    def __str__(self):
        description = super().__str__()
        return description + f", Standard version[{self.std_version}]"

    def compile(self):
        print(f"Compiling C code using standard version {self.std_version}")
