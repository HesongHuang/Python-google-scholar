import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json

number=[]
name=[]

def get_json():
	with open('journal.json') as json_file:
			data = json.load(json_file) 
	for key in data:
			number.append(data[key])
			key = key.replace("journal={","")
			key = key.replace("},","")
			name.append(key)

def draw():			
	plt.rcdefaults()
	fig, ax = plt.subplots()

	y_pos = np.arange(len(name))
	error = np.random.rand(len(name))

	ax.barh(y_pos, number, xerr=error, align='center',
			color='blue', ecolor='black')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(name)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Performance')
	ax.set_title('How fast do you want to go today?')

	plt.show()
	
if __name__=="__main__":
	get_json()
	draw()
