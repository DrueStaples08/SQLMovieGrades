

class MovieGrade:
    def __init__(self, title, grade, points, votes, mu):
        self.title = title
        self.grade = grade 
        self.points = points 
        self.votes = votes 
        self.mu = mu 

    def __repr__(self):
        print(f'Title: {self.title}, Grade: {self.grade}, Points: {self.points}, Votes: {self.votes}, Mu: {self.mu}')
        


    