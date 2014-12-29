#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################################################################
#
# MODULE:       v.out.png
# AUTHOR(S):    Luca Delucchi, Fondazione E. Mach (Italy)
#
# PURPOSE:      Pack up a vector map, collect vector map elements => gzip
# COPYRIGHT:    (C) 2011 by the GRASS Development Team
#
#               This program is free software under the GNU General
#               Public License (>=v2). Read the file COPYING that
#               comes with GRASS for details.
#
#############################################################################

#%module
#% description: Export vector map as PNG
#% keyword: vector
#% keyword: export
#% keyword: PNG
#%end
#%option G_OPT_V_INPUT
#%end
#%option G_OPT_F_OUTPUT
#% label: Name for new PNG file
#%end
#%option
#% key: rgb_column
#% type: string
#% description: Name of color definition column
#%end
#%option
#% key: compression
#% type: integer
#% options: 0-9
#% label: Compression level of PNG file
#% description: (0 = none, 1 = fastest, 9 = best)
#% answer: 6
#%end
#%option
#% key: width
#% type: integer
#% label: Width of PNG file
#% answer: 640
#%end
#%option
#% key: height
#% type: integer
#% label: Height of PNG file
#% answer: 480
#%end

import os
import sys
from grass.script import core as grass
from grass.script import gisenv
from grass.pygrass.modules.shortcuts import display as d
from grass.pygrass.modules.shortcuts import general as g


def main():
    os.environ['GRASS_RENDER_IMMEDIATE'] = 'png'
    os.environ['GRASS_RENDER_FILE'] = options['output']
    os.environ['GRASS_RENDER_FILE_COMPRESSION'] = options['compression']
    os.environ['GRASS_RENDER_WIDTH'] = options['width']
    os.environ['GRASS_RENDER_HEIGHT'] = options['height']

    monitor_old = None
    genv = gisenv()
    if 'MONITOR' in genv:
        monitor_old = genv['MONITOR']
        g.gisenv(unset='MONITOR')

    if options['rgb_column']:
        d.vect(map=options['input'], rgb_column=options['rgb_column'], flags='a',
               quiet=True)
    else:
        d.vect(map=options['input'])

    if monitor_old:
        g.gisenv(set='MONITOR=%s' % monitor_old)


if __name__ == "__main__":
    options, flags = grass.parser()
    sys.exit(main())
