# bashscript
# sed -n '10p' file.txt

# python code
with open("file.txt") as f:
    # print(f)
    for i, z in enumerate(f):
        if i == 9:
            print(i, z)

    # print(f.read())


#powershell code
Get-Content file.txt |Select-object -Index 9 