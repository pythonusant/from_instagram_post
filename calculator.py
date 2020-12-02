# import dari tkinter module 
from tkinter import *

# deklarasi variable expression untuk hitung
expression = "" 


# Function untuk update expression 
# di tempat text
def press(num): 
	# mengambil variable global untuk perhitungan
	global expression 

	# menggabungkan string agar muncul 
	expression = expression + str(num) 

	# update perhitungan dengan simbol hitung
	equation.set(expression) 


# Function untuk menghitung hasil akhir 
def equalpress(): 
	# Try and except digunakan untuk
    # cek jika ada perhitungan error
    # seperti dibagi dengan 0 dan lain-lain. 

	try: 

		global expression 

		# eval function digunakan untuk
        # verifikasi perhitungan kemudian
        # diubah menjadi string
		total = str(eval(expression)) 

		equation.set(total) 

		# mengembalikan nilai kosong ke kotak hitung 
		expression = "" 

	# untuk memunculkan jika terjadi error perhitungan
	except: 

		equation.set(" error ") 
		expression = "" 


# Function untuk mengosongi kotak perhitungan
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# membuat GUI window 
	gui = Tk() 

	# Menentukan warna latar GUI window 
	gui.configure(background="white") 

	# Judul window
	gui.title("Kalkulator Sederhana") 

	# Menentukan ukuran window
	gui.geometry("270x150") 

	equation = StringVar() 

	# membuat tempat untuk nilai yg dimasukkan
	expression_field = Entry(gui, textvariable=equation) 

	# mengatur penempatan tombol 
	expression_field.grid(columnspan=4, ipadx=70) 

	equation.set('Masukkan perhitungan') 

	# membuat tombol dan menempatkan pada posisinya 
	button1 = Button(gui, text=' 1 ', fg='black', bg='grey', 
					command=lambda: press(1), height=1, width=7) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='grey', 
					command=lambda: press(2), height=1, width=7) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='grey', 
					command=lambda: press(3), height=1, width=7) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='grey', 
					command=lambda: press(4), height=1, width=7) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='grey', 
					command=lambda: press(5), height=1, width=7) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='grey', 
					command=lambda: press(6), height=1, width=7) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='grey', 
					command=lambda: press(7), height=1, width=7) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='grey', 
					command=lambda: press(8), height=1, width=7) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='grey', 
					command=lambda: press(9), height=1, width=7) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='grey', 
					command=lambda: press(0), height=1, width=7) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='grey', 
				command=lambda: press("+"), height=1, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='grey', 
				command=lambda: press("-"), height=1, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='grey', 
					command=lambda: press("*"), height=1, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='grey', 
					command=lambda: press("/"), height=1, width=7) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='grey', 
				command=equalpress, height=1, width=7) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='grey', 
				command=clear, height=1, width=7) 
	clear.grid(row=5, column='1') 

	Decimal= Button(gui, text='.', fg='black', bg='grey', 
					command=lambda: press('.'), height=1, width=7) 
	Decimal.grid(row=6, column=0) 
	# start the GUI 
	gui.mainloop() 
