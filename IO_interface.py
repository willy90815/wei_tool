import os
class IO_interface:
    def __init__(self) -> None:
        pass
    def get_file_path(self=None, sub_dir="",default_num=None) -> str:
        '''sub_dir don't need to start with /'''
        # improve idea add cd function
        cur_dir = os.getcwd()+f"/{sub_dir}"
        files = os.listdir(cur_dir)

        print("\n\n\nNow your current directory is:", cur_dir)
        print(cur_dir)

        if (len(files) == 0):
            print("No file in this directory")
            return None
        for file in files[:-1]:
            print(f'├── {files.index(file)+1}. {file}')
        print(f'└── {files.index(files[-1])+1}. {files[-1]}')
        if default_num is not None:
            print(f'You choose file {default_num} : {files[int(default_num)-1]}')
            return f'{cur_dir}/{files[default_num-1]}'
        print("Enter file number to choose: ")
        file_num = input("[1],[2],[3]...: ")
        print(f'You choose file {file_num} : {files[int(file_num)-1]}')
        # lack no suck file detector
        return f'{cur_dir}/{files[int(file_num)-1]}'
    
    def get_all_file_path(self=None, sub_dir=""):
        '''sub_dir don't need to start with /'''
        cur_dir = os.getcwd()+f"/{sub_dir}"
        files = os.listdir(cur_dir)
        for file in files:
            files[files.index(file)] = f'{cur_dir}/{file}'
        return files
    

    def get_string(self,sub_dir="",default_num=None) -> str:
        return open(self.get_file_path(sub_dir=sub_dir,default_num=default_num), 'r').read()
if __name__ == "__main__":
    io = IO_interface()
    print(io.get_all_file_path("Page_Strings"))
    with open(io.get_all_file_path("Page_Strings")[0]) as f:
        pass