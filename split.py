
import io
import base64, cv2
import numpy as np
from fukuwarai import readImageFW
from roulette  import readImageRL
from PIL import Image

def run_fukuwarai(image):
    return readImageFW( data_uri_to_cv2_img( image ) )

def run_roulette(image):
    return readImageRL( data_uri_to_cv2_img( image ) )


def data_uri_to_cv2_img(uri):
    nparr = np.fromstring(base64.b64decode(uri), np.uint8)
    return cv2.imdecode(nparr, 1)


def ocv2b64(buf):
    buf = str(base64.b64encode( buf )).replace("b'",'')
    return buf.replace("'",'')