from sprite_atlas_functions import SpriteAtlas
import config


map_dirty_flag = True

def set_data(x,y,t):
    if x < 0 or x >= config.MAP_WIDTH or y < 0 or y >= config.MAP_HEIGHT:
        return False
    else:
        global map_dirty_flag
        data[x][y] = t
        map_dirty_flag = True
        
def get_data(x, y):
    if x < 0 or x >= config.MAP_WIDTH or y < 0 or y >= config.MAP_HEIGHT:
        return -1
    return data[x][y]
    
def generate_terrain(data):
    global map_dirty_flag
    map_dirty_flag = True
    for column in data:
        for y in range(config.MAP_HEIGHT):
            if(y == 10): column[y] = config.GRASSL
            elif(y > 10): column[y] = config.DIRT
    
'''def draw_map(surf):
    import main
    global map_dirty_flag
    if  map_dirty_flag == False:
        return   
    rint('drawing map', len(data))
    map_dirty_flag = False
    
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            if data[x][y] == -1:
                continue
            main.DISPLAYSURF.blit(sprite_atlas.get_image(data[x][y]), [x * TILE_SIZE, y * TILE_SIZE])'''
   
def init():
    global data, sprite_atlas, map_dirty_flag
    #rint('Initializing map data', map_dirty_flag)
    data = [[ -1 for x in range(config.MAP_WIDTH)] for y in range(config.MAP_HEIGHT)]

    generate_terrain(data)
    #image file name, size of tile on texture, tile width, tile height
    sprite_atlas = SpriteAtlas('terrain.png', 32, 4, 4) #2nd var is size of tile on texture
