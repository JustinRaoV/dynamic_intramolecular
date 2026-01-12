with open("group1.txt", "r") as file:
    # Read the file
    content = file.readlines()

lines = [line.strip() for line in content]
print(len(lines))
group1 = ["AGTCGATGTCAGTCCAATAATTCCTGTAGTGATTAATGAACCCCCT",
          "CCTACTACCCAATGTCTGTCAATTTTGTTGGGCTGTATGGTG",
          "GGTAACAATTAATCCCCGTCT",
          "TGCTCTTCAATTAAAGCGG",
          "GGGTTGTTAAATAAATTAGTGG",
          "GGGCAAATCGTGATTG"]
with open("inter1.txt", "w") as file:
    file.write("number,BIP,FIP,B3,F3,LoopB,LoopF,seq\n")
    count = 0
    for line in lines:
        file.write(f"{count}")
        for index in group1:
            if index in line:
                file.write(",1")
            else:
                file.write(",0")
        file.write(f",{line}\n")
        count += 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r'E:\LAMPseq\Pacbio\sencondseq\Run\inter3.csv')