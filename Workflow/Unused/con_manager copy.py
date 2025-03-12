#!/usr/bin/python3

import os
import shutil
import sys
import subprocess
from subprocess import PIPE
import shlex

from Alfred3 import Tools

query = Tools.getArgv(1)
adr, switch = tuple(query.split(";"))

blueutil = shutil.which('blueutil')

if blueutil:
    if switch == "disconnected":
        Tools.log("Connect")
        cmd = f'{blueutil} --connect {adr}'
    else:
        Tools.log("Disconnect")
        cmd = f'{blueutil} --disconnect {adr}'

    Tools.log(cmd)

    args = shlex.split(cmd)
    Tools.log(str(args))
    process = subprocess.Popen(args, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    Tools.log(stdout.decode(encoding='utf-8'))
    Tools.log(stderr.decode(encoding='utf-8'))

    Tools.log(str(process.returncode))

    Tools.log("Finished")