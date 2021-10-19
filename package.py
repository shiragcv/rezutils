# -*- coding: utf-8 -*-

name = 'rezutils'

version = '1.0.0'

description = 'Utilities for rez package manager'

build_command = 'pip install --upgrade --target={install_path} {root}'

tools = [
    'copy-folder'
]

def commands():
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.append('{root}')
