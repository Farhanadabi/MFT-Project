from tkinter import *
import os
import json
def root():
    global ws
    ws = Tk()
    ws.title('MFT Project')
    ws.geometry('960x540')
    ws.config(bg='#12181E')
    widgets()
def widgets():
    global lbl
    global login_btn
    global reg_btn
    global del_btn
    global exit_btn
    lbl=Label(ws,text='Login Or Register',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    lbl.pack()
    Label(text="",bg='#12181E').pack()
    Label(text="",bg='#12181E').pack()
    Label(text="",bg='#12181E').pack()
    
    #buttons
    login_btn=Button(ws,text='Login',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_login)
    login_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    reg_btn=Button(ws,text='Register',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_register)
    reg_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    del_btn=Button(ws,text='Delete Account',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_delete_account)
    del_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    exit_btn=Button(ws,text='Exit',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=ws.destroy)
    exit_btn.pack()
    ws.mainloop()
def destroy_to_login():
    try:
        for i in ws.winfo_children():
            i.forget()
        login_page()
    except:
        pass
def destroy_to_main():
    try:
        for i in ws.winfo_children():
            i.forget()
        widgets()
    except:
        pass
def destroy_to_register():
    try:
        for i in ws.winfo_children():
            i.forget()
        register_page()
    except:
        pass
def destroy_to_delete_account():
    try:
        for i in ws.winfo_children():
            i.forget()
        delete_account_page()
    except:
        pass

def login_page():
    #globalize
    global lgn_ent
    global lgn_pw_ent
    global lgn_msg
    #labels
    lgn_top=Label(ws,text='Login Page',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    lgn_top.pack()
    
    lgn_user_lbl=Label(ws,text='Username:',font=("default",15),fg='green',bg='#12181E')
    lgn_user_lbl.pack()
    #Entry
    
    lgn_ent=Entry(ws,width=21,font=("default",19))
    lgn_ent.pack()
    
    lgn_password_lbl=Label(ws,text='Password:',font=("default",15),fg='green',bg='#12181E')
    lgn_password_lbl.pack()
    
    
    lgn_pw_ent=Entry(ws,width=21,font=("default",19),show='*')
    lgn_pw_ent.pack()
    
    Label(text="",bg='#12181E').pack()
    #buttons
    lgn_btn=Button(ws,text='Login',height="2",font=('',11,'bold'), width="30",fg='white',bg='#51E79D',command=verify_login)
    lgn_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    bck_btn=Button(ws,text='back',height="2",font=('default',9,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_main)
    bck_btn.pack()
    
    lgn_msg=Label(ws,text='',fg='red',bg='#12181E')
    lgn_msg.pack()
def register_page():
    #globalize
    global reg_ent
    global reg_pw_ent
    global reg_msg
    #labels
    reg_st=Label(ws,text='Register Page',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    reg_st.pack()
    
    reg_username_lbl=Label(ws,text='Username:',font=("default",15),fg='green',bg='#12181E')
    reg_username_lbl.pack()
    #Entry
    
    reg_ent=Entry(ws,width=21,font=("default",19))
    reg_ent.pack()
    
    reg_password_lbl=Label(ws,text='Password:',font=("default",15),fg='green',bg='#12181E')
    reg_password_lbl.pack()
    
    
    reg_pw_ent=Entry(ws,width=21,font=("default",19),show='*')
    reg_pw_ent.pack()
    
    Label(text="",bg='#12181E').pack()
    #buttons
    reg_btn=Button(ws,text='Register',height="2",font=('',11,'bold'), width="30",fg='white',bg='#51E79D',command=register_user)
    reg_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    bck_btn=Button(ws,text='back',height="2",font=('default',9,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_main)
    bck_btn.pack()
    
    reg_msg=Label(ws,text='',fg='red',bg='#12181E')
    reg_msg.pack()
def delete_account_page():
    #globalize
    global del_ent
    global del_pw_ent
    global del_msg
    #labels
    del_st=Label(ws,text='Delete Account Page',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    del_st.pack()
    
    del_username_lbl=Label(ws,text='Username:',font=("default",15),fg='green',bg='#12181E')
    del_username_lbl.pack()
    #Entry
    
    del_ent=Entry(ws,width=21,font=("default",19))
    del_ent.pack()
    
    del_password_lbl=Label(ws,text='Password:',font=("default",15),fg='green',bg='#12181E')
    del_password_lbl.pack()
    
    
    del_pw_ent=Entry(ws,width=21,font=("default",19),show='*')
    del_pw_ent.pack()
    
    Label(text="",bg='#12181E').pack()
    #buttons
    del_btn=Button(ws,text='Delete Account',height="2",font=('',11,'bold'), width="30",fg='white',bg='#51E79D',command=check)
    del_btn.pack()
    
    
    Label(text="",bg='#12181E').pack()
    
    bck_btn=Button(ws,text='back',height="2",font=('default',9,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_main)
    bck_btn.pack()
    
    del_msg=Label(ws,text='',fg='red',bg='#12181E')
    del_msg.pack()

def verify_login():
    global login_yes_btn
    global error_login_screen
    try:
        u=lgn_ent.get()
        p=lgn_pw_ent.get()
        with open('users.json') as j:
            s=json.load(j)
        if u in s:
            if s[u]==p:
                lgn_msg.configure(text='Welcome',fg='green')
            else:
                lgn_msg.configure(text='Wrong Username Or Password!',fg='red')
        else:
            lgn_msg.configure(text='Wrong Username Or Password!',fg='red')
    except FileNotFoundError:
        json_error_box()

def register_user():
    try:
        u=reg_ent.get()
        p=reg_pw_ent.get()
        with open('users.json') as j:
            s=json.load(j)
        if u not in s:
            s[u]=p
            with open('users.json','w') as j:
                json.dump(s,j)
            reg_msg.configure(text='Registered',fg='green')
        else:
            reg_msg.configure(text='Username Already Exist',fg='red')
    except FileNotFoundError:
        json_error_box()
def delete_user():
    confirm_box.destroy()
    try:
        u=del_ent.get()
        p=del_pw_ent.get()
        with open('users.json') as j:
            s=json.load(j)
        if u in s:
            if s[u]==p:
                s.pop(u)
                with open('users.json','w') as j:
                    json.dump(s,j)
                del_msg.configure(text='Account Deleted Successfully',fg='green')
            else:
                del_msg.configure(text='Wrong Username Or Password!',fg='red')
        else:
            del_msg.configure(text='Wrong Username Or Password!',fg='red')
    except FileNotFoundError:
        json_error_box()
def json_error_box():
    global error_box
    #error box
    error_box = Toplevel()
    error_box.config(bg='#808080')
    error_box.geometry("300x105")
    error_box.title("File Not Find!")
        
    # json msg
    Label(error_box,text='Users.json Not Find! Do You Want To Create One?',fg='cyan',bg='#808080').pack()
        
        
        
    #yes and no buttons
    yes_btn=Button(error_box,text='Yes',width=7,command=Create_json,bg='#6495ED')
    yes_btn.place(x=150,y=74)
        
    no_btn=Button(error_box,text='No',width=7,command=error_box.destroy,bg='#6495ED',)
    no_btn.place(x=90,y=74)
def Create_json():
    try:
        dct={'farhan':'b1390'}
        with open('users.json','w') as j:
            json.dump(dct,j)
        error_box.destroy()
    except:
        pass
def confirm():
    global confirm_box
    #error box
    confirm_box = Toplevel()
    confirm_box.config(bg='#000000')
    confirm_box.geometry("300x105")
    confirm_box.title("Confirmation!")
        
    # json msg
    Label(confirm_box,text='your account will be deleted permanently Are You Sure?',fg='red',bg='#000000').pack()
        
        
        
    #yes and no buttons
    yes_btn=Button(confirm_box,text='Yes',width=7,command=delete_user,bg='#6495ED')
    yes_btn.place(x=150,y=74)
        
    no_btn=Button(confirm_box,text='No',width=7,command=confirm_box.destroy,bg='#6495ED',)
    no_btn.place(x=90,y=74)
def check():
    with open('users.json') as j:
        s=json.load(j)
    
    if del_ent.get() in s:
        return confirm()
    
    else:
        del_msg.configure(text='Wrong Username Or Password!',fg='red')

root()