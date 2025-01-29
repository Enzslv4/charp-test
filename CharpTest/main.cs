using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Digite o nome de quem deseja adicionar: ");
        string name = Console.ReadLine();

        Console.WriteLine("Digite o e-mail desta pessoa: ");
        string email = Console.ReadLine();

        Console.Write("Digite sua idade: ");
        int age = int.Parse(Console.ReadLine());
    }
}
