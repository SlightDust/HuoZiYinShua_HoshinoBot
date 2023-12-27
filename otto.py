import os

# self_path = os.path.join(os.path.dirname(__file__), 'latest.json')
self_path = os.path.dirname(__file__)

from HuoZiYinShua.huoZiYinShua import huoZiYinShua
import re
HZYS = huoZiYinShua("./HuoZiYinShua/settings.json")
print("ok")