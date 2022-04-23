# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:13:32 2022

@author: N
"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.player.setTilePos(100,100,100)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
#print(x,y,z)

time.sleep(1)
mc.player.setTilePos(x,y+100,z) #int 3
time.sleep(1)
mc.player.setTilePos(x,y+200,z)
time.sleep(1)
mc.player.setTilePos(x,y+300,z)
#mc.player.setPos(100.5,100.5,100.5) #float 0.3
"""
while True:
    mc.postToChat("HELLO!")
"""
    

