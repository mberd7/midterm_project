class Student: 
    
    #სტუდენტის პროგრამის ინიციალიზაცია ხდება
    def __init__(self, name,roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade


#სახელის გეთერი და სეთერი
    @property
    def name(self):
        return self._name

    #აუცილებელია რომ შემოწმდეს, სახელი ცარიელი არის თუარა და ასევე ასოებისგან
    #თუ შედგება
    @name.setter
    def name(self, name):  
         
        if not name or not str(name).strip():
            raise ValueError("აუცილებელია სახელის შეყვანა")
        
        if not all(word.isalpha() for word in name.strip().split()): #თუ სახელში რამდენიმე სიტყვა 
            #შედის მაშინ მათ ანაწევრებს და ისე ამოწმებს
            raise ValueError("სახელში აუცილებლად უნდა იყოს ასოები.")

        self._name = name.strip()


#რიგის ნომრის, სეთერი და გეთერი
    @property
    def roll_number(self):
        return self._roll_number
    
    
    @roll_number.setter
    def roll_number(self, roll_number):
        if not roll_number or not str(roll_number).strip():
            raise ValueError("აუცილებელია, სიის ნომრის შეყვანა")
        
        if not roll_number.strip().isdigit():
            raise ValueError("ნომერში უნდა შედიოდეს მხოლოდ რიცხვები, გამოტოვებების გარეშე!")
        
        self._roll_number = roll_number


#შეფასების გეთერი და სეთერი
    @property
    def grade(self):
        return self._grade
    
#შეფასება აუცილებლად უნდა იყოს "A", "B", "C", "D", "E" ან "F"
    @grade.setter
    def grade(self,grade):
        if grade not in {"A", "B", "C", "D", "E", "F"}:
            raise ValueError("შეფასება არ არის ვალიდური")
        self._grade = grade

#როდესაც ობიექტის მონაცემების დაბეჭვდა გვენდომება, ამ სახით დაიბეჭდება    
    def __str__(self):
        return f"სახელი: {self._name} | სიის ნომერი: {self._roll_number} | შეფასება: {self._grade}"


class StudentManagementSystem:

    def __init__(self):
        self.students = []  #იქმნება სია, რომელშიც სტუდენტების მონაცემები შეინახება
   
   #
   #მომდევნო სამი ფუნქციით მოწმდება შესული მონაცემების ვალიდაცია, რეალურად ზუსტად იგივე რამეს აკეთებს
   #რასაც სეთერი, თუმცა ასეთი ფორმატით პროგრამა უფრო ინტერაქციულია, რადგან შეცდომის შემთხვევაში პროგრამა
   #არ წყვეტს მუშაობას, არამედ მომხმარებელს აძლევს საშუალეას რომ ხელთავიდან ცადოს
   #
    def get_valid_number(self):
        while True:
            roll_number = input("სიის ნომერი: ").strip()
            try:
                if not roll_number or not roll_number.isdigit():
                    raise ValueError("ნომერი უნდა შედგებოდეს მხოლოდ რიცხვებით.")
                return roll_number
            except ValueError as error:
                print("შეცდომა:", error,  "- ცადე ხელთავიდან.")


    def get_valid_name(self):
        while True:
            name = input("სახელი: ").strip()
            try:
                if not name or not all(word.isalpha() for word in name.split()):
                    raise ValueError("სახელში აუცილებად უნდა იყოს ასოები.")
                return name
            except ValueError as error:
                print("შეცდომა:", error,  "- ცადე ხელთავიდან.")


    def get_valid_grade(self):
        while True:
            grade = input("შეიყვანეთ ნიშანი: ").strip()
            try:
                 if grade not in {"A", "B", "C", "D", "E", "F"}:
                  raise ValueError("შეფასება არ არის ვალიდური")
                 return grade
            except ValueError as error:
                 print("შეცდომა:", error,  "- ცადე ხელთავიდან.")


#ეს ფუქნცია პასუხისმგებელია, რომ დაამატოს სტუდენტი
    def add_new_student(self):
         roll_number = self.get_valid_number()
        #აუცილებელია შეამოწმოს არსებობს თუარა ეს სტუდენტი სიაში, თუ არსებობს, მაშინ არ უნდა დაემატოს სტუდენტი
        #სისტემასი
         if self.find_student(roll_number):
             print("ამ სიის ნომრით სტუდენტი უკვე არსებობს")
             return
         name =self.get_valid_name()
         grade = self.get_valid_grade()
         #იქმნება ობიექტი ამ მონაცემებით
         student = Student(name, roll_number, grade)
         self.students.append(student) #ინახება სიაში

    #ეს ფუნქცია პასუხისმგებელია, რომ ყველა სტუდენტი აჩვენოს
    def show_all_students(self):
        print("\n--- სტუდენტების სია ---")
        if not self.students:
            print("სისტემაში სტუდენტები არ არიან დამატებულები")
            return

        for i, student in enumerate(self.students, start = 1): #იტირებად ობიექტს(სტუდენტთა სიას) გადაყვება და გვიბეჭდავს
            print(f"{i}. {student}")

        
   #პასუხისმგებელია, რომ იპოვოს სტუდენტი ნომრის მიხედვით
    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None
    


    def search_student(self):
        print("\n ---სტუდენტის ძებნა ნომრის მიხედვით ---")

    #იღებს შესაბმის რიცხვსა და მის მიხედვით ეძებს სტუდენტს    
        roll_number = self.get_valid_number()
        student = self.find_student(roll_number)

        if student: #ამოწმებს მსგავსი სტუდენტი არსებობს თუარა
            print("სტუდენტი მოიძებნა: ")
            print(student)
        else:
            print("სტუდენტი მითითებული ნომრით არ მოიძებნება.")

   #შლის სტუდენტს სიიდან, მისი ნომრის მიხედვით
    def delete_student(self):
        print("\n ---სტუდენტის წაშლა ნომრის მიხედვით ---")
        
        roll_number = self.get_valid_number()
        student = self.find_student(roll_number)

        if student:
            self.students.remove(student)
            print("სტუდენტის მონაცემები წაიშალა სისტემიდან.")

        else:
            print("სტუდენტი მითითებული ნომრით არ მოიძებნება.")


#ცვლისს ტუდენტის ნიშანს.
    def change_grade(self):
        print("\n --- მოსწავლის შეფასების განახლება ---")
        roll_number = self.get_valid_number()
        student = self.find_student(roll_number)

        if not student:
            print("ასეთი სტუდენტი არ არსებობს")
            return
        
        new_grade = self.get_valid_grade()
        student.grade = new_grade


#კონსოლის ინტერაქციულობაზეა პასუხისმგებელი
    def run_the_system(self):
     while True:
           print("\n ==== სტუდენტის მართვის სისტემბა ====")
           print("1. ახალი სტუდენტის დამატება")
           print("2. ყველა სტუდენტის ნახვა")
           print("3. მოძებნეთ სტუდენტი ნომრით")
           print("4. განაახლეთ მოსწავლის შეფასება")
           print("5. სტუდენტის მონაცემების სისტემიდან წაშლა")
           print("6. სისტემიდან გამოსვლა")

           choice = input("აირჩიეთ პუნქტი (1-6): ").strip()

           if choice == "1":
              self.add_new_student()
           elif choice == "2":
               self.show_all_students()
           elif choice == "3":
               self.search_student()
           elif choice == "4":
               self.change_grade()
           elif choice == "5":
               self.delete_student()
           elif choice == "6":
               print("პროგრამა დასრულებულია, მადლობა!")
               break
           else:
            print("გთხოვთ აირჩიოთ 1-დან 6-მდე.")



       



if __name__ == "__main__":
    system = StudentManagementSystem() # პირველი ეს ბრძანება გაეშვება
    system.run_the_system()
    
