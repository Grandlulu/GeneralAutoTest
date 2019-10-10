**前言：**

本框架为综合性测试框架，初步设想整合接口测试，性能测试，ui自动化测试
>1 接口测试利用request第三方库，性能测试利用locust框架，也基于request库，这
样同一套请求，既可以满足于接口测试也可满足于性能测试。

>2 UI自动化分web和移动端，思路全部基于PageObjects进行页面分层测试，便于优化
维护用例
>>1. Android端使用开源项目openatx的uiautomator2作为底层调用，区别与appium和macaca
的本地服务启动，通过手机端的agent代理，实现快速的脚本响应，而不需要繁琐的服务启动
>>2. IOS端也将使用openatx的facebook-wda作为底层调用，同样通过在ISO真机上安装
WebDriverAgent代理，来运行脚本
>>3. web端则使用selenium作为底层操作web页面元素

>3 除性能测试外，接口和UI自动化测试全部可基于pytest单元测试框架进行设计，pytest
框架支持pytest的所有插件，包括失败重试，重复执行，用例排序，测试报告allure，用例
并发等

**安装**

**结构介绍**

**完成进度**
