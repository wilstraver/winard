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
  tx_str(TEXT,"A,B,C"); 
  tx_02(POSITION,5);
  tx_08(NOTEBOOK,1,ROOT,0,15,5,200,140);
  tx_str(TEXT,"this is tab A"); 
  tx_06(LABEL,4,TAB,0,40,35);   
  tx_str(TEXT,"this is tab B"); 
  tx_06(LABEL,5,TAB,1,40,55);   
  tx_str(TEXT,"this is tab C"); 
  tx_06(LABEL,6,TAB,2,40,75);
  tx_02(PRINTOBJECTS,1); 
}
