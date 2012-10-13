import pygame
import sys
import math
import os

import Colors

class Level:
	def __init__(self, kernel):
		self.mKernel = kernel

		self.mLevelName = ""

		self.mBackgroundImage = None
		self.mBackgroundRect = None
		self.mCollisionRects = []
		self.mEntities = []

		self.mLevelSurface = pygame.Surface((800, 600)).convert()
		self.mLevelRect = pygame.Rect(0, 0, 800, 600)

		self.mStartPosition = [0, 400]

		return

	# Loads a level
	def Load(self, name):
		self.mLevelName = name

		# Load the background image
		self.mBackgroundImage, self.mBackgroundRect = self.mKernel.ImageManager().LoadImage(name + ".bmp")

		# Load the collision data, which consists of a list of rects (left, top, width, height)
		collisionName = name + ".col"

		fullCollisionName = os.path.join("data", "levels", collisionName)

		if os.path.isfile(fullCollisionName):
			with open(fullCollisionName) as collisionFile:
				rectList = collisionFile.read().splitlines() 

				for rect in rectList:
					parts = rect.split()

					self.mCollisionRects.append(pygame.Rect(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]))) 

		# Load the entities data, which consists of a list of entity names followed by rect coords
		entitiesName = name + ".lvl"

		fullentitiesName = os.path.join("data", "levels", entitiesName)

		if os.path.isfile(fullentitiesName):
			with open(fullentitiesName) as entitiesFile:
				entitiesList = entitiesFile.read().splitlines() 

				for entity in entitiesList:
					parts = entity.split()

					if (parts[0] == 'Start'):
						self.mStartPosition =  [int(parts[1]), int(parts[2])]
						continue 

					entity = {
						"name": parts[0],
						"position": (int(parts[1]), int(parts[2]))
					}

					mod = __import__(entity["name"])
					EntityClass_ = getattr(mod, entity["name"])

					rawEntity = EntityClass_(self.mKernel, self)

					rawEntity.SetPosition(entity["position"])

					self.mEntities.append(rawEntity)
		print self.mStartPosition

		return

	def Save(self, rects):
		# Load the collision data, which consists of a list of rects (left, top, width, height)
		collisionName = self.mLevelName + ".col"

		fullCollisionName = os.path.join("data", "levels", collisionName)

		with open(fullCollisionName, 'w') as file:
			for rect in rects:
				file.write(str(rect.left) + " " + str(rect.top) + " " + str(rect.width) + " " + str(4) + "\n")

		self.Load(self.mLevelName)

	def Unload(self):
		self.mEntities = []
		self.mCollisionRects = []
		self.mBackgroundRect = None
		self.mBackgroundImage = None

	def DisplaySurface(self):
		return self.mLevelSurface

	def EntityInRect(self, rect):
		for entity in self.mEntities:
			if entity.Rect().colliderect(rect):
				return entity
		return

	def EntityAt(self, position):
		for entity in self.mEntities:
			if entity.Rect().collidepoint(position):
				return entity
		return

	def Update(self, delta):
		for entity in self.mEntities:
			entity.Update(delta)

	def Draw(self):
		self.mLevelSurface.blit(self.mBackgroundImage, self.mBackgroundRect)

		# for rect in self.mCollisionRects:
		# 	pygame.draw.rect(self.mLevelSurface, Colors.RED, rect, 2)

		for entity in self.mEntities:
			entity.Draw()

	def Blit(self):
		self.mKernel.DisplaySurface().blit(self.mLevelSurface, self.mLevelRect)
