import os
import sys
import werobot

# robot = werobot.WeRoBot(token='tokenhere', enable_session=True, session_storage=saekvstorage.SaeKVDBStorage())
robot = werobot.WeRoBot(token='tokenhere', enable_session=True, session_storage=saekvstorage.SaeKVDBStorage())


@robot.handler
def echo(message):
    return 'Hey! welcome to Linux Python with WeRoBot'