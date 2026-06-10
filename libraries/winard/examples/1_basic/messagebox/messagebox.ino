#include <winard.h>

const int input = A0; 
int buf[64];

void setup( )  
{ Serial.begin(115200); 
  startup();
  build_up();
  Serial.setTimeout(50);
}

void loop() { ;}

void build_up()
{ tx_02(PRINTBUILD,1); 
  tx_str(TEXT,"Winard");
  tx_04(ROOT,1,320,240);  

  tx_02(PRINTOBJECTS,1); 
  tx_02(PRINTBUILD,2); 

  tx_str(TEXT,"  This is Winard  ");
//  available message boxes:
  tx_02(MBOXINFO,0);
  tx_02(MBOXWARNING,0);
  tx_02(MBOXERROR,0);
  tx_02(MBOXQUESTION,0);
  tx_02(MBOXOKCANCEL,0);
  tx_02(MBOXYESNO,0);
  tx_02(MBOXRETRYCANCEL,0);
}    
