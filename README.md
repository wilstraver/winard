# Winard 

This program, written in Python, creates a window on your PC that works like a touch screen (display).<br>

How to proceed.<br>
Write some code, for example:<br>
<pre>
#include &ltwinard.h&gt
void setup()
{ Serial.begin(115200);
  tx_str(TEXT,"Winard");
  tx_04(ROOT,0,240,160);
  tx_str(TEXT,"button");
  tx_06(BUTTON,6,ROOT,0,80,120);
}
void loop() {;}
</pre>

Upload this code to the micro controller.<br>
Start Winard:
<pre>python3 winard.py /dev/ttyUSB0</pre>
The USB port used is /dev/ttyUSB0, this varies by computer operating system.
Linux Mint was used here.<br>
The result:

<img width="264" height="230" alt="Screenshot_2025-07-10_14-53-34" src="https://github.com/user-attachments/assets/32e8e8d7-96ff-449d-840a-c4747725b066" />

