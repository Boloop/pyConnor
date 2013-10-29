import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        
        
        self.ball = pygame.Surface((10,10))
        self.ball.fill((0,255,0))
        self.ballpos = (0,0)
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        """
        This will run all the logic of the players/menus in the game
        """
        self.ballpos = pygame.mouse.get_pos()
    def on_render(self):
        """
        Render a new scene. and swap the buffer.
        """
        self._display_surf.fill((255,0,0))
        self._display_surf.blit( self.ball, self.ballpos)
        pygame.display.flip()
        #pygame.time.Clock.tick(50)
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()