
#include <winard.h>
  
void setup( )  
{ Serial.begin(115200);
  build_up();
}

void loop( ) {;}

void build_up()
{ tx_02(PRINTBUILD,1);  
  tx_str(TEXT,"winard"); 
  tx_04(ROOT,0,240,160);

  tx_04(CBG,192,192,0);  
  tx_05(STYLE,0,ROOT,0,CBG);
  
  tx_08(SEPARATOR,1,ROOT,0,100,70,138,1);
  tx_08(SEPARATOR,1,ROOT,0,100,130,138,2);
  tx_08(SEPARATOR,1,ROOT,0,100,140,138,4);
  tx_08(SEPARATOR,1,ROOT,0,100,150,138,8);
  tx_08(SEPARATOR,2,ROOT,0,100,2,2,156); 

  tx_02(PRINTOBJECTS,1); 
}
