# notems-protect 

## 介绍  
这是个note.ms网络剪贴板保护装置，它可以不断覆盖目标网络剪贴板，从而达到保护的效果。  
 
## 依赖  
- Python3
- Python3的selenium, pywebview, pyperclip库
- 一个正常的浏览器，建议使用Chrome、Firefox、Edge浏览器
- 浏览器所需要的webdriver

## 使用
1. 克隆这个仓库到本地
2. 切换到仓库的目录
3. 根据 `bug.py` 里面的注释配置程序。注意，你必须安装 `Python3` `selenium库` `pywebview` `pyperclip`，下载所需要的webdriver
4. 执行 `python3 gui.py` ，启动程序

## 注意事项  
- 本程序**仅支持 Windows**
- 注意不要做出违反开源许可的行为

## 原理
很简单，就是模拟人类把内容复制下来，然后再粘贴
