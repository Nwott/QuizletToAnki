from pypdf import PdfReader

def main():
    reader = setup()
    get_text(reader)

def setup():
    # initialize reader
    reader = PdfReader("./files/quizlet.pdf")

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
            # if line contains any of the following, don't add line
            if(lines[0] in lines[j]):
                continue
            elif("/ " + str(number_of_pages) in lines[j]):
                continue
            elif("Study online at " in lines[j]):
                continue

            # if start of card, then do stuff idk
            if(str(index) + "." in lines[j] or replace_colon == True):
                if(index != 1):
                    lines[j] = '"\n' + lines[j]
                if(replace_colon == False):
                    index += 1
                if(":" in lines[j]):
                    lines[j] = lines[j].replace(":", ";", 1)
                    split = lines[j].split(";")
                    split[1] = '"' + split[1]
                    split[0] += ";"
                    lines[j] = split[0] + split[1]
                    replace_colon = False
                else:
                    replace_colon = True
            text += lines[j] 
            print(lines[j])

    # write to file
    with open("output.txt", "w", encoding="utf8") as f:
        f.write(text)


main()