/////////////////////////////////
// Generated with a lot of love//
// with TUNIOT FOR ESP8266     //
// Website: Easycoding.tn      //
/////////////////////////////////
#include <Wire.h>
#include "SSD1306.h"

SSD1306  display(0x3C, 4, 5);

void setup()
{
  Serial.begin(9600);
  display.init();

  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_10);
  //display.drawString(0, 0, "Hello World!");
  //display.drawLine(0,0,127,63);
  display.drawProgressBar(0,0,100,10,20);
  display.display();

}


void loop()
{


}
