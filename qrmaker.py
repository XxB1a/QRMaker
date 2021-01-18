import qrcode
import sys
import requests
from PIL import Image
from io import BytesIO

modes = [1, 'help', 'Help', 'HELP', 2]
helps = ['H', 'h', 'help', 'Help', 'HELP']
urls = ['U', 'u', 'url', 'Url', 'URL']
dirs = ['D', 'd', 'dir', 'Dir', 'DIR']

def helpmsg():
    return 'Usage: python qrmaker.py <MODE> <FILENAME> <"QR DATA"> <"IMAGE URL/DIR" (Mode 2 only!)> <URL/DIR (Mode 2 only!)> \nModes: [1] Text2QR | [2] Text2QR with an image in the center'

try:
    mode = int(sys.argv[1])

except IndexError:
    mode = 1
    print('Mode was not selected, going with mode 1!')

except ValueError:
    mode = 'help'

if mode in helps:
    print(helpmsg())
    sys.exit()

else:
    try:
        filename = f'{sys.argv[2]}.png'

    except IndexError:
        filename = 'MyQR.png'
        print('Filename was not specified. Going with "MyQR"')

    try:
        text = sys.argv[3]

    except IndexError:
        text = 'Hello World!'
        print('Text was not specified, going with "Hello World!"')

if mode in modes:
    if mode == 1:
        img = qrcode.make(text)
        img.save(filename)

    elif mode == 2:
        try:
            imgloc = sys.argv[4]

        except IndexError:
            print('No image was provided, going with the default one!')
            imgloc = 'https://svgtopng.com/files/6lldgu0p4szac8y5/o_1er05v6kt1ksorj9mhu1vfpe51b/thumb.png'
            url_or_dir = 'url'

        try:
            url_or_dir = sys.argv[5]

        except IndexError:
            print('You didn\'t specify wether the Image in the center is on your PC or an URL, going with URL by default!')
            url_or_dir = 'url'

        if url_or_dir in urls:
            response = requests.get(imgloc)
            data = BytesIO(response.content)

        elif url_or_dir in dirs:
            data = imgloc

        else:
            print(f'Option {url_or_dir} is not a valid option...')
            sys.exit()

        img = qrcode.make(text)
        logo_display = Image.open(data)
        logo_display.thumbnail((60, 60))

        logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
        img.paste(logo_display, logo_pos)

        img.save(filename)

    else:
        print('Sowwy, but IDK this mode!')

else:
    print('Sowwy, but that mode doesn\'t exist!')
