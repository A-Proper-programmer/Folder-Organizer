# Folder-Organizer
This project is to organize a folder based on extensions and seperate duplicate files.
It also makes a log file on the summary of what the program did.

Though it works flawlessly, the main problem is that it can't organize subfolders and stuff.
So I have updated it by finding all subdirectories using os.walk(), and running the program on it.

# Future Goals
Make sure the summary logs don't appear on each subdirectory and don't get organized.

Try to group file based on type of file (image, video) instead of raw extensions.
Need to upgrade to fix exceptions when files are password protected.
Handle situations where file to be organized has the same name as an already organized file.
