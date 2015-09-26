from pygame import *
import sys
import os

from Minigame import *
try:
    init()
    display.init()
    mixer.init()
    #correct_sound = mixer.Sound('assets//sound//correct_key.wav')
    bag_sound = mixer.Sound('assets//sound//bag_open.wav')
    eat_sound = mixer.Sound('assets//sound//ian_eating_even_faster.wav')
    mmm_sound = mixer.Sound('assets//sound//mmm_2.wav')
    hey_sound = mixer.Sound('assets//sound//hey.wav')
    what_sound = mixer.Sound('assets//sound//what.wav')
    sorry_sound = mixer.Sound('assets//sound//sorry.wav')
    
    res = (640, 480)
    screen_size = (display.Info().current_w, display.Info().current_h)
    #res = (800, 600)
    #res = (1280,800)
    screen = display.set_mode(res)
    title = image.load('assets//art//title_updated.png').convert()
    background = image.load('assets//art//background4.png').convert()
    hand_in = image.load('assets//art//hand_in.png').convert_alpha()
    hand_out = image.load('assets//art//hand_out.png').convert_alpha()
    bag_front = image.load('assets//art//bag_front.png').convert_alpha()
    bag_back = image.load('assets//art//bag_back.png').convert_alpha()
    mouse_pic = image.load('assets//art//mouse.png').convert_alpha()
    
    gummy_pic = []
    gummy_pic.append(image.load('assets//art//kid_blue.png').convert_alpha())
    gummy_pic.append(image.load('assets//art//kid_green.png').convert_alpha())
    gummy_pic.append(image.load('assets//art//kid_orange.png').convert_alpha())
    gummy_pic.append(image.load('assets//art//kid_red.png').convert_alpha())
    gummy_pic.append(image.load('assets//art//kid_yellow.png').convert_alpha())
    
    gummmy_loc = []
    init_size = background.get_size()
    title = transform.scale(title, res)
    background = transform.scale(background, res)
    new_size = background.get_size()
    ratio = tuple([float(i[1])/i[0] for i in zip(init_size, new_size)])
    display.update()
    done = False
    mini = Minigame((350,550,2000,1500), ratio)
    hand_height = hand_in.get_size()[1]
    hand_in = transform.scale(hand_in, tuple([int(i[0] * i[1]) for i in zip(hand_in.get_size(), ratio)]))
    hand_out = transform.scale(hand_out, tuple([int(i[0] * i[1]) for i in zip(hand_out.get_size(), ratio)]))
    bag_front = transform.scale(bag_front, tuple([int(i[0] * i[1]) for i in zip(bag_front.get_size(), ratio)]))
    bag_back = transform.scale(bag_back, tuple([int(i[0] * i[1]) for i in zip(bag_back.get_size(), ratio)]))
    mouse_pic = transform.scale(mouse_pic, tuple([int(i[0] * i[1]) for i in zip(mouse_pic.get_size(), ratio)]))
    for g in range(len(gummy_pic)):
        gummy_pic[g] = transform.scale(gummy_pic[g], tuple([int(i[0] * i[1]) for i in zip(gummy_pic[g].get_size(), ratio)]))
    font = font.Font(None, int(100 * ratio[1]))
    
    hand_pos = 0
    got_swag = False
    caught = False
    just_caught = False
    mouse_pos = (1850, 2100)
    mouse_bound = (1850, 2050, 2400, 3000)
    score_init = 100
    score = [score_init, 0]
    last_score = score_init
    tick = 0
    
    while event.peek(KEYDOWN) == False:
        screen.blit(title, (0, 0))
        display.flip()
    while not done:
        tick += 1
        if random.random() > .9999: 
            mmm_sound.play() 
        screen.blit(background, (0, 0))
        screen.blit(bag_back, (2725 * ratio[0], 890 * ratio[1]))
        if got_swag:
            for gummy in gummmy_loc:
                screen.blit(gummy_pic[gummy[0]], (gummy[1] * ratio[0], gummy[2] * ratio[0]))
                gummy[2] += 1
                if gummy[2] > 2500:
                    gummmy_loc.remove(gummy)        
        if not got_swag: screen.blit(hand_in, (2800 * ratio[0], hand_pos * ratio[1] - hand_in.get_size()[1]))
        else: 
            screen.blit(hand_out, (2800 * ratio[0], hand_pos * ratio[1] - hand_in.get_size()[1]))
            if random.random() > .999:
                gummmy_loc.append([random.randrange(len(gummy_pic)), random.randrange(100, 900) + 2800, hand_pos-500])
        pressed = key.get_pressed()
        done = pressed[K_ESCAPE]
        if pressed[K_ESCAPE]: done = True
        elif pressed[K_RETURN]: mini.next(K_RETURN)
        
        if pressed[K_DOWN] and not caught and hand_pos < hand_height and hand_pos < 2500: hand_pos += 1
        elif pressed[K_UP] and hand_pos > 0: hand_pos -= 1
        
        if caught and hand_pos > 0:
            if just_caught: 
                sorry_sound.play()
                just_caught = False
            got_swag = False
            hand_pos -= 2
        elif hand_pos > 2000 and not got_swag: 
            bag_sound.play()
            got_swag = True
        elif hand_pos <= 0 and got_swag: 
            eat_sound.play()
            got_swag = False
            score[0] -= 10
            score[1] += 10
        elif hand_pos <= 0: 
            caught = False
        if pressed[K_SPACE]:
            if random.random() > .5: 
                if got_swag and not caught and tick % 100 == 0:
                    hey_sound.play()
                    caught = True
                    just_caught = True
                elif not caught and tick % 100 == 0:
                    what_sound.play()
                    score[0] -= 10
                    score[1] += 10                
        elif pressed[K_a]: mini.next(K_a)
        elif pressed[K_b]: mini.next(K_b)
        elif pressed[K_c]: mini.next(K_c)
        elif pressed[K_d]: mini.next(K_d)
        elif pressed[K_e]: mini.next(K_e)
        elif pressed[K_f]: mini.next(K_f)
        elif pressed[K_g]: mini.next(K_g)
        elif pressed[K_h]: mini.next(K_h)
        elif pressed[K_i]: mini.next(K_i)
        elif pressed[K_j]: mini.next(K_j)
        elif pressed[K_k]: mini.next(K_k)
        elif pressed[K_l]: mini.next(K_l)
        elif pressed[K_m]: mini.next(K_m)
        elif pressed[K_n]: mini.next(K_n)
        elif pressed[K_o]: mini.next(K_o)
        elif pressed[K_p]: mini.next(K_p)
        elif pressed[K_q]: mini.next(K_q)
        elif pressed[K_r]: mini.next(K_r)
        elif pressed[K_s]: mini.next(K_s)
        elif pressed[K_t]: mini.next(K_t)
        elif pressed[K_u]: mini.next(K_u)
        elif pressed[K_v]: mini.next(K_v)
        elif pressed[K_w]: mini.next(K_w)
        elif pressed[K_x]: mini.next(K_x)
        elif pressed[K_y]: mini.next(K_y)
        elif pressed[K_z]: mini.next(K_z)
        
        mini.play(screen)
        
        screen.blit(bag_front, (2600 * ratio[0], 870 * ratio[1]))
        
        
        mouse_pos = [i[0] + i[1] for i in zip(mouse_pos, mouse.get_rel())]
        if mouse_pos[0] < mouse_bound[0]: mouse_pos[0] = mouse_bound[0]
        elif mouse_pos[1] < mouse_bound[1]: mouse_pos[1] = mouse_bound[1]
        elif mouse_pos[0] > mouse_bound[2]: mouse_pos[0] = mouse_bound[2]
        elif mouse_pos[1] > mouse_bound[3]: mouse_pos[1] = mouse_bound[3]
        
        screen.blit(mouse_pic, (mouse_pos[0] * ratio[0], mouse_pos[1] * ratio[1]))
        draw.line(screen, (0,0,0), ((mouse_pos[0] + 157) * ratio[0], (mouse_pos[1] + 50) * ratio[1]), (2337 * ratio[0],1777 * ratio[1]), 3)
        
        cur_score = mini.get_score()      
        #cur_score = cur_score[0] - cur_score[1] + score_init
        cur_score = cur_score[2]
        score[0] += cur_score - last_score
        
        label1 = font.render("%d" % score[0], 1, (0,0,0))
        label2 = font.render("%d" % score[1], 1, (0,0,0))
        screen.blit(label1,(1680 * ratio[0], 1700 * ratio[1]))
        screen.blit(label2,(1960 * ratio[0], 1680 * ratio[1]))
        
        last_score = cur_score
        display.flip()
        
        eve = event.poll()
        if eve.type == QUIT:
            break
finally:
    quit()
    
