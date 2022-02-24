import TaskOne
import TaskTwo
import TaskThree
import UserTestingMode
import ScatterplotMode
if input("Scatterplot mode? (y/n):")[0].lower() != 'y':
    UserTestingMode.Task.start()
else:
    ScatterplotMode.Task.start()