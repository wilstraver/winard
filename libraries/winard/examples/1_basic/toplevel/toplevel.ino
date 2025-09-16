
#include <winard.h>

void setup( )  
{ Serial.begin(115200);   
  build_up();
}

void loop( ) {;}

void build_up()
{ tx_02(PRINTBUILD,1);

  tx_str(TEXT,"Winard 0");
  tx_04(ROOT,0,240,160);
  
  tx_str(TEXT,"Winard 1");
  tx_04(TOPLEVEL,1,240,160);
  
  tx_str(TEXT,"Winard 2");
  tx_04(TOPLEVEL,2,240,160);

  tx_str(TEXT,"root");
  tx_06(LABEL,0,ROOT,0,60,25);
  
  tx_str(TEXT,"toplevel 1");
  tx_06(LABEL,1,TOPLEVEL,1,60,25);
  
  tx_str(TEXT,"toplevel 2");
  tx_06(LABEL,2,TOPLEVEL,2,60,25);
  
  tx_02(PRINTOBJECTS,1);
}
