import pygame,sys,random
from pygame.math import Vector2 #para trabajar con vectores bidimensionales-repres pocis y direcc 

class SNAKE:
	def __init__(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] # lista que epresentan las posiciones iniciales  del cuerpo de la serp
		self.direction = Vector2(0,0) #direccion inicial de la serp
		self.new_block = False #determina si la snake debe crecer en el siguiente paso

		#cabeza
		self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
		self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
		self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
		self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
		
		#cola
		self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
		self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
		self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
		self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

		#body
		self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
		self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
		
		#esquinas del cuerpo
		self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
		self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
		self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
		self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
		self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav') #sonido que se reproducira

	def draw_snake(self):
		self.update_head_graphics() #metodos para actualizar las img de la cabeza y cola segun su direccion
		self.update_tail_graphics()

		for index,block in enumerate(self.body): #itera sobre los bloques del cuerpo
			x_pos = int(block.x * cell_size)#calcula las posic
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)#se crea un rectangulo para repres el bloque en la screen

			if index == 0: #si el bloq es la head de la snake se dibuja la imagen en el rect 
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1: #si el bloq es la cola se dibuja ""
				screen.blit(self.tail,block_rect)
			else:#sino se determ la orientacion del cuerpo
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y: #se dibuja cuerpo vertical
					screen.blit(self.body_horizontal,block_rect)#se dibuja el cuerpo horizontal
				else:#se comprueba orientacion de bloques para determ las esquinas
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: #dibuja esquina sup izqui
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:#infe izq
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:#supe derecha
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:#inf derecha
						screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
		head_relation = self.body[1] - self.body[0] #direccion de movimiento de la head
		if head_relation == Vector2(1,0): self.head = self.head_left #head se mueve hacia la derecha 
		elif head_relation == Vector2(-1,0): self.head = self.head_right#head se mueve hacia la izquierda 
		elif head_relation == Vector2(0,1): self.head = self.head_up #head se mueve hacia arriba 
		elif head_relation == Vector2(0,-1): self.head = self.head_down #head se mueve hacia abajo

	def update_tail_graphics(self):
		tail_relation = self.body[-2] - self.body[-1] #direccion de movim de la cola
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def move_snake(self): #mueve a la snake y agg new block de ser nercesario
		if self.new_block == True: #verif si agregar un new bloque a la snake
			body_copy = self.body[:] #se realiza copia de la lista que representa el cuerpo 
			body_copy.insert(0,body_copy[0] + self.direction) #inserta new bloque en posc 0, simula el crec
			self.body = body_copy[:]#la lista orig que repres la snake se actualiza cn la copia 
			self.new_block = False #se reinicia para indicar que se agg new bloque
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True #indica que debe agg un new block 

	def play_crunch_sound(self):
		self.crunch_sound.play()

	def reset(self): #reestablece el estado inicial de la snake
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)


class FRUIT:
	def __init__(self):
		self.randomize() #metodo para inic la posc de la fruta de manera alatoria

	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)#recta creado con coordenadas y tamaño de la fruit
		screen.blit(apple,fruit_rect)#dibuja la imagen de la manzana
		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

	def randomize(self): #asigna posic alatorias a la fruit 
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)

class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()

	def update(self): #actualiza el estado del juego
		self.snake.move_snake()
		self.check_collision()
		self.check_fail() #verif si la snake ha fallado

	def draw_elements(self): #dibuja los elementos del juego en screen 
		self.draw_grass()#fondo
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.draw_score()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]: #verif si la head ha colisionado con la fruit
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()

		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def check_fail(self): 
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:#verif si la head de la snake esta fuera de los limites permitidos
			self.game_over()

		for block in self.snake.body[1:]:#para ver si ha chocado consigo misma
			if block == self.snake.body[0]: #verif si el bloq actual es igual a la head de la snake
				self.game_over()
		
	def game_over(self):
		self.snake.reset() #reinicia a un estado inicial el juego

	def draw_grass(self):
		grass_color = (167,209,61) #color de la pantalla
		for row in range(cell_number):#itera a traves de las filas
			if row % 2 == 0: 
				for col in range(cell_number):#itera a traves de las columnas
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)
			else:
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)			

	def draw_score(self): #dibuja el rect de puntuacion
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
		bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

		pygame.draw.rect(screen,(167,209,61),bg_rect)
		screen.blit(score_surface,score_rect)#dibuja texto de la puntuacion
		screen.blit(apple,apple_rect)#dibuja a la manzana
		pygame.draw.rect(screen,(56,74,12),bg_rect,2)#dibuja borde oscurso alrededor del fondo verde

pygame.mixer.pre_init(44100,-16,2,512)#inicial mod de sonido de pygame
pygame.init()
cell_size = 30#tamañ de cada celda 
cell_number = 20#numero de celdas en cada fila y col
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))#crea la ventana de juego
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)#controla la velcidad del juego 

main_game = MAIN()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1:
					main_game.snake.direction = Vector2(0,-1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)

	screen.fill((175,215,70))
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(60)