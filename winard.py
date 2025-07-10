
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tkFont
from functools import partial
from tkinter import messagebox 
#from ttkthemes import ThemedTk
import time

class Bag:
    data_b : bytes
    data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    titel       = ""
    token       = 0 
    tokenNum    = 0     # index number of the token
    td          = 1     # time delay in dSerial.py
    tags        = "one"
    arc         = "arc"
    arcNum      = 0
    atribute    = ""
    barmenu     = "Barmenu"
    barmenuNum  = 0
    bmcheck     = "Bmcheck"
    bmcheckNum  = 0
    bmcommand   = "Bmcommand"
    bmcommandNum= 0
    bmradio     = "Bmradio"
    bmradioNum  = 0
    bmsep       = "Bmseparator"
    bmsepNum    = 0
#    borderwidth = 3 
    button      = "Button"
    buttonNum   = 0
    canvas      = "Canvas"
    canvasNum   = 0      # index number of the canvas
    cbutton     = "Cbutton"
    cbuttonNum  = 0
    config      = "Tbutton"
    configNum   = 0
    dest        = "Root" #destination
    destNum     = 0
    entry       = "Entry"
    entryNum    = 0
    fontNum     = -1  #entry or spinbox fontnumber match
    frame       = "Frame"
    frameNum    = 0      # index number of the frame
    indon       = 1      # checkbutton layout, indicator on/off
    label       = "Label"
    labelNum    = 0
    lframe      = "Lframe"    # label frame
    lframeNum   = 0      # index number of the label frame
    line        = "Line"
    lineNum     = 0
    lineh      = "Lineh"
    linehNum   = 0
    linev      = "Linev"
    linevNum   = 0
    lineset     = 0
    linedis     = 10
    linestart   = 10
    lscale      = "Lscale"
    lscaleNum   = 0
    mbutton     = "Mbutton" # menubutton
    mbuttonNum  = 0
    mcbutton    = "Mcbutton" # menu checkbutton
    mcbuttonNum = 0
    menu        = "Menu"
    menuNum     = 0
    menubar     = "Menubar"
    menubarNum  = 0
    menuoptions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#    menuoptions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    menuconfig  = "" # result of menuoptions    
    menuoptions2= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#    menuoptions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    menuconfig2 = "" # result of menuoptions2
    menuconfig3 = "" # menuconfig2 without tears
    mrbutton    = "Mrbutton" # menu radiobutton
    mrbuttonNum = 0
    notebook    = "Notebook"
    notebookNum = 0
    oval        = "Oval"
    ovalNum     = 0
    place       = "Root0"
    position    = "n"  # north west south east
    prt         = 0
    rbutton     = "Rbutton"
    rbuttonNum  = 0
    rect        = "Rect"
    rectNum     = 0
    relief      = "sunken" #flat, groove, raised, ridge, solid, or sunken
    relief2     = "sunken"
    relief3     = "sunken"
    root        = "Root"
    rootNum     = 0
    scale       = "Scale"
    scaleNum    = 0
    scaleoptions= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#    scaleoptions = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    scaleconfig = "" # result of scaleoptions    
    separator   = "Separator"
    separatorNum= 0
    show        = ""
    spinbox     = "Spinbox"
    spinboxNum  = 0
    stringvar   = "1"
    style       = "Style"
    styleNum    = 0
    submenu     = "Submenu"
    submenuNum  = 0
    tab         = "Tab"
    tabNum      = 0
    tear        = 1
    text        = "arduino screen" 
    theme       = "default"
    themeNum    = 0
    tkscale     = "tkScale"
    tkScaleNum  = 0
    toplevel    = "Toplevel"
    toplevelNum = 0
    width1      = 3 # number of char., button
    width2      = 3
    width3      = 10
# coordinates
    X1    = 0   # first X coordinate
    Y1    = 0   # first Y coordinate
    X2    = 480  # second X or Xsize
    Y2    = 320  # second Y or Ysize
    Xd    = 0   # deltaX
    Yd    = 0   # deltaY
    Wbd   = 1   # border 
# canvas content:
    ArcStart   = 45
    ArcExtend  = 90
    ArcStyle   = 0 # 0=PIESLICE, 1=CHORD, 2=ARC
    arrow      = "" # none first last both
    arrowshape =[8,10,3]
    Coord = [] # multi line
    capstyle   = "butt"  # butt projecting round.
    Lw  = 1    # line width
    Ld  = 0    # dash 0=no 1=yes
    Ld1 = 8    # dash 1
    Ld2 = 5    # dash 2
    Lnvert     = 4  #number  vertical  lines
    Lnhorz     = 4  #number horizontal lines 
# slider (scale) and spinbox:
    Sfrom      = 0     # scale (slider), spinbox
    Sto        = 10    # scale, spinbox
    Sincrement = 1
    Slength    = 200   # scale, spinbox
    Srelief    = 4
    Sinterval  = 1     # scale, spinbox: increment
    Sset       = 4     # scale, spinbox
    Sorient    = "vertical"  #"horizontal" 
    Sjustify   = "left" # spinbox: justify
    Stype      = 0   # choice of type
    Sresolution= 3
    Svalstring = ""
    Sformat    = ""
    Sshowvalue = ""   # tk scale show values False or True

# colors:
    color1  = "#000"  # 88 
    color2  = "#ccc"  # 89  
    color3  = "#bbb"  # 90
    color4  = "#ffa"  # 91 
    color5  = "#999"  # 92 
    color6  = "#888"  # 93
    color7  = "#777"  # 94
    color8  = "#666"  # 95
    color9  = "#555"  # 96
    color10 = "#444"  # 97
    color11 = "#333"  # 98
    color12 = "#2ff"  
    color13 = "#111"  
    color14 = "#ddd"
    color15 = "#eee"
    color16 = "#fff"

# fonts:
    Font           = ""  # som font properties
    Fontfamily     = "Helvetica"  # font family     Helvetica, Times, Arial, Verdana
    Fontsize       = 8       # font size       pixels high
    Fontweight     = "normal" # font weight     normal, bold
    Fontslant      = "italic"  # font roman or italic
    Fontunderline  = ""       # font underline  0 or 1
    Fontoverstrike = ""       # font overstrike 0 or 1
    
    transmit = ""
    
    

class Objects:
    zero = 0






def calculateX1Y1(n):
    Bag.Coord.clear()
    Bag.X1 = Bag.data[n]    
    Bag.Y1 = Bag.data[n+1]

def calculateX1Y1X2Y2(n):
    Bag.Coord.clear()
    Bag.X1 = Bag.data[n]    
    Bag.Y1 = Bag.data[n+1]
    Bag.X2 = Bag.data[n+2]    
    Bag.Y2 = Bag.data[n+3]

def destination():   # to containers
    Bag.destNum = int(Bag.data[3]) 
    dest = int(Bag.data[2])
#    print("destination")
    if   dest==36: 
        Bag.dest = Bag.frame
    elif dest==37: 
        Bag.dest = Bag.lframe
    elif dest==38:
        Bag.dest = Bag.canvas
    elif dest==39: 
        Bag.dest = Bag.notebook
    elif dest==40: 
        Bag.dest = Bag.tab
    elif dest==41: 
        Bag.dest = Bag.root
    elif dest==42: 
        Bag.dest = Bag.toplevel   
    elif dest==48: 
        Bag.dest = Bag.mbutton
    elif dest==49: 
        Bag.dest = Bag.mbutton
    elif dest==50: 
        Bag.dest = Bag.mbutton
    elif dest==51: 
        Bag.dest = Bag.menubar
    elif dest==52: 
        Bag.dest = Bag.barmenu
    elif dest==57: 
        Bag.dest = Bag.submenu  

def configWidgetTheme():   
    dest = int(Bag.data[2])
#    print("configWidgetTheme")
    if   dest==24: 
        Bag.dest = "TLabel"
    elif dest==25:
        Bag.dest = "TButton"        
    elif dest==26:
        Bag.dest = "TRadiobutton"
    elif dest==27:
        Bag.dest = "TCheckbutton"        
    elif dest==28:
        Bag.dest = Bag.Sorient+"TScale"
    elif dest==29:
        Bag.dest = "TSpinbox"        
    elif dest==30:  
        Bag.dest = "TEntry"    
    elif dest==36:
        Bag.dest = "TFrame"
    elif dest==37:
        Bag.dest = "TLabelframe"
        if  int(Bag.data[1])==1: Bag.dest = Bag.dest+".Label"        
    elif dest==39:
        Bag.dest = "TNotebook"
        if  int(Bag.data[1])==1: Bag.dest = Bag.dest+".Tab"
    elif dest==40:
        Bag.dest = "TNotebook"
        if  int(Bag.data[1])==1: Bag.dest = Bag.dest+".Tab"
    elif dest==41:
        Bag.dest = "."
    elif dest==42:
        Bag.dest = "TToplevel"      
    elif dest==43:
        Bag.dest = "TSeparator"  
        
    elif dest==48:
        Bag.dest = "TMenubutton" 
    elif dest==49:
        Bag.dest = "TMenucheckbutton" 
    elif dest==50:
        Bag.dest = "TMenuradiobutton"         
    elif dest==107: Bag.dest = "."   # theme

def configWidget(): 
    dest = int(Bag.data[2])
#    print("configWidget")
    if   dest==24: 
        Bag.dest = Bag.label+str(Bag.data[3])+".TLabel"
    elif dest==25:
        Bag.dest = Bag.button+str(Bag.data[3])+".TButton"
    elif dest==26:
        Bag.dest = Bag.rbutton+str(Bag.data[3])+".TRadiobutton"
    elif dest==27:
        Bag.dest = Bag.cbutton+str(Bag.data[3])+".TCheckbutton"        
    elif dest==28:
        if Bag.X2>Bag.Y2: Bag.Sorient=".Horizontal"
        else: Bag.Sorient=".Vertical"
        Bag.dest = Bag.scale+str(Bag.data[3])+Bag.Sorient+".TScale"
    elif dest==29:
        Bag.dest = Bag.spinbox+str(Bag.data[3])+".TSpinbox"        
    elif dest==30:
        Bag.dest = Bag.entry+str(Bag.data[3])+".TEntry"          
    elif dest==36:
        Bag.dest = Bag.frame+str(Bag.data[3])+".TFrame"
    elif dest==37:
        Bag.dest = Bag.lframe+str(Bag.data[3])+".TLabelframe"
        if  Bag.data[1]==1: Bag.dest = Bag.dest+".Label"        
    elif dest==39:
        Bag.dest = Bag.notebook+str(Bag.data[3])+".TNotebook"
        if  Bag.data[1]==1: Bag.dest = Bag.dest+".Tab"
        print("Bag.dest",Bag.dest)        
    elif dest==40:
        Bag.dest = Bag.tab+str(Bag.data[3])+".TNotebook"
        if  Bag.data[1]==1: Bag.dest = Bag.dest+".Tab"
        print("Bag.dest",Bag.dest)  
    elif dest==41:
#        Bag.dest = Bag.root+str(Bag.data[3])+".T."
        Bag.dest = "." 
        print("C root")      
# temporary solution for root background color:
        if Bag.data[4]==89:
            Objects.Root0.configure(background=Bag.color2)
    elif dest==42:
        Bag.dest = Bag.tab+str(Bag.data[3])+".TToplevel"  
        print("C top")  
# temporary solution for toplevel background color:    
        if Bag.data[4]==89:
            tpl="Toplevel"+str(Bag.data[3])
            exec(f"Objects.{tpl}.configure(background=Bag.color2)")
    elif dest==43:
        Bag.dest = Bag.separator+str(Bag.data[3])+".TSeparator"  
    elif dest==48:
        Bag.dest = Bag.mbutton+str(Bag.data[3])+".TMenubutton"
    elif dest==49:
        Bag.dest = Bag.mcbutton+str(Bag.data[3])+".TMenucheckbutton"
    elif dest==50:
        Bag.dest = Bag.mrbutton+str(Bag.data[3])+".TMenuradiobutton"
                
    elif dest==106: Bag.dest = "."   # style

##               .....config( dest, Bag.config = Bag.atribute )
##   def destination(): ________|        |             |
##   def configWidget(): ________________|             |
##   def configAtribute(): ____________________________|
##       [0]     [1]        [2]       [3]     [4]        
##   [generate, number, destination, number, token/data 

def configAtribute():          ##  configure atribute  ##
    conf_atr = int(Bag.data[4])
#    print("configAtribute")
    if   conf_atr==71:
        Bag.config   = "relief"
        Bag.atribute = Bag.relief
    elif conf_atr==72:
        Bag.config   = "troughrelief"
        Bag.atribute = Bag.relief        
    elif conf_atr==82:
        Bag.config   = "tabposition"
        Bag.atribute = Bag.position
        print("tabposition")   
    elif conf_atr==83:
        Bag.config   = "width"
        Bag.atribute = Bag.width1       
    elif conf_atr==84:
        Bag.config   = "borderwidth"
        Bag.atribute = Bag.width2  
    elif conf_atr==85:
        Bag.config   = "sliderthickness"
        Bag.atribute = Bag.width1  
             
    elif conf_atr==88: 
        Bag.config   = "foreground"
        Bag.atribute = Bag.color1 
    elif conf_atr==89:
        Bag.config   = "background"
        Bag.atribute = Bag.color2 
    elif conf_atr==90: 
        Bag.config   = "activeforeground"
        Bag.atribute = Bag.color3          
    elif conf_atr==91: 
        Bag.config   = "activebackground"
        Bag.atribute = Bag.color4   
    elif conf_atr==92:
        Bag.config   = "selectforeground"
        Bag.atribute = Bag.color5 
    elif conf_atr==93:
        Bag.config   = "selectbackground"
        Bag.atribute = Bag.color6    
    elif conf_atr==94:
        Bag.config   = "bordercolor"
        Bag.atribute = Bag.color7            
    elif conf_atr==95:
        Bag.config   = "lightcolor"
        Bag.atribute = Bag.color8   
    elif conf_atr==96:
        Bag.config   = "darkcolor"
        Bag.atribute = Bag.color9      
    elif conf_atr==97:
        Bag.config   = "fieldbackground"
        Bag.atribute = Bag.color10         
    elif conf_atr==98:
        Bag.config   = "insertcolor"
        Bag.atribute = Bag.color11   
    elif conf_atr==103: 
        Bag.config   = "troughcolor"    # scale(slider)
        Bag.atribute = Bag.color16

def configMap():    
    dest = int(Bag.data[2])
    conf_atr = int(Bag.data[4]) 
#    print("configMap")
    if  dest==25:   # button
        if  conf_atr==88: 
            Bag.config   = "foreground" 
        elif  conf_atr==89: 
            Bag.config   = "background"
        Bag.atribute = "[('active', '"+Bag.color3+"')]"
    elif dest==26:  # Radiobutton
        if  conf_atr==88: 
            Bag.config   = "foreground" 
        elif  conf_atr==89: 
            Bag.config   = "background"
        elif  conf_atr==92: 
            Bag.config   = "indicatorcolor"
        Bag.atribute = "[('active', '"+Bag.color3+"'), ('selected', '"+Bag.color5+"'), ('!selected', '"+Bag.color6+"')]"
    elif dest==27:  # TCheckbutton
        if  conf_atr==88: 
            Bag.config   = "foreground" 
        elif  conf_atr==89: 
            Bag.config   = "background"
        elif  conf_atr==92: 
            Bag.config   = "indicatorcolor"
        Bag.atribute = "[('active', '"+Bag.color3+"'), ('selected', '"+Bag.color5+"'), ('!selected', '"+Bag.color6+"')]"
    elif dest==39:  # notebook tab label
        if   conf_atr==92:  
            Bag.config   = "background"       
            Bag.atribute = "[('selected','"+Bag.color5+"')]" 


def configMenuOptions():          ##  configure menus  tk version
    Bag.menuconfig=" "
    if Bag.menuoptions[1] == 1: Bag.menuconfig=Bag.menuconfig+",tearoff="+str(Bag.tear)
    if Bag.menuoptions[2] == 1: 
        font=",font='"+Bag.Fontfamily+" "+str(Bag.Fontsize)+" "+Bag.Fontslant+" "+Bag.Fontunderline+" "+Bag.Fontoverstrike+"'"
        Bag.menuconfig=Bag.menuconfig+font
    if Bag.menuoptions[3] == 1: Bag.menuconfig=Bag.menuconfig+",foreground='"+Bag.color1+"'"
    if Bag.menuoptions[4] == 1: Bag.menuconfig=Bag.menuconfig+",background='"+Bag.color2+"'"
    if Bag.menuoptions[5] == 1: Bag.menuconfig=Bag.menuconfig+",activeforeground='"+Bag.color3+"'"    
    if Bag.menuoptions[6] == 1: Bag.menuconfig=Bag.menuconfig+",activebackground='"+Bag.color4+"'"
    if Bag.menuoptions[7] == 1: Bag.menuconfig=Bag.menuconfig+",selectcolor='"+Bag.color5+"'"
    if Bag.prt == 1: print("    menuconfig: ",Bag.menuconfig)

def configMenuOptions2():          ##  configure menus  tk version
    Bag.menuconfig2=" "
#    if Bag.menuoptions2[1] == 1: Bag.menuconfig2=Bag.menuconfig2+",tearoff="+str(Bag.tear)
    if Bag.menuoptions2[2] == 1: 
        font=",font='"+Bag.Fontfamily+" "+str(Bag.Fontsize)+" "+Bag.Fontslant+" "+Bag.Fontunderline+" "+Bag.Fontoverstrike+"'"
        Bag.menuconfig2=Bag.menuconfig2+font
    if Bag.menuoptions2[3] == 1: Bag.menuconfig2=Bag.menuconfig2+",foreground='"+Bag.color1+"'"
    if Bag.menuoptions2[4] == 1: Bag.menuconfig2=Bag.menuconfig2+",background='"+Bag.color2+"'"
    if Bag.menuoptions2[5] == 1: Bag.menuconfig2=Bag.menuconfig2+",activeforeground='"+Bag.color3+"'"    
    if Bag.menuoptions2[6] == 1: Bag.menuconfig2=Bag.menuconfig2+",activebackground='"+Bag.color4+"'"
#    if Bag.menuoptions2[7] == 1: Bag.menuconfig2=Bag.menuconfig2+",selectcolor='"+Bag.color5+"'"  
    
    Bag.menuconfig3=Bag.menuconfig2
    if Bag.menuoptions2[1] == 1: Bag.menuconfig2=Bag.menuconfig2+",tearoff="+str(Bag.tear)
    if Bag.menuoptions2[7] == 1: Bag.menuconfig2=Bag.menuconfig2+",selectcolor='"+Bag.color5+"'"
##    if Bag.prt == 1: print("    menuconfig2:",Bag.menuconfig2)
##    if Bag.prt == 1: print("    menuconfig3:",Bag.menuconfig3)
    
def configScaleOptions():          ##  configure scale  tk version
    Bag.scaleconfig=" " 
    if Bag.scaleoptions[1] == 1: 
        font=",font='"+Bag.Fontfamily+" "+str(Bag.Fontsize)+" "+Bag.Fontslant+" "+Bag.Fontunderline+" "+Bag.Fontoverstrike+"'"
        Bag.scaleconfig=Bag.scaleconfig+font
    if Bag.scaleoptions[2] == 1: Bag.scaleconfig=Bag.scaleconfig+",background='"+Bag.color2+"'"
    if Bag.scaleoptions[3] == 1: Bag.scaleconfig=Bag.scaleconfig+",activebackground='"+Bag.color4+"'" 
    if Bag.scaleoptions[4] == 1: Bag.scaleconfig=Bag.scaleconfig+",troughcolor='"+Bag.color16+"'"
    if Bag.scaleoptions[5] == 1: Bag.scaleconfig=Bag.scaleconfig+",highlightcolor='"+Bag.color13+"'" 
    if Bag.scaleoptions[6] == 1: Bag.scaleconfig=Bag.scaleconfig+",highlightbackground='"+Bag.color14+"'" 
    if Bag.scaleoptions[7] == 1: Bag.scaleconfig=Bag.scaleconfig+",highlightthickness='"+str(Bag.width2)+"'" 
    if Bag.scaleoptions[8] == 1: Bag.scaleconfig=Bag.scaleconfig+",width='"+str(Bag.width1)+"'"
    if Bag.scaleoptions[9] == 1: Bag.scaleconfig=Bag.scaleconfig+",borderwidth='"+str(Bag.width3)+"'"
    if Bag.scaleoptions[10] == 1: Bag.scaleconfig=Bag.scaleconfig+",relief='"+Bag.relief+"'"
    if Bag.scaleoptions[11] == 1: Bag.scaleconfig=Bag.scaleconfig+",sliderrelief='"+Bag.relief3+"'"    
    if Bag.prt == 1: print("    scaleconfig:",Bag.scaleconfig)
          
              
def parser():
    data_b = Bag.data_b.split(b',')
    t = int(data_b[0])
    Bag.token = t
#next, tokens with text string
    if  t==0: return
    if  t<8:     
        data_str=Bag.data_b.decode('utf-8')
        n=data_str.find(',')+1
        l=len(data_str)-2
        if   t==2:
            Bag.text = data_str[n:l]
            if Bag.prt == 1: print("    text:",Bag.text)   
        elif t==3:   
            Bag.tags = data_str[n:l]
            if Bag.prt == 1: print("    tags:",Bag.tags)
        elif t==4:  
            Bag.show = data_str[n:l]
            if Bag.prt == 1: print("    show:",Bag.show)  
        elif t==5:  # spinbox opties, spinbox zie: elif t==29: 
            text = data_str[n:l]
            if Bag.prt == 1: 
                print("    spinbox set:",text,"  type", type(text))
            spin = text.split(" ")
            Bag.Stype    = spin[0]
            if   spin[1]=='0':  Bag.Sjustify="left"
            elif spin[1]=='1':  Bag.Sjustify="center"
            elif spin[1]=='2':  Bag.Sjustify="right"
            Bag.width1   = spin[2]
            Bag.Sset     = spin[3] 
        elif t==6:   
            Bag.tags = data_str[n:l]
            if Bag.prt == 1: print("    delete tags:",Bag.tags)
            tags2delete()             
        return()    
    else:
        l=len(data_b)-1
        for a in range(0,l):
            Bag.data[a] = int(data_b[a])
        Bag.tokenNum = int(data_b[1]) 

    if   t<14: 
        if   t==8:  # start with Bag.Coord
            l=len(data_b)-1
            Bag.Coord.clear()
            for a in range(1, l):
                Bag.Coord.append(int(data_b[a]))
            if Bag.prt == 1: print("    coordinates", Bag.Coord) 
        elif t==9:  # append Bag.Coord
            l=len(data_b)-1
            for a in range(1, l):
                Bag.Coord.append(int(data_b[a]))
            if Bag.prt == 1: print("    coordinates", Bag.Coord)
        elif t==10: # replace part of Bag.Coord
            lc=len(Bag.Coord)   # length Bag.Coord
            rf=int(data_b[1])   # replace from
            lr=len(data_b)-3+rf  # length to replace 
            i=2 
            while rf < lc:    # replace
                Bag.Coord[rf]=int(data_b[i])
                i += 1  
                rf += 1                
            la=lr-rf  # length to append
            while la > 0:     # append
                Bag.Coord.append(int(data_b[i]))
                la -= 1
                i += 1              
            if Bag.prt == 1: print("    coordinates", Bag.Coord)   
        elif t==11: # draw line, NEW
            Bag.lineNum = Bag.data[1]
            destination()
            createLine() 
  
        elif t==12: # 
            tmp=0
        elif t==13: # SETLINE
            Bag.lineset  =Bag.data[1]   # 0=xy, 1=x, 2=y
            Bag.linestart=Bag.data[2]
            Bag.linedis  =Bag.data[3]
#            print("lineset",Bag.lineset,"  linestart", Bag.linestart,"  distance",Bag.linedis)
                  
    elif t<24:   #draw figures rect, arc, line etc
        if   t== 14:
            Bag.lineNum = Bag.data[1]
            destination()
            l=len(data_b)-1
#            print("l=",l)
            Bag.Coord.clear()
            for a in range(4, l):
                Bag.Coord.append(int(data_b[a]))
#                Bag.Coord.append(Bag.data[a])
#            print("coord=",Bag.Coord)
            createLine()            
#            Bag.Coord.clear()
        elif t==15:
            calculateX1Y1X2Y2(4)
            destination()
            Bag.lineshNum = Bag.data[1]
            createLinesHorz()
        elif t==16:
            calculateX1Y1X2Y2(4)
            destination()
            Bag.linesvNum = Bag.data[1]
            createLinesVert()
        elif t==17:
            calculateX1Y1X2Y2(4)
            destination()
            Bag.rectNum = Bag.data[1]
            createRectangle()
        elif t==18:
            calculateX1Y1X2Y2(4)
            destination()
            Bag.ovalNum = Bag.data[1]
            createOval()
        elif t==19:
            calculateX1Y1X2Y2(4)
            destination()
            Bag.arcNum = Bag.data[1]
            createArc()

    elif t<36:
        if   t==24:  
            calculateX1Y1(4)
            Bag.labelNum = Bag.data[1]
            destination()
            createLabel()
        elif t==25:  
            calculateX1Y1(4)
            Bag.buttonNum = Bag.data[1]
            destination()
            createButton()
        elif t==26: 
            calculateX1Y1(4)
            Bag.rbuttonNum = Bag.data[1]
            destination()
            createRadioButton()
        elif t==27:  
            calculateX1Y1(4)
            Bag.cbuttonNum = Bag.data[1]
            destination()
            createCheckButton()
        elif t==28:  
            calculateX1Y1X2Y2(4)
            Bag.scaleNum = Bag.data[1]  
            destination()
            createScale()
        elif t==29: 
            calculateX1Y1(4)
            Bag.spinboxNum = Bag.data[1]  
            destination()
            createSpinbox() 
        elif t==30: 
            calculateX1Y1(4) 
            Bag.entryNum = Bag.data[1]
            Bag.token = 30
            destination()
            createEntry()
            
    elif t<48:       # containers:
        if   t==36: 
            calculateX1Y1X2Y2(4)
            Bag.frameNum = Bag.data[1]
            destination()
            createFrame()
        elif t==37:  
            calculateX1Y1X2Y2(4)
            Bag.lframeNum = Bag.data[1]
            destination()
            createLabelFrame()
        elif t==38: 
            calculateX1Y1X2Y2(4)
            Bag.canvasNum = Bag.data[1]
            destination()
            createCanvas() 
        elif t==39: 
            calculateX1Y1X2Y2(4)
            Bag.notebookNum = Bag.data[1]
            destination()
            createNotebook()   
        elif t==41: 
            calculateX1Y1(2)
            rootsize()
        elif t==42:
            calculateX1Y1(2)
            Bag.toplevelNum = Bag.data[1]
#            print("TopLevel")
            destination() 
            createToplevel()
        elif t==43:   
            calculateX1Y1X2Y2(4)
            Bag.separatorNum = Bag.data[1]
            destination()
            createSeparator()
        elif t==44: 
            Bag.canvasNum = Bag.data[1]   
            if Bag.prt == 1: print("    canvas select") 
            
    elif t<64:       # ### menu's ###
        if   t==48: 
            calculateX1Y1(4)
            Bag.menuNum = Bag.data[1]
            Bag.mbuttonNum = Bag.data[1]
            destination()
            configMenuOptions()
            createMenuButton()
        elif t==49: 
            Bag.menuNum = Bag.data[3]
            Bag.mcbuttonNum = Bag.data[1]
            destination()
            menubutton_add_checkbutton()
        elif t==50: 
            Bag.menuNum = Bag.data[3]
            Bag.mrbuttonNum = Bag.data[1]
            destination()
            menubutton_add_radiobutton()
        elif t==51:  
            Bag.menubarNum = Bag.data[1]
            destination()
            createMenubar() 
        elif t==52: 
            Bag.barmenuNum = Bag.data[1]
            destination()
            createBarMenu() 
        elif t==53:  
            Bag.bmcommandNum = Bag.data[1]
            destination()
            barmenu_add_command() 
        elif t==54:  
            Bag.bmradioNum = Bag.data[1]
            destination()
            barmenu_add_radiobutton()
        elif t==55:  
            Bag.bmcheckNum = Bag.data[1]
            destination()
            barmenu_add_checkbutton()
        elif t==56: 
            Bag.bmsepNum = Bag.data[1]
            destination()
            barmenu_add_separator()
        elif t==57: 
            Bag.submenuNum = Bag.data[1]
            destination()
            barmenu_add_submenu()
        elif t==58:  # root.config(menu=menubar)   # obsolate
            mbar = Bag.menubar+str(Bag.menubarNum)
            dest = Bag.dest+str(Bag.destNum) 
        elif t==59:  # checkbutton layout: indicatoron
            Bag.indon   = Bag.data[1] 
        elif t==60: 
            Bag.tearoff = Bag.data[1]     
        elif t==61: 
            Bag.menuoptions=Bag.data[:]
            configMenuOptions()
        elif t==62: 
            Bag.menuoptions2=Bag.data[:]
            configMenuOptions2()
            
    elif t<80:                     
        if t==64: 
            tmp=0             
            Bag.scaleoptions=Bag.data[:]
            configScaleOptions() 
        elif t==65:  # line width
            Bag.Lw  = Bag.data[1]  
        elif t==66:  # 
            Bag.Ld  = Bag.data[1]
            Bag.Ld1 = int(Bag.data[2])
            Bag.Ld2 = Bag.data[3]
        elif t==67:  #   # arrows
            if   Bag.data[1]==0:
                Bag.arrow = "none"   # arrow place
            elif Bag.data[1]==1:
                Bag.arrow = "first" 
            elif Bag.data[1]==2:
                Bag.arrow = "last"
            elif Bag.data[1]==3:
                Bag.arrow = "both"
        elif t==68:  #               # arrow shapes
            Bag.arrowshape =[Bag.data[1],int(Bag.data[2]),Bag.data[3]]
        elif t==69:  #  number vert. and horz. lines. distance vert. and horz. lines
            Bag.Lnvert = Bag.data[1]       # ????? not int ?
            Bag.Lnhorz = int(Bag.data[2])  # ????? int ?
            Bag.Xd = Bag.data[3]           # ?????
            Bag.Yd = int(Bag.data[4])      # ?????
        elif t==70: 
            Bag.ArcStart  = int(Bag.data[1])
            Bag.ArcExtend = int(Bag.data[2])
            Bag.ArcStyle  = int(Bag.data[3])
        elif (t==73)|(t==72)|(t==71):  # relief
            relief=""
            if  Bag.data[1] == 0: 
                relief = "flat"
            elif Bag.data[1] == 1:
                relief = "groove"
            elif Bag.data[1] == 2:
                relief = "raised"
            elif Bag.data[1] == 3:
                relief = "ridge"
            elif Bag.data[1] == 4:
                relief = "solid"
            elif Bag.data[1] == 5:
                relief = "sunken"
            if   t==71: Bag.relief  = relief
            elif t==72: Bag.relief2 = relief
            elif t==73: Bag.relief3 = relief
#            print("t=",t)
                
    elif t<88:       # fonts:"
        if   t==80: 
            if   int(Bag.data[4]) == 0:
                Bag.Fontfamily = "Helvetica"
            elif int(Bag.data[4]) == 1:
                Bag.Fontfamily = "Times"
            elif int(Bag.data[4]) == 2:
                Bag.Fontfamily = "Arial"
            elif int(Bag.data[4]) == 3:
                Bag.Fontfamily = "Verdana" 
            else: Bag.fontfamily = "Helvetica"
            Bag.Fontsize = Bag.data[5] 
            Bag.atribute = "'"+Bag.Fontfamily+"', "+ str(Bag.Fontsize) 
            if  Bag.data[6] == 0:
                Bag.Fontweight  = "normal"
            else: Bag.Fontweight = "bold"
            Bag.atribute = Bag.atribute+", '"+ Bag.Fontweight +"'"
            if  Bag.data[7] == 0:
                Bag.Fontslant  = "roman"
            else: Bag.Fontslant = "italic"
            Bag.atribute = Bag.atribute+", '"+ Bag.Fontslant +"'"
            if  Bag.data[8] == 1: 
                Bag.atribute=Bag.atribute+", 'underline'" 
                Bag.Fontunderline  = "underline" 
            else:  Bag.Fontunderline  = " "
            if  Bag.data[9] == 1: 
                Bag.atribute=Bag.atribute+", 'overstrike'"
                Bag.Fontoverstrike = "overstrike"  
            else:  Bag.Fontoverstrike = " "
            Bag.config = "font" 
            t2=int(Bag.data[2])
            if t2==107: 
                configWidgetTheme()
                changeFont()
            elif t2==30:
                Bag.fontNum=Bag.data[3]
            elif t2==29:
                Bag.fontNum=Bag.data[3]
            elif t2==1:
                Bag.fontNum=Bag.data[3]
                return()
            else: 
                configWidget()
                changeFont()
        elif t==82:  #
            if   Bag.data[1] == 0:  Bag.position = "nw"
            elif Bag.data[1] == 1:  Bag.position = "n"
            elif Bag.data[1] == 2:  Bag.position = "ne"
            elif Bag.data[1] == 3:  Bag.position = "en"
            elif Bag.data[1] == 4:  Bag.position = "e"
            elif Bag.data[1] == 5:  Bag.position = "es"
            elif Bag.data[1] == 6:  Bag.position = "se"
            elif Bag.data[1] == 7:  Bag.position = "s"
            elif Bag.data[1] == 8:  Bag.position = "sw"
            elif Bag.data[1] == 9:  Bag.position = "ws"
            elif Bag.data[1] == 10: Bag.position = "w"
            elif Bag.data[1] == 11: Bag.position = "wn" 
        elif t==83:
            Bag.width = Bag.data[1]
            Bag.width1 = Bag.data[1]
        elif t==84:  #
            Bag.Wbd = Bag.data[1]
            Bag.width2 = Bag.data[1]
        elif t==85:
            Bag.width1 = Bag.data[1]
            Bag.width3 = Bag.data[1]
            
    elif t<104:       # colors:
        byte_array = bytearray([Bag.data[1],Bag.data[2],Bag.data[3]])
        hex_string = byte_array.hex()
        colors = "#"+hex_string
#        print("Color string after conversion: " + colors)
        if   t==88:     
            Bag.color1 = colors 
        elif t==89:        
            Bag.color2 = colors     
        elif t==90:        
            Bag.color3 = colors         
        elif t==91:     
            Bag.color4 = colors 
        elif t==92:   
            Bag.color5 = colors 
        elif t==93:      
            Bag.color6 = colors              
        elif t==94:  
            Bag.color7 = colors 
        elif t==95: 
            Bag.color8 = colors 
        elif t==96: 
            Bag.color9 = colors     
        elif t==97: 
            Bag.color10 = colors    
        elif t==98: 
            Bag.color11 = colors 
        elif t==99:    
            Bag.color12 = colors                       
        elif t==100:   
            Bag.color13 = colors                               
        elif t==101:   
            Bag.color14 = colors             
        elif t==102:   
            Bag.color15 = colors      
        elif t==103:  
            Bag.color16 = colors 
            
    elif t<128:    
        if   t==104:  # print the content of class Objects 
            if int(Bag.data[1]) == 0: return
            print("class Objects:")
# Using the dir() function to get current properties and values
            obj = Objects()
            for attr in dir(obj):
        # Getting rid of dunder methods
                if not attr.startswith("__"):
                    print("   ",attr, getattr(obj, attr))
            print("class Objects end\n")
        elif t==105:  # 
            Bag.prt = int(Bag.data[1])
            if Bag.data[1] == 1: print("The construction:")
        elif t==106:  # style, one object
            configWidget()
            configAtribute()
##            destination()  # notebook works not well with this statement
            if Bag.data[2]!=41: changeStyle()
        elif t==107:  # theme, the style of the same type objects 
            configWidgetTheme()
            if int(Bag.data[4]) == 80: changeFont()
            else: 
                configAtribute()
                changeStyle()
        elif t==108:  # map
            configWidget()
#            configAtribute()
            configMap()
            changeMap()
        elif t==109:  # theme, the complete style set of all objects
            Bag.themeNum=int(Bag.data[1])
            changeTheme()            
# messages            
        elif t==112:
            messageboxInfo()
        elif t==113:
            messageboxWarning()
        elif t==114:
            messageboxError()
        elif t==115:
            messageboxQuestion()
        elif t==116:
            messageboxOkCancel()
        elif t==117:
            messageboxYesNo()
        elif t==118:
            messageboxRetryCancel()




  
import serial
import time
import sys

arduino=serial.Serial(port=sys.argv[1],baudrate=115200,timeout=0.05)  
arduino.close()
arduino.open()          

def transceiver():
    Bag.data_b = arduino.readline()
    l=len(Bag.data_b)
    if l>0:  # send code to arduino 
        arduino.write(bytes(Bag.transmit,'utf-8'))
        Bag.transmit="\0"
        parser()
    exec(f"Objects.{root}.after(Bag.td, transceiver)")



        


def createRoot():
    root  = Bag.root+str(Bag.rootNum)
    geometry="100x50" 
    exec(f"Objects.{root}=Tk()")
#    exec(f"Objects.{root}=ThemedTk(theme='default')")
    exec(f"Objects.{root}.after(200, transceiver)")
    exec(f"Objects.{root}.geometry('{geometry}')")
    exec(f"Objects.{root}.title(Bag.text)")
    Objects.style = Style()  
    Bag.rootNum = 1

def rootsize():
    root  = Bag.root+str(Bag.rootNum-1)
    geometry= str(Bag.X1)+"x"+str(Bag.Y1)
    if Bag.prt == 1: print("   ", root,"-> .","   geometry:",geometry)
    exec(f"Objects.{root}.geometry('{geometry}')")
    exec(f"Objects.{root}.title(Bag.text)")

#############################################################
def createToplevel():
    toplevel  = Bag.toplevel+str(Bag.toplevelNum)
    if Bag.prt == 1: print("   ", toplevel,"-> .")
    geometry= str(Bag.X1)+"x"+str(Bag.Y1)
    exec(f"Objects.{toplevel}=Toplevel()")
    exec(f"Objects.{toplevel}.geometry('{geometry}')")
    exec(f"Objects.{toplevel}.title(Bag.text)")

#############################################################
def createSeparator():
    separator = Bag.separator+str(Bag.separatorNum)
    dest = Bag.dest+str(Bag.destNum)
    if Bag.prt == 1: print("   ", separator,"->", dest)
    if Bag.X2 > Bag.Y2: 
        orient = 'horizontal'
    else: orient ='vertical'
    exec(f"Objects.{separator} = Separator(Objects.{dest}, orient=orient)")
    exec(f"Objects.{separator}.place(x=Bag.X1, y=Bag.Y1, width=Bag.X2, height =Bag.Y2)")

#############################################################
def createNotebook():
    notebook = Bag.notebook+str(Bag.notebookNum)
    dest = Bag.dest+str(Bag.destNum)
    tnotebook =  "Objects."+notebook+".TNotebook" 
    if Bag.prt == 1: print("   ", notebook,"->",dest,"  tabposition:",Bag.position)
    exec(f"Objects.{notebook}=Notebook(Objects.{dest}, width={Bag.X2}, height={Bag.Y2,})")
    exec(f"Objects.{notebook}.place(x={Bag.X1}, y={Bag.Y1}, width=Bag.X2, height=Bag.Y2)")
    exec(f"Objects.{notebook}['style'] = tnotebook") 
    exec(f"Objects.style.configure(style=tnotebook, tabposition=Bag.position)")
    tabs = Bag.text.split(",")
    for x in tabs:
        tab = Bag.tab+str(Bag.tabNum)
        Bag.tabNum = Bag.tabNum + 1
        ttab = "Objects."+tab+".TNotebook"
        name = tab+".TNotebook"
        exec(f"Objects.{tab}=Frame(Objects.{notebook}, borderwidth=0)")
        exec(f"Objects.{tab}['style'] = ttab") 
        exec(f"Objects.{tab}.pack(fill='both', expand=True)")
        exec(f"Objects.{notebook}.add(Objects.{tab},text='{x}')") 
        if Bag.prt == 1: print("   ", tab,"->",notebook,"       Style name:", name)

#############################################################
def createFrame():
    frame  = Bag.frame+str(Bag.frameNum)
    dest = Bag.dest+str(Bag.destNum) 
    tframe =  "Objects."+frame+".TFrame"
    name = frame+".TFrame"
    if Bag.prt == 1: print("   ", frame,"->", dest,"    Style name:", name)
    exec(f"Objects.{frame}=Frame(Objects.{dest})")
    exec(f"Objects.{frame}['style'] = tframe") 
    exec(f"Objects.{frame}.place(x={Bag.X1}, y={Bag.Y1}, width=Bag.X2, height=Bag.Y2)")

def createLabelFrame():
    lframe  = Bag.lframe+str(Bag.lframeNum)
    dest = Bag.dest+str(Bag.destNum)
    tlframe =  "Objects."+lframe+".TLabelframe"
    name = lframe+".TLabelframe"
    if Bag.prt == 1:
        print("   ", lframe,"->",dest,"    Style name:", name)
        print("                             label position:", Bag.position)
    exec(f"Objects.{lframe}=LabelFrame(Objects.{dest}, text=Bag.text, labelanchor=Bag.position, style = tlframe)")
    exec(f"Objects.{lframe}['style'] = tlframe")     
    exec(f"Objects.{lframe}.place(x={Bag.X1}, y={Bag.Y1}, width={Bag.X2}, height={Bag.Y2})")

#############################################################
def createCanvas():
    canv = Bag.canvas+str(Bag.canvasNum)
    dest = Bag.dest+str(Bag.destNum)
    if Bag.prt == 1: print("   ", canv,"->", dest)
    exec(f"Objects.{canv} = Canvas(Objects.{dest},width=Bag.X2,height=Bag.Y2, bg=Bag.color2,bd=Bag.Wbd,relief=GROOVE)")
    exec(f"Objects.{canv}.place(x=Bag.X1,y=Bag.Y1)")

#############################################################
def createLine0():  #obsolate
    line = Bag.line+str(Bag.lineNum)
    canv = Bag.canvas+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", line,"->", canv)
    dash = ""
    if Bag.Ld == 1:
        dash = ",dash=("+str(Bag.Ld1)+","+str(Bag.Ld2)+")"
    exec(f"Objects.{line}=Objects.{canv}.create_line(Bag.Coord,fill=Bag.color1,width=Bag.Lw{dash},arrow=Bag.arrow, arrowshape=Bag.arrowshape,capstyle=Bag.capstyle,tags=Bag.tags)")

def createLinesHorz():
    templine = Bag.line
    Bag.line = Bag.lineh
    Bag.lineNum = Bag.linehNum
    for x in range(0,Bag.Lnvert):
        Bag.Coord = [Bag.X1,Bag.Y1,Bag.X2,Bag.Y2]
        createLine()
        Bag.Y1  = Bag.Y1 + Bag.Yd
        Bag.Y2  = Bag.Y2 + Bag.Yd
        Bag.lineNum = Bag.lineNum + 1
    Bag.line = templine

def createLinesVert():
    templine = Bag.line
    Bag.line = Bag.linev
    Bag.lineNum = Bag.linehNum
    for y in range(0,Bag.Lnhorz):
        Bag.Coord = [Bag.X1,Bag.Y1,Bag.X2,Bag.Y2]
        createLine()
        Bag.X1  = Bag.X1 + Bag.Xd
        Bag.X2  = Bag.X2 + Bag.Xd
        Bag.lineNum = Bag.lineNum + 1
    Bag.line = templine
    
#############################################################
def createLine():
    line = Bag.line+str(Bag.lineNum)
    canv = Bag.canvas+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", line,"->", canv)
    dash = ""
    if Bag.Ld == 1:
        dash = ",dash=("+str(Bag.Ld1)+","+str(Bag.Ld2)+")"
    if Bag.lineset>0:
        l=len(Bag.Coord)*2   
        coord=[0]*l  
        dis=Bag.linestart  
        if Bag.lineset==1: 
            coord[0]=Bag.linestart
            coord[1]=Bag.Coord[0]
            c=3  #fillin place of coord
            d=2  #fillin place of dist
        else:
            coord[1]=Bag.linestart
            coord[0]=Bag.Coord[0]
            c=2  #fillin place of coord
            d=3  #fillin place of dist
        f=d      #fillin place
        while (f)<l:
            dis=dis+Bag.linedis
            coord[f]=dis
            f+=2
        f=c
        n=1
        while (f)<l:
            coord[f]=Bag.Coord[n]
            f+=2
            n+=1
        exec(f"Objects.{line}=Objects.{canv}.create_line(coord,fill=Bag.color1,width=Bag.Lw{dash},arrow=Bag.arrow, arrowshape=Bag.arrowshape,capstyle=Bag.capstyle,tags=Bag.tags)")
    else:
        exec(f"Objects.{line}=Objects.{canv}.create_line(Bag.Coord,fill=Bag.color1,width=Bag.Lw{dash},arrow=Bag.arrow, arrowshape=Bag.arrowshape,capstyle=Bag.capstyle,tags=Bag.tags)")

def createRectangle():
    rect = Bag.rect+str(Bag.rectNum)
    canv = Bag.canvas+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", rect,"->", canv)
    dash = ""
    if Bag.Ld == 1:
        dash = ",dash=("+str(Bag.Ld1)+","+str(Bag.Ld2)+")"
    exec(f"Objects.{rect}=Objects.{canv}.create_rectangle(Bag.X1,Bag.Y1,Bag.X2,Bag.Y2,outline=Bag.color1, fill=Bag.color2,width=Bag.Lw{dash},tags=Bag.tags)")

def createOval():
    oval = Bag.oval+str(Bag.ovalNum)
    canv = Bag.canvas+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", oval,"->", canv)
    dash = ""
    if Bag.Ld == 1:
        dash = ",dash=("+str(Bag.Ld1)+","+str(Bag.Ld2)+")"
    exec(f"Objects.{oval}=Objects.{canv}.create_oval(Bag.X1,Bag.Y1,Bag.X2,Bag.Y2,outline=Bag.color1, fill=Bag.color2,width=Bag.Lw{dash},tags=Bag.tags)")

def createArc():
    arc = Bag.arc+str(Bag.arcNum)
    canv = Bag.canvas+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", arc,"->", canv)
    dash = ""
    style = "ARC" 
    if Bag.ArcStyle == 0:
        style = "ARC"    
    if Bag.ArcStyle == 1:
        style = "PIESLICE"
    if Bag.ArcStyle == 2:
        style = "CHORD"
    if Bag.Ld == 1:
        dash = ",dash=("+str(Bag.Ld1)+","+str(Bag.Ld2)+")"
    Bag.Coord = [str(Bag.X1),str(Bag.Y1),str(Bag.X2),str(Bag.Y2)]
    exec(f"Objects.{arc}=Objects.{canv}.create_arc(Bag.Coord,fill=Bag.color2,width=Bag.Lw{dash}, start=Bag.ArcStart,extent=Bag.ArcExtend,outline=Bag.color1,style={style},tags=Bag.tags)")

#########################################
def changeFont():
    print("    style:",Bag.dest,"font=(",Bag.atribute,")")
    exec(f"Objects.style.configure(Bag.dest, {Bag.config}=({Bag.atribute}))")     
     
#########################################
def changeStyle():
    print("    style:",Bag.dest,",",Bag.config,"=",Bag.atribute)
    exec(f"Objects.style.configure(Bag.dest, {Bag.config}=Bag.atribute)")
   
#########################################
def changeMap():
    print("    map:  ",Bag.dest,",",Bag.config,"=",Bag.atribute)
    exec(f"Objects.style.map(Bag.dest, {Bag.config}={Bag.atribute})")
    
#########################################
def changeTheme():    
    a=0
    for l in Objects.style.theme_names():
        if a==Bag.themeNum: 
            Bag.theme = l
            Style().theme_use(l)
        a=a+1   
    if  Bag.themeNum > a:
        Bag.theme = "default"
        Style().theme_use("default")   
    print("    theme:",Bag.theme)
         
#########################################
def createLabel():
    label = Bag.label+str(Bag.labelNum)
    dest = Bag.dest+str(Bag.destNum)
    tlabel =  "Objects."+label+".TLabel"
    name = label+".TLabel"
    if Bag.prt == 1: print("   ", label,"->", dest,"    Style name:", name)
    exec(f"Objects.{label}=Label(Objects.{dest},text=Bag.text)")
    exec(f"Objects.{label}['style'] = tlabel")    
    exec(f"Objects.{label}.place(x={Bag.X1},y={Bag.Y1})")
   
#########################################
def createEntry():
    entry = Bag.entry+str(Bag.entryNum)
    dest = Bag.dest+str(Bag.destNum)
    tentry =  "Objects."+entry+".TEntry"
    name = entry+".TEntry"
    if Bag.prt == 1: print("   ", entry,"->", dest,"    Style name:", name)  
    var = StringVar()     
    if Bag.entryNum==Bag.fontNum:
        exec(f"Objects.{entry}=Entry(Objects.{dest}, show=Bag.show, font=(Bag.Fontfamily, Bag.Fontsize, Bag.Fontweight, Bag.Fontslant), textvariable = var, width=Bag.width1)")
        if Bag.prt == 1: print("    font", Bag.Fontfamily, Bag.Fontsize, Bag.Fontweight, Bag.Fontslant)
    else: 
        exec(f"Objects.{entry}=Entry(Objects.{dest}, show=Bag.show, textvariable = var, width=Bag.width1)")
    exec(f"Objects.{entry}['style'] = tentry")    
    exec(f"Objects.{entry}.place(x={Bag.X1},y={Bag.Y1})")    
    token=Bag.token
    num=Bag.entryNum  
# Next, a function() is generated on the fly. 
# After each \n comes an insertion each with the same number of spaces,
# as usual with a function().
    exec(f"def {entry}(b):\n  txt=Objects.{entry}.get()\n  tkn = {token}\n  enum = {num}\n  print(tkn,enum,txt)")      
    exec(f"Objects.{entry}.bind('<Return>',{entry})")

#########################################

def createSpinbox():
    spinbox = Bag.spinbox+str(Bag.spinboxNum)
    dest = Bag.dest+str(Bag.destNum)
    tspinbox =  "Objects."+spinbox+".TSpinbox"
    name = spinbox+".TSpinbox"
    if Bag.prt == 1: print("   ", spinbox,"->", dest,"    Style name:", name)
    font=""
    if Bag.spinboxNum==Bag.fontNum:
        font="font=('"+Bag.Fontfamily+"'," +str(Bag.Fontsize)+",'" +Bag.Fontweight +"','" +Bag.Fontslant +"'),"
        print("                     ",font)    
    var = StringVar()
    var.set(str(Bag.Sset))
    if Bag.Stype == '0':
        spin = Bag.text.split(" ")
        Bag.Sfrom      = float(spin[0])
        Bag.Sto        = float(spin[1])
        Bag.Sincrement = float(spin[2])
        Bag.Sformat    = spin[3]   
        exec(f"Objects.{spinbox} = Spinbox(Objects.{dest}, from_=Bag.Sfrom, to=Bag.Sto, increment=Bag.Sincrement, format=Bag.Sformat, width=Bag.width1, justify=Bag.Sjustify, {font} textvariable= var, command=partial(transmitCB, t=Bag.token, n=Bag.tokenNum, v=var))")   
    if Bag.Stype == '1':  
        exec(f"Objects.{spinbox} = Spinbox(Objects.{dest}, values=Bag.text, format=Bag.Sformat, width=Bag.width1, justify=Bag.Sjustify, {font} textvariable= var, command=partial(transmitCB, t=Bag.token, n=Bag.tokenNum, v=var))")       
    exec(f"Objects.{spinbox}['style'] = tspinbox")       
    exec(f"Objects.{spinbox}.place(x={Bag.X1},y={Bag.Y1})")      

#########################################
def createButton():
    button  = Bag.button+str(Bag.buttonNum)
    dest = Bag.dest+str(Bag.destNum)
    tbutton =  "Objects."+button+".TButton"
    name = button+".TButton"
    if Bag.prt == 1: print("   ", button,"->", dest,"    Style name:", name) 
    exec(f"Objects.{button} = Button(Objects.{dest}, text=Bag.text, command=partial(transmitB, t=Bag.token, n=Bag.tokenNum, v=0))")            
    exec(f"Objects.{button}['style'] = tbutton")    
    exec(f"Objects.{button}.place(x={Bag.X1},y={Bag.Y1})") 
# ttk, not supported: height, padx, pady


#########################################
def createRadioButton():
    rbutton  = Bag.rbutton+str(Bag.rbuttonNum)
    dest = Bag.dest+str(Bag.destNum)
    trbutton =  "Objects."+rbutton+".TRadiobutton"
    name = rbutton+".TRadiobutton"
    if Bag.prt == 1: print("   ", rbutton,"->", dest,"    Style name:", name)
    v=Bag.tokenNum 
    exec(f"Objects.{rbutton} = Radiobutton(Objects.{dest}, text=Bag.text, variable=Bag.tags, value=v,  command=partial(transmitB, t=Bag.token, n=Bag.tokenNum, v=v))")     
    exec(f"Objects.{rbutton}['style'] = trbutton")        
    exec(f"Objects.{rbutton}.place(x={Bag.X1},y={Bag.Y1})")

#########################################
def createCheckButton():
    cbutton  = Bag.cbutton+str(Bag.cbuttonNum)
    dest = Bag.dest+str(Bag.destNum)
    tcbutton =  "Objects."+cbutton+".TCheckbutton"
    name = cbutton+".TCheckbutton"
    if Bag.prt == 1: print("   ", cbutton,"->", dest,"    Style name:", name)
    var = IntVar()     
    exec(f"Objects.{cbutton} = Checkbutton(Objects.{dest}, text=Bag.text, variable=var, onvalue=1, offvalue=0 , command=partial(transmitCB, t=Bag.token,n=Bag.tokenNum,v=var))")     
    exec(f"Objects.{cbutton}['style'] = tcbutton")        
    exec(f"Objects.{cbutton}.place(x={Bag.X1},y={Bag.Y1})")

#########################################
def createMenuButton():   # ttk
    mbutton  = Bag.mbutton+str(Bag.mbuttonNum)
    dest = Bag.dest+str(Bag.destNum)
    menu = Bag.menu+str(Bag.menuNum)    
    tmbutton =  "Objects."+mbutton+".TMenubutton"
    name = mbutton+".TMenubutton"    
    if Bag.prt == 1: print("   ", mbutton,"->", dest,"    Style name:", name)
    exec(f"Objects.{mbutton} = Menubutton(Objects.{dest}, text=Bag.text)") 
    if Bag.prt == 1: print("   ", mbutton,"<- tk Menu options: ",Bag.menuconfig[2:]) 
    exec(f"Objects.{menu} = Menu(Objects.{mbutton} {Bag.menuconfig})")
    exec(f"Objects.{mbutton}['menu'] = Objects.{menu}")       
    exec(f"Objects.{mbutton}['style'] = tmbutton")        
    exec(f"Objects.{mbutton}.place(x={Bag.X1},y={Bag.Y1})") 

def menubutton_add_checkbutton():   # ttk
    var = IntVar()
    menu = Bag.menu+str(Bag.menuNum)
    mcbutton = Bag.mcbutton+str(Bag.mcbuttonNum)
    dest = Bag.dest+str(Bag.destNum)
    if Bag.prt == 1: print("   ", mcbutton,"->", dest) 
    exec(f"Objects.{menu}.add_checkbutton(label=Bag.text, variable=var, command=partial(transmitCB, Bag.token, Bag.mcbuttonNum, v=var))")
    
def menubutton_add_radiobutton():   # ttk
    menu = Bag.menu+str(Bag.menuNum)
    mrbutton = Bag.mrbutton+str(Bag.mrbuttonNum)
    dest = Bag.dest+str(Bag.destNum)
    if Bag.prt == 1: print("   ", mrbutton,"->", dest)
    v=Bag.mrbuttonNum    
    exec(f"Objects.{menu}.add_radiobutton(label=Bag.text, value=v, command=partial(transmitB, t=Bag.token, n=Bag.mrbuttonNum, v=v))")

#########################################
def scaleValues(t,n,r,v): # This a test function
    resolution="{: ."+str(r)+"f}"
    print (t, n, (resolution.format(float(v))), type(v))

def createScale():
    scale  = Bag.scale+str(Bag.scaleNum)
    dest = Bag.dest+str(Bag.destNum)
    if Bag.X2>Bag.Y2: 
        Bag.Sorient="horizontal"
        Bag.Slength=Bag.X2
        Bag.width1 =Bag.Y2
    else: 
        Bag.Sorient="vertical"
        Bag.Slength=Bag.Y2
        Bag.width1 =Bag.X2
 
    sc = Bag.text.split(" ")
    Bag.Stype       = int(sc[0])
    if Bag.Stype==1: Stype = "ttk"
    else: Stype = "tk"
    Bag.Sshowvalue  = int(sc[1])
    Bag.Sinterval   = float(sc[2])
    Bag.Sfrom       = float(sc[3])
    Bag.Sto         = float(sc[4])
    Bag.Sset        = float(sc[5])
    Bag.Sresolution = int(sc[6])
    if Bag.prt == 1: print("   ", scale,"->", dest," ",Stype,"  from",Bag.Sfrom," to",Bag.Sto," resolution",10**(-Bag.Sresolution)," ",Bag.Sorient)
    
    if Bag.Stype==1:                
        exec(f"Objects.{scale} = Scale(Objects.{dest}, from_=Bag.Sfrom, to=Bag.Sto, length=Bag.Slength, orient=Bag.Sorient, command=partial(transmitS, Bag.token, Bag.tokenNum, Bag.Sresolution))")             
        tscale =  "Objects."+scale+".Vertical.TScale"
        name = scale+".TScale"
        if Bag.prt == 1: print("                        Style name:", name)
        exec(f"Objects.{scale}['style'] = tscale")   
    else:
        resolution = 10**(-Bag.Sresolution) 
        exec(f"Objects.{scale} = tk.Scale(Objects.{dest}, from_=Bag.Sfrom, to=Bag.Sto, resolution=resolution, length=Bag.Slength, orient=Bag.Sorient, tickinterval=Bag.Sinterval,  showvalue=Bag.Sshowvalue {Bag.scaleconfig}, command=partial(transmitS, Bag.token, Bag.tokenNum, Bag.Sresolution))")  
    exec(f"Objects.{scale}.place(x={Bag.X1},y={Bag.Y1})")
 
#########################################
def createMenubar():   # tk
    mbar = Bag.menubar+str(Bag.menubarNum)
    dest = Bag.dest+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", mbar,"->", dest)
    if Bag.prt == 1: print("    - menubar config: ",Bag.menuconfig)
# Menubar is not part of ttk- tkinter.
# colors works well in Linux but not in windows.
    exec(f"Objects.{mbar} = Menu(Objects.{dest} {Bag.menuconfig})")
    exec(f"Objects.{dest}.config(menu=Objects.{mbar})")
    barmenus = Bag.text.split(",")
    for x in barmenus:
        barmenu = Bag.barmenu+str(Bag.barmenuNum)
        Bag.barmenuNum = Bag.barmenuNum + 1
        exec(f"Objects.{barmenu}=Menu(Objects.{mbar} {Bag.menuconfig2})")
        exec(f"Objects.{mbar}.add_cascade(label='{x}', menu=Objects.{barmenu})")
        if Bag.prt == 1: print("   ", barmenu,"->",mbar)
        if Bag.prt == 1: print("    - barmenu config:",Bag.menuconfig2)
 
def barmenu_add_submenu():   # tk
    submenu = Bag.submenu+str(Bag.submenuNum)
    dest = Bag.dest+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", submenu,"->", dest)
    if Bag.prt == 1: print("    - submenu config:",Bag.menuconfig2)
    exec(f"Objects.{submenu} = Menu(Objects.{dest} {Bag.menuconfig2})")
    exec(f"Objects.{dest}.add_cascade(label=Bag.text, menu=Objects.{submenu})")

def barmenu_add_command():   # tk
    bmc = Bag.bmcommand + str(Bag.bmcommandNum)
    dest = Bag.dest+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", bmc,"->", dest)
    if Bag.prt == 1: print("    - command config:",Bag.menuconfig3)
    exec(f"Objects.{dest}.add_command(label=Bag.text {Bag.menuconfig3}, command=partial(transmitB, Bag.token, Bag.tokenNum, 0))")

def barmenu_add_radiobutton():    # tk
    var = IntVar()
    bmr = Bag.bmradio + str(Bag.bmradioNum)
    dest = Bag.dest+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", bmr,"->", dest) 
    if Bag.prt == 1: print("    - radiobutton config:",Bag.menuconfig3)
    exec(f"Objects.{dest}.add_radiobutton(label=Bag.text {Bag.menuconfig3}, indicatoron=Bag.indon, variable=Bag.tags, value=var, command=partial(transmitB, Bag.token, Bag.tokenNum, 0))")

def barmenu_add_checkbutton():   # tk
    var = IntVar()
    bmc = Bag.bmcheck + str(Bag.bmcheckNum)
    dest = Bag.dest+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", bmc,"->", dest) 
    if Bag.prt == 1: print("    - checkbutton config:",Bag.menuconfig3)
    exec(f"Objects.{dest}.add_checkbutton(label=Bag.text {Bag.menuconfig3}, variable=var, indicatoron=Bag.indon, command=partial(transmitCB, Bag.token, Bag.tokenNum, v=var))")
    
def barmenu_add_separator():   # tk
    bms = Bag.bmsep + str(Bag.bmsepNum)
    dest = Bag.dest+str(Bag.destNum) 
    if Bag.prt == 1: print("   ", bms,"->", dest)
    exec(f"Objects.{dest}.add_separator()")
    
def tags2delete():
    name = "Objects.Canvas" + str(Bag.canvasNum)+ ".delete('"+Bag.tags+"')"
#    if Bag.prt == 1: print("   delete tag:",Bag.tags)
    exec(name)
#    print("   delete tags",Bag.token, Bag.tokenNum)



def transmitB(t,n,v): # buttons 
    Bag.transmit="1 "+str(t)+" "+str(n)+" "+str(v)
    if (Bag.prt == 1): print (Bag.transmit)
    
def transmitCB(t,n,v): #  checkbutton 
    Bag.transmit="1 "+str(t)+" "+str(n)+" "+str(v.get())
    if (Bag.prt == 1): print (Bag.transmit)
    
def transmitS(t,n,r,v): # scale / slider
    resolution="{: ."+str(r)+"f}"
    Bag.transmit="3 "+str(t)+" "+str(n)+" "+str(resolution.format(float(v)))
    if (Bag.prt == 1): print (Bag.transmit)

#########################################
def messageboxInfo():
    if Bag.prt == 1: print("    - info -")
    v=messagebox.showinfo("info", Bag.text)
    transmitB(Bag.token,Bag.tokenNum,1)

def messageboxWarning():
    if Bag.prt == 1: print("    - warning -")
    v=messagebox.showwarning("warning", Bag.text)
    transmitB(Bag.token,Bag.tokenNum,1)

def messageboxError():
    if Bag.prt == 1: print("    - error -")
    v=messagebox.showerror("error", Bag.text) 
    transmitB(Bag.token,Bag.tokenNum,1)

def messageboxQuestion():
    if Bag.prt == 1: print("    - question -")
    v=messagebox.askquestion("question", Bag.text)  
    if v=="yes": transmitB(Bag.token,Bag.tokenNum,1)
    else :       transmitB(Bag.token,Bag.tokenNum,0)

def messageboxOkCancel():
    if Bag.prt == 1: print("    - ok | cancel -")
    v=messagebox.askokcancel("ok or cancel", Bag.text) 
    if v==True:  transmitB(Bag.token,Bag.tokenNum,1)
    else :       transmitB(Bag.token,Bag.tokenNum,0)

def messageboxYesNo():
    if Bag.prt == 1: print("    - yes | no- ")
    v=messagebox.askyesno("yes or no", Bag.text) 
    if v==True:  transmitB(Bag.token,Bag.tokenNum,1)
    else :       transmitB(Bag.token,Bag.tokenNum,0)

def messageboxRetryCancel():
    if Bag.prt == 1: print("    - retry | cancel -")
    v=messagebox.askretrycancel("retry or cancel", Bag.text) 
    if v==True:  transmitB(Bag.token,Bag.tokenNum,1)
    else :       transmitB(Bag.token,Bag.tokenNum,0)



print("")
createRoot()
root  = Bag.root+"0"
exec(f"Objects.{root}.mainloop()")





