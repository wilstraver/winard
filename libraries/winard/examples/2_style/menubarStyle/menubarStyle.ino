
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
  tx_04(ROOT,0,290,220);  

  tx_04(CFG,255,0,0);  
  tx_04(CBG,0,255,0);
  tx_04(CSELECT_FG,0,0,255); 
  tx_04(CAFG,255,255,0); 
  tx_04(CABG,0,255,255);
  tx_10(FONT,0,SET,0,1,13,0,1,1,0); 
  tx_08(MENUOPTIONS,1,1,1,1,1,1,1);
// menubar options: 1 2 3 4 5 6 7
// 1-tear 2-font 3-foreground 4-background
// 5-activeforeground 6-activebackground
// 7-selectcolor

  tx_04(CFG,0,255,0);  
  tx_04(CBG,0,0,255);
  tx_04(CSELECT_FG,255,0,0); 
  tx_04(CAFG,0,255,255); 
  tx_04(CABG,255,0,255);
  tx_10(FONT,0,SET,0,1,11,0,0,0,0); 
  tx_08(MENUOPTIONS2,1,1,1,1,1,1,1);
// barmenu and submenu options

  tx_02(TEAR,1);
  tx_str(TEXT,"menu1,menu2,menu3");
  tx_04(MENUBAR,0,ROOT,0);
  
  tx_str(TEXT,"button1");
  tx_04(BMCOMMAND,1,BARMENU,0);
  tx_04(BMSEPARATOR,2,BARMENU,0);
  tx_str(TEXT,"submenu1");
  tx_04(CBG,255,0,255);
  tx_08(MENUOPTIONS2,1,1,1,1,1,1,1);
  tx_04(SUBMENU,0,BARMENU,0);
  tx_str(TEXT,"button2");
  tx_04(BMCOMMAND,2,SUBMENU,0);
  tx_str(TEXT,"button3");
  tx_04(BMCOMMAND,3,SUBMENU,0);
  tx_str(TEXT,"submenu2"); 
  tx_10(FONT,0,SET,0,1,11,0,1,0,0); 
  tx_04(CFG,0,0,0);   
  tx_04(CBG,255,255,0);
  tx_08(MENUOPTIONS2,1,1,1,1,1,1,1);
  tx_04(SUBMENU,2,SUBMENU,0);
  tx_str(TEXT,"button4");
  tx_04(BMCOMMAND,4,SUBMENU,2);
  
  tx_03(SELECT,BMRADIO,1);
  tx_str(TEXT,"radio1");
  tx_04(BMRADIO,1,BARMENU,0);
  tx_str(TEXT,"radio2");
  tx_04(CBG,0,255,255);
  tx_08(MENUOPTIONS2,1,1,1,1,1,1,1);
  tx_04(BMRADIO,2,BARMENU,0);
  tx_str(TEXT,"check1");
  tx_04(BMCHECK,1,BARMENU,0);
  
  tx_str(TEXT,"button5"); 
  tx_04(BMCOMMAND,5,BARMENU,1);
  tx_str(TEXT,"button6"); 
  tx_04(BMCOMMAND,6,BARMENU,1);
 
  tx_02(PRINTOBJECTS,1);
  tx_02(PRINTBUILD,2); 
}
