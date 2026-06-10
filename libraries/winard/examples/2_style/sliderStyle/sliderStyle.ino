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
  tx_04(ROOT,0,240,180); 

  tx_str(TEXT,"tk version");
  tx_06(LABEL,1,ROOT,0,10,30);

  tx_04(CBG,0,255,0);
  tx_04(CABG,0,0,255);
  tx_04(CTROUGH,255,0,255);
  tx_04(CHLBG,255,200,0);//highlightbackground
  tx_04(CHL,0,200,255);  //highlight
  tx_02(SLIDERWIDTH,16);
  tx_02(RELIEFWIDTH,4);
  tx_02(BORDERWIDTH,10);
  tx_02(RELIEFTROUGH,3);
  tx_02(RELIEFSLIDER,1);
  tx_10(FONT,0,SET,0,1,10,0,1,0,0);
  tx_12(SCALEOPTIONS,1,1,1,1,1,1,1,1,1, 1, 1);
//                   1 2 3 4 5 6 7 8 9 10 11
//option use, 0 not  1 yes: 
// 1-font  2-background  3-activebackground
// 4-troughcolor  5-highlightcolor
// 6-highlightbackground  7-sliderwidth
// 8-reliefwidth  9-borderwidth  
//10-relief 11-sliderrelief
  tx_str(TEXT,"0 1 4.0 -10.0 10.0 2.0 1");
  tx_08(SCALE,18,ROOT,0,10,50,150,12);

  tx_str(TEXT,"ttk version");
  tx_06(LABEL,1,ROOT,0,130,10);
  tx_str(TEXT,"1 1 2.0 20.0 -20.0 2.0 2");
  tx_08(SCALE,19,ROOT,0,200,10,0,150);

  tx_04(CSLIDER,0,0,255);
  tx_05(STYLE,0,SCALE,19,CSLIDER);    
  tx_04(CTROUGH,255,0,0);
  tx_05(STYLE,0,SCALE,19,CTROUGH);
  tx_02(SLIDERWIDTH,15);
  tx_05(STYLE,0,SCALE,19,SLIDERWIDTH);  
  tx_02(BORDERWIDTH,4);
  tx_05(STYLE,0,SCALE,19,BORDERWIDTH);  
  tx_02(RELIEFTROUGH,1);
  tx_05(STYLE,0,SCALE,19,RELIEFTROUGH);
    
  tx_02(PRINTOBJECTS,1); 
  tx_02(PRINTBUILD,2);
}
 
