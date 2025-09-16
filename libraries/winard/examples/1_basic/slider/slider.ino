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

  tx_str(TEXT,"0 1 4.0 -10.0 10.0 2.0 1");
  tx_08(SCALE,18,ROOT,0,10,50,150,12);
  tx_str(TEXT,"tk version");
  tx_06(LABEL,1,ROOT,0,10,40);

  tx_str(TEXT,"1 1 2.0 20.0 -20.0 2.0 2");
  tx_08(SCALE,19,ROOT,0,200,10,0,150);
  tx_str(TEXT,"ttk version");
  tx_06(LABEL,1,ROOT,0,130,10);
  
  tx_02(PRINTOBJECTS,1); 
}
