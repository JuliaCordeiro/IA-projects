import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

EPOCH = []


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
    tk_figure_agg = FigureCanvasTkAgg(figure, canvas)
    tk_figure_agg.draw()
    tk_figure_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return tk_figure_agg


def draw_initial_graph(canvas):
    figure = matplotlib.pyplot.figure()
    tk_initial_figure = draw_figure(canvas, figure)
    return tk_initial_figure


# def update_graph():
#     tk_figure_agg.get_tk_widget().forget()
#
#     matplotlib.pyplot.clf()