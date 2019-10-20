int clkPin = 53;
int lastClk = LOW;
int clk;
int pwm1Pin = 13;
int pwm2Pin = 12;
int pwm3Pin = 11;
int pwm4Pin = 9;

void setup() {
  // put your setup code here, to run once:
  pinMode(clkPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  clk = digitalRead(clkPin);
  if (clk != lastClk && clk == HIGH) {
    // Happens at clock pulse
    analogWrite(pwm1Pin, random(255));
    analogWrite(pwm2Pin, random(255));
    analogWrite(pwm3Pin, random(255));
    analogWrite(pwm4Pin, random(255));
  }
  lastClk = clk;
}
