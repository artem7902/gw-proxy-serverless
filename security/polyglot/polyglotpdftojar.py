import argparse

parser = argparse.ArgumentParser(description='Create a new pdf file containing the pdf file and the jar file.')
parser.add_argument('pdffile', help='The pdf file to use.')
parser.add_argument('jarfile', help='The jar file to hide.')
args = parser.parse_args()

pdf_file = open(args.pdffile, 'rb')
pdf_data = pdf_file.read()
pdf_file.close()

jar_file = open(args.jarfile, 'rb')
jar_data = jar_file.read()
jar_file.close()

new_file = open('new-file-from-pdf-jar.pdf', 'wb')
new_file.write(pdf_data)
new_file.write(jar_data)
new_file.close()