#include <winard.h>
int buf[64];

void setup( )  
{ Serial.begin(115200);
  Serial.setTimeout(50);
  build_up();
}

void loop() 
{ readcode();
  if (Bag.i2==26)
  { switch(Bag.i3)
    { case 1: tx_04(CFG,255,0,0);break;
      case 2: tx_04(CFG,255,255,0);break;
      case 3: tx_04(CFG,0,255,0);break;
      case 4: tx_04(CFG,0,255,255);break;
      case 5: tx_04(CFG,0,0,255);break;
      case 6: tx_04(CFG,255,0,255);break;
      case 7: tx_04(CFG,255,255,255);break;      
    }
  }
  if (Bag.i2==25)
  { switch(Bag.i3)
    { case 1: tx_str(TAGS,"func1"); funcsin(); break;
      case 2: tx_str(TAGS,"func2"); funcsquare(); break;
      case 3: tx_str(TAGS,"func3"); functriangle(); break;
      case 4: tx_str(TAGSDEL,"func1"); ; break;
      case 5: tx_str(TAGSDEL,"func2"); ; break;
      case 6: tx_str(TAGSDEL,"func3"); ; break;
    }
  }
}

void funcsin()
{ int a=0;
  tx_04(SETLINE,1,10,6);
//              |  | |_fix.distances X/Y dir.
//              |  |___startvalue X or Y
//              |_=0 line with X,Y amplitudes
//              |_=1 line, only  Y amplitudes
//              |_=2 line, only  X amplitudes 
  tx_02(COORD,(int) (50.0*sin(PI * a++/15)+70.0)); 
  while (a<31) {tx_02(COORDAPPEND,(int)(50.0*sin(PI * a++/15)+70.0));}
  tx_04(NEWLINE,7,CANVAS,1);
}
void funcsquare()
{ tx_04(SETLINE,0,10,6);
  tx_11(COORD,10,100,10,40,55,40,55,100,100,100);
  tx_11(COORDAPPEND,100,40,145,40,145,100,190,100,190,40);
  tx_04(NEWLINE,8,CANVAS,1);
}
void functriangle()
{ tx_04(SETLINE,1,10,45);
  tx_06(COORD,100,40,100,40,100);
  tx_04(NEWLINE,9,CANVAS,1);
}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,1,320,240);  
  
  tx_02(WIDTH,8);
  tx_05(THEMESTYLE,0,RBUTTON,0,WIDTH);
  
  tx_str(TAGS,"rb");
  tx_str(TEXT,"red     ");
  tx_06(RBUTTON,1,ROOT,0,230,20);
  tx_04(CBG,255,0,0);
  tx_05(STYLE,0,RBUTTON,1,CBG);
  tx_str(TEXT,"yellow     ");
  tx_06(RBUTTON,2,ROOT,0,230,50);
  tx_04(CBG,255,255,0);
  tx_05(STYLE,0,RBUTTON,2,CBG);
  tx_str(TEXT,"green");
  tx_06(RBUTTON,3,ROOT,0,230,80);
  tx_04(CBG,0,255,0);
  tx_05(STYLE,0,RBUTTON,3,CBG);
  tx_str(TEXT,"cyan");
  tx_06(RBUTTON,4,ROOT,0,230,110);
  tx_04(CBG,0,255,255);
  tx_05(STYLE,0,RBUTTON,4,CFG);
  tx_05(STYLE,0,RBUTTON,4,CBG);
  tx_str(TEXT,"blue   ");
  tx_06(RBUTTON,5,ROOT,0,230,140);
  tx_04(CFG,255,255,255);
  tx_04(CBG,0,0,255);
  tx_05(STYLE,0,RBUTTON,5,CFG);
  tx_05(STYLE,0,RBUTTON,5,CBG);
  tx_str(TEXT,"magenta");
  tx_06(RBUTTON,6,ROOT,0,230,170);
  tx_04(CBG,255,0,255);
  tx_05(STYLE,0,RBUTTON,6,CBG);
  tx_str(TEXT,"white");
  tx_06(RBUTTON,7,ROOT,0,230,200);
  tx_04(CBG,255,255,255);
  tx_05(STYLE,0,RBUTTON,7,CBG);

  tx_str(TEXT,"sinus");
  tx_06(BUTTON,1,ROOT,0,10,160);
  tx_str(TEXT,"square");
  tx_06(BUTTON,2,ROOT,0,80,160);
  tx_str(TEXT,"triangle");
  tx_06(BUTTON,3,ROOT,0,150,160);
  tx_str(TEXT,"delete");
  tx_06(BUTTON,4,ROOT,0,10,190);
  tx_str(TEXT,"delete");
  tx_06(BUTTON,5,ROOT,0,80,190);
  tx_str(TEXT,"delete");
  tx_06(BUTTON,6,ROOT,0,150,190);

  tx_02(WIDTH,6);
  tx_05(THEMESTYLE,0,BUTTON,0,WIDTH);
//  tx_10(FONT,0,THEMESTYLE,0,1,10,0,0,0,0);

  tx_10(FONT,0,SET,0,2,10,0,1,0,0);
  tx_05(THEMESTYLE,0,RBUTTON,0,FONT);

//  tx_10(FONT,0,SET,0,2,10,0,1,1,0);
//  tx_05(THEMESTYLE,0,BUTTON,0,FONT);
  
//  tx_10(FONT,0,BUTTON,6,0,16,0,1,0,0); only button 6
//  _/tx_10(FONT,0,SET,0,2,12,0,1,1,0); \_ together
//   \tx_05(THEMESTYLE,0,BUTTON,0,FONT);/
//  tx_10(FONT,0,THEMESTYLE,0,2,8,0,1,0,0); the whole theme
//
  
  tx_04(CFG,255,255,255);
  tx_04(CBG,0,0,0);
  tx_08(CANVAS,1,ROOT,0,10,10,200,140);
  tx_05(NLINES,7,10,20,20);
  tx_04(CFG,120,120,0);
  tx_02(LINEWIDTH,1);
  tx_04(DASH,1,2,2);
  tx_08(VLINES,3,CANVAS,1,10,10,10,130);
  tx_08(HLINES,3,CANVAS,1,10,10,190,10);  
  tx_04(CFG,255,255,255); 
  tx_04(DASH,0,8,8); 
  tx_02(LINEWIDTH,2);  

  tx_02(PRINTOBJECTS,1); 
//  tx_02(PRINTBUILD,0); 
}
