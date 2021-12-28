import os, time
import shutil

class Organize:
    def organize(self):
        print("Welcome to Junk File Organizer \n\x1B[3mOrganize you files fast like a Ninja\x1B[0m")
        print("")
        print("[1] Extenssion")
        print("[2] Last Modified")
        print("[3] Size")
        choice = int(input("Enter Your Choice: "))
        # Extension Method
        if choice == 1:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_ext(path)
            else:
                print("Directory Not Exists")
        
        # Modification Date Method
        elif choice == 2:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_modification_date(path)
            else:
                print("Directory Not Exists")
        
        # File Size Method
        elif choice == 3:
            path = input("Enter Directory: ")
            if(os.path.exists(path)):
                self.arrange_file_with_size(path)
            else:
                print("Directory Not Exists")
        
        else:
            print("Wrong Input !!")

    def make_base_directory(self, path):
        if os.path.exists(path+"/arranged"):
            pass
        else:
            os.mkdir(path+"/arranged")

    """ def make_day_directory(self, path):
        # For Today
        if os.path.exists(path+"/arranged/today"):
            pass
        else:
            os.mkdir(path+"/arranged/today")
        # For Yesterday
        if os.path.exists(path+"/arranged/yesterday"):
            pass
        else:
            os.mkdir(path+"/arranged/yesterday")
        
        # For Erlier
        if os.path.exists(path+"/arranged/earlier"):
            pass
        else:
            os.mkdir(path+"/arranged/earlier") """


    def remove_directory(self, path):
        all_dir = os.listdir(path)
        for dir in all_dir:
            rm_dir = path+"/"+dir
            if dir == "arranged":
                pass
            else:
                try:
                    shutil.rmtree(rm_dir)
                except NotADirectoryError:
                    os.unlink(rm_dir)
    

    def move_file(self, src, dest):
        try:
            return shutil.move(src, dest)
        except shutil.Error:
             print("Not Moved !!") 
    
    # ================Organize as per Extenssion Method =============
    def make_ext_dir(self, path):
        all_files = os.walk(path)
        for dir, fName, files in all_files:
            for file in files:
                ext = file.split(sep=".")
                directory = path+"/arranged/"+ext[-1]+"_files"
                if os.path.exists(directory):
                    pass
                else:
                    os.mkdir(directory)

    def arrange_file_with_ext(self, path):
        # Create base directory
        self.make_base_directory(path)
        self.make_ext_dir(path)

        all_files = os.walk(path)
        for dir, file_name, files in all_files:
            for f in files:
                directory = dir+'/'+f
                ext = f.split(sep=".")
                try:
                    moving_dir = path+"/arranged/"+ext[-1]+"_files"
                    shutil.move(directory, moving_dir)
                except shutil.Error:
                    # print("Not Moved !!")
                    continue
        print("Arranged All Files")

        # Remove empty folders
        self.remove_directory(path)

    # ================End Section=================================
    
# Create A Object
a = Organize()

# Callig arrange() method to arrange the file
a.organize()