package uk.co.ryanjamesbrown.dissertation;

public class Encryption {
	
	private String plaintext;
	private String key = "WINSTON"; //change key for the testing
	
	//start of the alphabet 'A' in the ASCII.
	private static final int ASCII_UPPERCASE = 65;
	
	private StringBuilder encryptedMessage;
	
	Encryption(String plaintext) {
		
		this.plaintext = plaintext.toUpperCase();
		this.encryptedMessage = new StringBuilder();
		
		startEncryption();
	}
	
	public void setPlainText(String plnText){
		
		this.encryptedMessage = new StringBuilder();
		this.plaintext = plnText.toUpperCase();
	}
	
	private void startEncryption() { 
		
		// Ci = Ti + Ki (mod 25)
		
		int keyNum = 0;

		//running through message characters
		for(int i = 0; i < plaintext.length(); i++){
			
			//gets the character at the specific point of message
			char plnTxt = plaintext.charAt(i);
			
			int convertASCII = (int) plnTxt;
			int plnTextNum = convertASCII - ASCII_UPPERCASE;
			
			char currentKey = key.charAt(keyNum);
			
			int convert_ASCII_key = (int) currentKey;
			int indexOfKey = convert_ASCII_key - ASCII_UPPERCASE;
			
			if(convertASCII >= 65 && convertASCII <= 90) {
				
				shiftLetters(plnTextNum, indexOfKey);
				
				if(keyNum < key.length()-1) {
					keyNum = keyNum + 1;
				} else {
					//reset
					keyNum = 0;
				}
			} 
		}
	}
	
	private void shiftLetters(int plainText, int key) {
		
		//	Ci = (Pi + Ki) mod 26;
		int newLetter = (plainText + key) % 26;
		
		int getAscii_letter = (newLetter + ASCII_UPPERCASE);
		char encryptedCharacter = (char) getAscii_letter;

		encryptedMessage.append(encryptedCharacter);
	}
	
	public StringBuilder getEncryptedMessage() {
		return encryptedMessage;
	}
	
	public String getKey() {
		return key;
	}
	
	public String getPlainText() {
		return plaintext;
	}

}
