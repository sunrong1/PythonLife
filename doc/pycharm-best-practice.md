# PyCharm和python最佳实践

## 基本配置
1. pycharm 基本配置（和Intellij保持基本一致）
字体大小：我一般配置18
页面颜色：家里的场景，我一般是高对比度
代码提示：取消大小写Case的匹配

2. pip 镜像配置
````xml
[global]
index-url = http://pypi.douban.com/simple

[install]
trusted-host = pypi.douban.com

````
3. env虚拟环境配置

- pycharm中可以直接创建不同的解释器；
- 自己独立创建虚拟环境
    - python -m venv 虚拟环境名
    - 激活(去激活)：linux source命令；Windows：运行 V1/scripts/ 目录，运行activate.bat文件即可
    - 删除，退出后，删除文件夹即可
## 常用快捷键
好的键盘，加自己熟悉的一套快捷配置和IDE自有的快捷特性，构成自己顺畅的编程环境。

## 插件



