import matplotlib


def error_values_plot(error, epoch, ax):
    # clear axis
    ax.cla()

    # plot error
    ax.plot(error)
    ax.scatter(len(error)-1, error[-1])
    ax.set_ylim(0, 1)

    matplotlib.pyplot.xticks(range(len(epoch)), epoch)
    matplotlib.pyplot.title("Erro X Época")
    matplotlib.pyplot.ylabel("Erro")
    matplotlib.pyplot.xlabel("Época")

    print("ERROR: {}".format(error))


def draw_graph(error, epoch, error_value):
    matplotlib.use('TkAgg')
    error.append(round(error_value, 5))
    epoch.append(len(error))
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    error_values_plot(error, epoch, ax)
    return fig
