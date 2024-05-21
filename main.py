import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task[0])



def mark_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, bg="ForestGreen")


def arch_task():
    selected_task = task_list.curselection()
    if selected_task:
        for task in selected_task:
            task_text = task_list.get(task)
            arch_list.insert(tk.END, task_text)
            task_list.delete(task)


root = tk.Tk()
root.title("Учет задач")
root.configure(background="DarkOrchid3")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="dark orange")
text1.pack(pady=5)

entry = tk.Entry(root, width=50, bg="gainsboro")
entry.pack(pady=10)

task_button = tk.Button(root, text="Добавить задачу", bg="ForestGreen", command=add_task)
task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", bg="firebrick3", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", bg="ForestGreen", command=mark_task)
mark_button.pack(pady=5)

arch_button = tk.Button(root, text="Убрать в архив",  bg="bisque3", command=arch_task)
arch_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="dark orange")
text2.pack(pady=5)

task_list = tk.Listbox(root, height=10, width=50, bg="gainsboro")
task_list.pack(pady=10)

arch_list = tk.Listbox(root, height=10, width=50, bg="bisque3")
arch_list.pack(pady=10)

root.mainloop()

