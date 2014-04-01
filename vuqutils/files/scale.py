import numpy as np
import pandas as pd
import re
import tables as pt

__all__ = ['read_sdf', 'write_sdf']

file_header_reader = re.compile('(^.*)energy boundaries:', re.DOTALL)
file_footer_reader = re.compile('\n\n(.*)', re.DOTALL)
sections = re.compile('^\S.*$', re.MULTILINE)
header_reader = re.compile(r"""
    ^\s*(?P<isotope>\S+)\s+(?P<reaction_type>\S+)\s+(?P<id>\S+)\s+(?P<mixture>\S+)
    \s+(?P<geometry>\S+).*$
""", re.X)
sens_reader = re.compile('\n?\s*', re.MULTILINE)

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
    headers = sections.findall(raw_text)[1:]
    raw_sens = sections.split(raw_text)[1:]
    # Hack to make the regexs match properly
    raw_sens[-1] += '\n'

    # First block is the energy boundaries
    energies = xs2numpy(raw_sens[0])
    r = [run_header, run_footer, energies]

    for (header, sens) in zip(headers, raw_sens[1:]):
        infodict = header_reader.match(header).groupdict()
        # Trim the first three, they aren't useful
        infodict['sensitivity'] = xs2numpy(sens)[3:]

        r.append(infodict)

    return(r)


def sensRecordBuilder(N):
    class SensRecord(pt.IsDescription):
        isotope = pt.StringCol(16)
        geometry = pt.Int64Col()
        id = pt.StringCol(16)
        mixture = pt.StringCol(16)
        reaction_type = pt.StringCol(16)
        sensitivity = pt.Float64Col(shape=(N,))

    return(SensRecord)

def write_sdf(filename, records):
    with pt.open_file(filename, mode='w', title='SCALE Sensitivity') \
            as h5file:
        ns = records[3]['sensitivity'].shape[0]

        runinfo = h5file.createArray(h5file.root, 'run_info',
                records[0], "Run information")
        valinfo = h5file.createArray(h5file.root, 'validation_info',
                records[1], "Validation information")
        energies = h5file.createArray(h5file.root, 'energies',
                records[2], "Energy boundaries")
        senstable = h5file.create_table(h5file.root, 'sensitivities',
                sensRecordBuilder(ns), 'Sensitivity run results')

        for record in records[3:]:
            sensvector = senstable.row

            for (field, setting) in record.iteritems():
                sensvector[field] = setting

            sensvector.append()
            senstable.flush()
