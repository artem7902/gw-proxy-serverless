import argparse

parser = argparse.ArgumentParser(description='Create a new pdf file containing the zip file and the pdf file.')
parser.add_argument('zipfile', help='The zip file to hide.')
parser.add_argument('pdffile', help='The pdf file to use.')
args = parser.parse_args()

zip_file = open(args.zipfile, 'rb')
zip_data = zip_file.read()
zip_file.close()

pdf_file = open(args.pdffile, 'rb')
pdf_data = pdf_file.read()
pdf_file.close()

new_file = open('new-file-from-zip-pdf.pdf', 'wb')
new_file.write(pdf_data)
new_file.write(zip_data)
new_file.close()