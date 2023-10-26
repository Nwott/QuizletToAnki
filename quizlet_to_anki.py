from pypdf import PdfReader

def main():
    reader = setup()
    
    if(reader == None):
        return

    get_text(reader)

    print("Quizlet exported to output.txt. Follow instructions on Github page to see how to import to Anki.")

def setup():
    reader = None

    # initialize reader
    try:
        reader = PdfReader("./files/quizlet.pdf")
    except:
        # if could not find file
        print("Could not find file named quizlet.pdf in files folder. Please follow instructions on Github.")
        return reader 

    # clear text
    with open("output.txt", "w", encoding="utf8"):
        pass

    return reader

def get_text(reader):
    text = ""

    index = 1

    replace_colon = False 
    number_of_pages = len(reader.pages)

    # loop through all pages
    for i in range(0, number_of_pages):
        # extract text from each line
        lines = reader.pages[i].extract_text().splitlines()
        
        for j in range(0, len(lines)):
            # if line contains any of the following, dont include line in export 
            if(lines[0] in lines[j]):
                continue
            elif("/ " + str(number_of_pages) in lines[j]):
                continue
            elif("Study online at " in lines[j]):
                continue

            # check if it is the start of the line or a colon
            if(str(index) + "." in lines[j] or replace_colon == True):
                # add \n to create new line if not the first line
                if(index != 1):
                    lines[j] = '"\n' + lines[j]

                # if there isn't an extra colon in the line, then increment index to go to next line
                if(replace_colon == False):
                    index += 1

                if(":" in lines[j]):
                    # change colon to semicolon so that it works in Anki
                    lines[j] = lines[j].replace(":", ";", 1)
                    split = lines[j].split(";")
                    
                    # surround the back side of the card in quotations
                    split[1] = '"' + split[1]
                    split[0] += ";"
                    lines[j] = split[0] + split[1]
                    replace_colon = False
                else:
                    replace_colon = True

            text += lines[j] 

    # write to file
    with open("output.txt", "w", encoding="utf8") as f:
        f.write(text)


main()