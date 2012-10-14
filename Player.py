import pygame
import sys
import math

from Entity import *
import Colors

class Player(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)

		self.mVelocity = [0, 0]

		self.mFootRect = pygame.Rect(0, 0, 15, 10)
		self.mLeftImage, self.mRect = self.mKernel.ImageManager().LoadImage("player_left.bmp")
		self.mRightImage, rrect = self.mKernel.ImageManager().LoadImage("player_right.bmp")

		self.mLeftAlertedImage, rrect = self.mKernel.ImageManager().LoadImage("player_left_alerted.bmp")
		self.mRightAlertedImage, rrect = self.mKernel.ImageManager().LoadImage("player_right_alerted.bmp")

		self.mImage = self.mLeftImage

		self.mCollisionRect = self.mRect.copy()

		self.mAlerted = False

		self.mGravity = 0.5
		self.mGravityThrottle = 10
		self.mFriction = 0

		self.mJumpVelocity = 10

		self.mMoveSpeed = 0.75
		self.mMoveThrottle = 4

		self.mMoves = {
			"left": False,
			"right": False
		}

		self.mLastDirection = ""

		self.mJumping = False
		self.mGrounded = False
		return

	def Reset(self):
		self.SetPosition([self.mLevel.mStartPosition[0], self.mLevel.mStartPosition[1]-self.mCollisionRect.height])
		self.mVelocity = [0, 0]

	def Jump(self):
		# Move off the ground block
		if (self.mGrounded and not self.mJumping):
			self.mFootRect.top -= 2

			self.mVelocity[1] = -1 * self.mJumpVelocity

			self.mJumping = True
			self.mGrounded = False

	def ChooseImage(self):
		if (self.mLastDirection == "left"):
			if (self.mAlerted):
				self.mImage = self.mLeftAlertedImage
			else:
				self.mImage = self.mLeftImage
		else:
			if (self.mAlerted):
				self.mImage = self.mRightAlertedImage
			else:
				self.mImage = self.mRightImage

	def Move(self, direction):
		self.mMoves[direction] = True

		self.mLastDirection = direction

		self.ChooseImage()

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

	def CollideEntities(self):
		for entity in self.mLevel.mEntities:
			if (self.CheckCollision(entity)):
				entity.OnCollision(self)

	def Interact(self):
		other = self.mLevel.EntityInRect(self.CollisionRect())

		if (other and other.mInteractable):
			other.Trigger(self)

	def Update(self, delta):

		startPos = self.mPosition

		if (self.mJumping and self.mGrounded):
			self.mJumping = False

		# Left/Right Movement
		# if (self.mGrounded):
		if (self.mMoves["left"] and self.mVelocity[0] > (-1 * self.mMoveThrottle)):
			self.mVelocity[0] -= self.mMoveSpeed
		
		if (self.mMoves["right"] and self.mVelocity[0] < self.mMoveThrottle):
			self.mVelocity[0] += self.mMoveSpeed

		if (self.mVelocity[0] != 0):
			self.mVelocity[0] = (self.mVelocity[0] / abs(self.mVelocity[0])) * min(abs(self.mVelocity[0]), self.mMoveThrottle)

		if (not self.mMoves["left"] and not self.mMoves["right"]):
			self.mVelocity[0] *= 0.5

			if (abs(self.mVelocity[0] - 0) < 0.01):
				self.mVelocity[0] = 0

		self.mPosition[0] += self.mVelocity[0]

		if (self.mPosition[0] < -20):
			self.mPosition[0] = -20
		elif (self.mPosition[0] > (800 - self.CollisionRect().width + 20)):
			self.mPosition[0] = 800 - self.CollisionRect().width + 20

		# Friction unless jumping

		# Gravity only if Jumping
		if (not self.mGrounded):
			if (self.mVelocity[1] < self.mGravityThrottle):
				self.mVelocity[1] += self.mGravity

			self.mPosition[1] += self.mVelocity[1]
			self.mCollisionRect.top = self.mPosition[1]

		self.mPosition[0] = int(self.mPosition[0])
		self.mPosition[1] = int(self.mPosition[1])

		self.CollideWorld()
		self.CollideEntities()

		if (self.mPosition[1] > 800):
			self.Reset()

		preAlertState = self.mAlerted

		if (self.mLevel.EntityInRect(self.CollisionRect()) and self.mLevel.EntityInRect(self.CollisionRect()).mInteractable):
			self.mAlerted = True
		else:
			self.mAlerted = False

		if (self.mAlerted != preAlertState):
			self.ChooseImage()

		# Keep rectangles in sync
		self.mCollisionRect.topleft = self.mPosition
		self.mFootRect.bottom = self.mCollisionRect.bottom
		self.mFootRect.left = self.mCollisionRect.left + 8.5

		return Entity.Update(self, delta)

	def Draw(self):
		Entity.Draw(self)

		# pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.BLUE, self.mRect, 2)
		# pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.TRANSPARENT, self.mCollisionRect, 2)
		# pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.GREEN, self.mFootRect, 2)
		return