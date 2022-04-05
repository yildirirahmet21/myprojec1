 
from plotly.offline import plot
import plotly.graph_objects as go

def grafik1(datalar):

    x = [e.Puan for e in datalar]
    y1 = [e.Puan for e in datalar]
  
    graphs = []

    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

 
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 700,
        'width': 800,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')


    return plot_div        