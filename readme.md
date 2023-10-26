# Quizlet to Anki
Quizlet is a website that allows users to access other user-submitted flash card decks. Anki is an application that shows users different flash cards based on spaced repetition. There is no built-in way to convert these flash card decks to Anki decks and many of the other programs made to do this have stopped working because Quizlet's API no longer works. This program uses a workaround which uses a PDF export of a Quizlet deck to convert into an Anki deck.

# Running Quizlet to Anki
1. Download the latest version of Quizlet to Anki from the releases.
2. On the page for the flash card deck that you want to export, click the ellipses next to the "Share" button and click "Print".
![image](/assets/ss_1.png)
3. Select Glossary and save it as a PDF. You might need to use a different browser if you're not given the option to save as a PDF.
![image](/assets/ss_2.png)
4. Unzip QuizletToAnki-release.zip
5. Place the PDF that was downloaded from Quizlet into the files folder in QuizletToAnki-release
6. Rename the PDF to "quizlet.pdf"
7. Run quizlet_to_anki.exe
8. In Anki, click File -> Import and select output.txt from the QuizletToAnki-release folder
9. Make sure the "Field separator" is set to "Semicolon" and click Import

# Developing Quizlet to Anki
## Prerequisites
Please make sure you have the following prerequisites:
- ```Python 3.11 or higher``` Older versions might also work, but Python 3.11 was used to code it originally
- ```pypdf 3.16.2``` 
