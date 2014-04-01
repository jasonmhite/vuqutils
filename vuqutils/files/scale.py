import numpy as np
import pandas as pd
import re

__all__ = ['read_sdf']

file_header_reader = re.compile('(^.*)energy boundaries:', re.DOTALL)
file_footer_reader = re.compile('\n\n(.*)', re.DOTALL)
sections = re.compile('^\S.*$', re.MULTILINE)
header_reader = re.compile(r"""
    ^\s*(?P<isotope>\S+)\s+(?P<type>\S+)\s+(?P<id>\S+)\s+(?P<mixture>\S+)
    \s+(?P<geometry>\S+).*$
""", re.X)
sens_reader = re.compile('\n??\s*', re.MULTILINE)

def xs2numpy(block):
    s = sens_reader.split(block)[1:-1]
    v = np.array(s, dtype=np.float64)
    return(v)

def read_sdf(filename):
    with open(filename) as f:
        raw_text = f.read()

    run_header = file_header_reader.findall(raw_text)[0]
    run_footer = file_footer_reader.findall(raw_text)[0]
    raw_text = raw_text.replace(run_header, '')
    raw_text = raw_text.replace(run_footer, '')
    raw_text = raw_text.replace('\n\n', '')
    headers = sections.findall(raw_text)[2:]
    raw_sens = sections.split(raw_text)[2:]

    # First block is the energy boundaries
    energies = xs2numpy(raw_sens[0])

    r = []

    for (header, sens) in zip(headers, raw_sens[1:]):
        infodict = header_reader.match(header).groupdict()
        # Trim the first three, they aren't useful
        infodict['sens'] = xs2numpy(sens)[3:]

        r.append(infodict)

    return(r)
