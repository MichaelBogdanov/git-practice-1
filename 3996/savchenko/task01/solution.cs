using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string s = Console.ReadLine();
        Stack<char> stack = new Stack<char>();
        bool ok = true;

        foreach (char c in s)
        {
            if (c == '(') stack.Push(')');
            else if (c == '[') stack.Push(']');
            else if (c == '{') stack.Push('}');
            else if (c == ')' || c == ']' || c == '}')
            {
                if (stack.Count == 0 || stack.Pop() != c)
                {
                    ok = false;
                    break;
                }
            }
        }
        if (stack.Count > 0) ok = false;
        Console.WriteLine(ok ? "YES" : "NO");
    }
}
