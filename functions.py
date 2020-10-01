import sys, os;
file_path = "Pillow-master";
sys.path.append( os.path.dirname( file_path ) );

from PIL import Image;
from PIL import ImageShow;

def get_tile ( I, x_start, y_start, x_end, y_end ):
    return I.crop( (x_start, y_start, x_end, y_end) );

#I = original image
#T = tile
#x = Original image x cordinate
#y = Original image y cordinate
def is_matching (I, T, x, y): 
    matching = True;

    tile_width, tile_height = T.size;

    for Y in range (0, tile_height):
        for X in range (0, tile_width):
            I_pixel = I.getpixel ( (x+X,y+Y) );
            T_pixel = T.getpixel( (X,Y) );
            if I_pixel != T_pixel:
                matching = False;
                return matching;

    return matching;


def get_similar_tile_count (I, T):
    image_width, image_height = I.size;
    tile_width, tile_height = T.size;

    count = 0;

    for Y in range (0, image_height-tile_height):
        for X in range (0, image_width-tile_width):
            if is_matching(I, T, X, Y):
                count += 1;

    return count;