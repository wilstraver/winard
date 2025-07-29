#include <winard.h>
  
void setup( )  
{ Serial.begin(115200); 
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);  

  tx_02(WIDTH,16);
  tx_10(FONT,0,ENTRY,3,1,10,0,1,0,0);
  tx_06(ENTRY,3,ROOT,0,60,30);
  
  tx_04(CFG, 255,0,0); 
  tx_04(CFIELD_BG,255,255,0);
  tx_05(STYLE,0,ENTRY,3,CFG);  
  tx_05(STYLE,0,ENTRY,3,CFIELD_BG);
    
  tx_str(SHOW,"#");
  tx_06(ENTRY,14,ROOT,0,60,70);
  tx_04(CFG, 0,0,0); 
  tx_04(CFIELD_BG,255,100,255);
  tx_05(STYLE,0,ENTRY,14,CFG);  
  tx_05(STYLE,0,ENTRY,14,CFIELD_BG);

  tx_str(SHOW,"");
  tx_06(ENTRY,23,ROOT,0,60,110);
  tx_04(CFG,255,0,255); 
  tx_04(CFIELD_BG,150,255,200);
  tx_05(STYLE,0,ENTRY,23,CFG);  
  tx_05(STYLE,0,ENTRY,23,CFIELD_BG);

  tx_02(PRINTOBJECTS,1);  
}
