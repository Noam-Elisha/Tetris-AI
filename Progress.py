import matplotlib.pyplot as plt
import pickle
import os

models = os.listdir('models')
models.sort(key = lambda x: int(x[:-5]))
maximum = []
minimum = []
average = []
for x in models:
	data = pickle.loads(open('models/' + x, 'rb').read())
	maximum.append(max(data, key = lambda a: a.score).score)
	minimum.append(min(data, key = lambda a: a.score).score)
	temp = [a.score for a in data]
	average.append(sum(temp)/len(temp))


plt.plot(maximum)
plt.plot(minimum)
plt.plot(average)
plt.show()



	