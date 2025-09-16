#include <winard.h>

void setup( )  
{ Serial.begin(115200);     //(115200); 
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160); 

// the tabs start with tab 0, 
// the next, tab 1 , tab 2, etc.

  tx_str(TEXT,"D,E,F"); 
  tx_02(POSITION,0);
  tx_08(NOTEBOOK,2,ROOT,0,15,5,210,140);
  tx_str(TEXT,"this is tab D");
  tx_06(LABEL,14,TAB,0,10,35);   
  tx_str(TEXT,"this is tab E"); 
  tx_06(LABEL,15,TAB,1,10,35);    
  tx_str(TEXT,"this is tab F"); 
  tx_06(LABEL,16,TAB,2,10,35); 

  tx_04(CBG,LIME);
  tx_05(STYLE,0,TAB,0,CBG);  
  tx_05(STYLE,0,TAB,1,CBG);
// style the label background too:  
  tx_05(STYLE,0,LABEL,15,CBG);
  
  tx_04(CBG,MAGENTA);
  tx_05(STYLE,1,NOTEBOOK,2,CBG);
//            \__ directs to tab 

  tx_04(CBG,PURPLE);
  tx_05(STYLE,0,NOTEBOOK,2,CBG);
//             \__ directs to notebook  

tx_04(CSELECT,250,250,0);
tx_05(MAP,1,NOTEBOOK,2,CSELECT);
//         \__ directs to tab
// MAP is a STYLE way too

  tx_10(FONT,0,LABEL,16,1,14,1,0,0,0);
  tx_10(FONT,1,NOTEBOOK,2,1,14,0,1,1,0);
//            \__ directs to tab 
// FONT is the STYLE way for fonts

  tx_str(TEXT,"ok"); 
  tx_06(BUTTON,6,TAB,2,40,120);
  tx_02(WIDTH,3); // number of characters
  tx_05(STYLE,1,BUTTON,6,WIDTH); 
  tx_04(CBG,150,250,50);  
  tx_05(STYLE,1,BUTTON,6,CBG);    
  tx_02(PRINTOBJECTS,1); 
}
