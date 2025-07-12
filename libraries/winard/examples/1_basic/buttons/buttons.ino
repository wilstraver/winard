
#include <winard.h>
  
void setup( )  
{ Serial.begin(115200);   
  build_up();
}

void loop( ) {;}

void build_up()
{ tx_02(PRINTBUILD,1);
  tx_str(TEXT,"Winard"); 
  tx_04(ROOT,0,240,160);
  tx_str(TEXT,"button");
  tx_06(BUTTON,6,ROOT,0,80,20);
  tx_str(TEXT,"radiobutton1");
  tx_06(RBUTTON,7,ROOT,0,70,60);
  tx_str(TEXT,"radiobutton2");
  tx_06(RBUTTON,8,ROOT,0,70,85);
  tx_str(TEXT,"checkbutton");
  tx_06(CBUTTON,9,ROOT,0,70,110);
  tx_02(PRINTOBJECTS,1);
}
