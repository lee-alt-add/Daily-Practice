using System;
using System.Linq;

public class Practice
{

    public int addNumbers(int a, int b)
    {
        return a + b;
    }

    public string greet(string name)
    {
        return $"Hello, {name}";
    }

    public string reverseString(string original)
    {

        char[] chars = original.ToCharArray();
        Array.Reverse(chars);
        return new string(chars);
    }

    public int findLargest(int[] numbers)
    {
        int largest = 0;
        foreach (int i in numbers)
        {
            if (i > largest)
            {
                largest = i;
            }
        }
        return largest;
    }
    
    public int countVowels(string originalString)
    {
        int output = 0;
        foreach (char i in originalString)
        {
            if ("aeiouAEIOU".Contains(i))
            {
                output++;
            }
        }

        return output;
    }

    public bool isPalindrome(string str)
    {
        char[] charArray = str.ToCharArray();
        Array.Reverse(charArray);
        return str == new string(charArray);
    }

    public double getAvarage(int[] numbers)
    {
        return numbers.Average();
    }

    public int countWords(string sentence)
    {
        return sentence.Split(' ').Length;
    }
    static void Main()
    {
        Practice practice = new Practice();
        Console.WriteLine(practice.countVowels("lindokuhle"));
        Console.WriteLine(practice.addNumbers(5, 10));
        Console.WriteLine(practice.greet("Lindo"));
        Console.WriteLine(practice.reverseString("hello"));
        Console.WriteLine(practice.findLargest(new int[] { 1, 5, 3, 9, 2 }));
    }
}