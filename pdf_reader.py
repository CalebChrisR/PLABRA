'''
"PLABRA"
Proyekto di @CalebChrisR

Nomber dor di @ChekeCur

Ayudi di @curasolenjo
~
Inspira dor di:
WORDLE
y
PALABRA di awe24.com

Esun di awe24 ta usa e reglanan di Aruba, Papiamento

Mi kier a traha un pa Korsou (y Boneiru), den Papiamentu

pdf_reader.py ta kompila tur palabra ku 5 leter for di
buki di oro ("oro.pdf"). si nomber di e pdf aki kambia, e no lo traha
'''

import PyPDF2
from tqdm import tqdm
from time import sleep    

EXCLUDES = ["(sus.)", "(v.)", "(ath.)", "(atv.)", "(int.)", "-nan"]

def main():
    # creating a pdf file object 
    buki_pdf = open('oro.pdf', 'rb')

    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(buki_pdf) 
        
    # assigns number of pages in pdf file 
    pdf_len = pdfReader.numPages
    print(pdf_len) 

    full_word_list = []
    # Loop thru all pages to find words
    for i in tqdm(range(38, 303), desc="Collecting Words"):
        # creating a page object 
        pageObj = pdfReader.getPage(i) 
        page_content = pageObj.extractText()
        content_list = page_content.split()
        cleaned_five = oro_filter(content_list)
        if (len(cleaned_five) > 0):
            for w in cleaned_five:
                if w not in full_word_list:
                    full_word_list.append(w)    
              
    # closing the pdf file object 
    buki_pdf.close()
    print(full_word_list)
    print("word amount: " + str(len(full_word_list)))

    list_to_file(full_word_list)

def oro_filter(list):
    filtered = []

    for x in list:
        if x.isalpha() and len(x) == 5 and x not in EXCLUDES and x not in filtered:
            filtered.append(x)
    
    return filtered    


def list_to_file(list):
    f = open("lista_di_sinku.txt", "w", encoding='utf-8')

    for l in tqdm(list, desc="Writing words to file"):
        f.write(l + "\n")
    print("Done writing to file!")
    f.close()


if __name__ == "__main__":
    main()

    
