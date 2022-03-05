import os
import argparse
import errno
from pathlib import Path

os.system("cls")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('required named arguments')
    
    requiredNamed.add_argument("-ds_p", "--dataset_path", help="Complete dataset path", type=Path, required=True)
    requiredNamed.add_argument("-op_p", "--output_path", help="Complete output path", type=Path, required=False)
    # parser.parse_args(['-h'])
    
    p = parser.parse_args()

    file = open("./paths.py", "w")
    print(p.dataset_path)
    print("1")
    print(p.dataset_path.exists())
    if p.dataset_path.exists() == False:
        print("faul")
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p.dataset_path)
    
    elif p.dataset_path.exists == True:
        print("efi")
        print(f"Dataset Path = {p.dataset_path}")    
        file.write(f'final_dataset_path = "{p.dataset_path}"\n')

    if p.output_path.exists() == False:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), p.dataset_path)

    elif p.output_path.exists == True:   
        print(f"Output Path = {p.output_path}")        
        file.write(f'final_output_path = "{p.output_path}"\n') 

    file.close()

    # os.system(f"python ./viren.py -ds_p {p.dataset_path} -op_p {p.output_path}")

