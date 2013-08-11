import argparse
import base64

from PIL import Image
import stepic

def encrypt_image(path, password):
    im = Image.open(path)
    passwd = base64.b64encode(password)
    im1 = stepic.encode(im, passwd)
    im1.save(path,'PNG')

def decrypt_image(path):
    im = Image.open(path)
    data = stepic.decode(im)
    passwd = base64.b64decode(data)
    return passwd
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creates an image with the hidden data.')
    parser.add_argument('--image', dest='image', default='', help='Absolute path to the image file.')
    parser.add_argument('--password', dest='password', default='', help='Password to be stored.')
    args = parser.parse_args()
    
    if len(args.image) == 0:
        raise Exception, '--image parameter is required.'
    if len(args.password) == 0:
        raise Exception, '--password parameter is required.'
        
    encrypt_image(args.image, args.password)
