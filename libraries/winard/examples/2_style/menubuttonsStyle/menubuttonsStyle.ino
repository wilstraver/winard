
#include <winard.h>

void setup( )  
{ Serial.begin(115200); 
  the_build();
}

void loop() {;}

void the_build()
{ tx_02(PRINTBUILD,1);
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);   

  tx_04(CFG,255,0,0);  
  tx_04(CBG,0,255,0);
  tx_04(CSELECT_FG,0,0,255); 
  tx_04(CAFG,255,255,0); 
  tx_04(CABG,0,255,255);
  tx_10(FONT,0,SET,0,1,12,0,0,1,0); 
  tx_08(MENUOPTIONS,1,1,1,1,1,1,1);
//                  1 2 3 4 5 6 7
// 1-tear 2-font 3-foreground 4-background
// 5-activeforeground 6-activebackground
// 7-selectcolor
  tx_str(TEXT,"select"); 
  tx_06(MBUTTON,2,ROOT,0,80,20);
  
  tx_04(CBG,220,220,255);
  tx_05(STYLE,0,MBUTTON,2,CBG); 
  tx_04(CFG,200,0,0);
  tx_05(STYLE,0,MBUTTON,2,CFG); 
  tx_10(FONT,0,MBUTTON,2,1,14,0,1,0,0); 
  
  tx_str(TEXT,"check");
  tx_04(MCBUTTON,3,MBUTTON,2);  
  tx_str(TEXT,"radio1");
  tx_04(MRBUTTON,5,MBUTTON,2);
  tx_str(TEXT,"radio2");
  tx_04(MRBUTTON,6,MBUTTON,2);
  tx_10(FONT,1,MRBUTTON,6,1,14,0,0,1,0); 
  
  tx_02(PRINTOBJECTS,1);
}
