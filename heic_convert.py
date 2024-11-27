# CONVERT STUPID HEIC FILES TO SENSIBLE IMAGE FILES
#
# put the files to be converted in "orginial" directory
# converted files will be in the "converted" directory, weird huh?


import os
from PIL import Image
from pillow_heif import register_heif_opener

# here's where the magic happens:
register_heif_opener()

# store the string in a var so it doesn't include all the weird
# extra stuff from doing the dir iteration (e.g. <Directory Object> "IMG_420.HEIC")
temp_name = ''

# iterate through the directory and create directory objects
for filename in os.scandir('original'):
    
    # don't fuck with rando shit
    if filename.is_file():
        
        # this is to shave off everything but the name of the file
        # look above at temp_name comment
        temp_str = str(filename)
        temp_name = temp_str[11:-7] 
        
        # open the image file so python can do its thing
        # HEIF:
        #image = Image.open(f'original/{temp_name}.HEIF')
        # HEIC:
        image = Image.open(f'original/{temp_name}.HEIC')
        # convert the motherfucker
        image.save(f'converted/{temp_name}.png')
        