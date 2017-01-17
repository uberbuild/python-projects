#Quiz
#By Aaron
import glob

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

    def runQuiz(self):
        self.score = 0
        self.maxscore = self.Numquestions

        self.i = 0
        for l in self.lines:

            if self.i == 0:
                print(l)

            if self.i == 1:
                print("A:",l)
            if self.i == 2:
                print("B:",l)
            if self.i == 3:
                print("C:",l)
            if self.i == 4:
                print("D:",l)

            if self.i == 5:

                self.answer = input("Answer: ")

                if self.answer.upper() == l[0].upper(): #Has to be l[0] because end of line characters
                    self.score+=1
                    print("Well done")
                else:
                    print("Incorrect, the answer was", l)


            if self.i < 5:
                self.i += 1
            else:
                self.i=0

        print(str(self.score) + " out of " + str(self.maxscore))

def makeQuiz():
    while True:
        quizName = "Quizzes/" + input("What is the name of your quiz? ") + ".txt"
        try: #Terrible ways of checking whether or not a file exists
            open(quizName)
        except FileNotFoundError:
            open(quizName,"x")
            break
        else:
            continue
    numQuestions = input("Number of questions: ")
    quizFile = open(quizName, "a")
    i = 0
    for i in range(int(numQuestions)):
        for j in range(6):# Dont even ask
            if j == 0:
                quizFile.write(input("What is your question? ")+"\n")
            elif j > 0 & j < 5:
                quizFile.write(input("Answer " + str(j)+": ") + "\n")
            else:
                quizFile.write(input("Correct answer (A,B,C,D): ") +"\n")
    quizFile.close()

while True: #Main quiz loop
    print("Would you like to play (p) or create (c) a quiz?")
    if (input("") == "c"):
        makeQuiz()
    else:
        quizzes = glob.glob("Quizzes/*.txt") + glob.glob("*.txt");
        #print(quizzes)
        print("Available Quizzes\n")
        for l in quizzes:
            print(l[0:-4]) #[0:4] removes .txt from end of file

        quiz = input("\nWhich quiz would you like to open? ") + ".txt"
        try:
            quizFile = open(quiz, "r")
        except FileNotFoundError:
            print(quiz,"file does not exist!")
        else:
            qClass = Quiz(quizFile)
            input("Press enter to begin the quiz! V1")
            qClass.runQuiz()