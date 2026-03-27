using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Zadacha4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = ""; 
            string content = File.ReadAllText(path);
            string[] items = content.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            HashSet<string> seen = new HashSet<string>();
            List<string> result = new List<string>();
            foreach (string item in items)
            {
                if (!seen.Contains(item))
                {
                    seen.Add(item);
                    result.Add(item);
                }
            }
            Console.WriteLine(string.Join(" ", result));
            File.WriteAllText("output.txt", string.Join(" ", result));
        }
    }
}