
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
  tx_06(BUTTON,6,ROOT,0,70,20);
  tx_10(FONT,0,BUTTON,6,0,16,0,1,0,0);
  
  tx_str(TAGS,"rb"); 
  tx_str(TEXT,"radiobutton1");
  tx_06(RBUTTON,7,ROOT,0,60,60);
  tx_10(FONT,0,RBUTTON,7,1,12,1,0,0,0);
  
  tx_str(TEXT,"radiobutton2");
  tx_06(RBUTTON,8,ROOT,0,60,85);
  tx_10(FONT,0,RBUTTON,8,2,12,0,1,1,0);
  
  tx_str(TEXT,"checkbutton");
  tx_06(CBUTTON,9,ROOT,0,60,110);
  tx_10(FONT,0,CBUTTON,9,3,8,0,0,0,1);
  
  tx_02(PRINTOBJECTS,1);
}
