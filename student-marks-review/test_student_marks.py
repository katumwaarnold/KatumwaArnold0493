#!/usr/bin/env python3
"""Run with: python3 test_student_marks.py /path/to/dotnet /path/to/StudentMarks.dll"""
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

DOTNET, DLL = map(os.path.abspath, sys.argv[1:3])
EXPECTED = ["ST001, Shaminah, 85", "ST002, Mahoro, 84", "ST003, Saum, 82", "ST004, Henry, 95"]

def run(cwd):
    return subprocess.run([DOTNET, DLL], cwd=cwd, input="\n", capture_output=True, text=True, timeout=10)

with tempfile.TemporaryDirectory() as td:
    path = Path(td) / "StudentMarks.txt"
    result = run(td)
    assert result.returncode == 0 and not result.stderr, (result.returncode, result.stderr)
    assert path.read_text(encoding="utf-8-sig").splitlines() == EXPECTED
    assert [s for s in result.stdout.splitlines() if s.startswith("ST00")] == EXPECTED
    assert "Student marks saved successfully!" in result.stdout
    assert "STUDENT NO  NAME   MARKS" in result.stdout
    print("PASS: absent file: creates and displays four original sample records")
    before = path.read_bytes()
    result = run(td)
    assert result.returncode == 0 and not result.stderr and path.read_bytes() == before
    assert "Existing StudentMarks.txt preserved" in result.stdout
    assert "saved successfully" not in result.stdout
    print("PASS: repeat run: preserves file bytes and reports preservation")
    for existing in (b"Existing marks: 17\r\nAnother student, 42\n", b""):
        path.write_bytes(existing)
        result = run(td)
        assert result.returncode == 0 and not result.stderr, (result.returncode, result.stderr)
        assert path.read_bytes() == existing
        assert "Existing StudentMarks.txt preserved" in result.stdout
        if existing:
            assert "Existing marks: 17" in result.stdout and "Another student, 42" in result.stdout
    print("PASS: pre-existing custom and empty files remain byte-for-byte unchanged; custom content displayed")

with tempfile.TemporaryDirectory() as td:
    (Path(td) / "StudentMarks.txt").mkdir()
    result = run(td)
    assert result.returncode == 1, (result.returncode, result.stdout, result.stderr)
    assert "error:" in result.stderr.lower() and "saved successfully" not in result.stdout
    print("PASS: path is a directory: error reported, exit code 1, no success claim")

with tempfile.TemporaryDirectory() as td:
    process = subprocess.Popen([DOTNET, DLL], cwd=td, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    deadline = time.monotonic() + 8
    while not (Path(td) / "StudentMarks.txt").exists() and time.monotonic() < deadline:
        time.sleep(0.05)
    time.sleep(0.2)
    assert process.poll() is None, "Process did not wait for Enter"
    stdout, stderr = process.communicate("\n", timeout=5)
    assert process.returncode == 0 and "Press Enter to exit." in stdout and not stderr, (stdout, stderr)
    print("PASS: waits for Enter while stdin remains open")
