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


def pdfExtract(input_pdf,output_folder,page_range=(0,1)):
    assert os.path.exists(input_pdf), " pdf file {} does not exist!".format(input_pdf)
    infile = PdfFileReader(open(input_pdf, 'rb'))

    if default.overwrite and os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    num_pages = infile.getNumPages()
    assert page_range[1] < num_pages, 'extract page({}) should be less than the total pages({})!'.format(page_range[1],num_pages)

    outfile = PdfFileWriter()
    for i_page in range(page_range[0],page_range[1]):
        outfile.addPage(infile.getPage(i_page))

    output_pdf = os.path.join(output_folder,'extract_range_{}_{}'.format(page_range[0],page_range[1]) +'.pdf' )
    if default.verbose:
        print 'output file: ', output_pdf

    with open(output_pdf,'wb') as f:
        outfile.write(f)


    return


def main():
    # pdfSplit(default.input_file,default.output_folder)
    pdfExtract(default.input_file, default.output_folder, page_range=(64,88))
    return


if __name__ == "__main__":
    main()
