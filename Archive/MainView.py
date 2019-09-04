import Tkinter
import tkMessageBox
import Aplikasi

def main():
    # Membuat form utama
    mainform = Tkinter.Tk()

    def buttonclick():
        app = Aplikasi.Aplikasi()
        result = app.main(txt.get("1.0", 'end-1c'))
        tkMessageBox.showinfo("Result", result)

    # Mengubah Title bar
    mainform.wm_title('News Categorization')

    # Mengubah background
    mainform['background'] = '#FFFFFF'

    # Membuat label
    lbl = Tkinter.Label(mainform)
    lbl['text'] = 'Masukan berita'
    lbl.pack()

    # Membuat input
    txt = Tkinter.Text(mainform)
    txt['width'] = 100
    txt['height'] = 40
    txt.pack()

    # Membuat objek button
    btn = Tkinter.Button(mainform, command=buttonclick)
    btn['text'] = 'Submit'
    btn.pack()

    # Menampilkan form
    mainform.mainloop()

if __name__ == '__main__':
    main()