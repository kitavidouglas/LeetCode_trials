package Week1;

import java.util.*;

public class roman_to_int {
    public static int romanToInt(String s) {
        HashMap<Character, Integer> romanValues = new HashMap<>();
        romanValues.put('I', 1);
        romanValues.put('V', 5);
        romanValues.put('X', 10);
        romanValues.put('L', 50);
        romanValues.put('C', 100);
        romanValues.put('D', 500);
        romanValues.put('M', 1000);
        
        int total = 0;
        int prevValue = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            int value = romanValues.get(currentChar);
            
            if (value > prevValue && prevValue != 0) {
                total += value - 2 * prevValue;
            } else {
                total += value;
            }
            
            prevValue = value;
        }
        
        return total;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a Roman numeral: ");
        String romanNumeral = scanner.nextLine().toUpperCase();
        scanner.close();

        int result = romanToInt(romanNumeral);
        if (result != -1) {
            System.out.println("The integer value of " + romanNumeral + " is: " + result);
        } else {
            System.out.println("Invalid Roman numeral entered!");
        }
    }
}
