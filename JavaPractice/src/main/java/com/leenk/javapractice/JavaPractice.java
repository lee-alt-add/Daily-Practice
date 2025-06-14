/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.leenk.javapractice;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 *
 * @author Other Leenks
 */
public class JavaPractice {

    public static void main(String[] args) {
//        System.out.println("FizzBuzz: " + FizzBuzz(20));
//        FizzBuzz1(20);
//        System.out.println("fibonnaciSequence: " + fibonnaciSequence(7));
        System.out.println("isPalindrome: " + isPalindrome("A man, a plan, a canal: Panama"));
    }
    
    public static List<String> FizzBuzz(int n) {
        return IntStream.rangeClosed(1, n).mapToObj(i -> i % 3 == 0 && i % 5 == 0 ? "FizzBuzz" :
                                                  i % 3 == 0 ? "Fizz" :
                                                  i % 5 == 0 ? "Buzz" :
                                                  String.valueOf(i))
                .collect(Collectors.toList());
    }
    
    public static void FizzBuzz1(int n) {
        IntStream.rangeClosed(1, n)
                .mapToObj(i -> i % 3 == 0 && i % 5 == 0 ? "FizzBuzz":
                          i % 3 == 0 ? "Fizz":
                          i % 5 == 0 ? "Buzz" :
                          String.valueOf(i))
                .forEach(System.out::println);
    }
    
    public static String fibonnaciSequence(int n) {
        List<Integer> fibList = new ArrayList<>(List.of(0,1));
        
        for (int i = 2; i < n; i++) {
            fibList.add(fibList.get(i - 1) + fibList.get(i - 2));
        }
        
        return String.join(" ", fibList.stream()
                .map(i -> String.valueOf(i))
                .collect(Collectors.toList()));
    }
    
    public static boolean isPalindrome(String string) {
        String str = string.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        StringBuilder sb = new StringBuilder(str);
        return str.equals(sb.reverse().toString());
    }
    
    public static String reverseString(String str) {
        StringBuilder sb = new StringBuilder(str);
        return sb.reverse().toString();
    }
}
