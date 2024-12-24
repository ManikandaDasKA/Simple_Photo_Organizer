import os
import shutil
from datetime import datetime
from tkinter import Tk,filedialog,Label,Button
from PIL import Image
from PIL.ExifTags import TAGS
class PhotoOrganizer:
    def __init__(self,root):
        self.root=root
        self.root.title("Photo Organizer")
        self.label=Label(root,text="Select a folder to organize photos by date",font=("Arial",12))
        self.label.pack(pady=10)
        self.select_button=Button(root,text="Select Folder",command=self.select_folder,font=("Arial",10))
        self.select_button.pack(pady=5)
        self.organize_button=Button(root,text="Organize Photos",command=self.organize_photos,font=("Arial",10),state="disabled")
        self.organize_button.pack(pady=5)
        self.status_label=Label(root,text="",font=("Arial",10))
        self.status_label.pack(pady=10)
        self.folder_path=""
    def select_folder(self):
        self.folder_path=filedialog.askdirectory()
        if self.folder_path:
            self.status_label.config(text=f"Selected Folder:{self.folder_path}")
            self.organize_button.config(state="normal")
        else:
            self.status_label.config(text="No folder selected.")
    def organize_photos(self):
        if not self.folder_path:
            self.status_label.config(text="No folder selected.")
            return
        image_extensions={".tiff",".tif",".jpg",".jpeg",".gif",".png",".webp",".heic",".heif",".avif",".bmp",".eps",".epsf",".epsi",".raw",".cr2",".nef",".orf",".sr2"}
        organized_count=0
        for file_name in os.listdir(self.folder_path):
            file_path=os.path.join(self.folder_path, file_name)
            if not os.path.isfile(file_path) or not file_name.lower().endswith(tuple(image_extensions)):
                continue
            try:
                creation_date=self.get_creation_date(file_path)
                if not creation_date:
                    creation_date=self.get_modified_date(file_path)
                year_folder=os.path.join(self.folder_path,str(creation_date.year))
                os.makedirs(year_folder,exist_ok=True)
                month_name=creation_date.strftime("%B")  
                month_folder=os.path.join(year_folder,month_name)
                os.makedirs(month_folder,exist_ok=True)
                date_folder=creation_date.strftime("%d")
                target_folder=os.path.join(month_folder,date_folder)
                os.makedirs(target_folder,exist_ok=True)
                shutil.move(file_path,os.path.join(target_folder,file_name))
                organized_count+=1
            except Exception as e:
                print(f"Error organizing file {file_name}: {e}")
        self.status_label.config(text=f"Organized {organized_count} photos into date-based folders.")
    @staticmethod
    def get_creation_date(file_path):
        try:
            image=Image.open(file_path)
            exif_data=image._getexif()
            if not exif_data:
                return None
            for tag_id,value in exif_data.items():
                tag=TAGS.get(tag_id, tag_id)
                if tag=="DateTimeOriginal":
                    return datetime.strptime(value,"%Y:%m:%d %H:%M:%S")
        except Exception:
            pass
        return None
    @staticmethod
    def get_modified_date(file_path):
        modified_time=os.path.getmtime(file_path)
        return datetime.fromtimestamp(modified_time)
if __name__=="__main__":
    root=Tk()
    app=PhotoOrganizer(root)
    root.geometry("620x200")
    root.mainloop()