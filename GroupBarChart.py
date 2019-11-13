import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['A1', 'B2', 'C3', 'D4', 'E5']
X_scores = [10, 20, 30, 40, 50]
Y_scores = [50, 25, 40, 35, 60]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, x_scores, width, label='X')
rects2 = ax.bar(x + width/2, y_scores, width, label='Y')

ax.set_ylabel('Scores')
ax.set_title('By group')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

