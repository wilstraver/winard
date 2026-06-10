#include <winard.h>
  
void setup( )  
{ Serial.begin(115200);
  startup();
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);  

  tx_str(SPINBOXSET,"0 2 6 1.0ºC");
  tx_str(TEXT,"0.0 10.0 0.1 %.1fºC ");
  tx_10(FONT,0,SPINBOX,1,2,14,0,1,0,0);
  tx_06(SPINBOX,1,ROOT,0,20,40);

  tx_04(CFG, 255,0,0);  
  tx_04(CBG, 255,0,255); 
  tx_04(CSELECT_FG,0,0,255);
  tx_04(CSELECT_BG,255,100,0);
  tx_04(CFIELD_BG, 255,255,0);
  tx_05(STYLE,0,SPINBOX,1,CFG);
  tx_05(STYLE,0,SPINBOX,1,CBG);
  tx_05(STYLE,0,SPINBOX,1,CFIELD_BG);
  tx_05(STYLE,0,SPINBOX,1,CSELECT_BG);
  tx_05(STYLE,0,SPINBOX,1,CSELECT_FG);

//remember, next line not longer then the buffer length
//including TEXT and the newline/feedback characters
  tx_str(TEXT,"-0.2V -0.1V 0.0V 0.1V 0.2V 0.5V 1.0V");  
  tx_str(SPINBOXSET,"1 2 5 0.2V");
  tx_10(FONT,0,SPINBOX,2,2,18,0,0,0,0);
  tx_06(SPINBOX,2,ROOT,0,130,40);

  tx_str(SPINBOXSET,"1 1 10 four");
  tx_str(TEXT,"one two three four five");
  tx_06(SPINBOX,3,ROOT,0,60,100);

  tx_04(CFG, 255,200,255); 
  tx_04(CBG, 0,150,150);  
  tx_04(CFIELD_BG,0,0,0); 
  tx_04(CSELECT_FG,255,255,255);  
  tx_04(CSELECT_BG,150,0,150);  
  tx_05(STYLE,0,SPINBOX,3,CFG);
  tx_05(STYLE,0,SPINBOX,3,CBG);
  tx_05(STYLE,0,SPINBOX,3,CFIELD_BG);
  tx_05(STYLE,0,SPINBOX,3,CSELECT_FG);
  tx_05(STYLE,0,SPINBOX,3,CSELECT_BG);
  
  tx_02(PRINTOBJECTS,1);
  tx_02(PRINTBUILD,2);
}
