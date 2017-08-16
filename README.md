# WeChatForRevocation<br><br>
基于<a href="https://github.com/littlecodersh/ItChat.git">itchat</a><br><br>
贡献者：<a href='https://github.com/XAS-712'>XAS-712</a>、 <a href='https://github.com/SLiNv'>SLiNv</a><br><br>
<hr />
环境：windows10 64位；Python版本：python3.5<br>
<strong>默认</strong>使用系统的图片查看程序打开二维码。如果没有默认的图片打开程序，请指定画图为默认打开程序。否则无法登陆。<br>
在Linux下如果在纯命令行模式下，则输出到命令行<br><br>
截图功能依赖: <br>
     python: pyscreenshot(only linux), PIL（python2.x）/Pillow（python3.x）<br>
     linux: scrot<br>
<hr />
### Linux环境配置

```pip install -r requirements.txt```
### Windows用户
可以直接下载已打包的程序，<a href='https://github.com/ZKeeer/WeChatForRevocation/releases'>点击这里</a>。<br><br>
<hr />
<strong><a href='http://zkeeer.space/?page_id=2'>TODO LIST</a></strong><br>
<ul class="contains-task-list">
    <li class="task-list-item">
        <input class="task-list-item" checked="" disabled="" type="checkbox">撤回消息备份
    </li>
    <li class="task-list-item">
        <input class="task-list-item" checked="checked" disabled="disabled" type="checkbox">关键词监听
    </li>
    <li class="task-list-item">
        <input class="task-list-item" checked="checked" disabled="disabled" type="checkbox">自动签到
    </li>
    <li class="task-list-item">
        <input class="task-list-item" checked="checked" disabled="disabled" type="checkbox">截图
    </li>
    <li class="task-list-item">
        <input class="task-list-item" disabled="disabled" type="checkbox">消息全备份
    </li>
    <li class="task-list-item">
        <input class="task-list-item" disabled="disabled" type="checkbox">在备份基础上提供消息查询和分析，以及做成数据可视化，群组聊天记录分析。好友的分析，包括地域、年龄 …
    </li>
    <li class="task-list-item">
        <input class="task-list-item" disabled="disabled" type="checkbox">定时发送消息；
    </li>
    <li class="task-list-item">
        <input class="task-list-item" disabled="disabled" type="checkbox">自定义规则消息回复；
    </li>
</ul>
<hr />
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

