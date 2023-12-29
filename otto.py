import os
import re

from nonebot import MessageSegment

import hoshino
from hoshino import Service,priv

from .HuoZiYinShua.huoZiYinShua import huoZiYinShua

self_path = os.path.dirname(__file__)
settings = {
    "sourceDirectory": os.path.join(self_path, 'HuoZiYinShua', 'sources',''),
    "ysddSourceDirectory": os.path.join(self_path, 'HuoZiYinShua', 'ysddSources',''),
    "dictFile": os.path.join(self_path, 'HuoZiYinShua', 'dictionary.json'),
    "ysddTableFile": os.path.join(self_path, 'HuoZiYinShua', 'ysddTable.json')
}

HZYS = huoZiYinShua(settings)

sv = Service(
    name = 'ottohzys',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = True, #是否默认启用
    )

# self_path = os.path.dirname(__file__)

@sv.on_prefix("otto",only_to_me=False)
async def ottohzys(bot, ev):
    txt = ev.message.extract_plain_text()
    pattern_reverse = re.compile(u'-reverse\s*$')
    
    if isinstance(re.search(pattern_reverse, txt), (re.Match)):
        # 结尾匹配到 -reverse
        reverse = True
        txt = re.sub(pattern_reverse, "", txt)
        txt = "，，，" + txt  # 加一段空白
    else:
        reverse = False
        txt = txt + "，，，" # 加一段空白
    
    b64audio = HZYS.export(txt,inYsddMode=True,reverse=reverse)
    await bot.send(ev, MessageSegment.record(f"base64://{b64audio.decode()}"))


