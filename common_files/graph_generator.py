import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

EPOCH = []
_VARS = {
    'fig_agg': False,
    'plt_fig': False
}


def error_values_plot(error, epoch, ax):
    # clear axis
    ax.cla()

    # plot error
    ax.plot(epoch, error)
    ax.scatter(len(error), error[-1])

    matplotlib.pyplot.title("Erro X Época")
    matplotlib.pyplot.ylabel("Erro")
    matplotlib.pyplot.xlabel("Época")


def draw_figure(canvas, figure):
    tk_figure_agg = FigureCanvasTkAgg(figure, canvas)
    tk_figure_agg.draw()
    tk_figure_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return tk_figure_agg


def draw_initial_graph(canvas):
    _VARS['plt_fig'] = matplotlib.pyplot.figure()
    matplotlib.pyplot.title("Erro X Época")
    matplotlib.pyplot.ylabel("Erro")
    matplotlib.pyplot.xlabel("Época")
    _VARS['fig_agg'] = draw_figure(canvas, _VARS['plt_fig'])


def update_graph(canvas, error):
    _VARS['fig_agg'].get_tk_widget().forget()

    matplotlib.pyplot.clf()

    if len(error) <= 1:
        EPOCH.clear()
    EPOCH.append(len(error))
    ax = _VARS['plt_fig'].add_subplot(1, 1, 1)
    error_values_plot(error, EPOCH, ax)

    _VARS['fig_agg'] = draw_figure(canvas, _VARS['plt_fig'])
