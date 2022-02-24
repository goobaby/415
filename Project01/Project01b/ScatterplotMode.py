import matplotlib.pyplot as plt


class Task():
    tasks = {}
    def __init__(self, order, niceIndex, name, xLabel, yLabel, domain, funcNames, funcs):
        self.order = order
        self.niceIndex = niceIndex
        self.name = name
        self.domain = domain
        self.funcNames = funcNames
        self.funcs = funcs
        self.labels = [xLabel,yLabel]
        Task.tasks[self.order] = self
    
    def getPrettyText(self):
        return str(self.niceIndex) + ": " + self.name

    def select(self):
        fig, ax = plt.subplots()
        for i in range(len(self.funcs)):
            points = []
            for j in self.domain:
                points.append(self.funcs[i](j))
            ax.scatter(self.domain,points,label=self.funcNames[i],s=4)
        ax.set_xlabel(self.labels[0])
        ax.set_ylabel(self.labels[1])
        ax.legend()
        plt.show()
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
        
