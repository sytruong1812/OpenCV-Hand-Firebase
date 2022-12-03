#include <ESP8266WiFi.h>
// Firebase Library
#include "FirebaseESP8266.h"
// Firebase Declare
#define FIREBASE_HOST "https://hand-opencv-esp-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "hNi0eRIeqMucClkf7XwUh6QBzIPEii8i0BzS0wbsF"
// Create  Variables
FirebaseData firebaseData;
FirebaseJson json;
// bien nhan data
int get_value;
 
// Connecting Wifi
const char* ssid = "2.4G_Phuongngoc lầu 2";
const char* password = "10111960";

void setup() {
pinMode(5, OUTPUT);

Serial.begin(9600);
WiFi.begin(ssid, password);
Serial.print("Connecting to WiFi");
while (WiFi.status() != WL_CONNECTED) {
  delay(300);
  Serial.print(".");
}
Serial.println("");
Serial.println("Connected to WiFi");
Serial.print("Local IP: ");
Serial.println(WiFi.localIP());
Serial.println("");
// Connecting Firebase
Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
Firebase.reconnectWiFi(true);
}

void loop() {
Firebase.getInt(firebaseData, "/Control/LED");
get_value = firebaseData.intData();
{
  Serial.println("data in /Control/LED is: ");
  Serial.println(get_value);
  delay(500);
}
  if(get_value == 1){
    digitalWrite(5, LOW);    
  }
  else{
    digitalWrite(5, HIGH);
  }
  delay(500);
}
