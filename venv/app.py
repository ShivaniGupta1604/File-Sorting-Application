from tkinter import *
from tkinter import ttk, filedialog,messagebox
import os, shutil

class sorting_app:

    def __init__(self, root):                           #=========constructor============
        self.root=root
        self.root.title("Sorting App")
        self.root.geometry('1550x1000+0+0')
        self.root.config(bg='white')
        self.logo_icon=PhotoImage(file='image/images.png')
        title=Label(self.root,borderwidth = 10, relief=RAISED,padx=10,image=self.logo_icon,compound =LEFT,text="File Sorting App",font=('Ink Free',50,'bold'),bg="#087587",fg="black").place(x=0.1,y=0,height=150,relwidth=0.99)

        #===================section1========================

        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text='Select folder',font=('times new roman',25),bg='white').place(x=50,y=180)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=('times new roman',18),bg='lightgray',state='readonly').place(x=265,y=170, height=50,width=550)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",bd=4,relief=RAISED,font=('times new roman',25,'bold'),bg='#262626',fg='white',cursor='hand2',activebackground='#262626',activeforeground='white').place(x=850,y=170,height=50)
        hr=Label(self.root,bg='lightgray').place(x=50,y=260,width=1430,height=3)

        #==================section2=========================

        self.image_extensions=["Image Extensions",".png",".jpg"]
        self.audio_extensions = ["Audio Extensions", ".amr", ".mp3"]
        self.video_extensions = ["Video Extensions", ".mp4", ".api",".mpeg4",".3gp"]
        self.doc_extensions = ["Documents Extensions", ".ppt", ".pptx",".xls",".pdf",".zip",".rar",".csv",".docx",".txt",".doc",".xlsx"]

        self.folders = {'videos': self.video_extensions,
                   'audios': self.audio_extensions,
                   'images': self.image_extensions,
                   'documents': self.doc_extensions
                   }


        lbl_support_ext = Label(self.root, text='Various Extensions Supported', font=('times new roman', 25), bg='white').place(x=50,y=280)

        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=('times new roman',20),state='readonly',justify=CENTER)
        self.image_box.place(x=100,y=330)
        self.image_box.current(0)

        self.audio_box = ttk.Combobox(self.root, values=self.audio_extensions, font=('times new roman', 20),state='readonly',justify=CENTER)
        self.audio_box.place(x=430, y=330)
        self.audio_box.current(0)

        self.video_box = ttk.Combobox(self.root, values=self.video_extensions, font=('times new roman', 20),state='readonly',justify=CENTER)
        self.video_box.place(x=760, y=330)
        self.video_box.current(0)

        self.doc_box = ttk.Combobox(self.root, values=self.doc_extensions, font=('times new roman', 20),state='readonly',justify=CENTER)
        self.doc_box.place(x=1100, y=330)
        self.doc_box.current(0)


        #=====================section3=================================

        self.image_icon = PhotoImage(file='image/im.png')
        self.audio_icon = PhotoImage(file='image/aud.png')
        self.video_icon = PhotoImage(file='image/vid.png')
        self.doc_icon = PhotoImage(file='image/doc.png')
        self.others_icon = PhotoImage(file='image/ot.png')

        Frame1=Frame(self.root,bd=6,relief=RIDGE,bg='lightgray')
        Frame1.place(x=50,y=400,width=1420,height=250)

        self.lbl_total_files = Label(Frame1, text='TOTAL FILES: ', font=('times new roman', 25),bg='lightgray')
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_images = Label(Frame1, text='',bd=4,relief=RAISED, image=self.image_icon ,compound=CENTER, font=('Arial BLACK', 18),bg='#087587',fg='black')
        self.lbl_total_images.place(x=20, y=50,width=250, height=180)

        self.lbl_total_audios = Label(Frame1,text='',bd=4,relief=RAISED,  image=self.audio_icon, compound=CENTER,font=('Arial BLACK', 18), bg='#087587',fg='black')
        self.lbl_total_audios.place(x=300, y=50, width=250, height=180)

        self.lbl_total_videos = Label(Frame1,text=' ',bd=4,relief=RAISED,  image=self.video_icon,compound=CENTER, font=('Arial BLACK', 18), bg='#087587',fg='black')
        self.lbl_total_videos.place(x=580, y=50, width=250, height=180)

        self.lbl_total_doc = Label(Frame1, text='',bd=4,relief=RAISED, image=self.doc_icon,compound=CENTER, font=('Arial BLACK', 18), bg='#087587',fg='black')
        self.lbl_total_doc.place(x=865, y=50, width=250, height=180)

        self.lbl_other_files = Label(Frame1,text='',bd=4,relief=RAISED,  image=self.others_icon, compound=CENTER,font=('Arial BLACK', 18), bg='#087587',fg='black')
        self.lbl_other_files.place(x=1140,y=50, width=250, height=180)

        # =====================section4=================================

        self.lbl_status = Label(self.root, text='STATUS : ', font=('times new roman', 28), bg='white')
        self.lbl_status.place(x=45, y=700)

        self.lbl_total = Label(self.root, text='', font=('times new roman', 20), bg='white')
        self.lbl_total.place(x=250, y=700)

        self.lbl_moved = Label(self.root, text='', font=('times new roman', 20), bg='white')
        self.lbl_moved.place(x=500, y=700)

        self.lbl_left = Label(self.root, text='', font=('times new roman', 20), bg='white')
        self.lbl_left.place(x=750, y=700)

        self.btn_clear = Button(self.root,command=self.clear, text="CLEAR",bd=4,relief=RAISED, font=('times new roman', 25, 'bold'), bg='#262626', fg='white',
                            cursor='hand2', activebackground='#262626', activeforeground='white')
        self.btn_clear.place(x=1000, y=690,height=50)

        self.btn_start = Button(self.root,state=DISABLED, command= self.start_function,text="START",bd=4,relief=RAISED, font=('times new roman', 25, 'bold'), bg='#262626', fg='white',
                            cursor='hand2', activebackground='#262626', activeforeground='white')
        self.btn_start.place(x=1250, y=690,height=50)


    def total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        combine_list=[]
        self.c=0

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i)) == True:
                self.c += 1
                ext = "." + i.split(".")[-1]
                for folder_name in self.folders.items():
                    for x in folder_name[1]:
                        combine_list.append(x)
                    #print(folder_name)
                    if ext.lower() in folder_name[1] and folder_name[0]=='images':
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=='audios':
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=='videos':
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=='documents':
                        documents+=1

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory, i)) == True:
                ext = "." + i.split(".")[-1]
                if ext.lower() not in combine_list:
                    others+=1

        self.lbl_total_images.config(text='TOTAL IMAGES: '+str(images))
        self.lbl_total_audios.config(text='TOTAL AUDIOS: ' + str(audios))
        self.lbl_total_videos.config(text='TOTAL VIDEOS: ' + str(videos))
        self.lbl_total_doc.config(text='TOTAL DOCS: ' + str(documents))
        self.lbl_other_files.config(text='OTHERS: ' + str(others))
        self.lbl_total_files.config(text='TOTAL FILES: '+str(self.c))


    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT self.folder FOR SORTING")
        if op!=NONE:
            self.var_foldername.set(str(op))
            self.directory = self.var_foldername.get()
            self.other_name = "Others"
            self.rename_folder()
            self.all_files = os.listdir(self.directory)  # This makes a list of all the files present on the given location.

            length = len(self.all_files)
            count = 1
            self.btn_start.config(state=NORMAL)
            self.total_count()



    def start_function(self):
        if self.var_foldername.get()!="":
            print('yes')
            self.btn_clear.config(state=DISABLED)
            count=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i)) == True:  # It returns true if the file present in the given location is a file and not a self.folder.
                    count += 1
                    self.create_move(i.split(".")[-1],i)  # we have used (os.path.join) so that we don't need to write it as (self.directory + "\\" + i)
                    self.lbl_total.config(text='TOTAL : '+str(self.c))
                    self.lbl_moved.config(text='MOVED : ' + str(count))
                    self.lbl_left.config(text='LEFT : ' + str(self.c-count))

                    self.lbl_total.update()
                    self.lbl_moved.update()
                    self.lbl_left.update()


            messagebox.showinfo('SUCCESS!'," All files have been sorted successfully .")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("ERROR!","Please select the required directory.")

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")

        self.lbl_total.config(text="")
        self.lbl_moved.config(text="")
        self.lbl_left.config(text="")

        self.lbl_total_images.config(text="")
        self.lbl_total_audios.config(text="")
        self.lbl_total_videos.config(text="")
        self.lbl_total_doc.config(text="")
        self.lbl_other_files.config(text="")
        self.lbl_total_files.config(text="Total files: ")


    def rename_folder(self):
        for self.folder in os.listdir(self.directory):
            if os.path.isdir(self.directory):
                if os.path.isdir(os.path.join(self.directory, self.folder)) == True:
                    os.rename(os.path.join(self.directory, self.folder), os.path.join(self.directory, self.folder.lower()))

    def create_move(self,ext, file_name):
        find = False
        for self.folder_name in self.folders:
            if "." + ext in self.folders[self.folder_name]:
                find = True
                if self.folder_name not in os.listdir(self.directory):  # It will make a new self.folders with req self.folder name for moving files
                    os.mkdir(os.path.join(self.directory, self.folder_name))
                shutil.move(os.path.join(self.directory, file_name), os.path.join(self.directory,
                                                                             self.folder_name))  # moving the self.folder from current files to requierd self.folder.
                break

        if find == False:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory, self.other_name))
            shutil.move(os.path.join(self.directory, file_name), os.path.join(self.directory, self.other_name))


root=Tk()
obj=sorting_app(root)
root.mainloop()
