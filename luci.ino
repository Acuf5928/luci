#include <LightDependentResistor.h>

#define LED 10
#define GND 11

#define LED_DUE 2

#define BUTTON 6
#define V 7 

#define GND2 13
#define SENSOR A4
#define LIGHT_LINE 0.70
#define OTHER_RESISTOR 10000 //ohms
#define USED_PHOTOCELL LightDependentResistor::GL5537_2
LightDependentResistor photocell(SENSOR, OTHER_RESISTOR, USED_PHOTOCELL);

bool statusLed = false;
bool autoLed = true;

int number = 0;

String inputString = "";       // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup()
{
  //Serial
  Serial.begin(9600);
  inputString.reserve(200);

  //First set of led
  pinMode(LED, OUTPUT);
  pinMode(GND, OUTPUT);

  //Second set of led
  pinMode(LED_DUE, OUTPUT);

  //Button
  pinMode(BUTTON, INPUT);
  pinMode(V, OUTPUT);

  //Sensor
  pinMode(GND2, OUTPUT);
  
  //Set standard value
  digitalWrite(GND2, LOW);
  digitalWrite(GND, LOW);
  digitalWrite(V, HIGH);
}

void loop()
{  
  checkButton(BUTTON);

  if (autoLed == true) {
    float light = LightDependentResistor::luxToFootCandles(photocell.getCurrentLux());
    
    if (light <= LIGHT_LINE)  {
      statusLed = true;
    } else {
      statusLed = false;
    }
    
    Serial.println(light);
    delay(500);
  }
  
  if (statusLed == true) {
    digitalWrite(LED, HIGH);
    digitalWrite(LED_DUE, HIGH);  
  } else {
    digitalWrite(LED, LOW);
    digitalWrite(LED_DUE, LOW); 
  }
  
  if (stringComplete) {
    number = inputString.toInt();

    if (number == 0) {
      autoLed = false;
      statusLed = false;
    } else if (number == 1) {
      autoLed = false;
      statusLed = true;
    } else if (number == 2) {
      autoLed = true;
    }
    
     // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:

    if (inputString == "TROVATO\n"){
        Serial.println("iM HERE");
        inputString = "";
      } else if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

void checkButton(int button) {
  if(digitalRead(button) == HIGH) {
    statusLed = !statusLed;
    delay(300);
    
    if(digitalRead(button) == HIGH) {
        delay(300);
        
        if(digitalRead(button) == HIGH) {
          autoLed = !autoLed;
        }
    }
    
    while (digitalRead(button) == HIGH) {
      delay(100);
    }
  }
}
