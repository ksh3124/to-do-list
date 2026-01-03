import customtkinter as ctk
import logic
import store_data
import os


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
        task_row = ctk.CTkFrame(task_view_frame, fg_color="#161B22", corner_radius=12)
        task_row.grid_columnconfigure(0, weight=1)

        task_row.pack(fill="x", padx=15, pady=8)

        label = ctk.CTkLabel(
            task_row,
            text=task_name,
            font=("SF Pro Text", 16),
            anchor="w",
            wraplength=420,
            text_color="#C9D1D9"
        )
        label.grid(row=0, column=0, sticky="w", padx=(20, 10), pady=15)

        if status:
            button_status = ctk.CTkButton(
                task_row,
                text="Completed",
                fg_color="#238636",
                state=ctk.DISABLED,
                width=110,
                height=32,
                font=("SF Pro Text", 12, "bold"),
                corner_radius=16
            )
        else:
            button_status = ctk.CTkButton(
                task_row,
                text="Pending",
                fg_color="#58A6FF",
                hover_color="#1F6FEB",
                width=110,
                height=32,
                font=("SF Pro Text", 12, "bold"),
                corner_radius=16,
                command=lambda t=task_name: complete_task(tasks, t, task_view_frame)
            )

        button_status.grid(row=0, column=1, padx=8, pady=12)

        button_delete = ctk.CTkButton(
            task_row,
            text="Delete",
            fg_color="#F85149",
            hover_color="#F66A6B",
            width=80,
            height=32,
            font=("SF Pro Text", 12, "bold"),
            command=lambda t=task_name: delete_task(tasks, t, task_view_frame)
        )
        button_delete.grid(row=0, column=2, padx=(0, 15), pady=12)


def main():
    tasks = store_data.load_tasks()

    app = ctk.CTk()
    app.title("To-Do")
    app.geometry("700x600")
    app.minsize(500, 450)
    app.resizable(True, True)
    app.configure(fg_color="#0D1117")

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(2, weight=1)

    welcome_text = ctk.CTkLabel(
        app,
        text="Welcome to To-Do",
        font=("SF Pro Text", 34, "bold"),
        text_color="#C9D1D9"
    )
    welcome_text.grid(row=0, column=0, pady=(20, 10))

    add_frame = ctk.CTkFrame(
        app,
        fg_color="#161B22",
        corner_radius=16,
        border_width=1,
        border_color="#30363D"
    )
    add_frame.grid(row=1, column=0, padx=25, pady=(0, 20), sticky="ew")
    add_frame.grid_columnconfigure(0, weight=1)

    new_task = ctk.CTkEntry(
        add_frame,
        placeholder_text="New Task",
        font=("SF Pro Text", 16),
        height=42,
        corner_radius=10,
        border_width=1,
        border_color="#30363D",
        text_color="#C9D1D9",
        fg_color="#0D1117"
    )
    new_task.grid(row=0, column=0, padx=(20, 10), pady=12, sticky="ew")

    def append_tasks():
        task_name = new_task.get().strip()
        if task_name:
            if logic.add_tasks(tasks, task_name):
                store_data.save_tasks(tasks)
                render_tasks(task_view_frame, tasks)
                new_task.delete(0, "end")

    submit = ctk.CTkButton(
        add_frame,
        text="Add",
        font=("SF Pro Text", 16, "bold"),
        fg_color="#238636",
        hover_color="#2EA44F",
        width=120,
        height=42,
        corner_radius=10,
        command=append_tasks
    )
    submit.grid(row=0, column=1, padx=(0, 20), pady=12)

    task_view_frame = ctk.CTkScrollableFrame(
        app,
        fg_color="#161B22",
        corner_radius=16,
        scrollbar_button_color="#484F58",
        scrollbar_button_hover_color="#6E7681"
    )
    task_view_frame.grid(row=2, column=0, padx=25, pady=(0, 25), sticky="nsew")

    render_tasks(task_view_frame, tasks)

    app.mainloop()


if __name__ == "__main__":
    main()
