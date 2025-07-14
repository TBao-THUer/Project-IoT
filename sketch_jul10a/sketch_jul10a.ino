int buzzerPin = 8;
char incomingByte;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);  // Must match Python baud rate
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();

    if (incomingByte == '1') {
      digitalWrite(buzzerPin, HIGH); // Drowsy detected - buzzer ON
    } else if (incomingByte == '0') {
      digitalWrite(buzzerPin, LOW);  // Not drowsy - buzzer OFF
    }
  }
}
