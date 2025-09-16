
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
  tx_str(TEXT,"select"); 
  tx_06(MBUTTON,2,ROOT,0,80,20);
  tx_str(TEXT,"check");
  tx_04(MCBUTTON,3,MBUTTON,2);  
  tx_str(TEXT,"radio1");
  tx_04(MRBUTTON,5,MBUTTON,2);
  tx_str(TEXT,"radio2");
  tx_04(MRBUTTON,6,MBUTTON,2);
  tx_02(PRINTOBJECTS,1);
}
