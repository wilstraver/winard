
#include <winard.h>

void setup( )  
{ Serial.begin(115200); 
  startup();  
  build_up();
}

void loop( ) {;}

void build_up()
{ tx_02(PRINTBUILD,1);

  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,320,240);

  tx_str(TEXT,"root");
  tx_06(LABEL,0,ROOT,0,60,25);
  
  tx_02(PRINTOBJECTS,1);
}
