# This will convert the PDF into images
# https://stackoverflow.com/a/64967365
# https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/

# pip install pdf2image==1.14.0
# https://pypi.org/project/pdf2image/
# Download https://github.com/oschwartz10612/poppler-windows/releases/


from pdf2image import *

# keep input pdf in same directory
file_path="input.pdf"

# image output directory
image_path = r".\output_image_dir"

# poppler_path = r"C:\path\to\poppler-xx\bin"
poppler_path = r"Release-22.01.0-0\poppler-22.01.0\Library\bin"
info = pdfinfo_from_path(file_path, userpw=None, poppler_path=poppler_path)
maxPages = info["Pages"]
image_counter = 0
if maxPages > 10:
    for page in range(1, maxPages, 10):
        pages = convert_from_path(file_path, dpi=300, first_page=page, 
                last_page=min(page+10-1, maxPages), poppler_path=poppler_path)
        for page in pages:
            page.save(image_path+'/' + str(image_counter) + '.png', 'PNG')
            image_counter += 1
else:
    pages = convert_from_path(file_path, 300, poppler_path=poppler_path)
    for i, j in enumerate(pages):
        j.save(image_path+'/' + str(i) + '.png', 'PNG')
