#include <winard.h>

const int buttonPin = 8; 
int buttonState = 0;    
int mem=0;

void setup() 
{ Serial.begin(115200);
  build_up();
  pinMode(buttonPin, INPUT);
}

void loop() 
{ buttonState = digitalRead(buttonPin);
  if ((buttonState == HIGH) & (mem==0))
  { tx_04(CBG, 255,0,0);  
    tx_05(STYLE,0,LABEL,3,CBG);
    tx_04(CFG,255,255,255); 
    tx_05(STYLE,0,LABEL,3,CFG);
    mem=1;
  }
  if ((buttonState == LOW) & (mem==1))
  { tx_04(CBG, 150,0,0); 
    tx_05(STYLE,0,LABEL,3,CBG);
    tx_04(CFG,0,0,0); 
    tx_05(STYLE,0,LABEL,3,CFG);
    mem=0;
  }  
}

void build_up()   
{ tx_02(PRINTBUILD,1);  
  tx_str(TEXT,"Winard");    
  tx_04(ROOT,0,240,160);  
  
  tx_str(TEXT,"warning"); 
  tx_06(LABEL,3,ROOT,0,60,50);  
  tx_10(FONT,0,LABEL,3,1,24,0,1,0,0);
  tx_04(CFG,0,0,0); 
  tx_05(STYLE,0,LABEL,3,CFG);
  tx_04(CBG, 150,0,0); 
  tx_05(STYLE,0,LABEL,3,CBG);
   
  tx_02(PRINTOBJECTS,1);  
}
