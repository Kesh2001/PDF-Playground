import PyPDF2

with open('dummy.pdf', 'rb') as file:# coverts it to binary mode to read
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	page = reader.getPage(0)
	writer = PyPDF2.PdfFileWriter()
	page.rotateCounterClockwise(90)
	writer.addPage(page)
	with open('tilt.pdf','wb') as new_file:
		writer.write(new_file)
