#include <winard.h>
  
void setup( )  
{ Serial.begin(115200);
  build_up();
}

void loop() {;}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);  

  tx_str(SPINBOXSET,"0 2 6 1.0ºC");
  tx_str(TEXT,"0.0 10.0 0.1 %.1fºC ");
  tx_06(SPINBOX,1,ROOT,0,50,20);

// remember, next line not longer then the 
// buffer length, including TEXT, spaces
// and the two newline/feedback characters

  tx_str(TEXT,"-0.2V -0.1V 0.0V 0.1V 0.2V 0.5V 1.0V");  
  tx_str(SPINBOXSET,"1 2 5 0.2V");
  tx_06(SPINBOX,2,ROOT,0,50,60);

  tx_str(SPINBOXSET,"1 1 10 four");
  tx_str(TEXT,"one two three four five");
  tx_06(SPINBOX,3,ROOT,0,50,100);
}
