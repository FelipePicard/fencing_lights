const int left_led = 4;
const int right_led = 3;
int message = 0;

void setup() {
  Serial.begin(9600);
  pinMode(left_led, OUTPUT);
  pinMode(right_led, OUTPUT);
}

void loop() {
  
  if(Serial.available() > 0){
    message = Serial.read();
  }
  if(message == '1'){
    digitalWrite(left_led, HIGH);
    delay(3000);
    digitalWrite(left_led, LOW);
  }
  
  if(message == '2'){
    digitalWrite(right_led, HIGH);
    delay(3000);
    digitalWrite(right_led, LOW);
  }
  
  if(message == '3'){
    digitalWrite(right_led, HIGH);
    digitalWrite(left_led, HIGH);
    delay(3000);
    digitalWrite(left_led, LOW);
    digitalWrite(right_led, LOW);
  }

  else{
    digitalWrite(left_led, LOW);
    digitalWrite(right_led, LOW);
  }
}