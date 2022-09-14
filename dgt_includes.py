from tkinter import *

def splashCenter(appRef, width, height):
    app_width = width
    app_height = height
    screen_width = appRef.winfo_screenwidth()
    screen_height = appRef.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    toRet = appRef.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    return toRet

class digiForm:
    def __init__(self, appRef):
        self.appRef = appRef

    def get_digiForm(self):
        return self.appRef
    
    def set_digiForm(self, newAppRef):
        self.appRef = newAppRef
        return self.appRef

    def dgt_formLabel(self, labelTxt, labelFontType, labelFontSize, labelGridRow, labelGridCol, stickyPosition):
        toRet       =   Label(self, text=labelTxt, font=(labelFontType, labelFontSize))
        toRet.grid(row=labelGridRow, column=labelGridCol, sticky=stickyPosition)
        #font=('bold', 14)
        #stickyPosition(W/E)

    def dgt_formElement(self, frmEltGridRow, frmEltGridCol, stickyPosition):
        toRet       =   StringVar()
        frmEntry    =   Entry(self, textvariable=toRet)
        frmEntry.grid(row=frmEltGridRow, column=frmEltGridCol, sticky=stickyPosition)

    def dgt_formButton(self, btnTxt, btnWidth, varCmd, btnGridRow, btnGridCol, btnPadY):
        newBtn      =   Button(self, text=btnTxt, width=btnWidth, command=varCmd)
        newBtn.grid(row=btnGridRow, column=btnGridCol, pady=btnPadY)