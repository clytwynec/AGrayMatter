import pygame
import sys
import math

from Entity import *
import Colors

class Player(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)

		self.mVelocity = [0, 0]

		self.mCollisionRect = pygame.Rect(0, 0, 50, 125)
		self.mFootRect = pygame.Rect(0, 124, 25, 10)
		self.mRect = pygame.Rect(0, 0, 50, 125)

		self.mGravity = 0.5
		self.mGravityThrottle = 10
		self.mFriction = 0

		self.mJumpVelocity = 10

		self.mMoveSpeed = 4
		self.mMoveThrottle = 4

		self.mMoves = {
			"left": False,
			"right": False
		}

		self.mJumping = False
		self.mGrounded = False
		return

	def Jump(self):
		# Move off the ground block
		if (self.mGrounded and not self.mJumping):
			self.mFootRect.top -= 2

			self.mVelocity[1] = -1 * self.mJumpVelocity

			self.mJumping = True
			self.mGrounded = False

	def Move(self, direction):
		self.mMoves[direction] = True

	def Stop(self, direction):
		self.mMoves[direction] = False

	def CollideWorld(self):
		# World Collision!
		self.mGrounded = False

		for rect in self.mLevel.mCollisionRects:
			if (self.mFootRect.colliderect(rect) and self.mVelocity[1] >= 0):
				self.mPosition[1] = rect.top - (self.CollisionRect().height - 1)

				self.mVelocity[1] = 0
				self.mGrounded = True

	def Update(self, delta):

		startPos = self.mPosition

		if (self.mJumping and self.mGrounded):
			self.mJumping = False

		# Left/Right Movement
		if (self.mGrounded):
			if (self.mMoves["left"] and self.mVelocity[0] > (-1 * self.mMoveThrottle)):
				self.mVelocity[0] -= self.mMoveSpeed
			
			if (self.mMoves["right"] and self.mVelocity[0] < self.mMoveThrottle):
				self.mVelocity[0] += self.mMoveSpeed

			if (not self.mMoves["left"] and not self.mMoves["right"]):
				self.mVelocity[0] = 0

		self.mPosition[0] += self.mVelocity[0]

		if (self.mPosition[0] < -20):
			self.mPosition[0] = -20
		elif (self.mPosition[0] > (800 - self.CollisionRect().width + 20)):
			self.mPosition[0] = 800 - self.CollisionRect().width + 20

		# Friction unless jumping

		# Gravity unless Jumping
		if (not self.mGrounded):
			if (self.mVelocity[1] < self.mGravityThrottle):
				self.mVelocity[1] += self.mGravity

			self.mPosition[1] += self.mVelocity[1]
			self.mCollisionRect.top = self.mPosition[1]

		self.mPosition[0] = int(self.mPosition[0])
		self.mPosition[1] = int(self.mPosition[1])

		self.CollideWorld()

		self.mCollisionRect.topleft = self.mPosition
		self.mFootRect.bottom = self.mCollisionRect.bottom
		self.mFootRect.left = self.mCollisionRect.left + 12.5

		return Entity.Update(self, delta)

	def Draw(self):
		Entity.Draw(self)

		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.BLUE, self.mRect, 2)
		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.TRANSPARENT, self.mCollisionRect, 2)
		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.GREEN, self.mFootRect, 2)
		return