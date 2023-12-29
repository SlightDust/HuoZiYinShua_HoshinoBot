# HuoZiYinShua_HoshinoBot

适用于HoshinoBot的otto活字印刷插件

核心代码来自[DSP-8192/HuoZiYinShua](https://github.com/DSP-8192/HuoZiYinShua)，参考了[Kazagumo/nonebot-HuoZiYinShua](https://github.com/Kazagumo/nonebot-HuoZiYinShua)的修改，截止本次编辑，两个仓库均未声明开源协议。

## 安装方法
1. 在hoshino/modules下clone本仓库`git clone https://github.com/SlightDust/HuoZiYinShua_HoshinoBot.git`
2. 在hoshino/config/__bot__.py中加入

```python
MODULES_ON = {
...
'HuoZiYinShua_HoshinoBot',  # otto活字印刷
}
```
3. 重启hoshino

另外需要手动安装以下pip库：  
soundfile  
psola  
numpy  
pypinyin  

功能默认开启。服务叫ottohzys。  

## 使用说明
|指令|说明|指令示例|
|----|----|----|
| otto 一些内容 | otto语音活字印刷 | otto 大家好啊，我是里见光钻 |
|otto 一些内容-reverse| 活字印刷，并倒放 | otto 哈里路大旋风 -reverse |

## Todo List
- [x] 基本功能  
- [ ] 异步  
- [ ] 添加更多原生大碟

## 日志
2023/12/27 缝好了，能用了  
2023/12/29 以-reverse结尾可以倒放