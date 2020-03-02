import argparse

parser = argparse.ArgumentParser(description='Create a new pdf file containing the pdf file and the html file.')
parser.add_argument('pdffile', help='The pdf file to use.')
parser.add_argument('htmlfile', help='The html file to hide.')
args = parser.parse_args()

pdf_file = open(args.pdffile, 'rb')
pdf_data = pdf_file.read()
pdf_file.close()

html_file = open(args.htmlfile, 'rb')
html_data = html_file.read()
html_file.close()

new_file = open('new-file-from-pdf-html.pdf', 'wb')
new_file.write(pdf_data)
new_file.write(html_data)
new_file.close()