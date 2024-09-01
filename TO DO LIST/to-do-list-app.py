import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        # Define colors
        self.bg_color = "#f0f0f0"
        self.fg_color = "#333333"
        self.button_color = "#4caf50"
        self.button_hover_color = "#45a049"
        self.entry_color = "#ffffff"
        self.listbox_color = "#ffffff"
        self.scrollbar_color = "#e0e0e0"
        self.completed_color = "#2196f3"  
        
        # Task list
        self.tasks = []
        
        # Main frame
        self.frame = tk.Frame(root, bg=self.bg_color, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Listbox to display tasks
        self.listbox = tk.Listbox(self.frame, width=40, height=10, bd=0, font=("Helvetica", 12),
                                 bg=self.listbox_color, fg=self.fg_color)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame, bg=self.scrollbar_color)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Entry box and buttons
        self.entry_frame = tk.Frame(root, bg=self.bg_color)
        self.entry_frame.pack(pady=5, fill=tk.X)
        
        # Entry box to input tasks
        self.entry = tk.Entry(self.entry_frame, width=30, font=("Helvetica", 12), bg=self.entry_color, fg=self.fg_color)
        self.entry.pack(pady=5, padx=5, side=tk.LEFT, fill=tk.X, expand=True)
        
        # Add Task button
        self.add_button = tk.Button(self.entry_frame, text="Add", width=10, command=self.add_task,
                                   bg=self.button_color, fg=self.bg_color, activebackground=self.button_hover_color)
        self.add_button.pack(pady=5, padx=5, side=tk.RIGHT)
        
        # Frame for action buttons
        self.button_frame = tk.Frame(root, bg=self.bg_color)
        self.button_frame.pack(pady=5)
        
        # Action buttons
        self.delete_button = tk.Button(self.button_frame, text="Delete", width=10, command=self.delete_task,
                                      bg=self.button_color, fg=self.bg_color, activebackground=self.button_hover_color)
        self.delete_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.update_button = tk.Button(self.button_frame, text="Update", width=10, command=self.update_task,
                                      bg=self.button_color, fg=self.bg_color, activebackground=self.button_hover_color)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.done_button = tk.Button(self.button_frame, text="Done", width=10, command=self.mark_as_done,
                                    bg="#2196f3", fg=self.bg_color, activebackground="#1976d2")
        self.done_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.exit_button = tk.Button(self.button_frame, text="Exit", width=10, command=root.quit,
                                    bg="#f44336", fg=self.bg_color, activebackground="#d32f2f")
        self.exit_button.grid(row=1, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]  
            self.listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0] 
            task = self.entry.get()
            if task != "":
                self.tasks[selected_task_index] = task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, task)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def mark_as_done(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]  
            task = self.listbox.get(selected_task_index)
            if task:
                completed_task = f"{task} [Complete]"
                self.listbox.itemconfig(selected_task_index, {'fg': self.completed_color})
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, completed_task)
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600")  
    app = ToDoApp(root)
    root.mainloop()
