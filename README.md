# WeChatForRevocation<br><br>
基于<a href="https://github.com/littlecodersh/ItChat.git">itchat</a>  
贡献者：<a href='https://github.com/XAS-712'>XAS-712</a>、 <a href='https://github.com/SLiNv'>SLiNv</a>、 <a href="https://github.com/linwencai">linwencai</a>  
欢迎好的idea和pull request  

-----
### 环境相关
Python版本：python3.5  

### Linux环境配置  
`pip install -r requirements.txt`  

### Windows用户  

可以直接下载已打包的程序，可以直接下载已打包的程序，[点击这里](https://github.com/ZKeeer/WeChatForRevocation/releases)。  
下载最新版替换原先的程序时，只需要替换exe文件，其他的不需要移动或者修改。  

--------
#######**NEW**##################################################################

#

#&nbsp;&nbsp;如果想要传送中文文件名的文件，把fields.py复制到requests包，&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#<br>
#&nbsp;&nbsp;requests/packages/urllib3/ 路径下，替换原来的fields.py文件。&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#<br>
#&nbsp;&nbsp;<a href="https://github.com/ZKeeer/WeChatAssistant/tree/master/fields/fields-py2">fields.py(py2)</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="https://github.com/ZKeeer/WeChatAssistant/tree/master/fields/fields-py3">fileds.py(py3)</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#<br>
#&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#<br>
#############################################################################


------
### 注意
**默认**使用系统的图片查看程序打开二维码。如果没有默认的图片打开程序，请指定画图为默认打开程序。否则无法登陆。  
在Linux下如果在纯命令行模式下，则输出到命令行

截图功能依赖:   
    python: pyscreenshot(only linux), PIL（python2.x）/Pillow（python3.x）  
    linux: scrot
    
默认：自动回复处于打开状态

------

**<a href='http://zkeeer.space/?page_id=2'>TODO LIST</a>**<br>
<ul type="circle">
    <li><del>撤回消息备份</del></li>
    <li><del>关键词监听</del></li>
    <li><del>自动签到</del></li>
    <li><del>截图</del></li>
    <li><del>今天吃什么</del></li>
    <li>消息全备份</li>
    <li>消息搜索，基于好友、内容</li>
    <li>在备份基础上提供信息分析，以及做成数据可视化，群组聊天记录分析。好友的分析，包括地域、年龄 …</li>
    <li>定时发送消息</li>
    <li><del>自定义规则消息回复</del></li>
</ul>

------
####支持以下指令（在文件助手发送任意词，即可获得命令）：


**查看/删除文件[文件名]** e.g. 查看文件[123345234.mp3]<br>
**撤回附件列表** (查看都有哪些保存在电脑中的已撤回附件)<br>
**清空附件列表** (清空已经保存在电脑中的附件)<br>
**添加关键词[关键词]**  e.g. 设置关键词[在不在]<br>
**删除关键词[关键词]**  e.g. 删除关键词[在不在]<br>
**清空关键词**  清空已经设置的所有关键词<br>
**查看关键词**  查看目前设置的关键词<br>
**添加签到口令[公众号:签到口令]**   e.g. 添加签到口令[招商银行信用卡:签到]<br>
**删除签到口令[公众号]**   e.g. 删除签到口令[招商银行信用卡]<br>
**查看签到口令**  查看已经存在的公众和和对应的签到口令<br>
**清空签到口令**  清空所有签到口令<br>
**截图** 截取当前屏幕发送到文件助手<br>
**添加自动回复[针对的关键词:回复内容]** e.g.添加自动回复[在不在:我现在有事情，待会儿回复你]<br>
**删除自动回复[针对的关键词]** e.g.删除自动回复#在不在#<br>
**清空自动回复** 清空所有的自定义回复规则<br>
**关闭自动回复** <br>
**打开自动回复** <br>
**今天吃什么** 纯粹是闹着玩的功能 <br>
**退出程序** <br>
