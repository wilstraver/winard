#include <winard.h>

const int input = A0; 
int buf[64];

void setup( )  
{ Serial.begin(115200); 
  build_up();
//  analogReference(INTERNAL);  

//  analogReference(EXTERNAL);
  analogReference(DEFAULT);
  Serial.setTimeout(50);
}

void loop() 
{ func();
}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,1,320,240);  
  tx_04(CFG,255,255,255);
  tx_04(CBG,0,0,0);
  tx_08(CANVAS,1,ROOT,0,10,5,300,200);  
  tx_05(NLINES,9,12,20,20);
  tx_04(CFG,120,120,0);
  tx_02(LINEWIDTH,1);
  tx_04(DASH,1,2,2);
  tx_08(VLINES,3,CANVAS,1,40,20,40,180);
  tx_08(HLINES,3,CANVAS,1,40,20,260,20);  
  tx_04(CFG,255,255,255); 
  tx_04(DASH,0,8,8); 
  tx_04(SETLINE,1,40,6);
  tx_str(TAGS,"two");
  tx_02(LINEWIDTH,2);  
  tx_02(PRINTOBJECTS,1); 
  tx_02(PRINTBUILD,0);  
}

void func()
{ int a=0;
  while (a<(38)) { buf[a++]=analogRead(A0);delay(1);}
  a=0;
  tx_02(COORD,buf[a++]/6+15);
  while (a<(38)) {tx_02(COORDAPPEND,buf[a++]/6+15);delay(2);}
  tx_str(TAGSDEL,"two");
  tx_04(NEWLINE,9,CANVAS,1);
}
