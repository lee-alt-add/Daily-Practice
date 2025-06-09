package com.assessment;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;

class AssessmentTest {

    @Test
    void testGenerateFibonacciSequence() {
        assertEquals(Collections.emptyList(), Assessment.generateFibonacciSequence(0));
        assertEquals(Collections.emptyList(), Assessment.generateFibonacciSequence(-5));
        assertEquals(List.of(0), Assessment.generateFibonacciSequence(1));
        assertEquals(List.of(0, 1), Assessment.generateFibonacciSequence(2));
        assertEquals(List.of(0, 1, 1, 2, 3), Assessment.generateFibonacciSequence(5));
        assertEquals(List.of(0, 1, 1, 2, 3, 5, 8, 13, 21, 34), Assessment.generateFibonacciSequence(10));
    }

    @Test
    void testIsPalindromeAdvanced() {
        assertTrue(Assessment.isPalindromeAdvanced("madam"));
        assertTrue(Assessment.isPalindromeAdvanced("Race car!"));
        assertTrue(Assessment.isPalindromeAdvanced("A man, a plan, a canal: Panama"));
        assertTrue(Assessment.isPalindromeAdvanced("Was it a car or a cat I saw?"));
        assertTrue(Assessment.isPalindromeAdvanced("No 'x' in Nixon"));
        assertFalse(Assessment.isPalindromeAdvanced("hello"));
        assertFalse(Assessment.isPalindromeAdvanced("Python"));
        assertTrue(Assessment.isPalindromeAdvanced("")); // Empty string
        assertTrue(Assessment.isPalindromeAdvanced("a"));   // Single character
    }

    @Test
    void testFindElementsInMatrixGreaterThanValue() {
        List<List<Integer>> matrix1 = List.of(
                List.of(1, 2, 3),
                List.of(4, 5, 6),
                List.of(7, 8, 9)
        );
        List<Integer> expected1 = List.of(6, 7, 8, 9);
        List<Integer> actual1 = Assessment.findElementsInMatrixGreaterThanValue(matrix1, 5);
        Collections.sort(actual1); // Sort actual as order doesn't matter
        assertEquals(expected1, actual1);

        List<Integer> expected2 = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9);
        List<Integer> actual2 = Assessment.findElementsInMatrixGreaterThanValue(matrix1, 0);
        Collections.sort(actual2);
        assertEquals(expected2, actual2);

        assertEquals(Collections.emptyList(), Assessment.findElementsInMatrixGreaterThanValue(matrix1, 9));

        List<List<Integer>> matrix2 = List.of(List.of(10));
        assertEquals(List.of(10), Assessment.findElementsInMatrixGreaterThanValue(matrix2, 5));
        assertEquals(Collections.emptyList(), Assessment.findElementsInMatrixGreaterThanValue(matrix2, 10));

        List<List<Integer>> emptyMatrix = Collections.emptyList();
        assertEquals(Collections.emptyList(), Assessment.findElementsInMatrixGreaterThanValue(emptyMatrix, 5));

        List<List<Integer>> matrixWithEmptyRow = List.of(Collections.emptyList(), List.of(1,2));
        List<Integer> actual3 = Assessment.findElementsInMatrixGreaterThanValue(matrixWithEmptyRow, 0);
        Collections.sort(actual3);
        assertEquals(List.of(1,2), actual3);
    }

    @Test
    void testFormatNamesList() {
        List<String> names1 = Arrays.asList("Ada Lovelace", "Charles Babbage", "Grace Hopper");
        List<Map<String, String>> expected1 = List.of(
                Map.of("firstName", "Ada", "lastName", "Lovelace"),
                Map.of("firstName", "Charles", "lastName", "Babbage"),
                Map.of("firstName", "Grace", "lastName", "Hopper")
        );
        assertEquals(expected1, Assessment.formatNamesList(names1));

        List<String> names2 = List.of("Alan Turing");
        List<Map<String, String>> expected2 = List.of(
                Map.of("firstName", "Alan", "lastName", "Turing")
        );
        assertEquals(expected2, Assessment.formatNamesList(names2));

        assertEquals(Collections.emptyList(), Assessment.formatNamesList(Collections.emptyList()));

        List<String> names3 = List.of("SingleName"); // Test for names without a space
        List<Map<String, String>> expected3 = List.of(
                Map.of("firstName", "SingleName", "lastName", "")
        );
        assertEquals(expected3, Assessment.formatNamesList(names3));
    }

    @Test
    void testSumDiagonalsSquareMatrix() {
        assertEquals(25, Assessment.sumDiagonalsSquareMatrix(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
        assertEquals(10, Assessment.sumDiagonalsSquareMatrix(new int[][]{{1, 2}, {3, 4}}));
        assertEquals(10, Assessment.sumDiagonalsSquareMatrix(new int[][]{{10}}));
        assertEquals(68, Assessment.sumDiagonalsSquareMatrix(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}}));

        assertEquals(0, Assessment.sumDiagonalsSquareMatrix(null)); // Null matrix
        assertEquals(0, Assessment.sumDiagonalsSquareMatrix(new int[][]{})); // Empty matrix
        assertEquals(0, Assessment.sumDiagonalsSquareMatrix(new int[][]{{1,2,3}, {4,5}})); // Jagged (not square)
        assertEquals(0, Assessment.sumDiagonalsSquareMatrix(new int[][]{{1,2,3}, {4,5,6,7}})); // Jagged (not square)
        assertEquals(0, Assessment.sumDiagonalsSquareMatrix(new int[][]{{1,2}, {3,4}, {5,6}})); // Rectangular (not square)
    }
}