
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
  tx_04(ROOT,0,240,160);               
  
  tx_str(TEXT,"button");       
  tx_06(BUTTON,16,ROOT,0,80,20); 
  tx_04(CFG,255,0,0); 
  tx_05(STYLE,0,BUTTON,16,CFG);
  tx_04(CBG,0,255,255);   
  tx_05(STYLE,0,BUTTON,16,CBG);

  tx_03(SELECT,RBUTTON,17);
 // tx_str(TAGS,"rb"); 
  tx_str(TEXT,"radiobutton1"); 
  tx_06(RBUTTON,17,ROOT,0,70,60); 
  tx_04(CFG,0,0,255); 
  tx_05(STYLE,0,RBUTTON,17,CFG);
  tx_04(CBG,255,255,0);   
  tx_05(STYLE,0,RBUTTON,17,CBG);
  
  tx_str(TEXT,"radiobutton2"); 
  tx_06(RBUTTON,18,ROOT,0,70,85); 
  tx_04(CFG,255,0,0); 
  tx_05(STYLE,0,RBUTTON,18,CFG);
  tx_04(CBG,0,255,0);   
  tx_05(STYLE,0,RBUTTON,18,CBG);
  
  tx_str(TEXT,"checkbutton  ");
  tx_06(CBUTTON,19,ROOT,0,70,110);
  tx_04(CFG,0,0,0); 
  tx_05(STYLE,0,CBUTTON,19,CFG);
  tx_04(CBG,255,0,255);   
  tx_05(STYLE,0,CBUTTON,19,CBG);

  tx_02(PRINTOBJECTS,1);
  tx_02(PRINTBUILD,2); 
}
