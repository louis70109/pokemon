# Pokemon Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/louis70109/pokemon#contributing)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://badge.fury.io/py/lotify)

It is a Type-Safe Python SDK which can enhance your Pokemon development.

# Usage

```shell
pip install pokemon

# or

python setup.py install
```

```python
from pokemon.sprite import Pokemon

pokemon = Pokemon().get('ivysaur')
print(pokemon.name)
print(pokemon.baseStats)
```

# Development

```shell
git clone
cd pokemon/
python -m pytest tests/
```

# License

[MIT](https://github.com/louis70109/pokemon/blob/master/LICENSE)
