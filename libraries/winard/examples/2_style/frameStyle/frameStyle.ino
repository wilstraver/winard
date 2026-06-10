#include <winard.h>

void setup( )  
{ Serial.begin(115200);
  startup();
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1);  
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);
  tx_08(FRAME,1,ROOT,0,50,20,140,100);
  tx_str(TEXT,"frame");
  tx_06(LABEL,4,FRAME,1,20,25); 
  tx_04(CFG, 255,0,0);
  tx_05(STYLE,0,LABEL,4,CFG);   
  tx_10(FONT,0,LABEL,4,1,14,1,1,1,0);
  tx_str(TEXT,"without label");
  tx_06(LABEL,5,FRAME,1,20,45); 
  tx_04(CBG, 220,220,255);   
  tx_05(STYLE,0,FRAME,1,CBG); 
  tx_05(STYLE,0,LABEL,4,CBG);
  tx_05(STYLE,0,LABEL,5,CBG);
  tx_02(RELIEF1,2);
// 0 flat, 1 groove, 2 raised,
// 3 ridge, 4 solid, 5 sunken  
  tx_05(STYLE,0,FRAME,1,RELIEF1);
  tx_02(BORDERWIDTH,3);
  tx_05(STYLE,0,FRAME,1,BORDERWIDTH);
  
  tx_02(PRINTOBJECTS,1);
}
