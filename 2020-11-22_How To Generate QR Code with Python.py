# install  first via command prompt: pillow qr code
import qrcode
from PIL import Image,ImageDraw
webname = "www.duckduckgo.com"
image = qrcode.make(webname)
image.save("QRCode_CuteDuckDuckGo.png")
