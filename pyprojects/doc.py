class MyDoctor:
    ''' No known errors '''
    
    def sayHi(self):
        print("Hi")

    def sayBye(self):
        print("Bye")

    def askDocQuestion(self):
        question = input("Do you want a health tip? Yes or no.").lower()
        
        if question == "yes":
            print("Good! Eat less suger.")
        else:
            print("Too bad!")
    
doc = MyDoctor()

print(doc.__doc__)

doc.sayHi()
doc.askDocQuestion()
doc.sayBye()
