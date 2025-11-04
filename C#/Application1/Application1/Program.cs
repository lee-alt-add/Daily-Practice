using System;

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

    static void Main()
    {
        Practice practice = new Practice();
        Console.WriteLine(practice.countVowels("lindokuhle"));
    }
}