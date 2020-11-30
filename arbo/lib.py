import os
from pathlib import Path
def create_arbo():
    name = input('Name of your project ? ')
    os.mkdir(name)
    os.mkdir(f'{name}/{name}')
    Path(f'{name}/{name}/lib.py').touch()
    Path(f'{name}/{name}/__init__.py').touch()


    os.mkdir(f'{name}/scripts')
    Path(f'{name}/scripts/{name}-run').touch()

    os.mkdir(f'{name}/tests')
    Path(f'{name}/tests/{name}_test.py').touch()
    Path(f'{name}/tests/__init__.py').touch()

    Path(f'{name}/requirements.txt').touch()
    Path(f'{name}/setup.py').touch()
