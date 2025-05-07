"""
Program description:
Tool to generate noise images.
"""
# Import
import tqdm
import numpy as np
from PIL import Image
from tkinter import filedialog
# Functions

def nig (width, height, depth):
    
    array = np.random.randint(0, 256, (height, width, depth), dtype=np.uint8)
    
    if depth == 1: img = Image.fromarray(array[:,:,0],'L')
    elif depth == 3: img = Image.fromarray(array,'RGB')
    else: img = [Image.fromarray(array[:,:,i], mode='L') for i in range(depth)] # A list of monochrom layers
    
    return array, img
    

# Main part
if __name__ == '__main__':
    
    width = int(input("Set width:"))
    height = int(input("Set height:"))
    depth = int(input("Set depth:"))

    num = int(input("Set number images to be generatet:"))
    path = filedialog.askdirectory(title='Create and / or select an folder for saving the generated images.')

    for n in tqdm.tqdm(range(num)):
        array, img = nig(width, height, depth)
        np.save(f'{path}/nig-{n}', array)
        if type(img) == list: img[0].save(f'{path}/nig-{n}.tiff', save_all=True, append_images=img[1:], compression='tiff_lzw')
        else: img.save(f'{path}/nig-{n}.png')
