package Week3;

import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        if (numRows <= 0)
            return triangle;

        // Adding the first row with a single element 1
        triangle.add(new ArrayList<>());
        triangle.get(0).add(1);

        // Generating subsequent rows
        for (int rowNum = 1; rowNum < numRows; rowNum++) {
            List<Integer> row = new ArrayList<>();
            List<Integer> prevRow = triangle.get(rowNum - 1);

            // The first element of each row is always 1
            row.add(1);

            // Calculate each element of the current row
            for (int j = 1; j < rowNum; j++) {
                row.add(prevRow.get(j - 1) + prevRow.get(j));
            }

            // The last element of each row is always 1
            row.add(1);

            // Add the current row to the triangle
            triangle.add(row);
        }

        return triangle;
    }

    public static void main(String[] args) {
        int numRows = 5;
        List<List<Integer>> pascalTriangle = generate(numRows);

        // Printing the generated Pascal's triangle
        for (List<Integer> row : pascalTriangle) {
            System.out.println(row);
        }
    }
}
