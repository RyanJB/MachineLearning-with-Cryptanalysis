package uk.co.ryanjamesbrown.dissertation;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class TestEncryption {

	public static void main(String[] args) {

		Result encrypted = JUnitCore.runClasses(Main.class);
		
		for(Failure fail : encrypted.getFailures()){
			System.out.println(fail.toString());
		}
		
		System.out.println("\nThe encryption was successful (TRUE) or failed (FALSE):\t" + encrypted.wasSuccessful());
	}

}
