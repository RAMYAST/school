import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
def login():
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()

    if role == "Student":
        file_name = "student_data.txt"
    else:
        file_name = "teacher_data.txt"

    with open(file_name, "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

    messagebox.showinfo("Login Successful", "Data saved successfully!")


class NextWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        label = tk.Label(self, text="GREEN PARK",font=("Courier", 20, "bold"),bg="#37FD12")
        label.pack(pady=10, padx=10)
        nav_frame = tk.Frame(self)
        nav_frame.pack(fill="x")
        about_button = ttk.Button(nav_frame, text="ABOUT",
                                      command=lambda: self.show_content("ABOUT"))
        join_button = ttk.Button(nav_frame, text="ENQUIRY",
                                   command=lambda: self.show_content("ENQUIRY"))
        packages_button = ttk.Button(nav_frame, text="EXTRA-CURRICULAR ACTIVITIES",
                                    command=lambda: self.show_content("ACTIVITY"))
        contact_button = ttk.Button(nav_frame, text="CONTACT US",
                                    command=lambda: self.show_content("CONTACT"))
        rules_button = ttk.Button(nav_frame, text="ACADEMIC SUCCESS",
                                    command=lambda: self.show_content("ACADEMIC"))

        
        about_button.pack(side="left")
        join_button.pack(side="left")
        packages_button.pack(side="left")
        contact_button.pack(side="left")
        rules_button.pack(side="left")
        
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill="both", expand=True)


    def show_content(self, content_type):
        for child in self.content_frame.winfo_children():
            child.destroy()
        
        if content_type == "ABOUT":
            content_frame = AboutContent(self.content_frame)
        elif content_type == "ENQUIRY":
            content_frame = JoinContent(self.content_frame)
        elif content_type == "ACTIVITY":
            content_frame = PackagesContent(self.content_frame)
        elif content_type == "CONTACT":
            content_frame = ContactContent(self.content_frame)
        elif content_type == "ACADEMIC":
            content_frame = RulesContent(self.content_frame)
        content_frame.pack(pady=10)


class AboutContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text_area = tk.Text(self, wrap=tk.WORD,font=("Courier",11),bg="yellow")
        self.text_area.pack(fill=tk.BOTH, expand=True)
        paragraph = """"SUCCESS IS NOT ABOUT THE APPLAUSE,BUT THE SATISFACTION OF KNOWING YOU'VE GIVEN YOUR BEST"


Welcome to Green Park Institutions, an esteemed educational hub that has been dedicated to providing exceptional learning experiences since its establishment in 1990. With a rich history of success and a commitment to nurturing young minds, we take pride in being a cornerstone of quality education.


Our Legacy of Excellence:
    For over three decades, Green Park Institutions have stood as a beacon of educational excellence. Our institution has evolved and adapted to the changing landscape of education, always striving to stay at the forefront of innovation while maintaining our core values.


Well-Equipped Staff:
    At the heart of our success is our dedicated and well-equipped staff. Our educators are not only experts in their respective fields but also passionate mentors who are deeply committed to shaping the future of our students. Their guidance and mentorship go beyond textbooks, fostering holistic development.


Enriching Ambience:
    Step onto our campus and experience an environment designed to promote learning, creativity, and personal growth. Our lush green surroundings and thoughtfully designed infrastructure create a conducive atmosphere where students can thrive academically, socially, and emotionally.


A Friendly Community:
    We take pride in the warm and welcoming community that makes up Green Park Institutions. Students, teachers, parents, and administrators come together to create a supportive network that encourages collaboration and mutual respect. Our emphasis on inclusivity and open communication sets the stage for lifelong friendships and positive learning experiences.


Progressive Approach:
    While rooted in tradition, we embrace a progressive approach to education. Our curriculum is designed to equip students with the skills, knowledge, and mindset needed to excel in an ever-changing world. We foster critical thinking, creativity, and adaptability, preparing our students to face challenges with confidence.


Continued Dedication:
    With a legacy spanning over thirty years, our dedication to serving the community and providing quality education remains unwavering. We continue to evolve, incorporating the latest pedagogical methods and technologies to ensure our students receive the best possible education.


Our institutions are run by a unique team of Directors who are elite and efficient in their respective subjects and working as full time teachers. We have plenty of talented and service-minded staff offering round the clock assistance to the curricular, co-curricular and non-curricular needs of the students. Our Institutions focus on the outcome of our students with flying colours in the Public Examinations along with personality development. With intensive care and individual-based attention, we make the students join reputable Medical and Engineering colleges.


At Green Park Institutions, we are not just an educational institution; we are a family that believes in the potential of each individual. Our journey since 1990 has been marked by success, growth, and a commitment to fostering excellence. As we look towards the future, we remain dedicated to nurturing the leaders, thinkers, and change-makers of tomorrow.


    """
        self.text_area.insert("1.0", paragraph)


class JoinContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=1, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Location:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Courses:").grid(row=4, column=0, padx=10, pady=5)
        self.membership_var = tk.StringVar(value="SELECT")   
        membership_choices = ["MAT-BIO", "MAT-CSC", "ARTS","PURE SCIENCE","COMMERCE/ACCOUNTANCY"]
        self.membership_dropdown = tk.OptionMenu(self,self.membership_var,*membership_choices)
        self.membership_dropdown.grid(row=4, column=1, padx=10, pady=5)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=6, columnspan=2, pady=10)

    def submit_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        membership = self.membership_var.get()
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Address:", address)
        print("Membership:", membership)


        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

       


class PackagesContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="""WHAT ARE EXTRACURRICULAR ACTIVITIES?

Extracurricular activities are programs outside of the regular school curriculum. They focus on a specific activity, goal, or purpose.

EXTRACURRICULAR ACTIVITIES FOR STUDENTS

Extracurricular activities help students show off their interests and personalities. These activities also demonstrate their ability to contribute, stick to their commitments, and manage their time and priorities. These include things like:

Athletics
Student Government
Community Service
Employment
Arts
Hobbies
Educational and Academic Clubs
Social activities

Extracurricular activities serve as an extension of the academic curriculum.""",font=("Courier",11),bg="yellow")
        label.pack()


class ContactContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text=" Green Park International Sr. Sec. School \n Tiruchengode(Po),\n Namakkal– Dt TamilNadu - 600000\n\n Phone:00000 - 11111,9999999999.\n E-Mail: greenparkschoolnkl@gmail.com \n \n follow on : \n \tFacebook : Green Tech Education \n Instagram : Green_tech\n\n",font=("Courier",11) )
        label.pack()

        image = Image.open("location.jpg")  
        image = image.resize((750,500))
        photo = ImageTk.PhotoImage(image)
        
        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack()


class RulesContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="ACHIEVEMENTS",font=("Courier", 20, "bold"))
        label.pack(pady=10, padx=10)
        nav_frame = tk.Frame(self)
        nav_frame.pack(fill="x")
        ab_button = ttk.Button(nav_frame, text="2022 NEET ACHIEVEMENTS",command=lambda: self.show_content("2022"))
        jo_button = ttk.Button(nav_frame, text="2021 NEET ACHIEVEMENTS",command=lambda: self.show_content("2021"))
        cd_button = ttk.Button(nav_frame, text="2020 NEET ACHIEVEMENTS",command=lambda: self.show_content("2020"))
        ef_button = ttk.Button(nav_frame, text="2019 NEET ACHIEVEMENTS",command=lambda: self.show_content("2019"))

        
        ab_button.pack(side="left")
        jo_button.pack(side="left")
        cd_button.pack(side="left")
        ef_button.pack(side="left")
        
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill="both", expand=True)

    def show_content(self, content_type):
        for child in self.content_frame.winfo_children():
            child.destroy()
        
        if content_type == "2022":
            content_frame = Abcontent(self.content_frame)
        elif content_type == "2021":
            content_frame = Jocontent(self.content_frame)
        elif content_type == "2020":
            content_frame = Cdcontent(self.content_frame)
        elif content_type == "2019":
            content_frame = Efcontent(self.content_frame)
        content_frame.pack(pady=10)

class Abcontent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="No.Of Students Joined MBBS In 2022: 296 \n Government College:211 \nPrivate College (Government Quota) : 85 ",font=("Courier",15))
        label.pack()

class Jocontent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text=" No.Of Students Joined MBBS In 2021:274 \n Government College:200\nPrivate College (Government Quota) : 74 ",font=("Courier",15))
        label.pack()

class Cdcontent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text=" No.Of Students Joined MBBS In 2020:250 \n Government College:205\nPrivate College (Government Quota) : 72 ",font=("Courier",15))
        label.pack()

class Efcontent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text=" No.Of Students Joined MBBS In 2019:190 \n Government College:190\nPrivate College (Government Quota) : 65",font=("Courier",15))
        label.pack()
        

    
def show_login_dialog():
    
    login_dialog = tk.Toplevel(root)
    login_dialog.title("LOGIN PAGE")

    paragraph_heading = "GREEN PARK "
    heading_message = tk.Message(login_dialog, text=paragraph_heading, font=("Courier", 22),bg="#37FD12")
    heading_message.pack(pady=50,padx=30)
    login_frame = tk.Frame(login_dialog, padx=10, pady=20)
    login_frame.pack()

    login_box = tk.LabelFrame(login_frame, text="Login", padx=20, pady=20)
    login_box.pack(padx=10, pady=10)

    
    username_label = tk.Label(login_dialog,text="Username:")
    
    username_label.pack()
    username_entry = tk.Entry(login_dialog)
    username_entry.pack()

    # Password Label and Entry
    password_label = tk.Label(login_dialog, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_dialog, show="*")
    password_entry.pack()

    # Role Radiobuttons
    role_var = tk.StringVar()
    role_var.set("Student")
    student_radio = tk.Radiobutton(login_dialog, text="Student", variable=role_var, value="Student")
    teacher_radio = tk.Radiobutton(login_dialog, text="Teacher", variable=role_var, value="Teacher")
    student_radio.pack()
    teacher_radio.pack()

    # Login Button
    login_button = tk.Button(login_dialog, text="Login", command=login)
    login_button.pack()

    login_button = tk.Button(login_dialog, text="next", command=NextWindow)
    login_button.pack()
    

root = tk.Tk()
root.title("GPInstitution")

bg_image = Image.open("j3.jpg")  # Replace with your image file
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

show_login_button = tk.Button(root, text="GREEN PARK GROUP OF INSTITUTIONS \n login here !!",font=("Courier",20),bg="#37FD12", command=show_login_dialog)
show_login_button.pack(pady=50,padx=10)

root.mainloop()
