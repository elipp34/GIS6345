>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> linestyle_str = [
     ('solid', 'solid')
     ('dashed', 'dashed')
     ('dotted', 'dotted')
     ('dashdot', 'dashdot')
def plot_linestyles (ax, linestyles):
     X, Y = np.linspace (0, 100, 10), np.zeros(10)
     yticklabels = []

     for i in enumerate(linestyles):
     ax.plot(X, Y+i, linestyle=linestyle, linewidth=1.5, color='black')
     yticklabels.append(name)

     ax.set(xticks=[], ylim=(-.05, len(linestyles)-.05),
            yticks.np.arange(len(linestyles)), yticklabels=yticklabels

    for i in enumerate(linestyles):
            ax.annotate(repr(linestyle),
                    xy=(0.0, i), xycoords=ax.get_yaxis_transform(),
                    xytext=(-6, -12), textcoords='offset points',
                    color="blue", fontsize=8, ha="right", family="monospace")

fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 3]},
                               figsize=(10, 8))
plot_linestyles(ax0, linestyle_str[::-1])

plt.tight_layout()
plt.show()

            
