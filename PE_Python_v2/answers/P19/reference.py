from matplotlib.figure import Figure

def build_chart(labels, values):
    fig = Figure()
    ax = fig.subplots()
    positions = list(range(len(labels)))
    ax.bar(positions, values)
    ax.set_xticks(positions, labels)
    ax.set_ylabel("Diem")
    ax.set_ylim(0, 10)
    return fig