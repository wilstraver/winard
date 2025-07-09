# Winard

This program, written in Python, creates a window on your PC that works like a touch screen (display).<br>

How to proceed.<br>
Write some code, for example<br>
<pre>
#include &ltwinard.h&gt
void setup( )
{ Serial.begin(115200);
  build_up();
}
void loop( ) {;}
void build_up()
{ tx_02(PRINTBUILD,1);
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);
  tx_str(TEXT,"button");
  tx_06(BUTTON,6,ROOT,0,80,20);
  tx_02(PRINTOBJECTS,1);
}
</pre>

Upload this code to micro controller.


