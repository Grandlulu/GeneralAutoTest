***前言：***

这次更新Android端自动化测试框架，也想开源到github，这样有人使用才能慢慢完善。

 

***思路：***

因为手机app里也是一个个页面组成的，本质上和web没什么太大区别，所以可以使用selenium的以PageObject进行封装思路，简化后续用例维护等工作。此框架使用的仍然是基于openatx开源项目，结合allure测试报告，pytest单元测试框架，达到并支持

1.响应速度快（atx基于手机的agent代理接受http请求运行脚本）

2.测试用例可定制化（pytest单元测试框架，通过装饰器支持多种功能，包括错误重试，重复执行，设定用例顺序等一系列功能，可自行查阅pytest插件）

3.支持同网段下通过wifi直接运行测试，不用连上usb数据线

4.支持多手机并发执行测试（满足不同机型的统一脚本兼容性测试）

5.支持Jenkins自动生成测试报告（allure本身支持Jenkins的CI特性）

 

***项目介绍：***


 

 APK_Package

此目录为手机包目录，可放置手机安装包

Base

此目录为核心目录



 

 

　　BaseDevicesInfo

　　此文件主要处理手机的一些信息获取，比如udid，电量，等方法封装

　　BasePage

　　此文件主要为通用的手机操作方法封装，比如滑动，查找元素等常规操作

　　BaseDecorator

　　此文件主要封装装饰器与错误截图，装饰器由用例调用，生成日志，添加错误截图到allure报告中

　　BaseInitPath

　　此文件主要为路径的静态方法

　　BaseLog

　　此文件主要为日志方法封装

　　BaseReadConfig

　　此文件主要为读取config文件方法封装

　　BaseRunCase

　　此文件集成了所有启动所需，多线程启动模式，邮件系统，压缩方法，日志等

　　BaseSentMail BaseZip

　　封装了邮件发送和压缩报告方法

Log Report

log为系统运行生成日志目录

report为测试完成后报告生成目录

PageObject

此目录为页面封装，通常在页面有调整时，只需调整此目录下的方法，不许逐条修改用例

TestSuite

此目录为测试用例集合

Tools

此目录中则是一些小工具，比如weditor支持编写脚本时的元素定位

 

***未来展望***

本框架为综合性测试框架设计思路，初步设想整合接口测试，性能测试，ui自动化测试
1 接口测试利用request第三方库，性能测试利用locust框架，也基于request库，这 样同一套请求，既可以满足于接口测试也可满足于性能测试。
2 UI自动化分web和移动端，思路全部基于PageObjects进行页面分层测试，便于优化 维护用例
Android端使用开源项目openatx的uiautomator2作为底层调用，区别与appium和macaca 的本地服务启动，通过手机端的agent代理，实现快速的脚本响应，而不需要繁琐的服务启动
IOS端也将使用openatx的facebook-wda作为底层调用，同样通过在ISO真机上安装 WebDriverAgent代理，来运行脚本
web端则使用selenium作为底层操作web页面元素
3 除性能测试外，接口和UI自动化测试全部可基于pytest单元测试框架进行设计，pytest 框架支持pytest的所有插件，包括失败重试，重复执行，用例排序，测试报告allure，用例 并发等

 

***未完待续：***
 
to be continue
　　
