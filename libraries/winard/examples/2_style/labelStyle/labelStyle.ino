
#include <winard.h>

void setup() 
{ Serial.begin(115200);
  startup();
  build_up();
}

void loop() {;}

void build_up()   
{ tx_02(PRINTBUILD,1);  
  tx_str(TEXT,"Winard");    
  tx_04(ROOT,0,240,160);  
  
  tx_str(TEXT,"Build up with Tkinter"); 
  tx_06(LABEL,3,ROOT,0,20,25);  
  tx_10(FONT,0,LABEL,3,1,16,0,1,0,0);
  tx_04(CFG, RED);   //color foreground
  tx_05(STYLE,0,LABEL,3,CFG);
 
  tx_06(LABEL,4,ROOT,0,20,65);  
  tx_10(FONT,0,LABEL,4,0,12,0,0,1,0);
  tx_05(STYLE,0,LABEL,4,CFG);
  tx_04(CBG, GREEN); //color background
  tx_05(STYLE,0,LABEL,4,CBG);
  
  tx_02(PRINTOBJECTS,1);  
}
