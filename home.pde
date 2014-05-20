void setup(){
	pinMode (13, OUTPUT);
	Serial.begin(9600);
}

void loop (){
	int temp_val, light_val;
	Serial.available();
	int usr_in = Serial.read();

	switch (usr_in){
		
		case '0':
      		digitalWrite(13, LOW);
      		Serial.println("Light OFF!");
      		break;

		case '1':
			digitalWrite(13, HIGH);            
      		Serial.println("Light ON!");
      		break;

		case '4':
			temp_val = analogRead(A0);
			Serial.println(( 5.0 * temp_val * 100) / 1024);
			break;

		case '5':
			light_val = analogRead(A1);
			if (light_val < 10) {
				Serial.println("Very Dark!");
			} else if(light_val < 200){
				Serial.println ("Dark!");
			}else if(light_val < 500){
				Serial.println("Medium");
			}else if(light_val < 800){
				Serial.println("Lightness!");
			}else{
				Serial.println("Very Lightness!");
			}
			break;

		default:
			Serial.println(light_val);
			Serial.println(temp_val);
	}
}


