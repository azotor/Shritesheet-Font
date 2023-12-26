import pygame, sys

from App.Font import Font

pygame.init()

class App:
    def __init__( self ):
        self.run = True
        self.clock = pygame.time.Clock()
        self.surf = pygame.display.set_mode( ( 800, 600 ) )
        pygame.display.set_caption( "Spritesheet font" )
        self.fontmain = Font(
            font = 'fontmain',
            width = 10,
            height = 10,
            scale = 3,
            alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        )
        self.fontlight = Font(
            font = 'fontlight',
            scale = 3
        )
        self.loop()

    def loop( self ):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.update()
            self.render()

        pygame.quit()
        sys.exit()
        

    def update( self ):
        pass

    def render( self ):
        self.surf.fill( "#222222" )
        self.fontmain.render(
            message = "TEST",
            pos = ( 100, 100 ),
            align = ( 0, 0 ),
            width = 200
        )
        self.fontmain.render(
            message = "ALA MA KOTA",
            pos = ( 300, 300 ),
            align = ( 1, 1 ),
            width = 100
        )
        self.fontmain.render(
            message = "AZOREK 2",
            pos = ( 400, 500 )
        )
        self.fontmain.renderByGridsX(
            message = "AZOREK POTWOREK",
            pos = ( 100, 500 ),
            align = ( 0, 0 ),
            gridsX = 3
        )
        self.fontmain.render(
            message = "KOTEK 123",
            pos = ( 700, 200 ),
            align = ( 1, 0 )
        )
        self.fontlight.render(
            message = "ALPHABET 123",
            pos = ( 350, 300 )
        )
        self.fontlight.render(
            message = "FONTLIGHT 3",
            pos = ( 350, 340 )
        )
        pygame.display.update()