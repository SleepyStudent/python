import numpy as np
import matplotlib.pyplot as plt
import math

class Tree(object):
	def __init__(self, n):
		self.children = []
		self.name = n
		self.distance = 0
		self.parent = None
		self.y = 0
		
	def addChild(self, c):
		self.children.append(c)
		c.parent = self
		c.distance = self.distance + 1
		self.onePlusToAll(c)
		
	def getY(self):
		if self.getNbrChildren() % 2 == 1: #odd
			self.y = self.children[math.floor(self.getNbrChildren() / 2)].y
		else:# self.getNbrChildren() % 2 == 2: #even
			self.y = (self.children[0].y + self.children[-1].y) / 2
		
	def getNbrChildren(self):
		return len(self.children)

	def onePlusToAll(self,c):
		for cc in c.children:
			cc.distance = cc.distance + 1
			c.onePlusToAll(cc)
	
	def getAll(self):
		l = self.getAC([])
		l.append(self)
		#l.sort(key=lambda x: x.name, reverse=True)
		return l

	def getAC(self,l):
		for c in self.children:
			l.append(c)
			c.getAC(l)
		return l
		
	def getEndNodes(self):
		t = self.getAll()
		endNodes = []
		i = 0
		for c in (y for y in t if y.getNbrChildren() == 0):
			endNodes.append(c)
		return endNodes
		
	def getDepth(self):
		dlist = []
		for c in self.getEndNodes():
			tmp	= c
			i = 0
			while tmp != self:
				tmp = tmp.parent
				i=i+1
			dlist.append(i)
			
		if dlist == []:
			return 0
		else:
			return max(dlist)

	def updateY(self):
		i = 0
		for c in self.getEndNodes():
			c.y = i
			i = i + 1
		
		for c in self.getAll():
			if c.getNbrChildren() != 0:
				c.getY()
		
	def plotTree(self):
		self.updateY()
		for c in self.getAll():
			x = c.distance
			y = c.y
			if len(c.children) == 0:
				plt.plot(x, y, "ro")
			else:
				plt.plot(x, y, "bo")
				for cc in c.children:
					plt.plot([x,cc.distance],[y,cc.y],"b")
			plt.annotate(c.name, [x,y],size=10)
		plt.axis('off')
		plt.show()
		
root = Tree("top") #0

ch1 = Tree("1") #1
ch2 = Tree("2") #1
ch3 = Tree("3") #1

ch21 = Tree("21") #2
ch22 = Tree("22") #2

ch11 = Tree("11") #2
ch12 = Tree("12") #2
ch13 = Tree("13") #2
ch131 = Tree("131") #3
ch132 = Tree("132") #3
ch133 = Tree("133") #3
ch1331 = Tree("1331") #4

ch1.addChild(ch11)
ch1.addChild(ch12)
ch1.addChild(ch13)
ch13.addChild(ch131)
ch13.addChild(ch132)
ch13.addChild(ch133)
ch133.addChild(ch1331)


ch2.addChild(ch21)
ch2.addChild(ch22)
root.addChild(ch1)
root.addChild(ch2)
root.addChild(ch3)

root.plotTree()
