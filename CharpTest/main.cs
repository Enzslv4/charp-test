using System;
using System.Collections.Generic;

class Program
{
    class User
    {
        public string Name { get; set; }
        public string Email { get; set; }
        public int Age { get; set; }

        public override string ToString()
        {
            return $"Nome: {Name}, E-mail: {Email}, Idade: {Age}";
        }
    }

    static void Main(string[] args)
    {
        List<User> users = new List<User>();
        int option;

        do
        {
            Console.WriteLine("\n=== Menu ===");
            Console.WriteLine("1. Cadastrar Usuário");
            Console.WriteLine("2. Listar Usuários");
            Console.WriteLine("3. Buscar Usuário");
            Console.WriteLine("0. Sair");
            Console.Write("Escolha uma opção: ");
            option = int.Parse(Console.ReadLine());

            switch (option)
            {
                case 1:
                    RegisterUser(users);
                    break;
                case 2:
                    ListUsers(users);
                    break;
                case 3:
                    SearchUsers(users);
                    break;
                case 0:
                    Console.WriteLine("Saindo da aplicação...");
                    break;
                default:
                    Console.WriteLine("Opção inválida! Tente novamente.");
                    break;
            }
        } while (option != 0);
    }

    static void RegisterUser(List<User> usuarios)
    {
        Console.WriteLine("\n=== Cadastro de Usuário ===");
        Console.Write("Digite o nome: ");
        string name = Console.ReadLine();

        Console.Write("Digite o e-mail: ");
        string email = Console.ReadLine();

        Console.Write("Digite a idade: ");
        int age = int.Parse(Console.ReadLine());

        usuarios.Add(new User { Name = name, Email = email, Age = age });

        Console.WriteLine("Usuário cadastrado com sucesso!");
    }

    static void ListUsers(List<User> users)
    {
        Console.WriteLine("\n=== Lista de Usuários ===");

        if (users.Count == 0)
        {
            Console.WriteLine("Nenhum usuário cadastrado.");
        }
        else
        {
            foreach (var user in users)
            {
                Console.WriteLine(user);
            }
        }
    }

    static void SearchUsers(List<User> users)
    {
        Console.WriteLine("\n=== Buscar Usuário ===");
        Console.Write("Digite o nome do usuário: ");
        string searchName = Console.ReadLine();

        // Procura o usuário na lista pelo nome
        var foundUser = users.Find(u => u.Name.Equals(searchName, StringComparison.OrdinalIgnoreCase));

        if (foundUser != null)
        {
            Console.WriteLine("Usuário encontrado:");
            Console.WriteLine(foundUser);
        }
        else
        {
            Console.WriteLine("Usuário não encontrado.");
        }
    }
}
