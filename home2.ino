float temp;
int tempPin = 0;
float light;
int lightPin = 1;
int usr_in;

void setup(){
	pinMode (13, OUTPUT);
	Serial.begin(9600);
}

void loop(){
	Serial.available();
	usr_in = Serial.read();

	switch (usr_in){
		
		case '0':
      		digitalWrite(13, LOW);
      		Serial.println("Light OFF!");
      		break;

		case '1':
			digitalWrite(13, HIGH);            
      		Serial.println("Light ON!");
      		break;

		case '3':
			temp = analogRead(tempPin);
			temp = ( 5.0 * temp * 100 ) / 1024;
			Serial.print("TEMPERATURE = ");
			Serial.print(temp);
			Serial.println();
			delay(1000);
			break;

		case '4':
			light = analogRead(lightPin);
			Serial.print("LIGHT = ");
			Serial.print(light);
			Serial.println();
			delay(1000);
			break;
	}
}