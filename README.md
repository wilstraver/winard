# Winard
## Window for arduino.

This program, written in Python, creates a window on your PC that works like a touch screen (display).<br>

How to proceed.<br>

Write some code, for example<br>
#include <winard.h><br>
void setup( )  <br>
{ Serial.begin(115200);   <br>
  build_up();<br>
}<br>
void loop( ) {;}<br>
void build_up()<br>
{ tx_02(PRINTBUILD,1);<br>
  tx_str(TEXT,"Winard");<br> 
  tx_04(ROOT,0,240,160);<br>
  tx_str(TEXT,"button");<br>
  tx_06(BUTTON,6,ROOT,0,80,20);<br>
  tx_02(PRINTOBJECTS,1);<br>
}<br>


