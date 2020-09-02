# Converter
Convert types of files to others using ffmpeg 

## Part 1 - Adding the button on the context menu
- Step 1: Open the regestry by clicking `win + r` and searching `regedit`.
- Step 2: Navigate to Computer\HKEY_CLASSES_ROOT\SystemFileAssociations\ and search for the suffix that you need (for example I used `.mp3`, `.ogg`).
- Step 3: Right click the folder, click on `New` -> `Key` and name it `Shell` (sometimes it already exists).
  - Step 3.1: Right click on `Shell` add a new `Key` the same way as before and call it the name you want the main button to be, I named it `Convert`.
  - Step 3.2: On the `Convert` file add a new `String value type REG_SZ` and call it `MUIVerb` and on the value data write `Convert`.
  - Step 3.3: On the same file add a new `String value type REG_SZ` and name it `SubCommands` (I'm not sure if it's necessary tho.
  - Step 3.4: Add a new `Key` (or file) and name it the sub-command title (for example ogg or mp3 or bananaman).
  - Step 3.4 Add a new `Key` and name it `command` and on the (Default) string value write the path to the exe file you want to run, the sub-command name (Will explain why in a bit) and "%1" like the following: `D:\example.exe ogg "%1"`.
  The reason why we add the sub-command name in the Data is because we want to know what to convert the file to without having to create a code for each scenario, so we get the sub-command name as a flag.

## Part 2 - Code
Now we have the the button when we right click the file with the suffix we chose. Now we need to convert it.

You can copy my code, I'll explain the code here.
First we get the flags using `sys.argv` when the first flag is the path to the exe file, the second flag is our sub-command name (Which is why we wrote it on `Part 1 Step 3.4`)
and the last flag is the path to the file we decided to convert.

We then use `subprocess.call` to use ffmpeg in order to convert the type to another type and lastly we remove the old file using `os`.

## Part 3- .py to .exe
The easiest way to do that is by using [Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/), simply write auto-py-to-exe on the terminal and following the steps.


And that's it! If you need any help I'll gladly help you. You can contact me on discord through on this [server](https://discord.gg/YZDFVhZ). I'll link a image to my regestry if you need examples.

<img src="https://cdn.discordapp.com/attachments/711183961937674290/750800461837238392/unknown.png" height="30%" width="30%" align="right">
