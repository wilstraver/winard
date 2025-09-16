
#include <winard.h>

void setup( )  
{ Serial.begin(115200);   
  build_up();
}

void loop( ) {;}

void build_up()
{ tx_02(PRINTBUILD,1);
  int x=240, y=160;
  
  tx_str(TEXT,"Winard 0");
  tx_04(ROOT,0,x,y);
  
  tx_str(TEXT,"Winard 1");
  tx_04(TOPLEVEL,1,x,y);
  
  tx_str(TEXT,"Winard 2");
  tx_04(TOPLEVEL,2,x,y);
  
  tx_str(TEXT,"Winard 3");
  tx_04(TOPLEVEL,3,x,y);
  
  tx_str(TEXT,"root");
  tx_06(LABEL,0,ROOT,0,60,25);
  
  tx_str(TEXT,"toplevel 1");
  tx_06(LABEL,1,TOPLEVEL,1,60,25);
  
  tx_str(TEXT,"toplevel 2");
  tx_06(LABEL,2,TOPLEVEL,2,60,25);

  tx_str(TEXT,"toplevel 3");
  tx_06(LABEL,3,TOPLEVEL,3,60,25);

  tx_04(CBG,255,255,220);
  tx_05(STYLE,0,ROOT,0,CBG);
  tx_05(STYLE,0,LABEL,0,CBG);

  tx_04(CBG,255,220,220);
  tx_05(STYLE,0,TOPLEVEL,1,CBG);
  tx_05(STYLE,0,LABEL,1,CBG);

  tx_04(CBG,220,220,255);
  tx_05(STYLE,0,TOPLEVEL,2,CBG);
  tx_05(STYLE,0,LABEL,2,CBG);
  
  tx_04(CBG,220,255,220);
  tx_05(STYLE,0,TOPLEVEL,3,CBG);
  tx_05(STYLE,0,LABEL,3,CBG);
  
  tx_02(PRINTOBJECTS,1);
}
