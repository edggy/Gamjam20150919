from pygame import *
import random

class Minigame(object):
    def __init__(self, bounds, ratio):
        self.state = 'init'
        self.font = font.Font(None, int(150 * ratio[1]))
        self.bounds = [int(float(i[1]) * i[0]) for i in zip(bounds, ratio + ratio)]
        self.tick = 0;
        self.key = ''
        self.loc = (0, 0)
        self.correct_sound = mixer.Sound('assets//sound//correct_key.wav')
        self.wrong_sound = mixer.Sound('assets//sound//wrong_key.wav')
        
        mixer.music.load('assets//sound//background_music_2.wav')
        mixer.music.set_volume(.50)
        self.score = [0,0,0]
        self.timeout_init = 5000
        self.timeout = self.timeout_init
        
        self.in_row = 0
    def play(self, screen):
        if self.state == 'init':
            label = self.font.render("Press Enter To Start!", 1, (255,255,0))
            size = label.get_size()[0]
            blink_speed = 500
            if(self.tick % blink_speed <= blink_speed / 2):
                screen.blit(label,((self.bounds[0] + self.bounds[2])/2 - size/2,(self.bounds[1] + self.bounds[3])/2))
                
        elif self.state == 'load':
            self.key = chr(ord('a') + random.randrange(26))
            self.loc = (random.randrange(self.bounds[0], self.bounds[2]), random.randrange(self.bounds[1] + int(self.font.size('X')[1]), self.bounds[3]))
            self.state = 'play'
            self.tick = 0
            self.state = 'wait'
        elif self.state == 'wait':
            if self.tick > 100: 
                self.state = 'play'
                self.tick = 0
        elif self.state == 'play':
            label = self.font.render(chr(ord(self.key) - ord('a') + ord('A')), 1, (255,255,0))
            screen.blit(label,self.loc)
        elif self.state == 'good':
            label = self.font.render("Combo!! x%d" % (self.in_row / 5 + 1), 1, (255,255,0))
            size = label.get_size()[0]
            screen.blit(label,((self.bounds[0] + self.bounds[2])/2 - size/2,(self.bounds[1] + self.bounds[3])/2))   
            self.tick = 0
            self.state = 'good2'
        elif self.state == 'good2':
            label = self.font.render("Combo!! x%d" % (self.in_row / 5 + 1), 1, (255,255,0))
            size = label.get_size()[0]
            screen.blit(label,((self.bounds[0] + self.bounds[2])/2 - size/2,(self.bounds[1] + self.bounds[3])/2))            
            if self.tick > 500: 
                self.state = 'load'
        if self.state == 'play' or self.state == 'wait' or self.state == 'load' or self.state == 'good' or self.state == 'good2':
            label = self.font.render("Right: %d Wrong: %d Score: %d" % tuple(self.score), 1, (255,255,0))
            screen.blit(label, (self.bounds[0], self.bounds[1]))
            if(self.tick > self.timeout): self.next(0)
            
        self.tick += 1
    def next(self, key):
        if self.state == 'init' and key == K_RETURN:
            mixer.music.play(100)
            self.state = 'load'
        elif self.state == 'play':
            if chr(key) == self.key:
                self.correct_sound.play()
                self.score[0] += 1
                self.score[2] += 1 * (self.in_row / 5 + 1)
                self.in_row += 1
                self.timeout *= 99/100.0
            else:
                self.wrong_sound.play()
                self.score[1] += 1
                self.score[2] -= 5
                self.in_row = 0
                self.timeout = self.timeout_init
            self.state = 'load'
            if self.in_row > 0 and self.in_row % 5 == 0:
                self.state = 'good'
    def get_score(self):
        return self.score
            
            