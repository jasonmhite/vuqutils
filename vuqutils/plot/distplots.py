import seaborn as sb
import pandas as pd

__all__ = ["uncertainty_plot"]

def uncertainty_plot(data, center=None, relative=False, filternull=True):
    """
    Take a Series object and make a relative uncertainty plot. This
    centers the plot and annotates with mean and standard deviation.

    Parameters
    ----------

    data:  a Pandas Series object that contains the data.
    center: If given, center the data on this point, otherwise center
            on the mean.
    filternull: If true (default), filter out null values in the data.
    relative: If true, normalize width to the standard deviation
              (default false)
    """

    if filternull is True:
        plotdata = data[data.notnull()]
    else:
        plotdata = data

    if center is None:
        center = plotdata.mean()

    if relative is True:
        plotdata /= plotdata.std()

    bbox_style = {'boxstyle': 'round', 'fc': 'white', 'lw': 2,
            'alpha': .7, 'ec': 'grey',}
    anntext = """$\mu={}$
    $\sigma={}$""".format(data.mean(), data.std())
    ax = sb.distplot(plotdata) 
    ax.text(.02, .88, anntext,
        transform=ax.transAxes,
        bbox=bbox_style,
        )
    ax.axvline(0, color='black')
    return(ax)
