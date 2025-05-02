package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
package Week1;

public class EqualStrings {

    public int minOperations(String s1, String s2, String s3) {
        int len1 = s1.length(), len2 = s2.length(), len3 = s3.length();
        int maxLen = Math.max(len1, Math.max(len2, len3));
        
        // Pad the strings with empty characters to make their lengths equal
        s1 = padString(s1, maxLen);
        s2 = padString(s2, maxLen);
        s3 = padString(s3, maxLen);
        
        int operations = 0;
        for (int i = maxLen - 1; i >= 0; i--) {
            char c1 = s1.charAt(i), c2 = s2.charAt(i), c3 = s3.charAt(i);
            
            // If all characters are equal, continue to the next character
            if (c1 == c2 && c2 == c3) continue;
            
            // If any character is different, increment the operations count
            operations++;
            
            // If any string is already empty, return -1
            if (c1 == ' ' || c2 == ' ' || c3 == ' ') return -1;
            
            // Otherwise, delete the rightmost character of the longest string
            if (len1 == maxLen) s1 = s1.substring(0, i);
            else if (len2 == maxLen) s2 = s2.substring(0, i);
            else s3 = s3.substring(0, i);
        }
        
        return operations;
    }
    
    // Pad the string with empty characters to make its length equal to maxLen
    private String padString(String s, int maxLen) {
        StringBuilder sb = new StringBuilder(s);
        while (sb.length() < maxLen) {
            sb.append(' ');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        EqualStrings solution = new EqualStrings();
        
        // Example usage:
        String s1 = "abc", s2 = "ab", s3 = "abcd";
        System.out.println(solution.minOperations(s1, s2, s3)); // Output: 1
    }
}
