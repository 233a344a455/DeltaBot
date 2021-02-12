
from nonebot import on_command, CommandSession, permission
import random

__plugin_name__ = 'bless(2021春节特供)'
__plugin_usage__ = r"""
给您拜个晚年！祝您晚年幸福！[Doge]
【过度使用可(bi)能(ran)触发风控】

Command(s):
 - /bless
    来句祝福吧~
    
 - /firework
    真·炸群工具【需要管理员权限】
""".strip()

# 素材来源于网络
b = """
电势 磁势 引力势 事事得势
重力 弹力 摩擦力 处处给力
匀速 加速 超音速 致富加速
动能 势能 机械能 万事皆能
质心 重心 几何心 天天顺心
强电 弱电 交流电 秒秒来电
重子 轻子 中微子 龙门贵子
虚像 实像 等大像 人人福像
叉积 点积 内外积 财运累积
积分 差分 偏微分 门门满分
动量 冲量 作用量 前途无量
恒星 行星 脉冲星 满天福星
阴极 阳极 南北极 登峰造极
电场 磁场 规范场 宏大气场
有机 无机 永动机 无限商机
自转 公转 螺旋转 行行玩转
平面 曲面 抛物面 有里有面
散度 旋度 自由度 大方有度
牛顿 莱顿 哈密顿 大吃一顿
三维 四维 十一维 精准思维
气流 湍流 交直流 一代风流
直角 锐角 倒三角 全做主角
固态 液态 双稳态 万方仪态
氢气 氦气 电子气 扬眉吐气
固体 气体 半导体 处处得体
施瓦兹不等式，均值不等式，柯西不等式，权方和不等式，舒尔不等式，琴生不等式，贝努利不等式，契比雪夫不等式，排序不等式，闵可夫斯基不等式，赫尔德不等式帮您精打细算、财源滚滚。
重心，垂心，外心，内心，界心，旁心，伴心，陪心让您心宽体胖、事事顺心。
五点圆、六点圆，七点圆，八点圆，九点圆，阿波罗尼斯圆，外接圆，旁切圆，内切圆，蒙日圆，萨蒙圆，形心圆，凡利圆，莱莫恩圆，图克圆，余弦圆，三乘比圆，重圆，泰勒圆，富尔曼圆，极圆，逆相似圆……让您顺顺利利、圆圆满满。
冒泡排序，选择排序，插入排序，快速排序，堆排序，归并排序，希尔排序，桶排序，基数排序新年帮您排忧解难。
有向图，无向图，有环图，无环图，完全图，稠密图，稀疏图，拓扑图祝您新年宏图大展。
最长路，最短路，单源路径，所有节点对路径祝您新年路路通畅。
线段树，二维线段树，二叉搜索树，平衡树，红黑树，小根二叉树，替罪羊树，仙人掌树，主席树，树链剖分，树上删边，树上DP，动态树，霍夫曼树，决策树，B-树，表达式树，二叉查找树，AVL树，Trie树， B+树，B*树， 珂朵莉树，线段树，树状数组，后缀树，子母树，树套树，zkw线段树，矩阵树祝您枝叶繁茂。
最大流，网络流，标准输入流，标准输出流，文件输入流，文件输出流祝您新年顺顺流流。
线性动规，区间动规，坐标动规，背包动规，树型动归为您的新年规划精彩。
散列表，哈希表，邻接表，双向链表，循环链表帮您在新年表达喜悦。
O(1), O(log n), O(n), O(nlog n), O(n^2), O(n^3), O(2^n), O(n!)祝您新年渐进步步高。
费马，欧几里得，欧拉，哈密尔顿，图灵各路大神新年助您一臂之力，愿您紫气东来，风调雨顺！
调和点列，调和线束，调和四边形，调和数列，调和平均数，调和级数帮您在新的一年里事业鹏程、阖府安康。
椎骨、胸骨、颅骨、骶骨，骨骨生威；
背肌、胸肌、颈肌、躯干肌，块块有力；
消化、呼吸、循环、泌尿、生殖、运动、神经、内分泌，八大系统团结友爱；
静脉、动脉，六脉调和；
体循环、肺循环、血液循环、体液循环，环环通畅；
右心房、右心室、左心房、左心室，心心向荣；
中枢神经系统、周围神经系统、躯体神经、内脏神经，协调运作、神清气爽。
祝福从延髓出发，沿着迷走神经穿过颈静脉孔，出颅绕左锁骨下动脉，越主动脉经左肺根，达第六胸椎左前方那个叫心脏的角落汹涌而出：2021快乐！空气分子振动通过鼓膜，顺着听小骨，通过内耳毛细胞点燃蜗螺旋神经节内的双极细胞，沿着蜗神经经蜗神经腹核和背核经蜗神经腹核和背核经斜方体并交叉上行，经下丘，内侧膝状体，经听辐射，通过内囊到达颞叶颞横回，让我们听到了新年的钟声。夜幕中的光线打到视网膜，经视锥细胞和视杆细胞，双极细胞，来到节细胞，通过视神经，视交叉，视束，外侧膝状体，视辐射止于距状沟周围皮质，绚丽的焰火展现在我们脑内。距状沟周围皮质的神经元将焰火经角回，wernicke区，弓状束，来到broca区，经中央前回，通过皮质脑干束，经内囊膝部下行至脑干，到达面神经核下部和舌下神经核，控制着舌，大声疾呼：2021，新年快乐！
在新的一年Windows开机蓝屏，Linux开机Kernel Panic，macos开机五国，服务器iDRAC/ iLO/IPMI/KVM全部失联，路由器全爆炸，路由表内存全溢出，交换机全环路，防火墙全阻断，无线信道全冲突，压接网线全短路，bgp全漏表，机柜全断电，raid全爆炸，nas数据全丢，光模块全炸，光纤全不通，光猫全烫手，电表全倒转，空开全烧穿。
PHP全Fatal Error，fileinfo全装不上，npm/composer install全报错，Laravel Mix全报未知错误，服务器全部宕机，电脑开机报错，Linux rm -rf /*，数据库Delete，CN2全绕路，线路全阻断，海外网站全被墙，服务器炸库，网关无响应，代理500，网站502，RAID组几个一起炸几个，UPS爆炸，一年到头DDOS CC不断，流量几千个T，并发上亿，ping全超时，备案全重审，资源404，SSL全重定向，CDN全不回源，爬虫永远不来你家，收录零蛋，数据库超时。
全家幸福快乐，身体健康，必须发财初一㊗️您twrp卡刷必报错 初二㊗️您第三方rom必变砖 初三㊗您️download模式必掉 初四㊗️您9008救砖救不过
""".strip().split('\n')

symbol = list('✿❀❁❂❃❇❈❉✾💮🌸🏵★☆⁂⁎⁑🍎🍊🍓💊🎄🌹🎉💝🎀🎈🐚🏆💰⚡🔑🐎🚀👍👌💪👊')


@on_command('bless', aliases=('拜年', '新年快乐'), permission=permission.SUPERUSER)
async def bless(session: CommandSession):
    msg = list(random.choice(b))
    for i in range(int(len(msg)/5)):
        msg.insert(random.randint(0, len(msg)), random.choice(symbol))
    await session.send('DeltaBot 祝您❷⓿②⓵年:\n' + ''.join(msg))

@on_command('firework', permission=permission.SUPERUSER)
async def firework(session: CommandSession):
    await session.send("【DANGER】本功能会炸群！会风控！会封号！\n确认作死请输入'y'")
    if await session.aget('inp') != 'y':
        await session.send("已取消")
        return
    await session.send("DeltaBot 祝您❷⓿②⓵年:")
    for msg in b:
        msg = list(msg)
        for i in range(int(len(msg) / 5)):
            msg.insert(random.randint(0, len(msg)), random.choice(symbol))
        await session.send(''.join(msg))