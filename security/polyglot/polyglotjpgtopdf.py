import argparse

parser = argparse.ArgumentParser(description='Create a new image containing the image and the zip file.')
parser.add_argument('zipfile', help='The zip file to hide.')
parser.add_argument('jpgfile', help='The jpeg file to use.')
args = parser.parse_args()

jpg_file = open(args.jpgfile, 'rb')
jpg_data = jpg_file.read()
jpg_file.close()

zip_file = open(args.zipfile, 'rb')
zip_data = zip_file.read()
zip_file.close()

new_file = open('polyglot/new-image.jpg', 'wb')
new_file.write(jpg_data)
new_file.write(zip_data)
new_file.close()