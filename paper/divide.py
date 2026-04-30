from pypdf import PdfReader, PdfWriter

input_file = 'main.pdf'
reader = PdfReader(input_file)
pages = reader.pages
N = len(pages)
step = N // 5

for i in range(5):
    writer = PdfWriter()
    for page in pages[step*i: step*(i+1)]:
        writer.add_page(page)
    with open(f'output_{i}.pdf', 'wb') as f:
        writer.write(f)
