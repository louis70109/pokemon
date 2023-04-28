import json

from pokemon.typing.sprite import Sprite


class Pokemon:

    def __init__(self, name=None, *args, **kwargs):
        super(Pokemon, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Pokemon>"

    def get(self, name="bulbasaur"):
        try:
            with open('statics/en_pokemon.json') as f:
                data = json.load(f)
            sprite = data[name.lower()]
            return Sprite(**sprite)
        except KeyError:
            # 如果名字不存在於 en_pokemon.json 文件中，返回一個錯誤消息
            return f"Error: Pokemon '{name}' not found"
