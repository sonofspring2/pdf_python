import os,shutil
from config import default
from PyPDF2 import PdfFileWriter, PdfFileReader


def pdfSplit(input_pdf, output_folder):
    assert os.path.exists(input_pdf), " pdf file {} does not exist!".format(input_pdf)
    infile = PdfFileReader(open(input_pdf, 'rb'))

    if default.overwrite:
        shutil.rmtree(output_folder)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)


    num_pages = infile.getNumPages()
    for i in range(num_pages):
        page = infile.getPage(i)
        outfile = PdfFileWriter()
        outfile.addPage(page)
        output_pdf = 'page-%05d' % i + '.pdf'
        if default.verbose:
            print 'output file: ', output_pdf

        with open(os.path.join(output_folder, output_pdf), 'wb') as f:
            outfile.write(f)
    return


def main():
    pdfSplit(default.input_file,default.output_folder)
    return


if __name__ == "__main__":
    main()
