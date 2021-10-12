import os
import setuptools


def get_configuration(path):
    if not os.path.exists(path):
        raise OSError('File not found')

    return setuptools.config.read_configuration(path)

def get_metadata(path):
    configuration = get_configuration(path) or {}
    return configuration.get('metadata') or {}
