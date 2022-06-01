import pyttsx3
import PyPDF2
from deep_translator import GoogleTranslator as gt

nome_livro = 'Data Science for Business'

file_pdf = f"{nome_livro}.pdf"
file_mp3 = f"{nome_livro}_menor.mp3"
full_path = 'C:\\Fontes\\Python-Scripts\\convert-pdf-to-audiobook\\'
file_pdf_path = f"{full_path}{file_pdf}"
file_mp3_path = f"{full_path}{file_mp3}"

pdfreader = PyPDF2.PdfFileReader(open(file_pdf_path, 'rb'))
speaker = pyttsx3.init()

def traduz(text):
    if text == None or text == "": return ""
    texto_pt = gt(source='auto', target='pt').translate(text)
    return texto_pt

texto_pt = ""
for page_num in range(10):
    print(f"página {page_num} de {pdfreader.numPages}...")
    page = pdfreader.getPage(page_num)
    text = page.extractText()
    cleaned_text = text.strip().replace('\n', ' ')
    #print("=== ORIGINAL ==")
    #print(cleaned_text)
    #print("=== TRADUZIDO ==")
    texto_pt = texto_pt + " " + traduz(cleaned_text)
    #print(texto_pt)

#speaker.say(cleaned_text)
speaker.save_to_file(texto_pt, file_mp3_path)
speaker.runAndWait()
speaker.stop()