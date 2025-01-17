from graia.saya import Saya, Channel
from graia.application import GraiaMiraiApplication
from graia.application.message.chain import MessageChain
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.elements.internal import Plain, Image
from graia.application.event.messages import Group, Member, GroupMessage

from SAGIRIBOT.Handler.Handler import AbstractHandler
from SAGIRIBOT.MessageSender.MessageItem import MessageItem
from SAGIRIBOT.MessageSender.MessageSender import GroupMessageSender
from SAGIRIBOT.decorators import frequency_limit_require_weight_free
from SAGIRIBOT.MessageSender.Strategy import GroupStrategy, Normal, QuoteSource

saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def template_handler(app: GraiaMiraiApplication, message: MessageChain, group: Group, member: Member):
    if result := await TemplateHandler.handle(app, message, group, member):
        await GroupMessageSender(result.strategy).send(app, result.message, message, group, member)


class TemplateHandler(AbstractHandler):
    __name__ = "TemplateHandler"
    __description__ = "Handler示例"
    __usage__ = "None"

    @staticmethod
    async def handle(app: GraiaMiraiApplication, message: MessageChain, group: Group, member: Member):
        expression = None
        if expression:
            return MessageItem(MessageChain.create([Plain(text="正常发送示例")]), Normal(GroupStrategy()))
        else:
            return MessageItem(MessageChain.create([Plain(text="回复示例")]), QuoteSource(GroupStrategy()))
