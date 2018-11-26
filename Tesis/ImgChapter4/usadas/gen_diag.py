# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

figsize = (10, 8)
cols = 2

fig1 = plt.figure(num=1, figsize=figsize)
# fig1 = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(4, cols, figure=fig1,
                       # height_ratios=[4,4,4,4] ,
                       # width_ratios=[2]*2
                       )
gs.update(hspace=1)

def add_sub(row, col, title, x, y, ylim=0.5):
    sub_plot = fig1.add_subplot(gs[row, col])
    sub_plot.set_title(title)
    sub_plot.set_xlabel(u"Iteración")
    sub_plot.set_ylabel("Distancia")
    sub_plot.set_xticks(x)
    sub_plot.set_ylim(0, ylim)
    sub_plot.plot(x, y, 'o', ls='-')


add_sub(0, 0, "Sentiment APIs", [0, 1], [0, 0.474])
add_sub(0, 1, "Game feeds", [0, 1], [0, 0.36])
add_sub(1, 0, "Tweeter APIS", range(7), [0, 0.1, 0.233, 0.3, 0.333, 0.358, 0.36])
add_sub(1, 1, "Bc Laws", range(6), [0.3999, 0.4, 0.692, 0.75, 0.77, 0.763], 1.0)
add_sub(2, 0, "Vat API", [0, 1, 2], [0.092, 0.303, 0.392])
add_sub(2, 1, "Azure SQL Database", [0, 1], [0.152, 0.19], 0.25)
add_sub(3, 0, "import.io", [0, 1, 2], [0, 0.1, 0.25], 0.4)
add_sub(3, 1, "loginstuff.web", [0, 1], [0.208, 0.276], 0.4)
fig1.tight_layout(pad=1.4, w_pad=0.5, h_pad=2.0)

plt.show()

