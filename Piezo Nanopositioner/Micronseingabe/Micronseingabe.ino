#include "DFRobot_GP8403.h"
DFRobot_GP8403 dac(&Wire,0x5B);
DFRobot_GP8403 dac2(&Wire,0x5F);
  String readstring;
  int Steigung = 189.5;
  int axisxy = 0;
  int updown_val = 0 ;
  int leftright_val = 0;
  int QE_val = 0;
  int move_speed = 20;

void setup() {
  Serial.begin(115200);
  dac.begin();
  dac2.begin();
  while(dac.begin()!=0){
    Serial.println("init error");
    delay(1000);
   }
  Serial.println("init succeed");

  dac.setDACOutRange(dac.eOutputRange10V);
  dac2.setDACOutRange(dac.eOutputRange10V);
}


void loop() {

  char incomingChar = 0;   // for incoming serial data

  while (Serial.available()) {
    delay(10);  
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readstring += c; //makes readstring from the single bytes
    } 
  }

  if (readstring.length() >0) {
    char carray[readstring.length() + 1]; //determine size of the array
    readstring.toCharArray(carray, sizeof(carray)); //put readstringinto an array
    int n = atoi(carray); //convert the array into an Integer  
    Serial.println(carray);

    if (readstring.charAt(0) == 'x' || readstring.charAt(0) == 'X') {
    axisxy = 0;
}

    else if (readstring.charAt(0) == 'y' || readstring.charAt(0) == 'Y') {
    axisxy = 1;
}
      else if (readstring.charAt(0) == 'z' || readstring.charAt(0) == 'Z') {
    axisxy = 3;
}

    else{
      if (axisxy == 3){
      dac2.setDACOutVoltage(n, 0); 
      }
      else{
      dac.setDACOutVoltage(n, axisxy);   
      }
    Serial.println("check");}

  } 
  readstring="";
    }
