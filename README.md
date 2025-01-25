# Photo Organizer
This Python script provides a Graphical User Interface (GUI) for organizing photos into folders based on their creation or modification dates. It utilizes the Tkinter library for the user interface and Pillow for extracting metadata from images. The script scans a selected folder, sorts the images into a structured date-based format, and moves them accordingly.

## Features
* Select a folder containing photos.
*	Organize photos based on their creation or modification date.
*	Photos are sorted into folders by year, month, and day.
*	Supports various image formats including .jpg, .png, .heic, .raw, and more.

## Requirements
Ensure the following dependencies are installed before running the script:
```
pip install pillow
```
## How to Use
1.	Run the script:
2.	python photo_organizer.py
3.	Select a folder containing photos by clicking the Select Folder button.
4.	Click the Organize Photos button to sort images into the appropriate year, month, and day folders.
5.	Check the status label to confirm the number of photos organized.

After running the script, the folder structure will look like:
```
Selected_Folder/
│-- 2024/
│   ├── January/
│   │   ├── 01/
│   │   │   ├── photo1.jpg
│   │   │   ├── photo2.jpg
│   ├── February/
│   │   ├── 05/
│   │   │   ├── image1.png
```

# About photo_organizer.exe
* photo_organizer.exe is developed using pyinstaller.
* PyInstaller is a tool that can be used to convert Python scripts into standalone executable applications. It packages Python code along with all of its dependencies into a single executable file for various platforms like Windows, macOS, and Linux. To make a Windows app you run PyInstaller on Windows, and to make a Linux app you run it on Linux, etc.

## How to develop 
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
   If there are any issues after installation, add PyInstaller to the environment path.

2. Running PyInstaller:
   
