import sys
import os
import shutil
import json


def get_launch(name):
    return {
        'name': f'Day {name}',
        'type': 'python',
        'request': 'launch',
        'program': f'day{name}/day{name}.py',
        'console': 'integratedTerminal',
        'args': [f'day{name}/sample.txt'],
        'justMyCode': True
    }


def add_day(name):

    # Create directory
    os.mkdir(f'day{name}')

    # Copy template
    shutil.copy('template.py', f'day{name}{os.sep}day{name}.py')

    # Add sample data
    with open(f'day{name}{os.sep}sample.txt', 'w') as fp:
        fp.write('0')

    # Add data file
    with open(f'day{name}{os.sep}data.txt', 'w') as fp:
        fp.write('0')

    # Modify launch.json
    data = {}
    with open('.vscode/launch.json', 'r') as fp:
        data = json.load(fp)

    data['configurations'].append(get_launch(name))

    with open('.vscode/launch.json', 'w') as fp:
        json.dump(data, fp)

    print(f'Generated day{name} files')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('need arg')
        sys.exit(-1)

    add_day(sys.argv[1])
