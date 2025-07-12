#include <winard.h>
  
void setup( )  
{ Serial.begin(115200);     //(115200); 
  build_up();
}

void loop()
{ delay(500) ;
  tx_02(CANVASSELECT,0);
  tx_str(TAGSDEL,"rect");
  delay(500) ;
  rectangles();
}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Arduino Display 0");
  tx_04(ROOT,0,240,350);  

  tx_04(CFG,255,255,255);
  tx_04(CBG,0,0,0);
  tx_08(CANVAS,0,ROOT,0,10,10,220,190);

  rectangles();
  tx_str(TAGS,"line");
  tx_02(LINEWIDTH,1);
  tx_02(ARROW,2);
  tx_04(ARROW,14,20,8);
  tx_08(LINE,5,CANVAS,0,60,20,100,150);

  tx_04(DASH,1,8,8);
  tx_04(CFG,255,0,0);
  tx_02(ARROW,0);
  tx_02(LINEWIDTH,4);
  tx_12(LINE,6,CANVAS,0,10,180,80,180,50,80,10,180);
  tx_04(DASH,0,8,8);
  tx_02(LINEWIDTH,1);
  tx_04(CBG,0,0,255);
  tx_08(OVAL,1,CANVAS,0,110,10,210,70);
// the oval is drawed in a rectangle X1,Y1  X2,Y2  
// draw a circle: X2-X1=Y2-Y1
  tx_04(CBG,0,0,0);
  tx_04(CFG,0,255,0);
  tx_04(ARCSHAPE,30,255,1);
//                |  |  |_0=arc  1=pieslice  2=chord
//                |  |____extend corner
//                |_______start corner
  tx_08(ARC,1,CANVAS,0,110,100,210,150);
// the underground shape of the arc is just like the oval 

  tx_04(CBG,0,0,0);
  tx_08(CANVAS,1,ROOT,0,10,220,180,120);
  tx_05(NLINES,5,8,20,20);
  tx_04(CFG,200,200,0);
  tx_02(LINEWIDTH,1);
  tx_04(DASH,1,2,2);
  tx_08(VLINES,3,CANVAS,1,20,20,20,100);
  tx_08(HLINES,3,CANVAS,1,20,20,161,20);
  tx_04(DASH,0,2,2);
//  rectangles();
  
  tx_02(PRINTOBJECTS,1); 
  tx_02(PRINTBUILD,0); 
}

void rectangles()
{ tx_str(TAGS,"rect");
  tx_04(CFG,255,255,255);
  tx_04(CBG,255,0,0);
  tx_08(RECT,5,CANVAS,0,10,10,40,20);
  tx_04(CBG,0,255,0);
  tx_08(RECT,6,CANVAS,0,10,30,40,40);
  tx_04(CBG,0,0,255);
  tx_08(RECT,7,CANVAS,0,10,50,40,60);
}
