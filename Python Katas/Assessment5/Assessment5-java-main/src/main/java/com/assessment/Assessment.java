package com.assessment;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Collections;

public class Assessment {

    /**
     * Generates the first n numbers in the Fibonacci sequence.
     * The Fibonacci sequence starts with 0 and 1.
     * Example: n=5 -> [0, 1, 1, 2, 3]
     *          n=1 -> [0]
     *          n=0 -> []
     *
     * @param n The number of Fibonacci numbers to generate. Must be non-negative.
     * @return A List containing the first n Fibonacci numbers.
     *         Returns an empty list if n is 0 or negative.
     * Learning Outcomes: Methods, Loops (1D), Control Flow, Data Structures (Lists), Problem-solving.
     */
    public static List<Integer> generateFibonacciSequence(int n) {
        // TODO: Implement this method
        return Collections.emptyList();

    }

    /**
     * Checks if a given string is a palindrome, ignoring case, spaces, and punctuation.
     * A palindrome is a word, phrase, number, or other sequence of characters
     * that reads the same backward as forward.
     *
     * @param text The string to check.
     * @return True if the text is a palindrome after cleaning, False otherwise.
     * Learning Outcomes: Methods, String Manipulation, Loops, Control Flow, Problem-solving.
     * Hint: Consider using StringBuilder and Character.isLetterOrDigit().
     */
    public static boolean isPalindromeAdvanced(String text) {
        // TODO: Implement this method
        return false;
    }

    /**
     * Given a matrix (List of Lists of Integers) and a value, returns a list
     * of all elements in the matrix that are strictly greater than the given value.
     * The order of elements in the returned list does not matter.
     *
     * @param matrix The input matrix (List of Lists of Integers).
     * @param value  The threshold value.
     * @return A List of Integers from the matrix that are greater than 'value'.
     *         Returns an empty list if the matrix is empty or no elements are greater.
     * Learning Outcomes: Methods, Loops (2D - nested), Control Flow, Data Structures (Lists).
     */
    public static List<Integer> findElementsInMatrixGreaterThanValue(List<List<Integer>> matrix, int value) {
        // TODO: Implement this method
        return Collections.emptyList();
    }

    /**
     * Takes a list of strings, where each string is a full name "FirstName LastName".
     * Returns a new list of Maps, where each Map has keys
     * "firstName" and "lastName" with the corresponding values.
     * <p>
     * Example: ["Ada Lovelace", "Charles Babbage"] ->
     *          [{"firstName": "Ada", "lastName": "Lovelace"},
     *           {"firstName": "Charles", "lastName": "Babbage"}]
     *
     * @param namesList A List of full names.
     * @return A List of Maps, each representing a parsed name.
     *         Returns an empty list if the input list is empty.
     *         Assumes valid "FirstName LastName" format for each string.
     *         If a name does not contain a space, the full name becomes "firstName" and "lastName" is empty.
     * Learning Outcomes: Methods, Loops (1D), String Manipulation (split), Data Structures (Lists, Maps).
     */
    public static List<Map<String, String>> formatNamesList(List<String> namesList) {
        // TODO: Implement this method
        return Collections.emptyList();
    }

    /**
     * Calculates the sum of the elements on the main diagonal and the anti-diagonal
     * of a square matrix (represented as a 2D integer array int[][]).
     * - Main diagonal: (0,0), (1,1), (2,2), ...
     * - Anti-diagonal: (0,n-1), (1,n-2), ..., (n-1,0)
     * If the matrix has an odd dimension, the center element (which is on both diagonals)
     * should only be counted once in the total sum.
     *
     * @param matrix A square 2D integer array.
     * @return The sum of the diagonal elements.
     *         Returns 0 if the matrix is null, empty, or not square.
     *         A matrix is not square if its rows have different lengths or
     *         the number of rows is not equal to the number of columns in the first row.
     * Learning Outcomes: Methods, Loops (1D or 2D), Control Flow, Data Structures (2D arrays), Problem-solving.
     */
    public static int sumDiagonalsSquareMatrix(int[][] matrix) {
        // TODO: Implement this method
        return 0;
    }
}