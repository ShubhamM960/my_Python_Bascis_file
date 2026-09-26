import PyPDF2

pdf = open("sample.pdf", 'rb')
reader = PyPDF2.PdfReader(pdf)

# Total pages
print("Total Pages:", len(reader.pages))

page = reader.getPage(0) # reader.pages[0]

page_content = page.extractText()
print(page_content)

for page in reader.pages:
    print(page.extractText())
    
#=============== WRITER  ========================    
import PyPDF2

pdf = open("sample.pdf", 'wb')
reader = PyPDF2.PdfReader(pdf)
writer = PyPDF2.PdfWriter()

page = reader.getPage(0)
writer.addPage(page)

writer.add_metadata(
    {
        "/Title": "My PDF",
        "/Author": "Your Name"
    }
)

new_pdf = open("new_smaple.pdf", 'wb')
writer.write(new_pdf)
new_pdf.close()

# with open("new_smaple.pdf", 'wb') as new_pdf:
#     writer.write(new_pdf)
#     new_pdf.close()

