import os

files_to_process = [r"D:\python\math_sin_square.py",r"D:\python\math_square_root.py"]

for file in files_to_process:
    print(os.path.basename(file))
    with open(file,"r") as f:
        source = f.read()
        exec(source)

