from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from .message import message_sign

import random
import time

command = on_command('/抽签', priority=6)
@command.handle()
async def lq_():
    await command.send(
        message="确定要抽取吗"
    )

@command.got("pb")
async def pq_(reply: str = ArgPlainText('pb')):
    if reply == '确定' or 'yes' or '抽取' or '嗯':
        for i in range(3):
            a = random.randint(0,100)
            if a >= 5 :
                pd=True
                await command.send(
                    message="抽到了正签"
                )
                break
            else:#为了模拟真实抛杯才设置空签
                await command.send(
                    message="是空签呢",
                    at_sender=True,
                )
                pd=False
                break

        if pd is True:
            await command.finish(message=f"\n{random.choice(message_sign)}",at_sender=True)
        else:
           await command.finish()
    else:
        await command.finish('\n放弃了抽取',at_sender=True,)


