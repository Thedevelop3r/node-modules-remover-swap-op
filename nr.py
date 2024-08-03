# this project purpose is to find directories with the name "node_modules" and list them and their size and their path



import os
import sys
import shutil


class State:
    def __init__(self):
        self.total_size = 0
        self.total_dirs = 0
        self.total_files = 0
        

state = State()

def find_node_modules():    
    for root, dirs, files in os.walk(os.getcwd()):
        if "node_modules" in dirs:
            # size in megabytes
            size = sum(os.path.getsize(os.path.join(root, name)) for name in files) / 1024 / 1024    
            state.total_size += size
            state.total_dirs += 1
            print("----------------------------------------------------")
            print(f"Directory: {root}")
            print(f"Size: {size:.2f} MB")
            print("----------------------------------------------------")
            print("----------------------------------------------------")
            print(f"Total Directories: {state.total_dirs}")
            print(f"Total Size: {state.total_size:.2f} MB")
            print("----------------------------------------------------")  
            # clear screen
            os.system("cls")
        
    


# delete the entire node_modules directory

def delete_node_modules():
    for root, dirs, files in os.walk(os.getcwd()):
        if "node_modules" in dirs:
            shutil.rmtree(os.path.join(root, "node_modules"))
            # os.system("cls")
            print("----------------------------------------------------")
            print(f"Deleted node_modules in {root}")
            print("----------------------------------------------------")
    print("Done!")



if __name__ == "__main__":
    find_node_modules()
    delete_node_modules()
    os.system("cls")
    # print final result
    print("----------------------------------------------------")
    print(f"Total Directories: {state.total_dirs}")
    print(f"Total Size: {state.total_size:.2f} MB")
    print("----------------------------------------------------")
    


