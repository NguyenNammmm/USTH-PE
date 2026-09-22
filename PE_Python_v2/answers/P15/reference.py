class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)