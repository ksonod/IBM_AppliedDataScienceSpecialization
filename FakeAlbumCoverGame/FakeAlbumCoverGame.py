# Python for Data Science (Coursera, IBM)
# FakeAlbumCoverGame

import requests

for j in range(2):
    wikipedia_link='https://en.wikipedia.org/wiki/Special:Random'

    raw_random_wikipedia_page=requests.get(wikipedia_link)

    wikipage=raw_random_wikipedia_page.text
    with open('/Users/kotarosonoda/Documents/Python_Practice/wikipedia.txt','w') as wiki:
        wiki.write(wikipage)

    # Extracting the title of the Wikipedia page.
    title_int=wikipage.find('<title>')
    title_fin=wikipage.find('</title>')

    if j==0:
        album_title=wikipage[title_int:title_fin]
        album_title=album_title.strip("<title>"" - Wikipedia")
        print('The title of an album is prepared.')
    elif j==1:
        band_name=wikipage[title_int:title_fin]
        band_name=band_name.strip("<title>"" - Wikipedia")
        print('The name of a band is prepared.')
    else:
        print('')

from IPython.display import Image as IPythonImage
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def display_cover(top,bottom ):
    import requests
    
    name='album_art_raw.png'
    # https://picsum.photos/ is a free service that provides images.
    album_art_raw = requests.get('https://picsum.photos/500/500/?random')
    with open(name,'wb') as album_art_raw_file:
       album_art_raw_file.write(album_art_raw.content)
    img = Image.open("album_art_raw.png")
    draw = ImageDraw.Draw(img)

    #Font. You might want to change a path.
    path="/System/Library/Fonts/Times.ttc"
    band_name_font = ImageFont.truetype(path,22)
    album_name_font = ImageFont.truetype(path,18)

    # the x,y coordinates for where our album name and band name text will start
    # counted from the top left of the picture (in pixels)
    band_x, band_y = 50, 50
    album_x, album_y = 50, 400

    outline_color ="black" #black border

    draw.text((band_x-1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x-1, band_y+1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y+1), top, font=band_name_font, fill=outline_color)

    draw.text((album_x-1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x-1, album_y+1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y+1), bottom , font=album_name_font, fill=outline_color)

    draw.text((band_x,band_y),top,(255,255,255),font=band_name_font)
    draw.text((album_x, album_y),bottom,(255,255,255),font=album_name_font)

    return img

img=display_cover(top=album_title,bottom=band_name) 
img.save('sample-out.png') #save the image 
im=Image.open('./sample-out.png')
im.show()
print('A fake album cover is created.')
