using System.Diagnostics;
Console.ForegroundColor = ConsoleColor.Red;
try
{
    string currentDir = Environment.CurrentDirectory;

    var psi = new ProcessStartInfo
    {
        FileName = "python",
        Arguments = $"{currentDir}\\DownMac.py",
        UseShellExecute = true,
        RedirectStandardOutput = false,
        RedirectStandardError = false,
        RedirectStandardInput = false
    };

    Process.Start(psi);
}

catch (Exception ex)
{
    Console.WriteLine($"If you see this, please install python\n\n{ex}");
    Console.ReadKey();
}



