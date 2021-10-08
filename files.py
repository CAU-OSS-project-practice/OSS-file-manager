import os
import PySimpleGUI as sg
import shutil
from send2trash import send2trash

sg.theme("SystemDefault1")
icon = "/images/files.png"
folder_icon = "/images/files_c.png"
file_icon = "/images/files_f.png"
home_icon = "/images/files_h.png"
up_icon = "/images/files_up.png"
main_path = "/home"
treedata = sg.TreeData()
hidden = False
reverse = False
sort_size = False
size_list = []
count = 0
s = "☐ Show hidden files"
h = "☑ Show hidden files"
hidd = s
ab = "▼ Reverse sort"
ba = "▲ Reverse sort"
revers = ba
nsort = "⇵ Sort by name"
ssort = "⇵ Sort by size"
sort = ssort
pa = "!▣ Paste"
pd = "▣ Paste"
paste = pa
c1 = "❐ Copy"
c2 = "!❐ Copy"
copy = c2
d1 = "✘ Delete in trash"
d2 = "!✘ Delete in trash"
delete = d2

def takeFirst(elem):
    return elem[0]
# Convert size
def add_size(name):
    s = os.stat(name).st_size
    if s < 1000:
        size = str(s) + " B"
    if s >= 1000:
        size = str(s/1000) + " KB"
    if s >= 1000000:
        size = str(s/1000000) + " MB"
    if s >= 1000000000:
        size = str(s/1000000000) + " GB"
    if s >= 1000000000000:
        size = str(s/1000000000000) + " TB"
    return [size, s]
# Updating files and folders
def add_files_in_folder(parent, dirname):
    files = os.listdir(dirname)
    if reverse == False:
        files.sort(key=str.lower)
    if reverse == True:
        files.sort(key=str.lower, reverse=True)
    global count
    global treedata
    treedata = sg.TreeData()
    for f in files:
        fullname = os.path.join(dirname, f)
        if hidden == False:
            if f.startswith("."):
                continue
            elif os.path.isdir(fullname):
                treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
                count += 1
            else:
                continue
        elif os.path.isdir(fullname):
            treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
            count += 1
        else:
            continue
    for f in files:
        fullname = os.path.join(dirname, f)
        size = add_size(fullname)
        if sort_size == True:
            if hidden == False:
                if f.startswith("."):
                    continue
                elif os.path.isdir(fullname):
                    continue
                else:
                    size_list_ml = [size[1], fullname, f, size[0]]
                    size_list.append(size_list_ml)
            elif os.path.isdir(fullname):
                continue
            else:
                size_list_ml = [size[1], fullname, f, size[0]]
                size_list.append(size_list_ml)
        else:
            if hidden == False:
                if f.startswith("."):
                    continue
                elif os.path.isdir(fullname):
                    continue
                else:
                    treedata.Insert(parent, fullname, f, values=[size[0]], icon=file_icon)
                    count += 1
            elif os.path.isdir(fullname):
                continue
            else:
                treedata.Insert(parent, fullname, f, values=[size[0]], icon=file_icon)
                count += 1
    if sort_size == True:
        if reverse == False:
            size_list.sort(key=takeFirst, reverse=True)
        if reverse == True:
            size_list.sort(key=takeFirst)
        for s in size_list:
            treedata.Insert(parent, s[1], s[2], values=[s[3]], icon=file_icon)
            count += 1
        size_list.clear()

add_files_in_folder("", main_path)
path_original = main_path

# The stuff inside window
menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
layout = [  [sg.ButtonMenu("≡", menu_def, size=(3,1), background_color="white", key="-MENU-"), sg.Button("↑", image_size=(16,16), image_filename=up_icon), sg.Button("⌂", image_size=(16,16), image_filename=home_icon), sg.Input(default_text=main_path, key="-OUT1-", expand_x=True, size=(50,1))],
            [sg.Tree(data=treedata, font=("Helvetica",15), headings=["size"], auto_size_columns=False, col_widths=[10], num_rows=None, col0_width=40, max_col_width=10, row_height=30, key="-TREE-", enable_events=True)],
            [sg.Text(text=str(count) + " objects", key="-OUT111-", justification="center", size=(20,1)), sg.Input(default_text=main_path, readonly=True, key="-OUT11-", size=(40,1), expand_x=True, visible=False)] ]

# The Window itself param
window = sg.Window("Files", layout, return_keyboard_events=True, element_justification="left", debugger_enabled=False, resizable=True, margins=(0,0), finalize=True, auto_size_buttons=True, font=("Helvetica",15), icon=icon)
window.set_min_size((800,500))
window["-TREE-"].expand(True, True)

# Main loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    up_string = values["-OUT1-"]
    down_string = values["-OUT11-"]
    window["-TREE-"].bind("<Double-Button-1>", "double")
    window["-TREE-"].bind("<Button-1>", "click")
    # Menus events
    if event == "-MENU-":
        event = values["-MENU-"]
    if event == "☐ Show hidden files":
        hidden = True
        hidd = h
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "☑ Show hidden files":
        hidden = False
        hidd = s
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "▲ Reverse sort":
        reverse = True
        revers = ab
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "▼ Reverse sort":
        reverse = False
        revers = ba
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "⇵ Sort by size":
        sort_size = True
        sort = nsort
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "⇵ Sort by name":
        sort_size = False
        sort = ssort
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "★ About...":
        sg.popup("Files", "0.5", "A simple file explorer", font=("Helvetica",13), icon=icon)
    # File operations
    if event == "❐ Copy":
        source = str(down_string)
        source_edit = source.rsplit("/", 1)
        paste = pd
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    if event == "▣ Paste":
        if source != "":
            source_1 = os.path.join(source_edit[0], source_edit[1])
            if os.path.isdir(source_1):
                if source_edit[0] == up_string:
                    destination = str(up_string) + "/" + source_edit[1] + " (copy)"
                else:
                    destination = str(up_string) + "/" + source_edit[1]
                shutil.copytree(source, destination)
                source = ""
                source_edit = ""
                destination = ""
            else:
                if source_edit[0] == up_string:
                    destination = str(up_string) + "/" + source_edit[1] + " (copy)"
                else:
                    destination = str(up_string) + "/"
                shutil.copy2(source, destination)
                source = ""
                source_edit = ""
                destination = ""                
            paste = pa
            menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
            window["-MENU-"].update(menu_definition=menu_def)
    if event == "✘ Delete in trash":
        del_path = str(down_string)
        del_edit = del_path.rsplit("/", 1)
        answer = sg.popup_yes_no(f"Delete '{del_edit[1]}' in trash?", font=("Helvetica",13), no_titlebar=True)
        if answer == "Yes":
            if os.path.exists(del_path):
                send2trash(del_path)
                up_string = path_original
                down_string = path_original
                window["-OUT1-"].update(up_string)
                window["-OUT11-"].update(down_string)
    # Screen with files and catalogs events
    if event == "-TREE-click":
        up_string = path_original
        down_string = path_original
        window["-OUT1-"].update(up_string)
        window["-OUT11-"].update(down_string)
    if event == "-TREE-":
        for row in values[event]:
            down_string = str(row)
        window["-OUT11-"].update(down_string)
        for row in values[event]:
            up_string = str(row)
            path_string_e = up_string.rsplit("/", 1)
            path_string_e1 = os.path.join(path_string_e[0], path_string_e[1])
            if os.path.isfile(path_string_e1):
                up_string = path_original
            window["-OUT1-"].update(up_string)
    # Buttons events
    if event == "⌂":
        up_string = main_path
        down_string = main_path
    if event == "↑":
        up_string = up_string.rsplit("/", 1)
        up_string = up_string[0]
        down_string = up_string
    # Strigs and menus validations
    if up_string == "":
        up_string = up_string + "/"
    if up_string[-1] == "/" and up_string != "" and up_string != "/":
        up_string = up_string[:-1]
    if down_string == "" or down_string == "/" or str(down_string) == str(up_string):
        copy = c2
        delete = d2
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    else:
        copy = c1
        delete = d1
        menu_def = ["≡", [hidd, "---", revers, sort, "---", copy, paste, delete, "---", "★ About..."]]
        window["-MENU-"].update(menu_definition=menu_def)
    # Main operation
    try:
        if event == "Open" or event == "✘ Delete in trash" or event == "▣ Paste" or event == "-TREE-double" or event == "KP_Enter:104" or event == "Return:36" or event == "↑" or event == "⌂" or event == "☐ Show hidden files" or event == "☑ Show hidden files" or event == "▲ Reverse sort" or event == "▼ Reverse sort" or event == "⇵ Sort by size" or event == "⇵ Sort by name":
            count = 0
            add_files_in_folder("", up_string)
            path_original = up_string
            window["-TREE-"].update(values=treedata)
            window["-OUT1-"].update(up_string)
            window["-OUT11-"].update(down_string)
            window["-OUT111-"].update(str(count) + " objects")          
    except PermissionError:
        sg.popup("No Access", font=("Helvetica",13), no_titlebar=True)
    except FileNotFoundError:
        sg.popup("No such directory", font=("Helvetica",13), no_titlebar=True)