from tkinter import *

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