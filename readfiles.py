endText = '</div></div><script src="./WhatsApp_files/progress.4bd94086ece318669d91782801fa50e3.js.download"></script></body></html>'

with open("./WhatsApp.html","r") as myFile:
    data = myFile.read()
    f = open("Godwin.html", "w+")
    f.write(data +"Msgs will come here"+endText)
    f.close()