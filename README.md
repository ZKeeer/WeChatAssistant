# WeChatForRevocation<br><br>
基于<a href="https://github.com/littlecodersh/ItChat.git">itchat</a><br><br>
贡献者：<a href='https://github.com/XAS-712'>XAS-712</a> <br><br>
环境：windows10 64位；Python版本：python3.5<br>
<strong>默认</strong>使用系统的图片查看程序打开二维码，如果没有图片打开程序，则输出到命令行<br><br>
PC端微信防撤回代码，多关键词监听<br>
2017/05/02 => 调整程序结构，添加关键词监听，支持多关键词<br>
微信公众号签到功能：添加/删除/查看/清空公众号签到口令<br>
2017-07-26 => 添加截图功能,仅针对有图形界面的机器,已在linux, windows测试<br>
截图功能依赖: <br>
     python: pyscreenshot(only linux), PIL（python2.x）/Pillow（python3.x）<br>
     linux: scrot<br>


<h4>支持以下指令（在文件助手发送任意词，即可获得命令）：</h4>
<strong>查看/删除文件[文件名]</strong> e.g. 查看文件[123345234.mp3]<br>
<strong>撤回附件列表</strong> (查看都有哪些保存在电脑中的已撤回附件)<br>
<strong>清空附件列表</strong> (清空已经保存在电脑中的附件)<br>
<strong>添加关键词[关键词]</strong>  e.g. 设置关键词[在不在]<br>
<strong>删除关键词[关键词]</strong>  e.g. 删除关键词[在不在]<br>
<strong>清空关键词</strong>  清空已经设置的所有关键词<br>
<strong>查看关键词</strong>  查看目前设置的关键词<br>
<strong>添加签到口令#公众号:签到口令#</strong>   e.g. 添加签到口令#招商银行信用卡:签到#<br>
<strong>删除签到口令#公众号#</strong>   e.g. 删除签到口令#招商银行信用卡#<br>
<strong>查看签到口令</strong>  查看已经存在的公众和和对应的签到口令<br>
<strong>清空签到口令</strong>  清空所有签到口令<br>
<strong>截图</strong> 截取当前屏幕发送到文件助手<br>
