import os
import tkinter
import tkinter.filedialog

import generator


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def ask_path():
    directory = tkinter.filedialog.askdirectory(initialdir=selected_label_folder["text"], parent=window)
    if directory and len(directory) > 0:
        selected_label_folder["text"] = directory


def generate():
    path = selected_label_folder["text"]
    file_number = file_number_scale.get()
    content_length = content_length_min.get() * 1_000_000, content_length_max.get() * 1_000_000
    assert content_length[0] <= content_length[1]
    generator.generate_random_files(path, file_number, content_length)


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Random File Generator")

    frame = tkinter.Frame(window)
    frame.pack(fill=tkinter.BOTH, padx=(20, 20), pady=(20, 20))

    # Folder selection
    folder_frame = tkinter.Frame(frame)
    folder_frame.grid(row=0, pady=(0, 20))

    button_folder = tkinter.Button(folder_frame, text="Select folder", command=ask_path)
    button_folder.grid(row=0, column=2)

    tkinter.Label(folder_frame, text="Selected folder: ").grid(row=0, column=0)

    selected_label_folder = tkinter.Label(folder_frame, text=os.getcwd())
    selected_label_folder.grid(row=1, column=0, columnspan=4)

    # Number of files
    number_files_frame = tkinter.Frame(frame)
    number_files_frame.grid(row=1, pady=(0, 20))

    tkinter.Label(number_files_frame, text="Number of files").grid(row=1, column=0)
    file_number_scale = tkinter.Scale(number_files_frame, from_=1, to=200, orient=tkinter.HORIZONTAL)
    file_number_scale.set(10)
    file_number_scale.grid(row=0, column=1, rowspan=2)

    # Content size
    content_length_frame = tkinter.Frame(frame)
    content_length_frame.grid(row=2, pady=(0, 20))

    tkinter.Label(content_length_frame, text="Content size").grid(row=0)

    tkinter.Label(content_length_frame, text="Min (MB)").grid(row=2, column=0)
    content_length_min = tkinter.Scale(content_length_frame, from_=1, to=1000, orient=tkinter.HORIZONTAL)
    content_length_min.set(20)
    content_length_min.grid(row=1, column=1, rowspan=2)

    tkinter.Label(content_length_frame, text="Max (MB)").grid(row=2, column=2)
    content_length_max = tkinter.Scale(content_length_frame, from_=10, to=10_000, orient=tkinter.HORIZONTAL)
    content_length_max.set(100)
    content_length_max.grid(row=1, column=3, rowspan=2)

    run_button = tkinter.Button(frame, text="Generate", command=generate)
    run_button.grid(row=3, pady=(0, 20))

    center(window)
    window.mainloop()

