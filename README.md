# Winard
Window for arduino.

This program, written in Python, creates a window on your PC that works like a touch screen (display).

How to proceed.

Write some code, for example


Upload the code to the micro controller.

[Up<!DOCTYPE html>
<html>
<head>
<title>Winard</title>
<meta name="generator" content="Bluefish 2.2.15" >
<meta name="author" content="Wil" >
<meta name="date" content="2025-07-08T21:27:13+0200" >
<meta name="copyright" content="">
<meta name="keywords" content="">
<meta name="description" content="">
<meta name="ROBOTS" content="NOINDEX, NOFOLLOW">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8">
<meta http-equiv="content-style-type" content="text/css">
<meta http-equiv="expires" content="0">
</head>
<body>
# Winard<br>
Window for arduino.<br>

This program, written in Python, creates a window on your PC that works like a touch screen (display).<br>

How to proceed.<br><br>
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

Upload the code to the micro controller.<br>
<img src="../manual/buttons.png" width="264" height="230" alt="">
</body>
</html>loading winard.html…]()


