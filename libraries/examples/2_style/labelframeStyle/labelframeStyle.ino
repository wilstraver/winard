

#include <winard.h>

void setup( )  
{ Serial.begin(115200);
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1);  
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);
  
  tx_str(TEXT,"label");
  tx_02(POSITION,2);
  tx_08(LABELFRAME,1,ROOT,0,30,10,180,130);
  tx_04(CBG, 220,255,220);   
  tx_05(STYLE,1,LABELFRAME,1,CBG);
//           /--- 1 directs to the label  
  tx_10(FONT,1,LABELFRAME,1,1,12,0,1,0,0);
  tx_02(RELIEF1,2);
// 0 flat, 1 groove, 2 raised,
// 3 ridge, 4 solid, 5 sunken  
  tx_05(STYLE,0,LABELFRAME,1,RELIEF1);
  tx_02(BORDERWIDTH,3);
  tx_05(STYLE,0,LABELFRAME,1,BORDERWIDTH);
  
  tx_str(TEXT,"frame");
  tx_06(LABEL,4,LABELFRAME,1,40,25); 
  tx_str(TEXT,"with label");
  tx_06(LABEL,5,LABELFRAME,1,40,45); 
  tx_05(STYLE,0,LABELFRAME,1,CBG); 
  tx_05(STYLE,0,LABEL,4,CBG);
  tx_05(STYLE,0,LABEL,5,CBG);
  
  tx_02(PRINTOBJECTS,1);
}
