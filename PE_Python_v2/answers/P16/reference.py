class Course:
    def passed(self, score):
        return score >= 5

class HonorsCourse(Course):
    def passed(self, score):
        return score >= 8