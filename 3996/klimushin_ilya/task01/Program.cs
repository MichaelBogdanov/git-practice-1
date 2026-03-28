using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string text = File.ReadAllText(args[0]);
        Console.WriteLine(Check(text) ? "YES" : "NO");
    }

    static bool Check(string s)
    {
        Stack<char> stack = new Stack<char>();
        foreach (char c in s)
        {
            if (c == '(' || c == '[' || c == '{')
                stack.Push(c);
            else if (c == ')' || c == ']' || c == '}')
            {
                if (stack.Count == 0) return false;
                char last = stack.Pop();
                if (c == ')' && last != '(') return false;
                if (c == ']' && last != '[') return false;
                if (c == '}' && last != '{') return false;
            }
        }
        return stack.Count == 0;
    }
}
