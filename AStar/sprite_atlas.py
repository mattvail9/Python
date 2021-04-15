import pygame
import config

class SpriteAtlas(object):
    
    def __init__(self, file, size, height, width):
        
        self.__subsurfaces = []
        image = pygame.image.load(file).convert()

        for x in range(width):
            for y in range(height):
                surf = image.subsurface((x * size, y * size, size, size)).convert()
                surf.set_colorkey(config.TRANSCOLOR)
                self.__subsurfaces.append(surf)
                
                
    def get_image(self, index):
        return self.__subsurfaces[index]
        
        '''self.tile_size = tile_size
        self.base_image = pygame.image.load(file_name)
        self.atlas = []
        
        for x in range(int(self.base_image.get_width() / tile_size)):
            for y in range(int(self.base_image.get_height() / tile_size)):
                self.atlas.append((x * tile_size, y * tile_size))
#x * width + y
#
#for x in w:
#   for y in h:
#       Do Stuff
#    VVV
#output = [y for x in w for y in h]
        #self.atlas = [y for x in range(w) for y in range(h)]
        #for x in self.atlas: rint(x)
        self.base_image.convert()
        
    def get_image(self, index):
        image = pygame.Surface([self.tile_size, self.tile_size]).convert()
        image.blit(self.base_image, (0, 0), (self.atlas[index][0], self.atlas[index][1], self.tile_size, self.tile_size))
        #sets the transparent background color on the atlas
        #image.set_colorkey((255, 255, 255))
        return image'''
