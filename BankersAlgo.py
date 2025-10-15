import tkinter as tk
from tkinter import messagebox, ttk

class BankersAlgorithmGUI:
    def __init__(self, root):  
        self.root = root
        self.root.title("Banker's Algorithm Visual Demo")
        self.root.geometry("900x650")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Banker's Algorithm - Interactive Learning Demo",
                 font=('Helvetica', 16, 'bold')).pack(pady=10)

        
        frame1 = tk.Frame(self.root)
        frame1.pack(pady=10)
        tk.Label(frame1, text="Number of Processes:").grid(row=0, column=0, padx=5)
        self.num_processes_entry = tk.Entry(frame1, width=5)
        self.num_processes_entry.grid(row=0, column=1)

        tk.Label(frame1, text="Number of Resources:").grid(row=0, column=2, padx=5)
        self.num_resources_entry = tk.Entry(frame1, width=5)
        self.num_resources_entry.grid(row=0, column=3)

        tk.Button(frame1, text="Next", command=self.create_input_table).grid(row=0, column=4, padx=10)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=10)

    def create_input_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        try:
            self.n = int(self.num_processes_entry.get())
            self.m = int(self.num_resources_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")
            return

        
        tk.Label(self.table_frame, text="Enter Allocation Matrix").grid(row=0, column=0, padx=10)
        tk.Label(self.table_frame, text="Enter Max Matrix").grid(row=0, column=self.m+1, padx=10)

        
        self.alloc_entries = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                e = tk.Entry(self.table_frame, width=5)
                e.grid(row=i+1, column=j)
                row.append(e)
            self.alloc_entries.append(row)

        
        self.max_entries = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                e = tk.Entry(self.table_frame, width=5)
                e.grid(row=i+1, column=self.m+1+j)
                row.append(e)
            self.max_entries.append(row)

        
        tk.Label(self.table_frame, text="Available:").grid(row=self.n+2, column=0, pady=10)
        self.avail_entries = []
        for j in range(self.m):
            e = tk.Entry(self.table_frame, width=5)
            e.grid(row=self.n+2, column=j+1)
            self.avail_entries.append(e)

        tk.Button(self.table_frame, text="Run Algorithm", command=self.run_algorithm).grid(
            row=self.n+3, column=0, columnspan=2, pady=10
        )

        self.result_box = tk.Text(self.table_frame, width=80, height=15)
        self.result_box.grid(row=self.n+4, column=0, columnspan=10, pady=10)

    def run_algorithm(self):
        try:
            alloc = [[int(self.alloc_entries[i][j].get()) for j in range(self.m)] for i in range(self.n)]
            max_need = [[int(self.max_entries[i][j].get()) for j in range(self.m)] for i in range(self.n)]
            avail = [int(self.avail_entries[j].get()) for j in range(self.m)]
        except ValueError:
            messagebox.showerror("Error", "Please fill all entries with integers")
            return

        need = [[max_need[i][j] - alloc[i][j] for j in range(self.m)] for i in range(self.n)]
        finish = [False] * self.n
        safe_seq = []
        work = avail[:]

        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, f"Need Matrix:\n{need}\n\n")

        while len(safe_seq) < self.n:
            allocated = False
            for i in range(self.n):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(self.m)):
                    self.result_box.insert(tk.END, f"Process P{i} can be allocated. Work: {work}\n")
                    for j in range(self.m):
                        work[j] += alloc[i][j]
                    safe_seq.append(f"P{i}")
                    finish[i] = True
                    allocated = True
                    break
            if not allocated:
                break

        self.result_box.insert(tk.END, "\nFinal Work Vector: " + str(work) + "\n")

        if len(safe_seq) == self.n:
            self.result_box.insert(tk.END, f"\n System is in SAFE STATE.\nSafe Sequence: {' -> '.join(safe_seq)}")
        else:
            self.result_box.insert(tk.END, "\n System is NOT in a safe state (Deadlock possible).")


if __name__ == "__main__":  
    root = tk.Tk()
    app = BankersAlgorithmGUI(root)
    root.mainloop()
    def __init__(self, root): 
        self.root = root
        self.root.title("Banker's Algorithm Visual Demo")
        self.root.geometry("900x650")


        self.create_widgets()
