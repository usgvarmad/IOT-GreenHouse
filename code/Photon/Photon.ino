#include "Adafruit_DHT.h"

#define DHT0PIN 4
#define DHT1PIN 5
#define DHT2PIN 6
#define DHT3PIN 7

#define DHTTYPE DHT11		// DHT 11

DHT dht0(DHT0PIN, DHTTYPE);
DHT dht1(DHT1PIN, DHTTYPE);
DHT dht2(DHT2PIN, DHTTYPE);
DHT dht3(DHT3PIN, DHTTYPE);

// Pins
int s0_pin = 0;
int s1_pin = 1;
int s2_pin = 2;
int s3_pin = 3;
int mux_pin = A0;
int fan_pin = A5;
int heat_pin = A6;
int light_pin = A7;
int w0_pin = A1;
int w1_pin = A2;
int w2_pin = A3;
int w3_pin = A4;

float temperature = 0; //average of all 4 sensors
float humidity = 0; //average of all 4 sensors
int light = 0; //average of all 4 sensors
int soil0 = 0;
int soil1 = 0;
int soil2 = 0;
int soil3 = 0;
int lastTemp =50;

String controlStr = "";

int soil0Arr[4] = {0,0,0,0};
int soil1Arr[4] = {0,0,0,0};
int soil2Arr[4] = {0,0,0,0};
int soil3Arr[4] = {0,0,0,0};

int flag = 0; //disconnect flag

TCPClient client;

//char server[] = "ec2-54-218-99-64.us-west-2.compute.amazonaws.com";
//**vvvvvv Make sure you change the line below vvvvvvvv**
byte server[] = { 172, 20, 10, 4 }; //change this to your computer's local IP address (IP address of python server)

void setup() {
  pinMode(s0_pin, OUTPUT);
  pinMode(s1_pin, OUTPUT);
  pinMode(s2_pin, OUTPUT);
  pinMode(s3_pin, OUTPUT);
  pinMode(fan_pin,OUTPUT);
  pinMode(heat_pin,OUTPUT);
  pinMode(light_pin,OUTPUT);
  pinMode(w0_pin,OUTPUT);
  pinMode(w1_pin,OUTPUT);
  pinMode(w2_pin,OUTPUT);
  pinMode(w3_pin,OUTPUT);

  selectChannel(0);
  dht0.begin();
  dht1.begin();
  dht2.begin();
  dht3.begin();

  Serial.begin(9600);
  Serial.println("Connecting...");
  if(client.connect(server,9999)){
    Serial.println("Connected!");


  }
  else{
    Serial.println("Connection failed.");
  }

}

void selectChannel(int i){
  digitalWrite(s0_pin,(i&1)>0 ? HIGH:LOW);
  digitalWrite(s1_pin,(i&2)>0 ? HIGH:LOW);
  digitalWrite(s2_pin,(i&4)>0 ? HIGH:LOW);
  digitalWrite(s3_pin,(i&8)>0 ? HIGH:LOW);
}

void setLight(int l0){
  if(controlStr.substring(0,l0).equals("light:on")){
    digitalWrite(light_pin,HIGH);
  }
  else if(controlStr.substring(0,l0).equals("light:off")){
    digitalWrite(light_pin, LOW);
  }
}

void setHeat(int l0, int l1){
  if(controlStr.substring(l0+1,l1).equals("heat:on")){
    digitalWrite(heat_pin,HIGH);
  }
  else if(controlStr.substring(l0+1,l1).equals("heat:off")){
    digitalWrite(heat_pin, LOW);
  }
}

void setFan(int l1, int l2){
  if(controlStr.substring(l1+1,l2).equals("fan:on")){
    digitalWrite(fan_pin,HIGH);
  }
  else if(controlStr.substring(l1+1,l2).equals("fan:off")){
    digitalWrite(fan_pin, LOW);
  }
}

void setWater(int l2, int l3,int l4,int l5){
  if(controlStr.substring(l2+1,l3).equals("w0:on")){
    digitalWrite(w0_pin,HIGH);
  }
  else if(controlStr.substring(l2+1,l3).equals("w0:off")){
    digitalWrite(w0_pin, LOW);
  }
  if(controlStr.substring(l3+1,l4).equals("w1:on")){
    digitalWrite(w1_pin,HIGH);
  }
  else if(controlStr.substring(l3+1,l4).equals("w1:off")){
    digitalWrite(w1_pin, LOW);
  }
  if(controlStr.substring(l4+1,l5).equals("w2:on")){
    digitalWrite(w2_pin,HIGH);
  }
  else if(controlStr.substring(l4+1,l5).equals("w2:off")){
    digitalWrite(w2_pin, LOW);
  }
  if(controlStr.substring(l5+1).equals("w3:on")){
    digitalWrite(w3_pin,HIGH);
  }
  else if (controlStr.substring(l5+1).equals("w3:off")){
    digitalWrite(w3_pin, LOW);
  }
}


void loop() {
    // get soil readings
    selectChannel(0);
    delay(1);
    soil0Arr[0] = soil0Arr[1];
    soil0Arr[1] = soil0Arr[2];
    soil0Arr[2] = soil0Arr[3];
    soil0Arr[3] = analogRead(mux_pin);
    soil0 = (soil0Arr[0] + soil0Arr[1] + soil0Arr[2] + soil0Arr[3])/4;
    selectChannel(1);
    delay(1);
    Serial.println("soil0 "+String(soil0));
    soil1Arr[0] = soil1Arr[1];
    soil1Arr[1] = soil1Arr[2];
    soil1Arr[2] = soil1Arr[3];
    soil1Arr[3] = analogRead(mux_pin);
    soil1 = (soil1Arr[0] + soil1Arr[1] + soil1Arr[2] + soil1Arr[3])/4;
    selectChannel(2);
    delay(1);
    Serial.println("soil1 "+String(soil1));
    soil2Arr[0] = soil2Arr[1];
    soil2Arr[1] = soil2Arr[2];
    soil2Arr[2] = soil2Arr[3];
    soil2Arr[3] = analogRead(mux_pin);
    soil2 = (soil2Arr[0] + soil2Arr[1] + soil2Arr[2] + soil2Arr[3])/4;
    selectChannel(3);
    delay(1);
    Serial.println("soil2 "+String(soil2));
    soil3Arr[0] = soil3Arr[1];
    soil3Arr[1] = soil3Arr[2];
    soil3Arr[2] = soil3Arr[3];
    soil3Arr[3] = analogRead(mux_pin);
    soil3 = (soil3Arr[0] + soil3Arr[1] + soil3Arr[2] + soil3Arr[3])/4;
    selectChannel(4);
    delay(1);
    Serial.println("soil3 "+String(soil3));
    // get light readings

    int light0 = analogRead(mux_pin);
    selectChannel(5);
    delay(1);
    int light1 = analogRead(mux_pin);
    selectChannel(6);
    delay(1);
    int light2 = analogRead(mux_pin);
    selectChannel(7);
    delay(1);
    int light3 = analogRead(mux_pin);

    light = (light0+light1+light2+light3)/4;
    Serial.println("light "+String(light));
    // get temperature readings
    selectChannel(8);
    delay(1);
    float temp0 = analogRead(mux_pin);
    temp0 = (temp0*0.805)/10;
    selectChannel(9);
    delay(1);
    float temp1 =  analogRead(mux_pin);
    temp1 = (temp1*0.805)/10;
    selectChannel(10);
    delay(1);
    float temp2 =  analogRead(mux_pin);
    temp2 = (temp2*0.805)/10;
    selectChannel(11);
    delay(1);
    float temp3 =  analogRead(mux_pin);
    temp3 = (temp3*0.805)/10;

    float tempvalue0 = dht0.getTempFarenheit();
    float tempvalue1 = dht1.getTempFarenheit();
    float tempvalue2 = dht2.getTempFarenheit();
    float tempvalue3 = dht3.getTempFarenheit();
    //Serial.println(String(tempvalue0));
    //Serial.println(String(tempvalue1));
    //Serial.println(String(tempvalue2));
    //Serial.println(String(tempvalue3));

    //if(isnan(temp0)|| isnan(temp1) || isnan(temp2) || isnan(temp3)){
      //
    //}

    temperature = (tempvalue0+tempvalue1+tempvalue2+tempvalue3)/4;
    if (temperature >1){
      lastTemp = (int)temperature;
    }
    // get temperature readings
    float humid0 = dht0.getHumidity();
    float humid1 = dht1.getHumidity();
    float humid2 = dht2.getHumidity();
    float humid3 = dht3.getHumidity();

    humidity = (humid0+humid1+humid2+humid3)/4.0;


    // Light level measurement
    //float temp_measurement = analogRead(temperature_pin);
    //temperature = (temp_measurement*0.805)/10;

    String str = String("sm0,"+String(soil0)+",")+
                  String("sm1,"+String(soil1)+",")+
                  String("sm2,"+String(soil2)+",")+
                  String("sm3,"+String(soil3)+",")+
                  String("temperature,"+String((int)lastTemp)+",")+
                  String("light,"+String(light)+",")+
                  String("humidity,"+String((int)humidity));

    Serial.println("\nConnecting to server...");
    if(client.connect(server,9999)){
      Serial.println("Connected!");
      //POST
      client.println(str);

      //Serial.println("str=" + str);
      //Serial.println("Content-Length: " + String(str.length()));

    }
    else{
      Serial.println("Connection failed.");
    }
    controlStr = "";
    while(flag==0){

      while(client.available()){
        //char c = client.read();
        controlStr = controlStr+String((char)client.read());
        //Serial.write(c);
        flag = 1;
      }

      // Stop client once disconnected
      if(!client.connected()){
        Serial.println();
        Serial.println("Disconnecting.");
        client.stop();
        flag = 1;
      }

    }
    client.stop(); // make sure the client is really stopped
    flag = 0; // reset disconnect flag
    Serial.println(controlStr);

    int l0= controlStr.indexOf(',');
    int l1= controlStr.indexOf(',',l0+1);
    int l2= controlStr.indexOf(',',l1+1);
    int l3= controlStr.indexOf(',',l2+1);
    int l4= controlStr.indexOf(',',l3+1);
    int l5= controlStr.indexOf(',',l4+1);

    setLight(l0);
    setHeat(l0,l1);
    setFan(l1,l2);
    setWater(l2,l3,l4,l5);



    delay(5000);

}
