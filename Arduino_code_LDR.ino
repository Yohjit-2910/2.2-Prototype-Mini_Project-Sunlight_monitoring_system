// Define the analog pin for the LDR
const int ldrPin = A0;


void setup() {
  // Start serial communication for debugging
  Serial.begin(9600);
}

void loop() {
  // Read analog value from LDR
  int ldrValue = analogRead(ldrPin);
  
  // Map the analog value to the sunlight intensity range (adjust min and max values as needed)
  float sunlightIntensity = map(ldrValue, 0, 1023, 0, 100);
  
  // Print the sunlight intensity to Serial Monitor
  Serial.print("Sunlight Intensity: ");
  Serial.print(sunlightIntensity);
  Serial.println("%");

  // Add a short delay before the next reading (adjust as needed)
  delay(500);
}
