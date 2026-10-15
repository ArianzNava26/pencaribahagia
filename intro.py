import sys
import subprocess

choose = str(input("\n\nChoose the language:\nA. Bahasa Indonesia\nB. English\n"))
if choose.lower() == "a":
    subprocess.run([sys.executable, "tanyahati.py"])
elif choose.lower() == "b":
    subprocess.run([sys.executable, "askingyourself.py"])
else:
    print("Please choose a or b next time!, program Quit.")
print()
