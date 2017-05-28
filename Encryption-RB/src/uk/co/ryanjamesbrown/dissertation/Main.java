package uk.co.ryanjamesbrown.dissertation;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Main {
	
	@Test
	public void testEncryption() {
		
		System.out.println("Enter message to encrypt here:\n");
		
		//String plaintext = "Our accounts show that the situation in Spain is deteriorating and that the Peninsula is not far from the starvation point. An offer by you to dole out food month by month so long as they keep out of the war might be decisive. Small things do not count now and this is a time for very plain talk to them. The occupation by Germany of both sides of the Straits would be a grievous addition to our naval strain, already severe. The Germans would soon have batteries working by radio direction finding which would close the Straits both by night and day. With a major campaign developing in the Eastern Mediterranean and need of reinforcement and supply of our armies there all round the Cape we could not contemplate any military action on the mainland at or near the Straits. The Rock of Gibraltar will stand a long siege but what is the good of that if we cannot use the harbour or pass the Straits? Once in Morocco the Germans will work South, and U-boats and aircraft will soon be operating from Casablanca and Dakar. I need not, Mr. President, enlarge upon the trouble this will cause to us or approach of trouble to the Western Hemisphere. We must gain as much time as possible.";
		String plaintext = "Oh, misty eye of the mountain below\r\n" + 
				"Keep careful watch of my brothers' souls\r\n" + 
				"And should the sky be filled with fire and smoke\r\n" + 
				"Keep watching over Durin's son\r\n" + 
				"If this is to end in fire\r\n" + 
				"Then we should all burn together\r\n" + 
				"Watch the flames climb high into the night\r\n" + 
				"Calling out for the rope, sent by and we will\r\n" + 
				"Watch the flames burn on and on the mountain side hey\r\n" + 
				"And if we should die tonight\r\n" + 
				"Then we should all die together\r\n" + 
				"Raise a glass of wine for the last time\r\n" + 
				"Calling out for the rope\r\n" + 
				"Prepare as we will\r\n" + 
				"Watch the flames burn on and on the mountain side\r\n" + 
				"Desolation comes upon the sky\r\n" + 
				"Now I see fire, inside the mountain\r\n" + 
				"I see fire, burning the trees\r\n" + 
				"And I see fire, hollowing souls\r\n" + 
				"And I see fire, blood in the breeze\r\n" + 
				"And I hope that you'll remember me\r\n" + 
				"Oh, should my people fall\r\n" + 
				"Then surely I'll do the same\r\n" + 
				"Confined in mountain halls\r\n" + 
				"We got too close to the flame\r\n" + 
				"Calling out father hold fast and we will\r\n" + 
				"Watch the flames burn on and on the mountain side\r\n" + 
				"Desolation comes upon the sky\r\n" + 
				"Now I see fire, inside the mountain\r\n" + 
				"I see fire, burning the trees\r\n" + 
				"And I see fire, hollowing souls\r\n" + 
				"And I see fire, blood in the breeze\r\n" + 
				"And I hope that you'll remember me\r\n" + 
				"And if the night is burning\r\n" + 
				"I will cover my eyes\r\n" + 
				"For if the dark returns then\r\n" + 
				"My brothers will die\r\n" + 
				"And as the sky's falling down\r\n" + 
				"It crashed into this lonely town\r\n" + 
				"And with that shadow upon the ground\r\n" + 
				"I hear my people screaming out\r\n" + 
				"Now I see fire, inside the mountain\r\n" + 
				"I see fire, burning the trees\r\n" + 
				"And I see fire, hollowing souls\r\n" + 
				"And I see fire, blood in the breeze\r\n" + 
				"I see fire, oh you know I saw a city burning (fire)\r\n" + 
				"And I see fire, feel the heat upon my skin (fire)\r\n" + 
				"And I see fire (fire)\r\n" + 
				"And I see fire (burn on and on and mountains side)\r\n" + 
				"";
		Encryption encrypt = new Encryption(plaintext);
		String encryptedMessage = encrypt.getEncryptedMessage().toString();
		
		System.out.println("Plain Text:\t" + encrypt.getPlainText() +"\n\nEncrypted Message:\t" + encryptedMessage);
		
		assertEquals(encryptedMessage, "KCESVQBQVGKLVBSBUSMHUAAVLNOGEWAAGGCWQA");
	}
}
