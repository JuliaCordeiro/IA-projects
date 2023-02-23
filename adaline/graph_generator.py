import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

EPOCH = []
TK_FIGURE = None

def error_values_plot(error, epoch, ax):
    # clear axis
    ax.cla()

    # plot error
    ax.plot(error)
    ax.scatter(len(error)-1, error[-1])
    ax.set_ylim(0, 20)

    matplotlib.pyplot.xticks(range(len(epoch)), epoch)
    matplotlib.pyplot.title("Erro X Época")
    matplotlib.pyplot.ylabel("Erro")
    matplotlib.pyplot.xlabel("Época")

    print("ERROR: {}".format(error))


def draw_graph(error):
    if len(error) <= 1:
        EPOCH.clear()
    EPOCH.append(len(error))

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    error_values_plot(error, EPOCH, ax)
    return fig


def draw_figure(canvas, figure):
    global TK_FIGURE
    if TK_FIGURE is not None:
        TK_FIGURE.get_tk_widget().destroy()
    TK_FIGURE = FigureCanvasTkAgg(figure, canvas)
    TK_FIGURE.draw()
    TK_FIGURE.get_tk_widget().pack(side='top', fill='both', expand=1)
    return TK_FIGURE
