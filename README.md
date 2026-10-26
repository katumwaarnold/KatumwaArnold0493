# KatumwaArnold0493
Excercises  ' Store student marks in the text file used streamWriter
    Using writer As New StreamWriter(fileName, False)
        writer.WriteLine("ST001, Shaminah, 85")
        writer.WriteLine("ST002, Mahoro, 84")
        writer.WriteLine("ST003, Saum, 82")
        writer.WriteLine("ST004, Henry, 95")
    End Using
    Console.WriteLine("Student marks saved successfully!")
    Console.WriteLine()
    ' Read student marks
    Console.WriteLine("STUDENT NO  NAME   MARKS")
    Console.WriteLine("---------------------------")

    ' Using StreamReader
    Using reader As New StreamReader(fileName)
        Dim line As String
        ' Reade each line until the end of the file
        Do
            line = read.ReadLine()
            If line Is Nothing Then
                Exit Do
            End If
            ' Display the student record
            console.writeLine(line)
        Loop
    End using
    ' Keep console open until the user presses Enter Kex on Keyboard
    Console.WriteLine()
    Console.WriteLine("Press Enter to exit.")
    Console.WriteLine()
End Sub
End Module

09:36


Import System.IO
Module Program
Sub Main()
' Name the text file
Dim fileName As String = "StudentMarks.txt"

    ' Store student marks in the text file used streamWriter
    Using writer As New StreamWriter(fileName, False)
        writer.WriteLine("ST001, Shaminah, 85")
        writer.WriteLine("ST002, Mahoro, 84")
        writer.WriteLine("ST003, Saum, 82")
        writer.WriteLine("ST004, Henry, 95")
    End Using
    Console.WriteLine("Student marks saved successfully!")
    Console.WriteLine()
    ' Read student marks
    Console.WriteLine("STUDENT NO  NAME   MARKS")
    Console.WriteLine("---------------------------")

    ' Using StreamReader
    Using reader As New StreamReader(fileName)
        Dim line As String
        ' Reade each line until the end of the file
        Do
            line = read.ReadLine()
            If line Is Nothing Then
                Exit Do
            End If
            ' Display the student record
            console.writeLine(line)
        Loop
    End using
    ' Keep console open until the user presses Enter Kex on Keyboard
    Console.WriteLine()
    Console.WriteLine("Press Enter to exit.")
    Console.WriteLine()
End Sub
End Module

09:36
