# -*- coding:utf-8 -*-
import werobot

#robot = werobot.WeRoBot(token='robot', enable_session=True, session_storage=saekvstorage.SaeKVDBStorage())
#robot = werobot.WeRoBot(token='testrobot', enable_session=True, session_storage=filestorage.FileStorage())
robot = werobot.WeRoBot(token='testrobot', enable_session=True)

@robot.subscribe
def subscribe(message):
    return '欢迎关注本公众号！使用方法是：直接向公众号发送语音消息，如果第一个消息是汉语语音，则自动翻译成英语语音；如果第一个消息是外语语音（不限语言种类）则自动翻译成中文文本，随后再发送汉语语音均将自动翻译为该语种的语音消息。借此，您可以使用本公众号跟外国人对话，录一句翻一句；也可以学习外语，先发一个该语种语音消息，随后发送汉语的语音消息就够了。'

@robot.handler
def echo(message):
    return '我是WeRoBot机器人'

robot.run(server='cherrypy',host='0.0.0.0',port=80)