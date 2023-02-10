from TetrisAI import *
collision = pygame.sprite.spritecollide
group_collide = pygame.sprite.groupcollide
TILE = 26
x0 = 370
y0 = 26

class GridBlock(pygame.sprite.Sprite):

	def __init__(self, color, x = None, y = None):

		super().__init__()
		self.image = pygame.Surface([25, 25])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		if x != None and y != None:
			self.rect.x = x
			self.rect.y = y

class Tetromino:

	def __init__(self):
		self.orientation = 2
		self.centerx = x0 + 5*TILE
		self.centery = y0
		self.blocks = self.orientation2()
		self.num_rotations = 4

	def add_to_stack(self):
		for block in self.blocks:
			stack.add(block)

	def collision(self):
		collisions_list = []
		for x in self.blocks:
			collisions_list.extend(collision(x, stack, False))
			collisions_list.extend(collision(x, border, False))
		return len(collisions_list) != 0

	def translate(self, x, y):
		self.centerx += x*TILE
		self.centery -= y*TILE
		for block in self.blocks:
			block.rect.x += x*TILE
			block.rect.y -= y*TILE

	def rotate_left(self):
		self.orientation = (self.orientation - 1)%self.num_rotations
		for block in self.blocks:
			all_sprites_list.remove(block)
		if self.orientation == 0:
			self.blocks = self.orientation0()
		elif self.orientation == 1:
			self.blocks = self.orientation1()
		elif self.orientation == 2:
			self.blocks = self.orientation2()
		elif self.orientation == 3:
			self.blocks = self.orientation3()

	def rotate_right(self):
		self.orientation = (self.orientation + 1)%self.num_rotations
		for block in self.blocks:
			all_sprites_list.remove(block)
		if self.orientation == 0:
			self.blocks = self.orientation0()
		elif self.orientation == 1:
			self.blocks = self.orientation1()
		elif self.orientation == 2:
			self.blocks = self.orientation2()
		elif self.orientation == 3:
			self.blocks = self.orientation3()

class I(Tetromino):

	idnum = 0

	def __init__(self):
		super().__init__()

	def orientation0(self):
		block1 = GridBlock((0,255,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,255), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((0,255,255), x = self.centerx + 2*TILE, y = self.centery)	
		block4 = GridBlock((0,255,255), x = self.centerx - TILE, y = self.centery)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation1(self):
		block1 = GridBlock((0,255,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,255), x = self.centerx, y = self.centery - TILE)
		block3 = GridBlock((0,255,255), x = self.centerx, y = self.centery + TILE)	
		block4 = GridBlock((0,255,255), x = self.centerx, y = self.centery + 2*TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation2(self):
		block1 = GridBlock((0,255,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,255), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((0,255,255), x = self.centerx - 2*TILE, y = self.centery)	
		block4 = GridBlock((0,255,255), x = self.centerx - TILE, y = self.centery)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation3(self):
		block1 = GridBlock((0,255,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,255), x = self.centerx, y = self.centery - TILE)
		block3 = GridBlock((0,255,255), x = self.centerx, y = self.centery + TILE)	
		block4 = GridBlock((0,255,255), x = self.centerx, y = self.centery - 2*TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

class O(Tetromino):

	idnum = 1

	def __init__(self):
		super().__init__()

	def orientation2(self):
		block1 = GridBlock((255,255,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,255,0), x = self.centerx + TILE, y = self.centery + TILE)
		block3 = GridBlock((255,255,0), x = self.centerx + TILE, y = self.centery)	
		block4 = GridBlock((255,255,0), x = self.centerx, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def rotate_right(self):
		return

	def rotate_left(self):
		return

class Z(Tetromino):

	idnum = 2

	def __init__(self):
		super().__init__()

	def orientation0(self):
		block1 = GridBlock((255,0,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,0,0), x = self.centerx - TILE, y = self.centery - TILE)
		block3 = GridBlock((255,0,0), x = self.centerx + TILE, y = self.centery)	
		block4 = GridBlock((255,0,0), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation1(self):
		block1 = GridBlock((255,0,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,0,0), x = self.centerx + TILE, y = self.centery - TILE)
		block3 = GridBlock((255,0,0), x = self.centerx, y = self.centery + TILE)
		block4 = GridBlock((255,0,0), x = self.centerx + TILE, y = self.centery)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation2(self):
		block1 = GridBlock((255,0,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,0,0), x = self.centerx - TILE, y = self.centery)
		block3 = GridBlock((255,0,0), x = self.centerx, y = self.centery + TILE)
		block4 = GridBlock((255,0,0), x = self.centerx + TILE, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation3(self):
		block1 = GridBlock((255,0,0), x = self.centerx - TILE, y = self.centery + TILE)
		block2 = GridBlock((255,0,0), x = self.centerx - TILE, y = self.centery)
		block3 = GridBlock((255,0,0), x = self.centerx, y = self.centery)
		block4 = GridBlock((255,0,0), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

class S(Tetromino):

	idnum = 3

	def __init__(self):
		super().__init__()

	def orientation0(self):
		block1 = GridBlock((0,255,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,0), x = self.centerx + TILE, y = self.centery - TILE)
		block3 = GridBlock((0,255,0), x = self.centerx - TILE, y = self.centery)	
		block4 = GridBlock((0,255,0), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation1(self):
		block1 = GridBlock((0,255,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,0), x = self.centerx + TILE, y = self.centery + TILE)
		block3 = GridBlock((0,255,0), x = self.centerx, y = self.centery - TILE)
		block4 = GridBlock((0,255,0), x = self.centerx + TILE, y = self.centery)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation2(self):
		block1 = GridBlock((0,255,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,255,0), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((0,255,0), x = self.centerx, y = self.centery + TILE)
		block4 = GridBlock((0,255,0), x = self.centerx - TILE, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation3(self):
		block1 = GridBlock((0,255,0), x = self.centerx - TILE, y = self.centery - TILE)
		block2 = GridBlock((0,255,0), x = self.centerx - TILE, y = self.centery)
		block3 = GridBlock((0,255,0), x = self.centerx, y = self.centery)
		block4 = GridBlock((0,255,0), x = self.centerx, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)


class L(Tetromino):

	idnum = 4

	def __init__(self):
		super().__init__()

	def orientation0(self):
		block1 = GridBlock((255,165,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,165,0), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((255,165,0), x = self.centerx - TILE, y = self.centery)	
		block4 = GridBlock((255,165,0), x = self.centerx + TILE, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation1(self):
		block1 = GridBlock((255,165,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,165,0), x = self.centerx + TILE, y = self.centery + TILE)
		block3 = GridBlock((255,165,0), x = self.centerx, y = self.centery + TILE)
		block4 = GridBlock((255,165,0), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation2(self):
		block1 = GridBlock((255,165,0), x = self.centerx, y = self.centery)
		block2 = GridBlock((255,165,0), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((255,165,0), x = self.centerx - TILE, y = self.centery)
		block4 = GridBlock((255,165,0), x = self.centerx - TILE, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation3(self):
		block1 = GridBlock((255,165,0), x = self.centerx - TILE, y = self.centery - TILE)
		block2 = GridBlock((255,165,0), x = self.centerx, y = self.centery + TILE)
		block3 = GridBlock((255,165,0), x = self.centerx, y = self.centery)
		block4 = GridBlock((255,165,0), x = self.centerx, y = self.centery- TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

class J(Tetromino):

	idnum = 5

	def __init__(self):
		super().__init__()

	def orientation0(self):
		block1 = GridBlock((0,0,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,0,255), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((0,0,255), x = self.centerx - TILE, y = self.centery)	
		block4 = GridBlock((0,0,255), x = self.centerx - TILE, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation1(self):
		block1 = GridBlock((0,0,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,0,255), x = self.centerx + TILE, y = self.centery - TILE)
		block3 = GridBlock((0,0,255), x = self.centerx, y = self.centery + TILE)
		block4 = GridBlock((0,0,255), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation2(self):
		block1 = GridBlock((0,0,255), x = self.centerx, y = self.centery)
		block2 = GridBlock((0,0,255), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((0,0,255), x = self.centerx - TILE, y = self.centery)
		block4 = GridBlock((0,0,255), x = self.centerx + TILE, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation3(self):
		block1 = GridBlock((0,0,255), x = self.centerx - TILE, y = self.centery + TILE)
		block2 = GridBlock((0,0,255), x = self.centerx, y = self.centery + TILE)
		block3 = GridBlock((0,0,255), x = self.centerx, y = self.centery)
		block4 = GridBlock((0,0,255), x = self.centerx, y = self.centery- TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

class T(Tetromino):

	idnum = 6

	def __init__(self):
		super().__init__()

	def orientation0(self):
		block1 = GridBlock((153,50,204), x = self.centerx, y = self.centery)
		block2 = GridBlock((153,50,204), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((153,50,204), x = self.centerx - TILE, y = self.centery)	
		block4 = GridBlock((153,50,204), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation1(self):
		block1 = GridBlock((153,50,204), x = self.centerx, y = self.centery)
		block2 = GridBlock((153,50,204), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((153,50,204), x = self.centerx, y = self.centery + TILE)
		block4 = GridBlock((153,50,204), x = self.centerx, y = self.centery - TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation2(self):
		block1 = GridBlock((153,50,204), x = self.centerx, y = self.centery)
		block2 = GridBlock((153,50,204), x = self.centerx + TILE, y = self.centery)
		block3 = GridBlock((153,50,204), x = self.centerx - TILE, y = self.centery)
		block4 = GridBlock((153,50,204), x = self.centerx, y = self.centery + TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

	def orientation3(self):
		block1 = GridBlock((153,50,204), x = self.centerx - TILE, y = self.centery)
		block2 = GridBlock((153,50,204), x = self.centerx, y = self.centery + TILE)
		block3 = GridBlock((153,50,204), x = self.centerx, y = self.centery)
		block4 = GridBlock((153,50,204), x = self.centerx, y = self.centery- TILE)
		all_sprites_list.add(block1, block2, block3, block4)
		return (block1, block2, block3, block4)

pygame.init()

pygame.display.set_caption("Tetris!")
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)

def start_game():
	global all_sprites_list, stack, border, test_line, temp_group
	all_sprites_list = pygame.sprite.Group()
	stack = pygame.sprite.Group()
	border = pygame.sprite.Group()
	test_line = pygame.sprite.Group()
	temp_group = pygame.sprite.Group()

	x_placeholder = 370

	for i in range(10):
		y_placeholder = 26
		for j in range(24):
			block = GridBlock((0,0,0))
			block.rect.x = x_placeholder
			block.rect.y = y_placeholder

			y_placeholder += 26
			all_sprites_list.add(block)
		x_placeholder += 26

	for i in range(10):
		block = GridBlock((255/2, 255/2, 255/2), x = 370 + i * TILE, y = y_placeholder)
		block2 = GridBlock((255/2, 255/2, 255/2), x = 370 + i * TILE, y = 0)
		block3 = GridBlock((255/2, 255/2, 255/2), x = 370 + i * TILE, y = y_placeholder + TILE)
		test_block = GridBlock((255, 0, 0), x= 370 + i * TILE, y= y_placeholder - TILE) 
		border.add(block)
		border.add(block2)
		border.add(block3)
		all_sprites_list.add(block)
		all_sprites_list.add(block2)
		test_line.add(test_block)

	for i in range(26):
		block = GridBlock((255/2, 255/2, 255/2), x = 370 - TILE, y = 0 + i * TILE)
		block2 = GridBlock((255/2, 255/2, 255/2), x = 370 + 10 * TILE, y = 0 + i * TILE)
		border.add(block)
		border.add(block2)
		all_sprites_list.add(block)
		all_sprites_list.add(block2)

	return all_sprites_list, stack, border, test_line, temp_group


flatten = lambda l: [item for sublist in l for item in sublist]