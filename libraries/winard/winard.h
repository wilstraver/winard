
# define SET            1  
# define TEXT           2  
# define TAGS           3 
# define SHOW           4  
# define SPINBOXSET     5 
# define TAGSDEL        6  

# define COORD          8
# define COORDAPPEND    9
# define LINEAPPEND     9
# define COORDREPLACE  10 
# define LINEREPLACE   10
# define NEWLINE       11

# define SETLINE       13
# define LINE          14    
# define HLINES        15 
# define VLINES        16   
# define RECT          17 
# define OVAL          18 
# define ARC           19  

# define LABEL         24 
# define BUTTON        25 
# define RBUTTON       26 
# define CBUTTON       27 
# define SCALE         28 
# define SLIDER        28 
# define SPINBOX       29 
# define ENTRY         30 
# define LISTBOX       31
# define SELECT        32  //rbutton
# define UNSELECT      33  //rbutton

# define FRAME         36 
# define LABELFRAME    37 
# define CANVAS        38 
# define NOTEBOOK      39 
# define TAB           40  //?????
# define ROOT          41 
# define TOPLEVEL      42 
# define SEPARATOR     43 
# define CANVASSELECT  44 

# define MBUTTON       48
# define MCBUTTON      49
# define MRBUTTON      50
# define MENUBAR       51
# define BARMENU       52
# define BMCOMMAND     53
# define BMRADIO       54
# define BMCHECK       55
# define BMSEPARATOR   56
# define SUBMENU       57
# define ROOTCONFIG    58
# define INDON         59
# define TEAR          60
# define MENUOPTIONS   61
# define MENUOPTIONS2  62

# define SCALEOPTIONS  64
# define LINEWIDTH     65
# define DASH          66
# define ARROW         67
# define ARROWS        68
# define NLINES        69
# define ARCSHAPE      70  //
# define RELIEF        71  // flat, groove, raised, ridge, solid, sunken
# define RELIEF1       71
# define RELIEFTROUGH  72 
# define RELIEF2       73 
# define RELIEFSLIDER  73 

# define FONT          80
# define POSITION      82
# define WIDTH         83
# define WIDTH1        83
# define SLIDERWIDTH   83
# define WIDTH2        84
# define BORDERWIDTH   84
# define WIDTH3        85
# define RELIEFWIDTH   85

# define COLOR1        88   // foreground  CFG
# define CFG           88   // Style Map foreground color1
# define COLOR2        89   // background  CBG  CSLIDER
# define CBG           89   // Style Map background color2
# define CSLIDER       89   // slider               color2
# define COLOR3        90   // CACTIVE_FG
# define CAFG          90   // active               color3
# define CACTIVE_FG    90   //       Map
# define COLOR4        91   // CACTIVE_BG
# define CABG          91   // active               color4
# define CACTIVE_BG    91   //       Map
# define COLOR5        92   // CSELECT     CINDICATOR
# define CPFG          92   // press       
# define CSELECT_FG    92   // select,  color7,    color5
# define CSELECT       92   //       Map selected   color5
# define CINDICATOR    92  
# define CIND          92  
# define COLOR6        93   // CNSELECT
# define CPBG          93   // press                color6
# define CSBG          93   // select               color8
# define CSELECT_BG    93 
# define CNSELECT      93   //       Map !selected  color6
# define COLOR7        94 
# define COLOR8        95   // CLIGHT
# define CLIGHT        95   // 27-04-2025
# define COLOR9        96   // CDARK
# define CNSFG         96   // press                color9
# define CDARK         96   // 27-04-2025
# define COLOR10       97 
# define CFIELD_BG     97 
# define COLOR11       98  indicator
# define COLOR12       99 
# define CSELECTED     99 
# define COLOR13      100 
# define CHL          100  // highlightcolor
# define COLOR14      101 
# define CHLBG        101  // highlightbackground
# define COLOR15      102 
# define COLOR16      103   // troughcolor  CTROUGH
# define CTROUGH      103   // scale troughcolor
# define PRINTOBJECTS 104
# define PRINTBUILD   105
# define STYLE        106
# define THEMESTYLE   107
# define MAP          108
# define THEME        109

# define MBOXINFO     112         
# define MBOXWARNING  113 
# define MBOXERROR    114 
# define MBOXQUESTION 115 
# define MBOXOKCANCEL 116 
# define MBOXYESNO    117 
# define MBOXRETRYCANCEL 118 

# define START        128

# define RED          255,0,0
# define GREEN        0,255,0
# define BLUE         0,0,255
# define YELLOW       255,255,0
# define CYAN         0,255,255
# define MAGENTA      255,0,255
# define ORANGE       255,130,0
# define LIME         180,255,70
# define BLACK        0,0,0
# define WHITE        255,255,255
# define PURPLE       150,150,250


char print_str[64];

void tx_02(int a,int b)
{ sprintf(print_str,"%d,%d,",a,b);
  Serial.println(print_str);
}

void tx_03(int a,int b,int c)
{ sprintf(print_str,"%d,%d,%d,",a,b,c);
  Serial.println(print_str); 
}

void tx_04(int a,int b,int c,int d)
{ sprintf(print_str,"%d,%d,%d,%d,",a,b,c,d);
  Serial.println(print_str);
}

void tx_05(int a,int b,int c,int d,int e)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,",a,b,c,d,e);
  Serial.println(print_str); 
}

void tx_06(int a,int b,int c,int d, int e,int f)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,",a,b,c,d,e,f);
  Serial.println(print_str); 
}

void tx_07(int a,int b,int c,int d,int e, int f,int g)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,%d,", a,b,c,d,e,f,g);
  Serial.println(print_str);  
}

void tx_08(int a,int b,int c,int d,int e,int f, int g,int h)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,%d,%d,", a,b,c,d,e,f,g,h);
  Serial.println(print_str);  
}

void tx_09(int a,int b,int c,int d,int e,int f, int g,int h,int i)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,%d,%d,%d,", a,b,c,d,e,f,g,h,i);
  Serial.println(print_str);  
}

void tx_10(int a,int b,int c,int d,int e,int f,int g, int h,int i,int j)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,", a,b,c,d,e,f,g,h,i,j);
  Serial.println(print_str);  
}

void tx_11(int a,int b,int c,int d,int e,int f,int g,int h, int i,int j,int k)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,", a,b,c,d,e,f,g,h,i,j,k);
  Serial.println(print_str);  
}

void tx_12(int a,int b,int c,int d,int e,int f,int g,int h, int i,int j,int k,int l)
{ sprintf(print_str,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,", a,b,c,d,e,f,g,h,i,j,k,l);
  Serial.println(print_str);  
}

void tx_str(int a,const char *str)
{ sprintf(print_str,"%d,%s", a,str);
  Serial.println(print_str);  
}

String str1;
char   str2[64];  

struct bag
{ int i1=0, i2=0, i3=0, i4=0;
  float fl;
  char str[64];
} Bag;  

void readcode()
{ int a=0, len;
  Bag.i1=0, Bag.i2=0, Bag.i3=0, Bag.i4=0;
  if (Serial.available());
  { str1=Serial.readString();
    for (a=0; a<64; a++) str2[a]=str1[a];
    sscanf(str2,"%d", &Bag.i1);
    switch(Bag.i1)
    { case 1: sscanf(str2,"%d%d%d%d",&Bag.i1,&Bag.i2,&Bag.i3,&Bag.i4);break;
      case 2: sscanf(str2,"%d%d%d%s",&Bag.i1,&Bag.i2,&Bag.i3,&Bag.str);break; 
      case 3: sscanf(str2,"%d%d%d%s",&Bag.i1,&Bag.i2,&Bag.i3,&Bag.str);
              Bag.fl=atof(Bag.str);
              Bag.i4=Bag.fl; break;   
    }
  }
}

void startup()
{ Bag.i1 = 0;
  while (Bag.i1 != 128)
  { tx_02(128,128);
    readcode();  
  }
}









  

