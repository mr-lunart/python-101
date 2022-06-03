import tkinter as tk

def dataReader(filenames):
    with open(filenames) as temp_data:
        
        while True:
            char=temp_data.read().splitlines()
            if len(char)>0:
                lines=char
            if not char:
                break

    array_temp=[]
    for x in range(len(lines)):
        row=lines[x]
        block=[]
        for y in range(len(row)):
            block.append(row[y])
        array_temp.append(block)
    lines=[]
    x=None
    y=None
    return (array_temp)

def drawBox(X1,Y1,X2,Y2,warna):
    return cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill=warna)

def drawMap(files):
    Y1=30
    Y2=60
    panjang=30
    block=True
    for i in range(len(files)):
        
        X1=30
        X2=60
        cnv.create_text((X1-15, Y1+15), text=i)
        
        for y in range(len(files[i])):
            
            if block == True:
                cnv.create_text((X1+15, Y1-15), text=y)
                if y+1 == len(files[i]):
                    block=False

            if files[i][y] == '0':
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='white')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=files[i][y])
                #time.sleep(0.1)
                # print(files[i][y])

            elif files[i][y] =='1':
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='grey')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=files[i][y])
                #time.sleep(0.1)
                # print(files[i][y])

            elif files[i][y] =='a':
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='green')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=' A')
                #time.sleep(0.1)
                # print(files[i][y])
                
            elif files[i][y] =='b':
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='green')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=' B')
                #time.sleep(0.1)
                # print(files[i][y])

            elif int(files[i][y]) == 2:
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='yellow')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=files[i][y])
                #time.sleep(0.1)
                # print(files[i][y])

            elif int(files[i][y]) == 3:
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='red')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=files[i][y])
                #time.sleep(0.1)
                # print(files[i][y])

            elif int(files[i][y]) == 1:
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='yellow')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=files[i][y])
                #time.sleep(0.1)
                # print(files[i][y])
            else:
                cnv.create_rectangle(X1,Y1,X2,Y2, outline='black', fill='yellow')
                cnv.create_text((X1+panjang/2, Y1+panjang/2), text=files[i][y])
            X1=X1+panjang
            X2=X2+panjang

        Y1=Y1+panjang
        Y2=Y2+panjang
    cnv.create_text((X2+200, Y2/2), text='Pilih Titik Awal dan Akhir dengan Memasukan\nNilai Koordinat Pada Konsole atau Terminal. Contoh (x,y) : 9,8 ',)

def detector(y,x):
    ganti=0
    if files[y][x+1]=='1' or files[y][x+1]==3 or files[y+1][x]==1:
        ganti=ganti+1
        # ganti=files[y][x]
        # files[y][x]=int(ganti)+1
        # ganti=None
    
    if files[y+1][x]=='1' or files[y+1][x]==3 or files[y+1][x]==1:
        ganti=ganti+1

    if files[y][x-1]=='1' or files[y][x-1]==3 or files[y+1][x]==1:
        ganti=ganti+1

    if files[y-1][x]=='1' or files[y-1][x]==3 or files[y+1][x]==1:
        ganti=ganti+1
    
    files[y][x]=ganti
    
    return


print("\n File Testcase harus berisi hanya data array peta labirin (0 dan 1) saja \n")
# filenames=input("Masukan Nama File Testcase lengkap dengan ekstensi,contoh(d3.txt) : ")
filenames=input("masukan nama file dan ekstensinya : ")
print("\n")
files=dataReader(filenames)
window = tk.Tk()
window.title('pertemuan 10')
cnv = tk.Canvas(window, width=1000, height=600)
cnv.pack()
drawMap(files)
titik = input("Masukan Koordinat Titik Awal contoh  'x,y' : ")
x1 = int(titik.split(',')[0])
y1 = int(titik.split(',')[1])
titik = input("Masukan Koordinat Titik Akhir contoh  'x,y' : ")
x2 = int(titik.split(',')[0])
y2 = int(titik.split(',')[1])
if files[y1][x1]=='0':
    files[y1][x1]='a'
if files[y2][x2]=='0':
    files[y2][x2]='b'
test=30
while True:
    for y in range(len(files)):
        for x in range(len(files[y])):
            if x > 0 and y > 0 and x < len(files[y])-1 and y < len(files[y])-1:
                if files[y][x]=='0' or files[y][x]==2 or files[y][x]==1 or files[y][x]==4:
                    detector(y,x)
                
    if test==0:
        break
    test=test-1


    
drawMap(files)



window.mainloop()
