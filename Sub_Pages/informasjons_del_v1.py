import ttkbootstrap as ttk
import pandas as pd
from tkinter import filedialog, messagebox
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as mlp

#------------------------------------------------------------------------------
#CSV FIler
#------------------------------------------------------------------------------
def csv_leser():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV-filer", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path, encoding="utf-8", sep=csv_sep())
            antall_rader = min(len(df), len(df))
            widgets_combobox_head["values"] = [i for i in range(1, antall_rader + 1)]

            kolonne_navn = df.columns.to_list()
            widgets_combobox_4["values"] = kolonne_navn
            widgets_combobox_5["values"] = ["None"] + kolonne_navn

            widgets_combobox_head.current(4)
            messagebox.showinfo("Suksess", "Fil lastet inn!")
        except Exception as e:
            messagebox.showerror("Feil", f"Kunne ikke lese filen: {e}")
            print(df.info)

#------------------------------------------------------------------------------
#Csv_Sep
#------------------------------------------------------------------------------
def csv_sep():
    global csv_sep_valgt
    csv_sep_valgt = widgets_sep_entry.get()
    return csv_sep_valgt    

#------------------------------------------------------------------------------
#Vanlig info "Skjerm 1"
#------------------------------------------------------------------------------
def skjerm_1(event):
    if "df" not in globals():
        box1_label.delete("1.0", "end")
        box1_label.insert("end", "Putt inn CSV Fil")
        return
    
    valgt_info = widgets_combobox_1.get().lower()
    try:
        if valgt_info == "lengde":
            a = len(df)
        elif valgt_info == "columns":
            a = "Kolonner:\n" + "\n".join(df.columns.to_list())
        elif valgt_info == "dtypes":
            a = f"Datatyper:\n{df.dtypes}"
        elif valgt_info == "head":
            b = widgets_combobox_head.get()
            a = f"Head:\n{df.head(int(b)).to_string(index = False)}"
        elif valgt_info == "statistikk":
            a = f"Describe:\n{df.describe().to_string()}"
        elif valgt_info == "manglende info":
            a = f"Manglende Info:\n{df.isnull().sum().to_string()}"
        elif valgt_info == "info":
            buffer = io.StringIO()
            df.info(buf=buffer)
            a = f"Info:\n{buffer.getvalue()}"
        elif valgt_info == "unike verdier":
            a = f"Unike Verdier Per kolonner:\n{df.nunique().to_string()}"
        elif valgt_info == "duplikat":
            a = f"Duplikater:\n{df.duplicated().sum()}"
        elif valgt_info == "skjevhetsfordeling":
            a = f"Skjevhetsfordeling:\n{df.skew(numeric_only= True).round(3).to_string()}"
        else:
            a = "Går ikke"
        box1_label.config(state = "normal")
        box1_label.delete("1.0", "end")
        box1_label.insert("end", a)
        box1_label.config(state = "disabled")
    except Exception as e:
        box1_label.config(state= "normal")
        box1_label.insert("end", f"\nFeil: {e}")

def meny_help_func_skjerm_1():
    a = (
        "Columns:\n\tReturnerer navnene på alle kolonnene i DataFrame.\n\tdf.columns"\
        "\n\nInfo:\n\tGir kompakt info om 'df'\n\tInneholder:\n\t\tColumns Navn \n\t\tLen(df)\n\t\tDtypes\n\tdf.info()"\
        "\n\nLengde:\n\tReturnerer lengde på 'df' som integer\n\tlen(df), kan bruke df.shape[0]"\
        "\n\nDtypes:\n\tReturnere datatypen til hver kolonne: \n\t\tinteger/int64 \n\t\tstr/object\n\t\tfloat/float64\n\tdf.dtypes"\
        "\n\nHead:\n\tViser antall rader basert på X\n\tdf.head(x)"\
        "\n\nStatistikk\n\tViser:\n\t\tGjennomsnitt/Mean\n\t\tAvvik/std\n\t\t\tLav Verdi = Tallene ligger nærmere Mean"\
        "\n\t\t\t Høy Verdi = Tallene variere og stor avstand mellom høye og lave tall"\
        "\n\t\tMin/Max\n\t\tKvartiler:\n\t\t\tViser kun 1 verdi FRA 'df'\n\t\t\t25%: 25% minste tall\n\t\t\t50%: Median\n\t\t\t75%: Top 25 største tall\n\t\tdf.describe()"\
        "\n\nManglende Info:\n\tGir Antall manglende verdier per kolonne\n\tReturnere enten True/False eller 1/0\n\tdf.isnull().sum()"\
        "\n\nUnike Verdier:\n\tTeller antall unike verdier per kolonne\n\tdf.nunique()"\
        "\n\nDuplikater:\n\tAntall dupliserte rader, inkluderer ikke første forekomst\n\tdf.duplicated().sum()"\
        "\n\nSkjevhetsfordeling:\n\tSammenligner all data med Mean og om på verdi til hvert tall\n\tEks:[2, 4, 5, 7, 200] \n\tvil gjøre skew veldig positiv"\
        "\n\tdf.skew.round(3)"
    )

    box1_label.config(state = "normal")
    box1_label.delete("1.0", "end")
    box1_label.insert("end", a)
    box1_label.config(state = "disabled")
#-----------------------------------------------------------------------------
#Funksjoner for skjerm 2
#-----------------------------------------------------------------------------
def skjerm_2(event):
    if "df" not in globals():
        return
    try:
        # 1. Hent verdiene. VIKTIG: Ikke bruk .lower() på kolonnenavnene!
        global k1, k2, hvilken_analyse
        hvilken_analyse = widgets_combobox_2.get().lower()
        head_graf = widgets_combobox_3.get().lower()
        k1 = widgets_combobox_4.get() 
        k2 = widgets_combobox_5.get()

        if hvilken_analyse and head_graf and k1:
            
            a = None

            if hvilken_analyse == "groupby":
                if head_graf == "head":
                    if k2 == "None" or k2 == "":
                        a = df.groupby(k1).size()
                    else:
                        a = df.groupby(k1)[k2].mean()

                elif head_graf == "graf":
                    if k2 == "None" or k2 == "":
                        b = df.groupby(k1).size()
                        graf_skjerm_2(b)
                    else:
                        b = df.groupby(k1)[k2].mean()
                        graf_skjerm_2(b)

            elif hvilken_analyse == "sort values":
                if head_graf == "head":
                    if k2 == "None" or k2 == "":
                        a = df.sort_values(by=k1, ascending=False).head(len(df))
                    else:
                        a = df.sort_values(by=[k1, k2], ascending=[True, False]).head(len(df))
                elif head_graf == "graf":
                    if k2 == "None" or k2 == "":
                        b = df.sort_values(by=k1, ascending=False).head(len(df))
                        graf_skjerm_2(b)
                    else:
                        b = df.sort_values(by=[k1, k2], ascending=[True, False]).head(len(df))
                        graf_skjerm_2(b)

            elif hvilken_analyse == "value counts":
                if head_graf == "head":
                    if k2 == "None" or k2 == "":
                        a = df[k1].value_counts()
                    else:
                        a = df[[k1, k2]].value_counts()
                elif head_graf == "graf":
                    if k2 == "None" or k2 == "":
                        b = df[k1].value_counts()
                        graf_skjerm_2(b)
                    else:
                        b = df[[k1, k2]].value_counts()
                        graf_skjerm_2(b)

            elif hvilken_analyse == "boolean verdi":
                if head_graf == "head":
                    # Her filtrerer vi k1 basert på verdien i k2
                    a = df[df[k1].astype(str) == k2]

                elif head_graf == "graf":
                    b = df[df[k1].astype(str) == k2]
                    graf_skjerm_2(b)

            elif hvilken_analyse == "pivot table":
                if head_graf == "head":
                    if k2 != "None" and k2 != "":
                        a = df.pivot_table(index=k1, columns=k2, aggfunc='size', fill_value=0)
                    else:
                        a = "Velg en kolonne 2 for Pivot Table"
                elif head_graf == "graf":
                    if k2 != "None" and k2 != "":
                        b = df.pivot_table(index=k1, columns=k2, aggfunc='size', fill_value=0)
                        graf_skjerm_2(b)
                    else:
                        b = "Velg en kolonne 2 for Pivot Table"
                        graf_skjerm_2(b)

            # 3. Sjekk om vi faktisk fikk et resultat før vi prøver å vise det
            if a is not None:
                if not box2_label.winfo_exists():
                    liv_tekstboks()

                res_tekst = a.to_string() if isinstance(a, (pd.DataFrame, pd.Series)) else str(a)
                
                box2_label.config(state="normal")
                box2_label.delete("1.0", "end")
                box2_label.insert("end", res_tekst)
                box2_label.config(state="disabled")
            else:
                # Hvis head_graf er "graf", men ikke implementert ennå
                box2_label.config(state="normal")
                box2_label.delete("1.0", "end")
                box2_label.insert("end", "Valgt visning (f.eks Graf) er ikke klar.")
                box2_label.config(state="disabled")
        
        else:
            # Denne vises hvis brukeren mangler å velge noe i boksene
            box2_label.config(state="normal")
            box2_label.delete("1.0", "end")
            box2_label.insert("end", "Vennligst velg Analyse, Head/Graf og Kolonne 1")
            box2_label.config(state="disabled")

    except Exception as e:
        box2_label.config(state="normal")
        box2_label.delete("1.0", "end")
        box2_label.insert("end", f"Feil: {e}")
        box2_label.config(state="disabled")

def graf_skjerm_2(info_pakke):
    if isinstance(info_pakke, str):
        messagebox.showwarning("Feil", info_pakke)
        return

    for widget in box2_frame.winfo_children():
        widget.destroy()

    box2_frame.grid_propagate(False)
    box2_frame.config(width = 600, height = 500)


    fig = mlp.Figure(figsize= (4, 3), dpi= 100)
    c = fig.add_subplot(111)

    try:
        info_pakke.plot(kind = "bar", ax = c, color = "#4ec3ad")
        c.set_title(f"Graf.{hvilken_analyse}.{k1}.{k2}:")
        c.tick_params(axis= "x", rotation = 45, labelsize = 7)
        c.tick_params(axis = "y", labelsize = 8)
        fig.tight_layout()
        
        graf_bilde = FigureCanvasTkAgg(fig, master= box2_frame)
        cdd = graf_bilde.get_tk_widget()
        cdd.config(width= 100, height= 100)
        cdd.pack(
            side = "top",
            fill = "both",
            expand= True
        )
        graf_bilde.draw()
    except Exception as e:
        messagebox.showerror("Graf feil", f"Error: {e}")

def liv_tekstboks():
    global box2_label

    for widget in box2_frame.winfo_children():
        widget.destroy

    box2_scrollbar = ttk.Scrollbar(
        box2_frame, 
        orient= "vertical"
    )
    box2_scrollbar.pack(
        side= "right",
        fill = "y"
    )
    box2_scrollbar_x = ttk.Scrollbar(
        box2_frame,
        orient = "horizontal"
    )
    box2_scrollbar_x.pack(
        side = "bottom",
        fill = "x"
    )

    box2_label = ttk.Text(
        box2_frame, 
        width = 50,
        height= 30, 
        wrap = "none",
        font = ("Courier", 10),
        yscrollcommand= box2_scrollbar.set,
        xscrollcommand= box2_scrollbar_x.set
    )
    box2_label.pack(
        side = "left",
        fill = "both",
        expand= True
    )

def meny_help_func_skjerm_2():
    a = (
        "Groupby:\n\t1 Kolonne:\n\t\tGrupperer alle rader etter verdiene i kolonnen via gjennomsnitt\n\t\tdf.groupby('k1').size()"\
        "\n\t2 Kolonne:\n\t\tLager grupper basert på kombinasjonen av kolonne 1 og 2\n\t\tdf.groupby('k1')['k2'].mean()"\
        
        "\n\nSort Values\n\t1 Kolonne:\n\t\tSortere rader etter verdier i én kolonner, via synkende\n\t\tdf.sort_values(by='k1', ascending=False).head(len(df))"\
        "\n\t2 Kolonne:\n\t\tSorterer først etter col1, deretter col2 hvis det er likhet i første"\
        "\n\t\tRekkefølgen bestemmer prioritet på hva som er likt\n\t\tdf.sort_values(by=['k1', 'k2'], ascending=[True, False]).head(len(df))"\
        
        "\n\nValue Counts:\n\t1 Kolonne:\n\t\tReturnerer hvor mange ganger hver verdi forekommer"\
        "\n\t\tdf[k1].value_counts()\n\t2 Kolonne:\n\t\tfinner alle unike par av verdier som finnes i de to kolonnene "\
        "\n\t\tog teller hvor mange ganger akkurat den kombinasjonen forekommer\n\t\tdf[['k1', 'k2']].value_counts()"\
        
        "\n\nBoolean Verdi."\
        "\n\t1 Kolonne:"\
        "\n\t\tBrukes for å filtrere rader basert på betingelser \n\t\tBruker <,>,==,!=,<=,>=, etc\n\t\tdf[df['1 Kolonne'] > 10]"\
        "\n\t2 Kolonne"\
        "\n\t\tDet samme, men at begge skal være True (bruk tegnet &)\n\t\tEnten Kolonne 1 eller 2 er True (bruk tegnet |)"\
        "\n\t\tEks:df[(df['1 Kolonne'] > 30) | (df['2 Kolonne'] == x)]"

        "\n\nPivot Table:\n\t1 Kolonne:"\
        "\n\t\tBrukes for å lage en oppsummert tabell (krysstabell)\n\t\tpd.pivot_table(df, values= '1 Kolonne', index= '2 Kolonne', aggfunc='mean')"\
        "\n\t2 Kolonne:"\
        "\n\t\tOmgjør 1 Kolonne til ROWS, 2 Kolonne til COLUMNS\n\t\tLager et Datasett ved de to kolonnene"\
        "\n\t\tdf.pivot_table(index=k1, columns=k2, aggfunc='size', fill_value=0)"
    )

    box2_label.config(state = "normal")
    box2_label.delete("1.0", "end")
    box2_label.insert("end", a)
    box2_label.config(state = "disabled")

#------------------------------------------------------------------------------
#Tkinter del
#------------------------------------------------------------------------------
def tkinter_del(vindu):
    global content_frame, widgets_sep_entry, widgets_combobox_1, box1_label, box2_label, widgets_combobox_head, widgets_combobox_5, widgets_combobox_2, widgets_combobox_3, widgets_combobox_4, box2_frame
    content_frame = vindu
    content_frame.columnconfigure(0, weight=1)
    content_frame.columnconfigure(1, weight=2)
    content_frame.columnconfigure(2, weight=3)
    #widgets --------------------------------------------------------------------------------
    
    widgets_frame = ttk.Frame(
        content_frame
    )
    widgets_frame.grid(
        column = 0, 
        row = 0, 
        padx= 20
    )

    widgets_heading = ttk.Label(
        widgets_frame, 
        text = "CSV Leser"
    )
    widgets_heading.pack(pady = 10)

    widgets_velg_fil_button = ttk.Button(
        widgets_frame, 
        command= csv_leser, 
        text = "Velg CSV FIl"
    )
    widgets_velg_fil_button.pack(pady = 10)


    widgets_sep_label = ttk.Label(
        widgets_frame,
        text = "hvilken Sep\nBruker CSV"
    )
    widgets_sep_label.pack(pady = 10)

    widgets_sep_entry = ttk.Entry(
        widgets_frame
    )
    widgets_sep_entry.pack()


    #-------------------------------------------------------------
    #Hvilken type basic info
    CB_Value_1 = ["Columns", "Info","Lengde", "Dtypes", "Head", "Statistikk", "Manglende Data", "Unike Verdier", "Duplikat", "Skjevhetsfordeling"]

    widgets_combobox_1_label = ttk.Label(
        widgets_frame,
        text= "Bruker Valg"
    )
    widgets_combobox_1_label.pack(pady = 10)

    #Basic info
    widgets_combobox_1 = ttk.Combobox(
        widgets_frame,
        values= CB_Value_1, 
        state= "readonly"
    )
    widgets_combobox_1.pack(pady = 10)

    widgets_combobox_head = ttk.Combobox(
        widgets_frame, 
        values= [],
        state = "readonly"
    )
    widgets_combobox_head.pack(pady = 10)

    #Andre skjerm-------------------------------------------------------------------------
    #Velge om groupby etc
    CB_Value_2 = ["Groupby", "Sort values", "Value counts", "Boolean Verdi", "Pivot table"]

    CB_Value_3 = ["Head", "Graf"]

    widgets_combobox_2_label = ttk.Label(
        widgets_frame,
        text= "Filtrering\nStatistikk"
    )
    widgets_combobox_2_label.pack(pady = 10)

    #Velge groupby og de andre tingene
    widgets_combobox_2 = ttk.Combobox(
        widgets_frame,
        values= CB_Value_2,
        state= "readonly"
    )
    widgets_combobox_2.pack(pady = 10)

    widgets_combobox_3_label = ttk.Label(
        widgets_frame,
        text= "Head/Graf"
    )
    widgets_combobox_3_label.pack(pady = 10)

    #Velge Head eller graf
    widgets_combobox_3 = ttk.Combobox(
        widgets_frame,
        values= CB_Value_3,
        state= "readonly"
    )
    widgets_combobox_3.pack(pady = 10)

    #.....................................

    widgets_combobox_4_label = ttk.Label(
        widgets_frame,
        text= "Kolonne 1"
    )
    widgets_combobox_4_label.pack(pady = 10)

    #Velge andre kolonne
    widgets_combobox_4 = ttk.Combobox(
        widgets_frame,
        values= [],
        state= "readonly"
    )
    widgets_combobox_4.pack(pady = 10)

    widgets_combobox_5_label = ttk.Label(
        widgets_frame,
        text= "Kolonne 2"
    )
    widgets_combobox_5_label.pack(pady = 10)

    #Velge verdi innenfor kolonne valgt
    widgets_combobox_5 = ttk.Combobox(
        widgets_frame,
        values= [],
        state= "readonly"
    )
    widgets_combobox_5.pack(pady = 10)


    #box 1 --------------------------------------------------------------------------------------

    box1_frame = ttk.Frame(
        content_frame
    )
    box1_frame.grid(
        column= 1, 
        row = 0, 
        padx  = 20
    )

    box1_scrollbar = ttk.Scrollbar(
        box1_frame, 
        orient= "vertical"
    )
    box1_scrollbar.pack(
        side= "right",
        fill = "y"
    )
    box1_scrollbar_x = ttk.Scrollbar(
        box1_frame,
        orient = "horizontal"
    )
    box1_scrollbar_x.pack(
        side = "bottom",
        fill = "x"
    )

    box1_label = ttk.Text(
        box1_frame, 
        width = 40,
        height= 30, 
        wrap = "none",
        font = ("Courier", 10),
        yscrollcommand= box1_scrollbar.set,
        xscrollcommand= box1_scrollbar_x.set
    )
    box1_label.pack(
        side = "left",
        fill = "both",
        expand= True
    )

    box1_label.insert("end", "results")
    box1_label.config(state = "disabled")


    meny_help = ttk.Button(
        content_frame, 
        text = "Help Skjerm 1",
        command= meny_help_func_skjerm_1
    )
    meny_help.grid(
        pady= 7,
        column = 1,
        row = 1, 
        ipadx = 20, 
        ipady= 15
    )

    #box 2 ---------------------------------------------------------------------------------------
    box2_frame = ttk.Frame(
        content_frame
    )
    box2_frame.grid(
        column= 2, 
        row = 0, 
        padx  = 20
    )

    box2_scrollbar = ttk.Scrollbar(
        box2_frame, 
        orient= "vertical"
    )
    box2_scrollbar.pack(
        side= "right",
        fill = "y"
    )
    box2_scrollbar_x = ttk.Scrollbar(
        box2_frame,
        orient = "horizontal"
    )
    box2_scrollbar_x.pack(
        side = "bottom",
        fill = "x"
    )

    box2_label = ttk.Text(
        box2_frame, 
        width = 50,
        height= 30, 
        wrap = "none",
        font = ("Courier", 10),
        yscrollcommand= box2_scrollbar.set,
        xscrollcommand= box2_scrollbar_x.set
    )
    box2_label.pack(
        side = "left",
        fill = "both",
        expand= True
    )

    meny_help = ttk.Button(
        content_frame, 
        text = "Help Skjerm 2",
        command= meny_help_func_skjerm_2
    )
    meny_help.grid(
        pady= 7,
        column = 2,
        row = 1, 
        ipadx = 20, 
        ipady= 15
    )

    box2_label.insert("end", "results")
    box2_label.config(state = "disabled")

    #-----------------------------------------------------------------------------------
    box1_scrollbar.config(command= box1_label.yview)
    box1_scrollbar_x.config(command= box1_label.xview)

    box2_scrollbar.config(command= box2_label.yview)
    box2_scrollbar_x.config(command= box2_label.xview)

    #For at den skal oppdateres hver gang combobox endres
    widgets_combobox_1.bind("<<ComboboxSelected>>", skjerm_1)
    widgets_combobox_head.bind("<<ComboboxSelected>>", skjerm_1)
    widgets_combobox_2.bind("<<ComboboxSelected>>", skjerm_2)
    widgets_combobox_3.bind("<<ComboboxSelected>>", skjerm_2)
    widgets_combobox_4.bind("<<ComboboxSelected>>", skjerm_2)
    widgets_combobox_5.bind("<<ComboboxSelected>>", skjerm_2)


if __name__ == "__main__":
    tkinter_del()
