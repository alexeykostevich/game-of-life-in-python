# Conway's Game of Life
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in Python 3.6.

```python
from life import Cell, ClosedWorld, Life


# Simulate 'The Game of Life' in a 10 x 10 world
world = ClosedWorld.random(10, 10, Cell.likely)
life = Life(world)

for world in life:
    print(world)
    input('Press Enter to continue...')
```

## Demo
```bash
# Requires a Posix-compatible terminal (Linux or OS X)
$ python3 demo.py
```

## Technology Stack
|                      | Technology                                         |
| -------------------- |----------------------------------------------------|
| Language             | [Python 3.6](https://www.python.org/)              |
| Linter               | [Flake8 3.5](http://flake8.pycqa.org/en/latest/)   |

## Development
### Prerequisites
1. [Python 3.6](https://www.python.org/downloads/)

### Quickstart
1. [Creates and activates](https://docs.python.org/3/library/venv.html) a Python virtual environment

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
```

2. Install dependencies

```bash
$ pip install -r requirements.txt
```

### Unit Tests
Use [test discovery](https://docs.python.org/3/library/unittest.html#test-discovery) to run all unit tests at once.

```bash
$ python -m unittest discover
```

### Styleguide
The project uses [PEP8](https://www.python.org/dev/peps/pep-0008/). [Flake8](http://flake8.pycqa.org/en/latest/) is setup to enforce the rules.

```bash
$ flake8
```
