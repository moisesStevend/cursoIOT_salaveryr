/////////////////////////////////
// Generated with a lot of love//
// with TUNIOT FOR ESP8266     //
// Website: Easycoding.tn      //
/////////////////////////////////
#include "DHT.h"

//DHT dht5(5,DHT22);
DHT dht5(5,DHT11);

void setup()
{
  Serial.begin(9600);
  dht5.begin();
  Serial.println("Empezamos");

}

void loop()
{
    Serial.println((dht5.readTemperature( )));
    delay(2000);
}
