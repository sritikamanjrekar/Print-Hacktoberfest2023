import java.util.Arrays;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {

    // create an object of Scanner class
    Scanner input = new Scanner(System.in);

    // take input from users
    System.out.print("Enter first String: ");
    String str1 = input.nextLine();
    System.out.print("Enter second String: ");
    String str2 = input.nextLine();

    // check if length is same
    if(str1.length() == str2.length()) {

      // convert strings to char array
      char[] charArray1 = str1.toCharArray();
      char[] charArray2 = str2.toCharArray();

      // sort the char array
      Arrays.sort(charArray1);
      Arrays.sort(charArray2);

      // if sorted char arrays are same
      // then the string is anagram
      boolean result = Arrays.equals(charArray1, charArray2);

      if(result) {
        System.out.println(str1 + " and " + str2 + " are anagram.");
      }
      else {
        System.out.println(str1 + " and " + str2 + " are not anagram.");
      }
    }
    else {
      System.out.println(str1 + " and " + str2 + " are not anagram.");
    }

    input.close();
  }
}
