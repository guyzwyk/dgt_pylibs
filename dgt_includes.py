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
    def __init__(self, appRef, formBg="#326273", form_txtColor="#fff"):
        self.appRef = appRef
        self.formBg = formBg
        self.form_txtColor = form_txtColor

    def get_digiForm(self):
        return self.appRef
    
    def set_digiForm(self, newAppRef):
        self.appRef = newAppRef
        return self.appRef

    def set_formBgColor(self, new_bgColor):
        self.formBg = new_bgColor
        return self.formBg

    def set_formForeColor(self, new_foreColor):
        self.form_txtColor = new_foreColor
        return self.form_txtColor

    def dgt_formLabel(self, labelTxt, labelFontDescription, labelBg="#000", labelFg="#000"):
        #labelFontDescription = ('fontType, fontSize') ex: "arial 14"
        toRet       =   Label(self, text=labelTxt, font=labelFontDescription, bg=labelBg, fg=labelFg)
        #toRet.grid(row=labelGridRow, column=labelGridCol, sticky=stickyPosition)
        #font=('bold', 14)
        #stickyPosition(W/E)
        return toRet
    
    def dgt_formInput(self, frm_textVariable, inputWidth=15, inputBorder=2, input_fontSize=10):
        #toRet       =   StringVar()
        frmEntry    =   Entry(self, textvariable=frm_textVariable, width=inputWidth, bd=inputBorder, font=input_fontSize)
        return frmEntry

    def dgt_formButton(self, varCmd, btnTxt="Button", btnWidth=10, btnBg="#000", btnFg="#000"):
        newBtn      =   Button(self, text=btnTxt, width=btnWidth, command=varCmd, bg=btnBg, fg=btnFg)
        return newBtn

    def dgt_formElement(self, frm_textVariable, width=35, bd=2, font=10):
        #toRet       =   StringVar()
        frmEntry    =   Entry(self, textvariable=frm_textVariable)
        return frmEntry


myForm = digiForm("MyRef", "BgColor=blue", "ForeColor=white")

print(myForm)