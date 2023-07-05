# Aplikacja, która na podstawie wprowadzonych danych w pola wejściowe
# oblicza średnią końcoworoczną ocen ucznia klasy 4-6 (trzeba sprawdzić,
# jakie są przedmioty w klasach 4-6), a następnie pokazuje komunikat
# (świadectwo bez wyróżnienia, świadectwo z wyróżnieniem). Świadectwo
# jest świadectwem z wyróżnieniem, gdy średnia ucznia wynosi co
# najmniej 4,75, a zachowanie ucznia jest co najmniej bdb. Program
# powinien zawierać etykiety przedmiotów, pola wejściowe do
# wprowadzania ocen oraz dwa pola tekstowe, pierwsze, w którym
# wyświetla się średnia oraz drugie, w którym wyświetla się napis
# „świadectwo z wyróżnieniem” lub „świadectwo bez wyróżnienia”. Błędy
# wprowadzanych danych zabezpieczyć oknami dialogowymi.

from tkinter import *
from tkinter import messagebox
import textwrap

class Aplikacja_projektowa(object):
    ilosc_przedmiotow,suma_ocen,klasy4,klasy56=0,0,["4","IV","iv"],["5","6","V","VI","v","vi"]
    def __init__(self):
        self.okno = Tk()
        self.okno.configure(background="#d4e3f4")
        self.okno.title("Świadectwo ucznia")
        self.okno.geometry("700x400")
        self.ramka=Frame(self.okno,bg="#d4e3f4")
        self.ramka.grid()
        self.__stworz_widgety__()

    def __wyczysc__(self):
        self.wprImie.delete(0, END)
        self.wprNazwisko.delete(0, END)
        self.wprDateUrodzenia.delete(0, END)
        if self.wprKlase.get() in self.klasy4 or self.wprKlase.get() in self.klasy56:
            self.etykieta11.destroy()
            self.wprJezykPolski.destroy()
            self.etykieta12.destroy()
            self.wprWF.destroy()
            self.etykieta13.destroy()
            self.wprWychowawcza.destroy()
            self.etykieta14.destroy()
            self.wprHistoria.destroy()
            self.etykieta15.destroy()
            self.wprMatematyka.destroy()
            self.etykieta16.destroy()
            self.wprPlastyka.destroy()
            self.etykieta21.destroy()
            self.wprTechnika.destroy()
            self.etykieta22.destroy()
            self.wprPrzyroda.destroy()
            self.etykieta23.destroy()
            self.wprMuzyka.destroy()
            self.etykieta24.destroy()
            self.wprInformatyka.destroy()
            self.etykieta25.destroy()
            self.wprJezykObcy.destroy()
        if self.wprKlase.get() in self.klasy56:
            self.wprRE.destroy()
            self.etykieta17.destroy()
            self.etykieta26.destroy()
            self.wprGeografia.destroy()
            self.etykieta27.destroy()
            self.wprDrugiJezykObcy.destroy()
        self.etykieta6.destroy()
        self.poletext1.destroy()
        self.etykieta7.destroy()
        self.poletext2.destroy()
        self.wprKlase.delete(0, END)

    def uruchom(self):
        self.okno.mainloop()

    def __stworz_widgety__(self):
        self.etykieta1 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
        self.etykieta1["text"] = "Imię ucznia: "
        self.etykieta1.grid(row=0,column=0,sticky=EW)
        self.wprImie = Entry(self.ramka,width=32)
        self.wprImie.grid(row=0,column=1,sticky=EW)

        self.etykieta2 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
        self.etykieta2["text"] = "Nazwisko ucznia: "
        self.etykieta2.grid(row=1,column=0,sticky=EW)
        self.wprNazwisko = Entry(self.ramka,width=32)
        self.wprNazwisko.grid(row=1,column=1,sticky=EW)

        self.etykieta3 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
        self.etykieta3["text"] = "Data urodzenia: "
        self.etykieta3.grid(row=0,column=2,sticky=EW)
        self.wprDateUrodzenia = Entry(self.ramka,width=12)
        self.wprDateUrodzenia.grid(row=0,column=3,sticky=EW)

        self.etykieta4 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
        self.etykieta4["text"] = "Klasa: "
        self.etykieta4.grid(row=1,column=2,sticky=EW)
        self.wprKlase = Entry(self.ramka,width=4)
        self.wprKlase.grid(row=1,column=3,sticky=EW)

        self.przycisk1 = Button(self.ramka,width=20,height=1,bg="#95bae4",activebackground="#6ca0da",font=("Arial", 10,"bold"))
        self.przycisk1.grid(row=3,column=1,sticky=N)
        self.przycisk1["text"] = "Lista przedmiotów"
        self.przycisk1["command"] = self.__ktore_przedmioty__

        self.etykieta5 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
        self.etykieta5["text"] = "Przedmioty"
        self.etykieta5.grid(row=4, column=1, sticky=EW)
        self.etykieta6 = Label(self.ramka,bg="#dfeaf6")
        self.etykieta6["text"] = textwrap.fill("(w przypadku, w którym nie chodzisz na jakiś przedmiot - wpisz 0)",width=30)
        self.etykieta6.grid(row=5, column=1, sticky=EW)

        self.przycisk2 = Button(self.ramka, width=20, height=1,bg="#95bae4",activebackground="#6ca0da",font=("Arial", 10,"bold"))
        self.przycisk2.grid(row=15, column=1, sticky=EW)
        self.przycisk2["text"] = "Średnia i wyróżnienie"
        self.przycisk2["command"] = self.__srednia_wyr__

        self.przycisk3 = Button(self.ramka, width=20, height=1, bg="#95bae4", activebackground="#6ca0da",font=("Arial", 10, "bold"))
        self.przycisk3.grid(row=18, column=1, sticky=EW)
        self.przycisk3["text"] = "Wyczyść"
        self.przycisk3["command"] = self.__wyczysc__

    def __srednia_wyr__(self):
        try:
            napisnapasek="Brak wyróżnienia z czerwonym paskiem"
            srednianapis=""
            lista_ocen = [self.wprJezykPolski.get(),self.wprWF.get(),self.wprJezykObcy.get(),
            self.wprInformatyka.get(),self.wprMuzyka.get(),self.wprPrzyroda.get(),self.wprTechnika.get(),self.wprPlastyka.get(),
            self.wprMatematyka.get(),self.wprHistoria.get()]
            if self.wprKlase.get() in self.klasy56:
                    lista_ocen.append(self.wprGeografia.get())
                    lista_ocen.append(self.wprRE.get())
                    lista_ocen.append(self.wprDrugiJezykObcy.get())
            for i in lista_ocen:
                ocena = float(i)
                if (ocena<1 or ocena>6) and ocena!=0:
                    raise ValueError
                if ocena>=1 and ocena<=6:
                    self.suma_ocen += ocena
                    self.ilosc_przedmiotow+=1
            srednia=self.suma_ocen/self.ilosc_przedmiotow
            srednianapis=str(srednia)
            super_zachowanie=["bdb","bardzo dobry","cel","celujący","5","6","celujacy"]
            if srednia >= 4.75 and (self.wprWychowawcza.get().lower() in super_zachowanie):
                napisnapasek="Wyróżnienie z czerwonym paskiem"
        except:
            messagebox.showerror("BŁĘDNE DANE!","Wprowadź oceny za pomocą cyfr lub liczb zmiennoprzecinkowych ze znakiem \".\" w przedziale 1-6"
                                                " (jedynie zachowanie możesz zapisać słownie).")
        else:
            self.etykieta6 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta6["text"] = "Średnia: "
            self.etykieta6.grid(row=16, column=0,sticky=EW)
            self.poletext1 = Text(self.ramka, width=4, height=1,font=("Arial", 10))
            self.poletext1.grid(row=16, column=1,sticky=EW)
            self.poletext1.delete(0.0, END)
            self.poletext1.insert(0.0,srednianapis)
            self.poletext1.config(state=DISABLED)

            self.etykieta7 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta7["text"] = "Wyróżnienie: "
            self.etykieta7.grid(row=17, column=0, sticky=EW)
            self.poletext2 = Text(self.ramka, width=40, height=1,font=("Arial", 10))
            self.poletext2.grid(row=17, column=1,sticky=EW)
            self.poletext2.delete(0.0, END)
            self.poletext2.insert(0.0,napisnapasek)
            self.poletext2.config(state=DISABLED)

    def __ktore_przedmioty__(self):
        if self.wprKlase.get() in self.klasy4 or self.wprKlase.get() in self.klasy56:
            self.etykieta11 = Label(self.ramka, bg="#aac7e9",font=("Arial", 10))
            self.etykieta11["text"] = "Zachowanie: "
            self.etykieta11.grid(row=6, column=0, sticky=EW)
            self.wprWychowawcza = Entry(self.ramka, width=5)
            self.wprWychowawcza.grid(row=6, column=1, sticky=EW)

            self.etykieta12 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta12["text"] = "Język polski: "
            self.etykieta12.grid(row=7, column=0, sticky=EW)
            self.wprJezykPolski = Entry(self.ramka, width=5)
            self.wprJezykPolski.grid(row=7, column=1, sticky=EW)

            self.etykieta13 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta13["text"] = "Historia: "
            self.etykieta13.grid(row=8, column=0, sticky=EW)
            self.wprHistoria = Entry(self.ramka, width=5)
            self.wprHistoria.grid(row=8, column=1, sticky=EW)

            self.etykieta14 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta14["text"] = "Matematyka: "
            self.etykieta14.grid(row=9, column=0, sticky=EW)
            self.wprMatematyka = Entry(self.ramka, width=5)
            self.wprMatematyka.grid(row=9, column=1, sticky=EW)

            self.etykieta15 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta15["text"] = "Plastyka: "
            self.etykieta15.grid(row=10, column=0, sticky=EW)
            self.wprPlastyka = Entry(self.ramka, width=5)
            self.wprPlastyka.grid(row=10, column=1, sticky=EW)

            self.etykieta16 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta16["text"] = "Przyroda: "
            self.etykieta16.grid(row=11, column=0, sticky=EW)
            self.wprPrzyroda = Entry(self.ramka, width=5)
            self.wprPrzyroda.grid(row=11, column=1, sticky=EW)

            self.etykieta21 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta21["text"] = "Muzyka: "
            self.etykieta21.grid(row=6, column=2, sticky=EW)
            self.wprMuzyka = Entry(self.ramka, width=5)
            self.wprMuzyka.grid(row=6, column=3, sticky=EW)

            self.etykieta22 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta22["text"] = "Informatyka: "
            self.etykieta22.grid(row=7, column=2, sticky=EW)
            self.wprInformatyka = Entry(self.ramka, width=5)
            self.wprInformatyka.grid(row=7, column=3, sticky=EW)

            self.etykieta23 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta23["text"] = "Wychowanie fizyczne: "
            self.etykieta23.grid(row=8, column=2, sticky=EW)
            self.wprWF = Entry(self.ramka, width=5)
            self.wprWF.grid(row=8, column=3, sticky=EW)

            self.etykieta24 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta24["text"] = "Technika: "
            self.etykieta24.grid(row=9, column=2, sticky=EW)
            self.wprTechnika = Entry(self.ramka, width=5)
            self.wprTechnika.grid(row=9, column=3, sticky=EW)

            self.etykieta25 = Label(self.ramka, bg="#aac7e9",font=("Arial", 10))
            self.etykieta25["text"] = "Język obcy: "
            self.etykieta25.grid(row=10, column=2, sticky=EW)
            self.wprJezykObcy = Entry(self.ramka, width=5)
            self.wprJezykObcy.grid(row=10, column=3, sticky=EW)

        if self.wprKlase.get() in self.klasy56:
            self.etykieta26 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta26["text"] = "Drugi język obcy: "
            self.etykieta26.grid(row=11, column=2, sticky=EW)
            self.wprDrugiJezykObcy = Entry(self.ramka, width=5)
            self.wprDrugiJezykObcy.grid(row=11, column=3, sticky=EW)

            self.etykieta17 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta17["text"] = "Geografia: "
            self.etykieta17.grid(row=12, column=0, sticky=EW)
            self.wprGeografia = Entry(self.ramka, width=5)
            self.wprGeografia.grid(row=12, column=1, sticky=EW)

            self.etykieta27 = Label(self.ramka,bg="#aac7e9",font=("Arial", 10))
            self.etykieta27["text"] = "Religia/ Etyka: "
            self.etykieta27.grid(row=12, column=2, sticky=EW)
            self.wprRE = Entry(self.ramka, width=5)
            self.wprRE.grid(row=12, column=3, sticky=EW)




Aplikacja_projektowa().uruchom()