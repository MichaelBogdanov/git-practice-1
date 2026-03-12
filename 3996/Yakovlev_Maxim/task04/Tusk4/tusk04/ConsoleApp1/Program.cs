string text = File.ReadAllText("file.txt");
string[] elements = text.Split(' ');

List<string> unique = new List<string>();

for (int i = 0; i < elements.Length; i++)
{
    if (!unique.Contains(elements[i]))
    {
        unique.Add(elements[i]);
    }
}

File.WriteAllText("output.txt", string.Join(" ", unique));