from simmodel import SimModel
import matplotlib.pyplot as plt

elements = 2

timesList = []
elList = []

while elements <= 100:
    sim = SimModel()
    time = sim.main(elements)
    elList.append(elements)
    elements += 1
    timesList.append(time)

print(timesList)
print(elList)

timesArr = [i['time'] for i in timesList ]

plt.plot(timesArr)
plt.ylabel('Execution time')
plt.show()
