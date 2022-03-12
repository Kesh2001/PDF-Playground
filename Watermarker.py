import PyPDF2
# edit to get dynamic input
template = PyPDF2.PdfFileReader(open('Super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)
	with open('Watermarked_output.pdf','wb') as file:
		output.write(file)
