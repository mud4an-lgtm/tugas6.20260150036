#import modul_evaluasi

def input_angka_valid(prompt,min_val,max_val):
 while True:
   try:
        #teks_input = input(f"masukkan angka{prompt,min_val,max_val}")
        #nilai = float(teks_input)
        nilai = float(input(prompt))        
        #if nilai<0 or nilai > 100:
         #    print("[WARNING]nilai")
          #   continue 
        #
        #return nilai
    #except ValueError:
     #  print("ERROR SISTEM")
        if nilai < min_val or nilai >max_val:
           print("[WARNING]Angka harus antara",min_val, "sampai",max_val)
        else: 
              return   nilai 
   #while True:
      #   try:
       #      pilihan = int(input(""))  
