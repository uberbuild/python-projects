#Quiz
#By Aaron

class Quiz:
    def __init__(self, quizFile):
        self.lines = []
        self.Numquestions = 0
        i = 0
        for line in quizFile:
            i += 1
            if i == 6:
                self.Numquestions +=1
                i=0
            self.lines.append(line)

        print("Quiz contains", self.Numquestions, "questions.")
        #self.questions = [[0,0,0,0,0,0] for j in range(self.Numquestions)]


    def runQuiz(self):
        self.score = 0
        self.maxscore = self.Numquestions

        self.qNum = 1
        self.i = 0
        for l in self.lines:
            if self.i == 0:
                print(l)
                self.i+= 1
            if self.i > 0 & self.i < 5:
                print(l)
                self.i += 1
            if self.i == 5:
                self.answer = input("Answer: ")
                if self.answer.upper() == l.upper():
                    self.score+=1
                    print("Well done")
                else:
                    print("Incorrect, the answer was", l)
                self.i=0
        print(str(self.score) + " out of " + str(self.maxscore))

quiz = input("Which quiz would you like to open? ") + ".txt"
quizFile = open(quiz, "r")
qClass = Quiz(quizFile)
input("Press enter to begin the quiz!")
qClass.runQuiz()
