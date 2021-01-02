# QRMaker
A Python program to make your own QR codes! It has support for both normal QR codes and QR codes with an Image in the center!

# Usage
Usage: `python qrmaker.py <MODE> <FILENAME> <"QR DATA"> <"IMAGE URL/DIR" (Mode 2> <URL/DIR (Mode 2)>`
<br>

# Help
`<MODE>` : There are 2 modes; Mode 1 and Mode 2. Select Mode 1 if you want a regular QR code, select Mode 2 if you want a QR code with an Image in the center.
<br><br>
`<FILENAME>` : The filename for the result. Example: `MyFirstQRCode`
<br><br>
`<"QR DATA">` : The text to be putten into the QR code. Example: `"Hello World!"`
<br><br>
`<"IMAGE URL/DIR">` : (Mode 2 only!!) The URL or DIR that you want to put into the center. URL example: `"https://www.website.com/image.png"`, DIR example: `"C:\image.png"`
<br><br>
`<IRL/DIR>` : (Mode 2 only!!) Specify whether the image to put in the center is an URL or a DIR.
<br>

# Example for Mode 1:
`python qrmaker.py 1 MyFileName "My QR Code's Data!"`


# Examples for Mode 2:
For URL: `python qrmaker.py 2 MyFileName "My QR Code's Data!" "https://www.website.com/image.png" URL`
<br>
Or if you want DIR: `python qrmaker.py 2 MyFileName "My QR Code's Data!" "C:\image.py" DIR`
<br>

# Extra:
This is a QR code of this repo:
<br>
![qrcode](https://scontent-amt2-1.cdninstagram.com/v/t51.2885-15/e15/134724685_387172739044838_6969441886377221893_n.jpg?_nc_ht=scontent-amt2-1.cdninstagram.com&_nc_cat=102&_nc_ohc=geh-hpvUw_QAX-Fp-Io&tp=1&oh=608ef0d1216904c5750735638127c8fb&oe=601AE216&ig_cache_key=MjQ3NzQwNDUwMjQzNjUxNDE5Ng%3D%3D.2)
