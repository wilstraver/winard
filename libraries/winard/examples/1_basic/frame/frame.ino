

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
  tx_str(TEXT,"without label");
  tx_06(LABEL,5,FRAME,1,20,45); 
  tx_02(RELIEF,1);
  tx_05(STYLE,0,FRAME,1,RELIEF);
  tx_02(BORDERWIDTH,2);
  tx_05(STYLE,0,FRAME,1,BORDERWIDTH);
  
  tx_02(PRINTOBJECTS,1);
}
