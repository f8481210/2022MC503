# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:57:27 2022

@author: N
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("I'm watching you")

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("you are located on X:"+str(x)
                  +",Y:"+str(y)+" Z:"+str(z))