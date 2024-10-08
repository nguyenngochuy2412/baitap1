import tkinter as tk
from tkinter import messagebox

# Hàm để giải phương trình bậc 1
def giaiphuongtrinh_bac1():
    try:
        # Lấy giá trị từ các ô nhập liệu
        a = float(entry_a.get())
        b = float(entry_b.get())
        
        # Giải phương trình bậc 1: ax + b = 0
        if a == 0:
            if b == 0:
                kq = "Phương trình có vô số nghiệm"
            else:
                kq = "Phương trình vô nghiệm"
        else:
            x = -b / a
            kq = f"Phương trình có nghiệm: x = {x:.2f}"
        
        kq_pt.config(text=kq)
    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

# Hàm thoát chương trình
def exit_program():
    if messagebox.askyesno("Thoát", "Bạn có muốn thoát không?"):
        win.quit()

# Tạo cửa sổ chính
win = tk.Tk()
win.title("Giải Phương Trình Bậc 1")

# Tạo menu
menu_bar = tk.Menu(win)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)
win.config(menu=menu_bar)

# Tạo LabelFrame để nhập các giá trị a, b
frame_input = tk.LabelFrame(win, text="Nhập các hệ số", padx=10, pady=10)
frame_input.pack(side=tk.LEFT, padx=10, pady=10)

# Label và Entry cho hệ số a
so_a = tk.Label(frame_input, text="Hệ số a:")
so_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_input)
entry_a.grid(row=0, column=1, padx=5, pady=5)

# Label và Entry cho hệ số b
so_b = tk.Label(frame_input, text="Hệ số b:")
so_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_input)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Tạo LabelFrame để hiển thị nút giải và kết quả
frame_result = tk.LabelFrame(win, text="Kết quả", padx=10, pady=10)
frame_result.pack(side=tk.RIGHT, padx=10, pady=10)

# Nút giải phương trình
kq_btn = tk.Button(frame_result, text="Giải", command=giaiphuongtrinh_bac1)
kq_btn.grid(row=0, column=0, padx=5, pady=5)

# Label để hiển thị kết quả
kq_pt = tk.Label(frame_result, text="Kết quả sẽ hiển thị tại đây")
kq_pt.grid(row=0, column=1, padx=5, pady=5)

# Chạy chương trình
mainloop()
