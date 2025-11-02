### This is my markdown page

which will be converted to html

to create a virtual environment :

python3 -m venv workspace

we use it to use markdown library of python.

we setup workspace so that if in future the version changes it should not conflict with depriciated features on out old and new library versions. there for we use workspace.
virtual environment help to maintain the library for only that worksapce project

### to activate it


- python code in worksapce

 .\workspace\Scripts\activate.bat
as it is stored in this bat file so first it need to be run.

import markdown as md

def convertHtml(source,dest):
    try:
        with open(source,"r") as f:
            md_text=f.read()
        html_text=md.markdown(md_text)

        with open(dest,'w') as f:
            f.write(html_text)
    except:
        print("File not found")

convertHtml('sample.md','md.html')

