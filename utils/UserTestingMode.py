class Task():
    tasks = {}
    def __init__(self, order, niceIndex, name, argsText, argsType, func):
        self.order = order
        self.niceIndex = niceIndex
        self.name = name
        self.argsText = argsText
        self.argsType = argsType
        self.func = func
        Task.tasks[self.order] = self
    
    def getPrettyText(self):
        return str(self.niceIndex) + ": " + self.name

    def select(self):
        argsGiven = []
        for i in range(len(self.argsText)):
            argsGiven.append(self.argsType[i](input(self.argsText[i] + ": ")))
        print(self.func(*argsGiven))

    @staticmethod
    def start():
        for i in range(len(Task.tasks)):
            print(Task.tasks[i].getPrettyText())
        
        selection = -1
        while selection == -1:
            selectionInput = input(":").lower()
            for i in Task.tasks:
                if Task.tasks[i].niceIndex.lower() == selectionInput:
                    selection = i
            if selection == -1:
                print("Invalid input!")
        Task.tasks[selection].select()
        
