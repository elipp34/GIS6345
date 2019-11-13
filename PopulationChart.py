Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib
>>> import matplotlib.pyplot as plt
import
>>> import numpy as np
>>> fig, ax = plt.subplots()

>>> cities = ('Mecca', 'Djibouti', 'Jiddah', 'Khartoum', 'Nairobi')
>>> y_pos = np.arange(len(cities))
>>> population = 100000 + 100000 * np.random.rand(len(people))
error = np.random.rand(len(cities))

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    population = 100000 + 100000 * np.random.rand(len(people))
NameError: name 'people' is not defined
>>> population = 100000 + 100000 * np.random.rand(len(cities))
error = np.random.rand(len(cities))
>>> ax.barh(y_pos, population, xerr=error, align='center')

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ax.barh(y_pos, population, xerr=error, align='center')
NameError: name 'error' is not defined
>>> error = np.random.rand(len(cities))
>>> ax.barh(y_pos, population, xerr=error, align='center')
<Container object of 5 artists>
>>> ax.set_yticks(y_pos)
[<matplotlib.axis.YTick object at 0x041823B0>, <matplotlib.axis.YTick object at 0x041822B0>, <matplotlib.axis.YTick object at 0x041F3110>, <matplotlib.axis.YTick object at 0x041F3650>, <matplotlib.axis.YTick object at 0x041F3B90>]
>>> ax.set_yticklabels(cities)
[<matplotlib.text.Text object at 0x0418D950>, <matplotlib.text.Text object at 0x041A0610>, <matplotlib.text.Text object at 0x041F3590>, <matplotlib.text.Text object at 0x041F3AD0>, <matplotlib.text.Text object at 0x041FC030>]
>>> ax.invert_yaxis()
>>> ax.set_xlabel('Population')
<matplotlib.text.Text object at 0x03FC5B70>
>>> ax.set_title('Africa City Population')
<matplotlib.text.Text object at 0x041A0DB0>
>>> 
>>> plt.show()
