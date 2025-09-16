

#include <winard.h>

void setup( )  
{ Serial.begin(115200);
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1);  
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,180);
  tx_str(TEXT,"label");
  tx_02(POSITION,6);
  tx_08(LABELFRAME,1,ROOT,0,45,15,150,150);
  tx_str(TEXT,"frame with label");
  tx_06(LABEL,5,LABELFRAME,1,20,35); 
  tx_02(PRINTOBJECTS,1);
}
