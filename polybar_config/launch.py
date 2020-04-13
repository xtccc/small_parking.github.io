#!/bin/python3

import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk
import os

allmonitors = []
gdkdsp = Gdk.Display.get_default()

os.system('killall -q polybar')
os.system('while pgrep -u $UID -x polybar > /dev/null; do sleep 1; done')

for i in range(gdkdsp.get_n_monitors()):
    monitor = gdkdsp.get_monitor(i)
    primary = monitor.is_primary()
    allmonitors.append([monitor.get_model()] + [primary])

monitorint = len(allmonitors)


for i, x in zip(range(monitorint), allmonitors):
    print('x[1]={}'.format(x[1]))
    if x[1]:
        os.system(f'MONITOR={x[0]} polybar -r main &')
    else:
        os.system(f'MONITOR={x[0]} polybar -r main &')
