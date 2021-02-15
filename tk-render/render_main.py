import tkinter as tk
from text_box import TextBox


def render():
    window = tk.Tk(className='python-tbag')
    tf = tk.LabelFrame().pack()
    label = tk.Label(master=tf, text='This is a test', fg='white', bg='black').pack()

    window.mainloop()


if __name__ == '__main__':
    render()
