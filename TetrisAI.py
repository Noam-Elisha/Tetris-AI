import random
import pygame
import numpy as np

UP = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
DOWN = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
LEFT = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
RIGHT = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)

outputs = [UP, DOWN, LEFT, RIGHT, None]

class NeuralNetwork:

	def __init__(self, inputs, depth = 165, layers = 2, outputs = 5):
		self.score = 0
		self.inputs = inputs
		self.depth = depth
		self.layers = layers
		self.outputs = outputs
		self.inputs_layer1 = np.random.rand(inputs,depth)
		self.layer1_layer2 = np.random.rand(depth,depth)
		self.layer2_output = np.random.rand(depth,outputs)

	def get_output(self, state):
		state = np.array(state)
		temp = state.dot(self.inputs_layer1)
		temp = temp.dot(self.layer1_layer2)
		temp = temp.dot(self.layer2_output)
		temp_sum = np.sum(temp)
		for i in range(len(temp)):
			temp[i] = temp[i]/temp_sum
		return random.choices(outputs, temp)[0]
	
	def reproduce(self):
		new_agent = NeuralNetwork(self.inputs, self.depth, self.layers, self.outputs)
		new_agent.inputs_layer1 = self.inputs_layer1
		new_agent.layer1_layer2 = self.layer1_layer2
		new_agent.layer2_output = self.layer2_output
		new_agent.inputs_layer1 += np.random.normal(scale = 2.5, size = (self.inputs,self.depth))
		new_agent.layer1_layer2 += np.random.normal(scale = 2.5, size = (self.depth,self.depth))
		new_agent.layer2_output += np.random.normal(scale = 2.5, size = (self.depth,self.outputs))
		return new_agent
