## A Fibonacci Sequence Term finder by Michael Lian Gau
# This is one of the 30 days coding challenge.

import tkinter

seqNum = []
sNum = 0


def fibSeq():
    getNum = int(numEntry.get())
    sNum = 0
    while (sNum <= getNum):
        if (len(seqNum) < 2):
            seqNum.append(sNum)

        if (len(seqNum) >= 2):
            calNum = seqNum[-1] + seqNum[-2]
            seqNum.append(calNum)
        sNum += 1
    
    print(seqNum[-1])
    resLbl.config(text = str(getNum)+ "th term is : " + str(seqNum[-1]))
    seqNum.clear()

mw = tkinter.Tk()
mw.title("Fibonacci Sequence")
numEntry = tkinter.Entry(mw)
numEntry.grid(row = 0, column = 0, padx = 5, pady= 5)
numEntry.focus()

calBtn = tkinter.Button(mw, text = "Find Fibonacci Term Sequence", command = fibSeq)
calBtn.grid(row = 0, column = 1, padx = 5, pady =5 )

resLbl = tkinter.Label(mw, text = "Result")
resLbl.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)


mw.mainloop()