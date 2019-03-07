from simmodel import SimModel
import matplotlib.pyplot as plt

elements = 10

timesList = []

while elements <= 500:
    sim = SimModel()
    time = sim.main(elements)
    elements += 10
    timesList.append(time)

print(timesList)

timesArr = [i['time'] for i in timesList ]

plt.plot(timesArr)
plt.ylabel('Execution time')
plt.show()