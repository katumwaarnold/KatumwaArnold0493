# Student marks — AI-assisted correction for review

This source and its tests/notes were prepared with AI assistance. The source is a standalone correction of the student marks example in the repository's root README at commit `eca35035d000c44a156e9399ab8869f2bbd3589f`. That example has duplicated/incomplete text and transcription mistakes such as `Import` and `read.ReadLine()`. This proposal does not modify the original README or the unrelated forex form `stuvb.VB.txt` and does not restore or prove a complete application.

## Important intentional behavior change

The original `New StreamWriter(fileName, False)` overwrites an existing `StudentMarks.txt` on each run. **This version intentionally differs: it preserves an existing file**, reads and displays its existing contents, and never overwrites it with sample records. If no file exists, it atomically creates one using `FileMode.CreateNew` and writes the four original sample records. The file is in the process's current working directory, not necessarily this folder. An existing empty file stays empty. It reports file/access errors on stderr with exit code 1; it prompts for Enter on success or error. The lines are displayed as stored, not padded into columns.

## Build and tested behavior

The repository has no VB project file for this exercise. On Debian Linux, an independently created .NET 8 VB console project using SDK **8.0.428** and runtime **8.0.34** compiled this exact source with **0 warnings and 0 errors**. The accompanying Python integration suite ran the compiled DLL in temporary directories and passed these checks:

1. Missing file: creates and displays the four original sample records.
2. Repeat run: file bytes stay unchanged and the preservation message appears.
3. Custom existing file and empty file: bytes stay unchanged; custom content is displayed.
4. A directory named `StudentMarks.txt`: an error is reported, exit code 1, no success claim.
5. With stdin held open, the program waits until Enter.

To reproduce with a .NET 8 SDK and Python 3, from this folder:

```sh
dotnet new console --language VB --framework net8.0 --output /tmp/StudentMarksTest
cp StudentMarks.vb /tmp/StudentMarksTest/Program.vb
dotnet build /tmp/StudentMarksTest
python3 test_student_marks.py "$(command -v dotnet)" /tmp/StudentMarksTest/bin/Debug/net8.0/StudentMarksTest.dll
```

The tests use temporary working directories; do not run the program in a directory containing sensitive data without understanding which file will be read.

## Limitations

These checks do not test Windows, permission-denied errors, all I/O failures, concurrent external modifications, symbolic links, or arbitrary encodings/binary contents. Atomic create protects an already-existing file from being truncated; it is not a transaction: a write failure may leave a partially written *new* file. Other processes could change the file between creation and reading. The suite and scratch console project are not evidence that the unrelated form or any missing original project/build files work. Review and adapt before use.
