# QRMaker
A Python program to make your own QR codes! It has support for both normal QR codes and QR codes with an Image in the center!

# Usage
Usage: `python qrmaker.py <MODE> <FILENAME> <"QR DATA"> <"IMAGE URL/DIR" (Mode 2 only!)> <URL/DIR (Mode 2 only!)>`
<br>
`<MODE>` : There are 2 modes; Mode 1 and Mode 2. Select Mode 1 if you want a regular QR code, select Mode 2 if you want a QR code with an Image in the center.
<br>
`<FILENAME>` : The filename for the result. Example: `MyFirstQRCode`
<br>
`<"QR DATA">` : The text to be putten into the QR code. Example: `"Hello World!"`
<br>
`<"IMAGE URL/DIR">` : (Mode 2 only!!) The URL or DIR that you want to put into the center. URL example: `"https://www.website.com/image.png"`, DIR example: `"C:\image.png"`
<br>
`<IRL/DIR>` : (Mode 2 only!!) Specify wether the image to put in the center is an URL or a DIR.
<br>

# Example for Mode 1:
`python qrmaker.py 1 MyFileName "My QR Code's Data!"`


# Examples for Mode 2:
For URL: `python qrmaker.py 2 MyFileName "My QR Code's Data!" "https://www.website.com/image.png" URL`
<br>
Or if you want DIR: `python qrmaker.py 2 MyFileName "My QR Code's Data!" "C:\image.py" DIR`
