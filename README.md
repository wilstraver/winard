# winard
Window for arduino.

This program, written in Python, creates a window on your PC that works like a touch screen (display).

How to proceed.

Write some code, for example


Upload the code to the micro controller.



[Upl<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 24.2.7.2 (Linux)"/>
	<meta name="created" content="2025-07-08T20:45:01.312585951"/>
	<meta name="changed" content="2025-07-08T20:46:11.106994699"/>
	<style type="text/css">
		@page { size: 210.01mm 297mm; margin: 20mm }
		p { line-height: 115%; margin-bottom: 2.47mm; background: transparent }
	</style>
</head>
<body lang="en-US" link="#000080" vlink="#800000" dir="ltr"><p style="line-height: 100%; margin-bottom: 0mm">
# winard</p>
<p style="line-height: 100%; margin-bottom: 0mm">Window for arduino.</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">This program,
written in Python, creates a window on your PC that works like a
touch screen (display).</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">How to proceed.</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">Write some code, for
example</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">#include &lt;winard.h&gt;</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">void setup( )  
</p>
<p style="line-height: 100%; margin-bottom: 0mm">{
Serial.begin(115200);   
</p>
<p style="line-height: 100%; margin-bottom: 0mm">  build_up();</p>
<p style="line-height: 100%; margin-bottom: 0mm">}</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">void loop( ) {;}</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">void build_up()</p>
<p style="line-height: 100%; margin-bottom: 0mm">{
tx_02(PRINTBUILD,1);</p>
<p style="line-height: 100%; margin-bottom: 0mm"> 
tx_str(TEXT,&quot;Winard&quot;); 
</p>
<p style="line-height: 100%; margin-bottom: 0mm"> 
tx_04(ROOT,0,240,160);</p>
<p style="line-height: 100%; margin-bottom: 0mm"> 
tx_str(TEXT,&quot;button&quot;);</p>
<p style="line-height: 100%; margin-bottom: 0mm"> 
tx_06(BUTTON,6,ROOT,0,80,20);;</p>
<p style="line-height: 100%; margin-bottom: 0mm"> 
tx_02(PRINTOBJECTS,1);</p>
<p style="line-height: 100%; margin-bottom: 0mm">}</p>
<p style="line-height: 100%; margin-bottom: 0mm"><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0mm">Upload the code to
the micro controller.</p>
</body>
</html>oading test 1.html…]()



