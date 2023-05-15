# Web-stock-detector-by-Selenium-Python
A Web stock detector demo by Python
============================================================================================================================
运行environment.yaml 安装对应依赖环境，建议使用anaconda

使用说明：
直接运行webSearcher.py ，在main.py内可配置指定需要检测的url
如需要添加新的检测网页，需要添加指定网页想要检测的对象或者按钮，详情请查询Sleenium使用指南
默认内置网页：Yostar Shop / 蜜瓜

=============================================================================================================================
傻瓜式使用
点击已打包好的exe文件，双击启动
如果需要开机启动
1.右键——将需要开启启动的脚本，发送到桌面快捷方式
2.ctr+r——打开“运行”——输入“shell:startup”——确定
3.将第一步中生成的快捷方式放入到开机启动项中
4：重启机器，python脚本自动再后台运行

============================================================================================================================
Python打包为可执行文件
采用pyinstaller将python程序和依赖环境一起打包成可执行程序。
http://www.pyinstaller.org

注意事项
pyinstaller针对不同平台（windows、linux...），需要打包成不同平台的可执行文件。

安装
pip install pyinstaller
pyinstaller安装时，会一同安装其他依赖包，建议pip在线安装。安装成功后，在控制台输出一起安装的包。提示如下：

Successfully installed altgraph-0.17 future-0.18.2 pefile-2019.4.18 pyinstaller-3.6 pywin32-ctypes-0.2.0

常用参数
参数	参数说明
-F, --onefile	创建单个可执行文件
-D, --onedir	产生一个目录（包含多个文件）作为可执行程序（默认参数）
-p DIR, --paths DIR	添加搜索路径，让其找到对应的库，可以为多个值。（和使用PYTHONPATH效果相似，建议加上此参数，否则可能依赖包无法打包）
--distpath DIR	生成文件的路径，默认为.\dist
--clean	打包之前，删除之前打包的目录（建议加上，免去手动删除之前编译生成的目录）
3 打包可执行程序
当前操作系统：win10，运行后生成exe程序。同理，linux可执行程序，需要在linux环境下生成。

3.1 打包成单个文件
执行命令：

pyinstaller -F xxx.py --clean
命令目录下将生成如下文件和文件夹：

__pycache__ #缓存目录，存储的pyc格式的编译后的程序，有python和依赖包的环境，可以直接执行
build #打包过程的目录，其中存储了打包过程的相关日志和配置
dist #打包结果目录，对应生成的xxx.exe程序
baiduVoiceToZip.spec #打包配置文件，可手动编写，通过其他方式打包
文件夹dist中存储了打包生成的exe文件，命名和主python脚本的名字一致，如xxx.exe。

如python程序有其他依赖配置文件，需手动将配置文件，拷贝到.exe目录下，直接发布到其他环境执行即可。

参数--clean用于删除之前打包生成的相关文件

指定包路径
打包文件时，可手动指定python的本地安装依赖包的路径：

和使用PYTHONPATH效果相似，建议加上此参数，否则可能依赖包无法打包

pyinstaller -F -p "D:\Program Files\Python\Python36\Lib\site-packages;" xxx.py
打包生成结果，仍然为单个.exe文件


