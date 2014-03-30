import seaborn as sb
import pandas as pd

__all__ = ["uncertainty_plot"]

def uncertainty_plot(data, center=None, filternull=True):
    """
    Take a Series object and make a relative uncertainty plot. This
    centers the plot and annotates with mean and standard deviation.

    Parameters
    ----------

    data:  a Pandas Series object that contains the data.
    center: If given, center the data on this point, otherwise center
            on the mean.
    filternull: If true (default), filter out null values in the data.
    """

    if filternull is True:
        plotdata = data[data.notnull()]
    else:
        plotdata = data

    if center is None:
        center = plotdata.mean()

    bbox_style = {'boxstyle': 'round', 'fc': 'white', 'lw': 2,
            'alpha': .7, 'ec': 'grey',}
    anntext = """$\mu={}$
    $\sigma={}$""".format(data.mean(), data.std())
    ax = sb.distplot(data - center) 
    ax.text(.02, .88, anntext,
        transform=ax.transAxes,
        bbox=bbox_style,
        )
    ax.axvline(0, color='black')
    return(ax)
