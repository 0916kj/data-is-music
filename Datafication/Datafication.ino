int clkPin = 53;
int lastClk = LOW;
int clk;
int pwm1Pin = 13;
int pwm2Pin = 12;
int pwm3Pin = 11;
int pwm4Pin = 9;
int temp = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(clkPin, INPUT);
  pinMode(pwm1Pin, OUTPUT);
  pinMode(pwm2Pin, OUTPUT);
  pinMode(pwm3Pin, OUTPUT);
  pinMode(pwm4Pin, OUTPUT);
  Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  clk = digitalRead(clkPin);
  if (clk != lastClk && clk == HIGH) {
    // Happens at clock pulse
    Serial.write(0);
    while (Serial.available() < 4) {
      // Wait for available data
    }
    temp = Serial.read();
    analogWrite(pwm1Pin, temp);
    analogWrite(pwm2Pin, Serial.read());
    analogWrite(pwm3Pin, Serial.read());
    analogWrite(pwm4Pin, Serial.read());
  }
  lastClk = clk;
}
