import json

with open('./config/configure.json', 'r') as conf:
    stConf = json.load(conf)

geometry = stConf['win.geometry']
caption = stConf['win.caption']
framerate = stConf['win.framerate']
version = stConf['win.version']

playerSpeed = stConf['player.speed']
playerSpeedShift = stConf['player.speed.shift']