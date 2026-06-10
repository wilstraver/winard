
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
  tx_02(TEAR,1);
  tx_str(TEXT,"menu1,menu2,menu3");
  tx_04(MENUBAR,0,ROOT,0);
  tx_str(TEXT,"button1");
  tx_04(BMCOMMAND,1,BARMENU,0);
  tx_04(BMSEPARATOR,2,BARMENU,0);
  tx_str(TEXT,"submenu1");
  tx_04(SUBMENU,0,BARMENU,0);
  tx_str(TEXT,"button2");
  tx_04(BMCOMMAND,2,SUBMENU,0);
  tx_str(TEXT,"button3");
  tx_04(BMCOMMAND,3,SUBMENU,0);
  tx_str(TEXT,"submenu2");  
  tx_04(SUBMENU,2,SUBMENU,0);
  tx_str(TEXT,"button4");
  tx_04(BMCOMMAND,4,SUBMENU,2);
  tx_03(SELECT,BMRADIO,1); 
  tx_str(TEXT,"radio1");
  tx_04(BMRADIO,1,BARMENU,0);
  tx_str(TEXT,"radio2");
  tx_04(BMRADIO,2,BARMENU,0);
  
  tx_03(SELECT,BMRADIO,4); 
  tx_str(TEXT,"radio3");
  tx_04(BMRADIO,3,SUBMENU,0);
  tx_str(TEXT,"radio4");
  tx_04(BMRADIO,4,SUBMENU,0);
  
  tx_str(TEXT,"check1");
  tx_04(BMCHECK,1,BARMENU,0);
  tx_str(TEXT,"button5"); 
  tx_04(BMCOMMAND,5,BARMENU,1);
  tx_str(TEXT,"button6"); 
  tx_04(BMCOMMAND,6,BARMENU,1);
  tx_04(BMSEPARATOR,0,BARMENU,1);
  tx_str(TEXT,"button7"); 
  tx_04(BMCOMMAND,7,BARMENU,1);
  tx_02(PRINTBUILD,2); 
  tx_02(PRINTOBJECTS,1); 
}
