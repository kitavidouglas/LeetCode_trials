public class Day2 {
    public static void main(String[] args) {
        // Example string
        String s = "Hello World";

        // Split the string into words based on spaces
        String[] words = s.split(" ");

        // Retrieve the last word from the array of words
        String lastWord = words[words.length - 1];

        // Calculate the length of the last word
        int lengthOfLastWord = lastWord.length();

        // Print the length of the last word
        System.out.println("Length of the last word: " + lengthOfLastWord); // Output: 5
    }
}
