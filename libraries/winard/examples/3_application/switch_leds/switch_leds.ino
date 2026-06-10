#include <winard.h>

int red=5, green=6, blue=7;

void setup( )  
{ Serial.begin(115200);  
  startup(); 
  build_up();
  Serial.setTimeout(200);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop( ) 
{ readcode();
  if (Bag.i2==CBUTTON)
  { if (Bag.i3==1)
    { if (Bag.i4==1) digitalWrite(red,  HIGH); 
      if (Bag.i4==0) digitalWrite(red,  LOW); 
    }
    if (Bag.i3==2)
    { if (Bag.i4==1) digitalWrite(green,HIGH); 
      if (Bag.i4==0) digitalWrite(green,LOW);
    } 
    if (Bag.i3==3)
    { if (Bag.i4==1) digitalWrite(blue, HIGH); 
      if (Bag.i4==0) digitalWrite(blue, LOW); 
    }
  }
}

void build_up()
{ tx_02(PRINTBUILD,1);
  tx_str(TEXT,"Winard"); 
  tx_04(ROOT,0,240,40);
  
  tx_str(TEXT,"red     ");
  tx_06(CBUTTON,1,ROOT,0,10,10);
  tx_04(CFG,0,0,0); 
  tx_04(CBG,255,0,0);   
  tx_05(STYLE,0,CBUTTON,1,CFG);
  tx_05(STYLE,0,CBUTTON,1,CBG);

  tx_str(TEXT,"green");
  tx_06(CBUTTON,2,ROOT,0,95,10);
  tx_04(CBG,0,255,0);   
  tx_05(STYLE,0,CBUTTON,2,CFG);
  tx_05(STYLE,0,CBUTTON,2,CBG);

  tx_str(TEXT,"blue  ");
  tx_06(CBUTTON,3,ROOT,0,180,10);
  tx_04(CFG,255,255,255); 
  tx_04(CBG,0,0,255);   
  tx_05(STYLE,0,CBUTTON,3,CFG);
  tx_05(STYLE,0,CBUTTON,3,CBG);
  
  tx_02(PRINTOBJECTS,1);
//  tx_02(PRINTBUILD,0);
}
