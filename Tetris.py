from setup import *
import pickle
import os
import matplotlib.pyplot as plt

def rotate_block(block):
    state = block.orientation
    block.rotate_right()
    collisions_list = []

    if state == 0:
        for x in [(0,0),(-1,0),(-1,1),(0,-2),(-1,-2)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    if state == 1:
        for x in [(0,0),(1,0),(1,-1),(0,2),(1,2)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    if state == 2:
        for x in [(0,0),(1,0),(1,1),(0,-2),(1,-2)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    if state == 3:
        for x in [(0,0),(-1,0),(-1,-1),(0,2),(-1,2)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    block.rotate_left()

def rotate_line(block):
    state = block.orientation
    block.rotate_right()
    collisions_list = []

    if state == 0:
        for x in [(0,0),(-2,0),(1,0),(-2,-1),(1,2)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    if state == 1:
        for x in [(0,0),(-1,0),(2,0),(-1,2),(2,-1)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    if state == 2:
        for x in [(0,0),(2,0),(-1,0),(2,1),(-1,-2)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    if state == 3:
        for x in [(0,0),(1,0),(-2,0),(1,-2),(-2,1)]:
            block.translate(x[0],x[1])
            if not block.collision():
                return
            block.translate(-1*x[0],-1*x[1])
    block.rotate_left()


quit = False

def play(agent = None, generation = None, num_in_gen = None, net = None, makeDataset = False, frameSpeed = None):
    if net != None and agent != None:
        print("Can't have both agent and net")
        return
    all_sprites_list, stack, border, test_line, temp_group = start_game()
    if agent != None or net != None:
        speed = 2
        clock_speed = 600
    else:
        speed = 15
        clock_speed = 60
    if frameSpeed != None:
        speed = frameSpeed
    tetrominos = [I,J,L,O,S,Z,T]
    score = 0
    done = False
    spawn_new_block = True
    frame = 0
    block = None
    init = True
    grace = 5
    graces = [5,5,5]
    extraspins = 0
    next_block = 0
    score = 0
    up = True
    y_placeholder = 24*TILE
    allow_spin = True
    max_height = y_placeholder
    open_space = 0
    lean = 0
    x_mid = 370 + 5*TILE
    global quit
    dataset = []
    # -------- Main Program Loop -----------
    while not done:
        game_state = [[0 for j in range(10)] for i in range(24)]
        for event in pygame.event.get():
            multiplier = 0
            pause = True
            if event.type == pygame.QUIT: 
                quit = True
                done = True
                continue
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                temp_done = False
                while not temp_done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                            quit = True
                            temp_done = True
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            temp_done = True
            elif block == None:
                continue
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and allow_spin:
                if type(block) == I:
                    rotate_line(block)
                else:
                    rotate_block(block)
                extraspins -= 1
                if extraspins == 0:
                    allow_spin = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                multiplier = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                multiplier = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                block.translate(0, -1)
                if block.collision():
                    block.translate(0,1)
            if makeDataset:
                temp = flatten(game_state)
                if event.type == pygame.KEYDOWN:
                    dataset.append([temp, event.key])
                else:
                    dataset.append([temp, None])
            if multiplier == 0:
                continue
            block.translate(multiplier, 0)
            if block.collision():
                block.translate(-1*multiplier, 0)

        #Move the tetromino down, spawn new one if needed
        if frame == 0:
            temp_done = True
            while not temp_done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        temp_done = True
                        quit = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        temp_done = True

            if spawn_new_block:
                if next_block == 0:
                    random.shuffle(tetrominos)
                block = tetrominos[next_block]()
                next_block = (next_block + 1)%7
                spawn_new_block = False
                if block.collision():
                    done = True
                deepest_row = block.centery
                allow_spin = True
                score += 1
            else:
                block.translate(0, -1)
                if block.collision():
                    block.translate(0, 1)
                    if grace == 0:
                        spawn_new_block = True
                        block.add_to_stack()
                        grace = 5
                        allow_spin = False
                    grace -= 1
                if block.centery > deepest_row:
                    deepest_row = block.centery
                    grace = 5
                    extraspins = 5


        #Line Clearing
        if done or (spawn_new_block and not init and frame == speed - 1):
            i = y_placeholder
            for x in test_line:
                x.rect.y = y_placeholder
            while i != 0:
                line_collision = group_collide(stack, test_line, False, False)
                for x in line_collision:
                    lean += x_mid - x.rect.x
                if len(line_collision) > 0:
                    max_height = i
                if len(line_collision) == 10:
                    score += 100
                    line_collision = group_collide(stack, test_line, False, False)
                    for x in line_collision:
                        temp_group.add(x)
                        stack.remove(x)
                        all_sprites_list.remove(x)
                    group_collide(test_line, temp_group, False, True)
                    for x in stack:
                        if x.rect.y < i:
                            x.rect.y += TILE
                else:
                    #if done:
                        #score += (len(line_collision)**8)/(10**8)
                    for x in test_line:
                        x.rect.y -= TILE
                    i -= TILE
            for x in test_line:
                x.rect.y = max_height
            open_space = 10 - len(group_collide(stack, test_line, False, False))


        
        for x in stack:
            game_state[(x.rect.y - y0)//TILE][(x.rect.x - x0)//TILE] = 1
        block_state = []
        for x in block.blocks:
            block_state += [x.rect.x, x.rect.y]

        screen.fill((255, 255, 255))
        all_sprites_list.draw(screen)
        for i in range(24):
            text = font.render(str(game_state[i]), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (800, 50+ i * 22)
            screen.blit(text,textRect)
        text = font.render("Computer Vision", True, (0, 0, 0))
        text_Rect = text.get_rect()
        textRect.center = (840, 28)
        screen.blit(text, textRect)

        text = font.render("Score: {}".format(score), True, (0, 0, 0))
        text_Rect = text.get_rect()
        textRect.center = (240, 28)
        screen.blit(text, textRect)

        if agent != None:
            text = font.render("Generation: {}".format(generation), True, (0, 0, 0))
            text_Rect = text.get_rect()
            textRect.center = (240, 50)
            screen.blit(text, textRect)

            text = font.render("Agent number: {}".format(num_in_gen), True, (0, 0, 0))
            text_Rect = text.get_rect()
            textRect.center = (240, 78)
            screen.blit(text, textRect)

        pygame.display.flip()
        clock.tick(clock_speed)
        frame = (frame + 1) % speed
        init = False

        if agent != None and frame == 1:
            action = agent.get_output(flatten(game_state))
            if action != None:
                pygame.event.post(action)
        if net != None and frame == 1:
            actions = net.activate(flatten(game_state) + [max_height, len(stack), open_space, lean, block.idnum] + block_state)
            action = outputs[actions.index(max(actions))]

            if action != None:
                pygame.event.post(action)
    if makeDataset:
        pickle.dump(dataset, open(f"Data/data_{len(os.listdir('Data'))}.dat", "wb"))
    print(f"Your Score: {score}")
    return score



def train():
    models = os.listdir('models')
    if len(models) == 0:
        model_num = 0
        agents = [NeuralNetwork(240) for i in range(50)]
    else:
        models.sort(reverse = True, key = lambda x: int(x[:-5]))
        model_num = int(models[0][:-5])
        agents_file = open('models/{}'.format(models[0]), 'rb')
        agents = pickle.loads(agents_file.read())
        agents_file.close()
    while not quit:
        for i in range(len(agents)):
            agents[i].score = play(agents[i], model_num, i + 1)
            print(agents[i].score)
            if quit:
                break
        if quit:
            break
        agents.sort(reverse = True, key = lambda x: x.score)
        for i in range(10,50, 4):
            agents[i:i+4] = [agents[(i-10)//4].reproduce() for x in range(4)]
        with open('models/{}.ttrs'.format(model_num + 1), 'wb') as agents_file:
            agents_file.write(pickle.dumps(agents))
            model_num += 1

def demonstrate():
    models = os.listdir('models')
    if len(models) == 0:
        print("There are no models to demonstrate. You must train the network first")
    else:
        models.sort(reverse = True)
        model_num = int(models[0][:-5])
        agents_file = open('models/{}'.format(models[0]), 'rb')
        agents = pickle.loads(agents_file.read())
        agents_file.close()
        play(agents[0])

def eval_genomes(genomes, config):
    global quit
    for genome_id, genome in genomes:
        genome.fitness = 4
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = play(net = net)
        if quit:
            break


def run():
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                'config.txt')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes,1000)

play(makeDataset = True, frameSpeed = 5)
pygame.quit()