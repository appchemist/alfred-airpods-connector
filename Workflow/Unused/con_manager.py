#!/usr/bin/python3

import os
import shutil
import sys

from Alfred3 import Tools

query = Tools.getArgv(1)
adr, switch = tuple(query.split(";"))
Tools.log(adr)
Tools.log(switch)

blueutil = shutil.which('blueutil')
Tools.log(blueutil)

if blueutil:
    if switch == "disconnected":
        Tools.log("Connect")
        cmd = f'{blueutil} --connect {adr}'

    else:
        Tools.log("Disconnect")
        cmd = f'{blueutil} --disconnect {adr}'

    Tools.log(cmd)
    sys.stdout.write(cmd)
