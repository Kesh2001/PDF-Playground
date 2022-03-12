import PyPDF2
import sys
# do error handlinng
inputs = sys.argv[1:] # going to grab all into a list

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)
	merger.write('Super.pdf')
		

pdf_combiner(inputs)
