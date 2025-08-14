import pyttsx3
import PyPDF2

with open("B:\96hrs-python-coffee-and-code\python_misc_projects\Black Hat Bash.pdf", 'rb')as book:
    
    full_text= " "
    reader = PyPDF2.PdfReader(book)
    
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate",200)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()
        full_text +=content
        
    audio_reader.save_to_file(full_text,"myaudiobook.mps")
    audio_reader.runAndWait()
