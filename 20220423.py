# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:49:27 2022

@author: N
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x+1,y,z,21)
mc.setBlock(x-1,y,z,12)
mc.setBlock(x,y,z+1,13)
mc.setBlock(x,y,z-1,14)
mc.setBlock(x+1,y,z+1,15)
mc.setBlock(x-1,y,z+1,16)
mc.setBlock(x+1,y,z-1,17)
mc.setBlock(x-1,y,z-1,20)
"""
mc.setBlocks(x,y,z,x+10,y+10,z+10,73)
mc.setBlocks(x+1,y+1,z+1,x+9,y+9,z+9,0)"
"""