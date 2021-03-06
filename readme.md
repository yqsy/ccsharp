<!-- TOC -->

- [1. 简要说明](#1-简要说明)
- [2. 本项目是做什么的](#2-本项目是做什么的)

<!-- /TOC -->


<a id="markdown-1-简要说明" name="1-简要说明"></a>
# 1. 简要说明

为了解决传统行业不重视技术的特点,例如:

* *.exe,*.dll,bin 加到了版本管理之内
* 各种vs的中间文件放到了版本管理工具之内 .cache,.user ...
* 明明是依赖于其他工程库,却依赖了生成目录的DLL,当生成目录不存在DLL时,编译失败
* 每次编译都要打开sln,点击编译.无法持续集成
* 不知道编译生成的程序是运行在x86,还是x86_64上的.选择了默认的anycpu,导致在64位机器上无法加载32位的native dll
* 没有包管理,版本管理.底层库的状态是生成一下,用qq/ftp/邮件拷贝来拷贝去.
* 有了版本管理还会加'add by xxxx on',把代码弄得非常难看
* 没有格式整理,代码风格不一致(需要类似go的gofmt或者c++ clang-format或者...)
* 没有单元测试,代码质量无法保证
* 各种警告,视若无物
* 生产环境使用debug模式的编译产物...
* ......

当写一个简单的程序时,这些都不重要.当面临到一个10W+行的代码,不注重这些,项目是无法进行的.会频频出现问题,影响业务的正常进行


<a id="markdown-2-本项目是做什么的" name="2-本项目是做什么的"></a>
# 2. 本项目是做什么的

本项目并不是为了一揽子解决以上所有的问题.只是为了解决首当其冲的,也是最痛苦的问题.

问题是: 拿到一个工程,编译不过...


整理的是`*.csproj`工程文件
```
find -name '*.csproj' -type f  | wc -l
```

解决包括
* 依赖关系,如果能找到依赖项目就依赖该项目,而不是依赖BIN目录的生成文件
* 生成至统一的目录
* 统一x86或者x64,release/debug
