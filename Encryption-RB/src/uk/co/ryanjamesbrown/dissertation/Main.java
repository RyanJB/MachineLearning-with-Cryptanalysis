package uk.co.ryanjamesbrown.dissertation;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Main {
	
	@Test
	public void testEncryption() {
		
		System.out.println("Enter message to encrypt here:\n");
		
		//String plaintext = "Our accounts show that the situation in Spain is deteriorating and that the Peninsula is not far from the starvation point. An offer by you to dole out food month by month so long as they keep out of the war might be decisive. Small things do not count now and this is a time for very plain talk to them. The occupation by Germany of both sides of the Straits would be a grievous addition to our naval strain, already severe. The Germans would soon have batteries working by radio direction finding which would close the Straits both by night and day. With a major campaign developing in the Eastern Mediterranean and need of reinforcement and supply of our armies there all round the Cape we could not contemplate any military action on the mainland at or near the Straits. The Rock of Gibraltar will stand a long siege but what is the good of that if we cannot use the harbour or pass the Straits? Once in Morocco the Germans will work South, and U-boats and aircraft will soon be operating from Casablanca and Dakar. I need not, Mr. President, enlarge upon the trouble this will cause to us or approach of trouble to the Western Hemisphere. We must gain as much time as possible.";
		String plaintext = "Why is it we are here. we could be in the other solutions"; 

		Encryption encrypt = new Encryption(plaintext);
		String encryptedMessage = encrypt.getEncryptedMessage().toString();
		
		System.out.println("Plain Text:\t" + encrypt.getPlainText() +"\n\nEncrypted Message:\t" + encryptedMessage);
		
		assertEquals(encryptedMessage, "KCESVQBQVGKLVBSBUSMHUAAVLNOGEWAAGGCWQA");
	}
}
