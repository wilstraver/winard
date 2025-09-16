#include <winard.h>

const int red  =5, green=6, blue =9;

void setup( )  
{ Serial.begin(115200);   
  build_up();
  Serial.setTimeout(200);  // reaction speed
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop( ) 
{ readcode();
  if (Bag.i2==SLIDER)
  { switch(Bag.i3)  
    { case 1: analogWrite(red,  Bag.i4/3); break;
      case 2: analogWrite(green,Bag.i4/3); break;
      case 3: analogWrite(blue, Bag.i4/3); break;
    }
  }
}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,180); 

  tx_str(TEXT,"0 0 20 100 0 0 0");
  tx_04(CTROUGH,255,0,0);
  tx_12(SCALEOPTIONS,0,0,0,1,0,0,0,0,0,0,0);
  tx_08(SCALE,1,ROOT,0,10,10,15,150);

  tx_str(TEXT,"0 0 20 100 0 0 0");
  tx_04(CTROUGH,0,255,0);
  tx_12(SCALEOPTIONS,0,0,0,1,0,0,0,0,0,0,0);
  tx_08(SCALE,2,ROOT,0,90,10,15,150);
  
  tx_str(TEXT,"0 0 20 100 0 0 0");
  tx_04(CTROUGH,0,0,255);
  tx_12(SCALEOPTIONS,0,0,0,1,0,0,0,0,0,0,0);
  tx_08(SCALE,3,ROOT,0,170,10,15,150);

  tx_02(PRINTOBJECTS,1); 
}
