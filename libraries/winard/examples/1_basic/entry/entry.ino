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

  tx_02(WIDTH,16);
  tx_06(ENTRY,3,ROOT,0,60,30);
  
  tx_str(SHOW,"#");
  tx_06(ENTRY,14,ROOT,0,60,70);

  tx_02(PRINTOBJECTS,1);  
}
