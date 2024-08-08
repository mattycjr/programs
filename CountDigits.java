/** Count each digit from 1 to whatever number you like...

	Not very efficient, but it works....good up until you hit the billions.


	The Second set of code at the bottom is more efficient thanks to Adam Watters!
  */

import java.io.*;
import java.util.*;


class CountDigits {
	
			
		
	public static int gotonum = 1000000;
	public static int numLen;

	public static void main(String[] args) {
		int ones = 0;
		int twos = 0;
		int threes = 0;
		int fours = 0;
		int fives = 0;
		int sixes = 0;
		int sevens = 0;
		int eights = 0;
		int nines = 0;    
		int zeroes = 0;
	
		System.out.println("\n\n1 to " + gotonum + "\n");
	
	// Initial loop for counting from 1 to whatever number....	
		for (int k = 1; k <= gotonum; k++) {
		   
		   // Turns the number to be counted into a string, gets the length, and puts it in an array.	
			numLen = Integer.toString(k).length();
			String digits = Integer.toString(k);
			char[] arr = digits.toCharArray();


		   //	System.out.println(arr);                       // Testing purposes
		   //	int i = Integer.parseInt(numLen);		// Testing purposes
			
		   // For loop to check each individual digit and compare below	
			for (int j = 0; j <= numLen-1; j++) {
				int i = Integer.parseInt(arr[j] + "");
			

				if (i==1) { ones++;}
				else if (i==2){twos++;}
			/*	else if (i==3){threes++;}
				else if (i==4){fours++;}
				else if (i==5){fives++;}
				else if (i==6){sixes++;}
				else if (i==7){sevens++;}
				else if (i==8){eights++;}
				else if (i==9){nines++;}     */
				else if (i==0){zeroes++;}
			}
			//System.out.println("X = " + i);
		}
		System.out.println("0 = " + zeroes);
		System.out.println("1 = " + ones);
		System.out.println("2-9 = " + twos);
	/*	System.out.println("3 = " + threes);
		System.out.println("4 = " + fours);
		System.out.println("5 = " + fives);
		System.out.println("6 = " + sixes);
		System.out.println("7 = " + sevens);
		System.out.println("8 = " + eights);
		System.out.println("9 = " + nines);  */

/****************************
	  ADAM WATTERS CODE BELOW.....TRANSLATED TO JAVA BY ME!
*****************************/

		System.out.println("\n" + "Watters Code now!");
  		
		int onesW = 0;
		int twosW = 0;
		int zeroesW = 0;
		
		for (int p = 1; p <= gotonum; p++) {
			numLen = Integer.toString(p).length();
			int place = 10;
			int r = 0;

			for ( int q = 1; q <= numLen; q++) {
				if (q == 1) { r = p % 10; }
				else  { r = (p/place)%10; 
					place *= 10;      }
				
				if (r==1) { onesW++;}
				else if (r==2){twosW++;}
				else if (r==0){zeroesW++;}

			}
						
		}
		System.out.println("0 = " + zeroesW);
		System.out.println("1 = " + onesW);
		System.out.println("2-9 = " + twosW);
	}
	
}

