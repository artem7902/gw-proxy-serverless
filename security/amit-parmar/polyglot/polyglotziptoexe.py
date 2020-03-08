import argparse

parser = argparse.ArgumentParser(description='Create a new zip file containing the zip file and the exe file.')
parser.add_argument('zipfile', help='The zip file to use.')
parser.add_argument('exefile', help='The exe file to hide.')
args = parser.parse_args()

zip_file = open(args.zipfile, 'rb')
zip_data = zip_file.read()
zip_file.close()

exe_file = open(args.exefile, 'rb')
exe_data = exe_file.read()
exe_file.close()

new_file = open('new-file-from-zip-exe.zip', 'wb')
new_file.write(zip_data)
new_file.write(exe_data)
new_file.close()