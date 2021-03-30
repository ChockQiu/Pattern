# Pattern
一个基于正则表达式匹配字符串的命令行工具

#### 为了解决什么问题而开发？
1. 输出匹配的字符串内容
与grep不同，这个功能是仅输出正则表达式匹配字段的内容；对于仅需要匹配字符串而不是整个行内容的命令行需求会很有用；例如在一堆数据中包含了一个版本号，下一个命令需要用到这个版本号时，便可使用这个命令将这个版本号输出作为下一个命令行的输入；

2. 输出匹配的行
这个功能基本跟grep命令类似，输出包含匹配字符串行的内容；

3. 插入内容
在配置文件或者流的匹配字段【前/后】插入特定内容，这对于修改配置文件会很有用，例如在配置文件的某个字段前或者后加入一项内容；

4. 替换字符串
在文件或者流中通过正则表达式匹配替换字符串为想要的字符串，同样在修改配置文件时会很有用；例如在配置文件中将某个字段替换为想要的内容；

#### 有哪些功能？
```
C:\Windows\System32>pattern -h
usage: pattern [-h] [-f filename] -p PATTERN [-r REPLACEMENT] [-m {0,1,2,3,4,5,6}]

正则表达式命令行工具

optional arguments:
  -h, --help            show this help message and exit
  -f filename, --filename filename
                        目标文件名,如果未提供文件则运行为流模式
  -p PATTERN            正则匹配表达式
  -r REPLACEMENT        需要替换成字符串的值(mode等于3、4、5时忽略)
  -m {0,1,2,3,4,5,6}, --mode {0,1,2,3,4,5,6}
                        模式选择: 0(输出匹配的行,default), 1(前边插入), 2(后边插入), 3(输出匹配字符串), 4(输出第一个匹配的字符串), 5(输出所以匹配的字符串),
                        6(替换模式, 输出替换后的字符串)
```
#### 源码地址
https://github.com/JerryQch/Pattern

#### 使用示例
1. 模式0
> ls -l | pattern -p "Nov"

这个模式与grep用法类似

![image.png](https://upload-images.jianshu.io/upload_images/13651212-27d5e71424b97334.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


2. 模式1 - 在匹配字段前端插入
> pattern -f config.xml -p "</driverVer>" -r "1.0.0" -m 1

![image.png](https://upload-images.jianshu.io/upload_images/13651212-add0b7e9b68e64e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 模式2 - 在匹配字段后端插入
> pattern -f config.xml -p "</driverVer>" -r "1.0.0" -m 2

![image.png](https://upload-images.jianshu.io/upload_images/13651212-d4ec427a2c77f766.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4. 模式3 - 输出匹配字段
> pattern -f config.xml -p "[0-9\.]{5}" -m 3

![image.png](https://upload-images.jianshu.io/upload_images/13651212-b8eff2c869830410.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

5. 模式6 - 替换匹配字段
> pattern -f config.xml -p "[0-9\.]{5}" -r "2.0.0" -m 6

![image.png](https://upload-images.jianshu.io/upload_images/13651212-61ee2d014a90414d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

