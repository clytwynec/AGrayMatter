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

					entity = {
						"name": parts[0],
						"position": (int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]))
					}

					mod = __import__(entity["name"])
					EntityClass_ = getattr(mod, entity["name"])

					rawEntity = EntityClass_(self.mKernel, self)

					rawEntity.SetPosition(entity["position"])

					self.mEntities.append(rawEntity)

		return

	def EntityAt(self, position):
		for entity in self.mEntities:
			if entity.Rect().collidepoint(position):
				return entity
		return

	def Draw(self):
		self.mKernel.DisplaySurface().blit(self.mBackgroundImage, self.mBackgroundRect)

		for rect in self.mCollisionRects:
			pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.RED, rect, 2)

		for entity in self.mEntities:
			entity.Draw()
