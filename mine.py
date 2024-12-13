import tkinter as tk
from tkinter import messagebox

def play_text():
    text = entry.get()
    if text.strip():
        # هنا يمكن إدراج أي وظيفة لتحويل النص إلى كلام
        print(f"Playing: {text}")
    else:
        messagebox.showwarning("تنبيه", "الرجاء إدخال نص لتشغيله.")

def exit_program():
    root.destroy()

def clear_text():
    entry.delete(0, tk.END)

# إنشاء نافذة GUI
root = tk.Tk()
root.title("Text to Speech")

# حقل إدخال النص
entry = tk.Entry(root, width=100)
entry.pack(pady=10)

# زر التشغيل
play_button = tk.Button(root, text="Play", command=play_text)
play_button.pack(side=tk.LEFT, padx=10)

# زر الإغلاق
exit_button = tk.Button(root, text="Exit", fg="red", command=exit_program)
exit_button.pack(side=tk.LEFT, padx=10)

# زر المسح
set_button = tk.Button(root, text="set", command=clear_text)
set_button.pack(side=tk.LEFT, padx=10)

# تشغيل التطبيق
root.mainloop()