import customtkinter as ctk
import logic
import store_data

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def delete_task(tasks, task, task_view_frame):
    logic.delete_tasks(tasks, task)
    store_data.save_tasks(tasks)
    render_tasks(task_view_frame, tasks)

def complete_task(tasks, task, task_view_frame):
    logic.edit_tasks(tasks, task, True)
    store_data.save_tasks(tasks)
    render_tasks(task_view_frame, tasks)

def render_tasks(task_view_frame, tasks):
    for widget in task_view_frame.winfo_children():
        widget.destroy()

    for task_name, status in tasks.items():
        task_row = ctk.CTkFrame(task_view_frame, fg_color="#161B22", corner_radius=10)
        task_row.pack(fill="x", padx=15, pady=8)

        label = ctk.CTkLabel(
            task_row,
            text=task_name,
            font=("SF Pro Text", 16),
            anchor="w",
            wraplength=400,
            text_color="#C9D1D9"
        )
        label.pack(side="left", padx=(20, 10), pady=15, fill="x", expand=True)

        button_delete = ctk.CTkButton(
            task_row,
            text="Delete",
            fg_color="#F85149",
            hover_color="#F66A6B",
            width=80,
            height=30,
            font=("SF Pro Text", 12, "bold"),
            command=lambda t=task_name: delete_task(tasks, t, task_view_frame)
        )
        button_delete.pack(side="right", padx=(10, 15), pady=12)

        if status:
            button_status = ctk.CTkButton(
                task_row,
                text="Completed",
                fg_color="#238636",
                state=ctk.DISABLED,
                width=100,
                height=30,
                font=("SF Pro Text", 12, "bold"),
                corner_radius=15
            )
            button_status.pack(side="right", padx=10, pady=12)
        else:
            button_status = ctk.CTkButton(
                task_row,
                text="Pending",
                fg_color="#58A6FF",
                hover_color="#1F6FEB",
                width=100,
                height=30,
                font=("SF Pro Text", 12, "bold"),
                corner_radius=15,
                command=lambda t=task_name: complete_task(tasks, t, task_view_frame)
            )
            button_status.pack(side="right", padx=10, pady=12)

def main():


    def append_tasks():
        task_name = new_task.get().strip()
        if task_name == "":
            return

        added = logic.add_tasks(tasks, task_name)
        if added:
            store_data.save_tasks(tasks)
            render_tasks(task_view_frame, tasks)
            new_task.delete(0, "end")
        else:
            pass

    tasks = store_data.load_tasks()

    app = ctk.CTk()
    app.title("To-Do")
    app.geometry("600x550")
    app.resizable(width=False, height=False)
    app.configure(fg_color="#0D1117")

    welcome_text = ctk.CTkLabel(
        app,
        text="Welcome to To-Do",
        font=("SF Pro Text", 32, "bold"),
        text_color="#C9D1D9",
        pady=10
    )
    welcome_text.pack(pady=(20, 10))

    add_frame = ctk.CTkFrame(app, fg_color="#161B22", corner_radius=15, border_width=1, border_color="#30363D")
    add_frame.pack(fill="x", padx=25, pady=(0, 20))

    new_task = ctk.CTkEntry(
        add_frame,
        placeholder_text="New Task",
        font=("SF Pro Text", 16),
        height=40,
        border_width=1,
        border_color="#30363D",
        corner_radius=10,
        text_color="#C9D1D9",
        fg_color="#0D1117"
    )
    new_task.pack(side="left", fill="x", expand=True, padx=(20, 10), pady=10)

    submit = ctk.CTkButton(
        add_frame,
        text="Submit",
        font=("SF Pro Text", 16, "bold"),
        fg_color="#238636",
        hover_color="#2EA44F",
        width=120,
        height=40,
        corner_radius=10,
        command=append_tasks
    )
    submit.pack(side="right", padx=(0, 20), pady=10)

    task_view_frame = ctk.CTkScrollableFrame(
        app,
        fg_color="#161B22",
        corner_radius=15,
        border_width=0,
        height=350,
        scrollbar_button_color="#484F58",
        scrollbar_button_hover_color="#6E7681"
    )
    task_view_frame.pack(fill="both", padx=25, pady=(0, 25))

    render_tasks(task_view_frame, tasks)

    app.mainloop()

if __name__ == '__main__':
    main()
