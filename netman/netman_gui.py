# netman netman_gui
# Copyright (C) 2016 John Phillips, SPAWAR Systems Center Pacific
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import Tkinter as tk
import tkMessageBox
import tkFileDialog

from subprocess import Popen

class Main_Application(object):

    # Initialize main window
    def __init__(self, master):
        self.master = master
        
        self._max_input = 10
        self._filename_default = 'No file selected'
        
        self._threshold = 40
        
        self._contact_frames = []
        self._ground_truth = self._filename_default
        self._save_filename = self._filename_default
        
        # Build top frame
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, column=0)
        
        # Populate top frame
        self.open_groundtruth_button = tk.Button(self.top_frame, text="Ground Truth MEDAL File", height=1, width=20, command = self.open_filename)
        self.open_groundtruth_button.grid(row=0, column=0, padx=10, pady=10)

        self.open_groundtruth_text = tk.StringVar()
        tk.Label(self.top_frame, textvariable = self.open_groundtruth_text, relief=tk.GROOVE, height=1, width=20).grid(row=0, column=1, padx=10, pady=10)
        self.open_groundtruth_text.set(self._ground_truth)
        
        # Build middle frame / first inner frame
        self.middle_frame = tk.Frame(self.master)
        self.middle_frame.grid(row=1, column=0)

        # Build first inner frame and populate
        self.new_contact_frame()
            
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.grid(row=2, column=0)
        
        # Populate the bottom frame
        self.save_file_button = tk.Button(self.bottom_frame, text="Save As", height=1, width=20, command = self.save_filename)
        self.save_file_button.grid(row=0, column=0, padx=10, pady=10)

        self.save_filename_text = tk.StringVar()
        tk.Label(self.bottom_frame, textvariable = self.save_filename_text, relief=tk.GROOVE, height=1, width=20).grid(row=0, column=1, padx=10, pady=10)
        self.save_filename_text.set(self._save_filename)

        self.analyze_button = tk.Button(self.bottom_frame, text="Analyze", height=1, width=20, command=self.analyze_files)
        self.analyze_button.grid(row=1, column=0, padx=10, pady=10)

        self.add_file_button = tk.Button(self.bottom_frame, text="Add Contact MEDAL File", height=1, width=20, command=self.new_contact_frame)
        self.add_file_button.grid(row=1, column=1, padx=10, pady=10)

        threshold_label = tk.Label(self.bottom_frame, text="Match Threshold (m)")
        threshold_label.grid(row=2, column=0, padx=10, pady=10)

        self.threshold = tk.Text(self.bottom_frame, height=1, width=18)
        self.threshold.grid(row=2, column=1, padx=10, pady=10)
        self.threshold.insert(tk.END, self._threshold)
        
    def open_filename(self):
        filename = tkFileDialog.askopenfilename(filetypes = (("All files", "*.*")
                                                         ,("MEDAL files", "*.XML")))
    
        if len(filename) > 0:
            filename = filename.split('/')
            filename = filename[len(filename) - 1]
            self.open_groundtruth_text.set(filename)
            self._ground_truth = filename
        
    def new_contact_frame(self):
        if len(self._contact_frames) < self._max_input:
            self.frame = Contact_Frame(self)
            # Add to list of inner frames
            self._contact_frames.append(self.frame)
        else:
            self.error(2)
        
    def save_filename(self):
        
        filename = tkFileDialog.asksaveasfilename(filetypes = (("All files", "*.*")
                                                           ,("CSV files", "*.csv")), defaultextension = ".csv")
        if len(filename) > 0:
            #path = filename
            filename = filename.split('/')
            filename = filename[len(filename) - 1]
            self.save_filename_text.set(filename)
            self._save_filename = filename
            
    def analyze_files(self):
        return
            
    def error(self, error_code):
        if error_code == 2:
            tkMessageBox.showerror("Input File Error", "Maximum number of input files (10) reached.\n\n\nPress OK to continue.")
        if error_code == 3:
            tkMessageBox.showerror("File Error", "I/O file name not selected.\n\n\nPress OK to continue.")
        
class Contact_Frame:
    def __init__(self, master):
        self.master = master
        
        self.current_row = len(master._contact_frames)
        self._filename = master._filename_default
        
        self.middle_frame_0 = tk.Frame(master.middle_frame)
        self.middle_frame_0.grid(row=self.current_row, column=0)
            
        open_file_button = tk.Button(self.middle_frame_0, text="Contact MEDAL File", height=1, width=20, command = self._set_filename)
        open_file_button.grid(row=0, column=0, padx=10, pady=10)

        self.open_filename_text = tk.StringVar()
        tk.Label(self.middle_frame_0, textvariable = self.open_filename_text, relief=tk.GROOVE, height=1, width=20).grid(row=0, column=1, padx=10, pady=10)
        # set file name to default
        self.open_filename_text.set(self._filename)
        
    def _set_filename(self):
        filename = tkFileDialog.askopenfilename(filetypes = (("All files", "*.*")
                                                         ,("MEDAL files", "*.XML")))
    
        if len(filename) > 0:
            filename = filename.split('/')
            filename = filename[len(filename) - 1]
            self.open_filename_text.set(filename)
            self._filename = filename
        
def main(): 
    top = tk.Tk()
    top.title("Network Management Tool v1.0 b1")
    top.minsize(250, 100)
    top.iconbitmap('default.ico')
    Main_Application(top)
    top.mainloop()

if __name__ == '__main__':
    main()