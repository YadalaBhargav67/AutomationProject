# import os
# import shutil

files = os.listdir(".")

for item in files:

    if os.path.isfile(item):

        if item.endswith(".pdf"):
            os.makedirs("PDFs", exist_ok=True)
            shutil.move(item, os.path.join("PDFs", item))

        elif item.endswith(".jpg"):
            os.makedirs("Images", exist_ok=True)
            shutil.move(item, os.path.join("Images", item))

        elif item.endswith(".txt"):
            os.makedirs("Text", exist_ok=True)
            shutil.move(item, os.path.join("Text", item))   
             
        
