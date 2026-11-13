' AI-assisted correction of the student marks example in the repository README.
Option Strict On
Option Explicit On

Imports System
Imports System.IO

Module Program
    Sub Main()
        ' Relative to the process's current working directory.
        Dim fileName As String = "StudentMarks.txt"

        Try
            Dim newFile As FileStream = Nothing
            Try
                ' Atomic create: do not truncate or replace an existing file.
                newFile = New FileStream(fileName, FileMode.CreateNew, FileAccess.Write, FileShare.None)
            Catch ex As IOException When File.Exists(fileName)
                Console.WriteLine("Existing StudentMarks.txt preserved; displaying its contents.")
            End Try

            If newFile IsNot Nothing Then
                Using writer As New StreamWriter(newFile)
                    writer.WriteLine("ST001, Shaminah, 85")
                    writer.WriteLine("ST002, Mahoro, 84")
                    writer.WriteLine("ST003, Saum, 82")
                    writer.WriteLine("ST004, Henry, 95")
                End Using
                Console.WriteLine("Student marks saved successfully!")
            End If

            Console.WriteLine()
            Console.WriteLine("STUDENT NO  NAME   MARKS")
            Console.WriteLine("---------------------------")
            Using reader As New StreamReader(fileName)
                Dim line As String = reader.ReadLine()
                While line IsNot Nothing
                    Console.WriteLine(line)
                    line = reader.ReadLine()
                End While
            End Using
        Catch ex As IOException
            Console.Error.WriteLine("File error: " & ex.Message)
            Environment.ExitCode = 1
        Catch ex As UnauthorizedAccessException
            Console.Error.WriteLine("Access error: " & ex.Message)
            Environment.ExitCode = 1
        End Try

        Console.WriteLine()
        Console.WriteLine("Press Enter to exit.")
        Console.ReadLine()
    End Sub
End Module
