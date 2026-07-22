import json

#გლობალური ცვლადები
file = "translator/dictionary.json" #ჯეისონ ფიალი, რომელიც ინახავს ლექსიკოს

language_pairs = {
   "1" : ("Ge-En", "ქართული -> ინგლისური"),
   "2" : ("En-Ge", "ინგლისური -> ქართული" )
} #ჩვენი შესაძლო ენების წყვილი

#ხსნის ჩვენს ლექსიკონს
def load_dictionary():
    try:
        with open(file, 'r', encoding = "utf-8") as f: #ცდის რომ ეს ფაილი წაიკითხოს
            data = json.load(f)
        return data
    except FileNotFoundError: #თუ მითითებულ მისამართზე არ გვაქვს ფაილი
        #მაშინ ვქმნით ცარიელ სტრუქტურას
         return {
            "Ge-En": {},
            "En-Ge": {}
        } 
    

#ინახავს მონაცემებს ლექსიკონში
def save_dictionary(data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

#ვირჩევთ მონაცემთა წყვილს
def choose_language_pair():
    while True: # თუ მომხმარებელმა არასწორი ღილაკი აკრიფა, მაშინ აქვს საშუალება კიდევ ცადოს
        print("\n --- აირჩიეთ ენის წყვილი ---")
        
        for key, (code, label) in language_pairs.items(): #.items() (გასაღები, მონაცემი) წყვილებად ყოფს ჩვენს ლექსიკონს
            print(f"{key}. {label}")

        choice = input("შეიყვანეთ სასურველი მონაცემი: ").strip()
        
        # არჩევანის მიხდვით გვეუბნება რომელი წყვილია
        if choice in language_pairs:
            code, label = language_pairs[choice]
            return code
        else:
            print("არასწორი არჩევანი, ცადეთ ხელთავიდან!")


def translate_word(dictionary, language_pair):
   #სათარგმელი სიტყვა
   word = input("\n შეიყვანეთ სიტყვა ან ფრაზა: ").strip().lower()

   if not word:
       print("სიტყვა არ შეგიყვანიათ")
       return
   
   #ენების წყვილს იღებს და შესაბამისად ამ გასაღებით ეძებს სიტყვებს
   pair_dict = dictionary[language_pair]
   
   if word  in pair_dict:
       print(f"თაგმანი: {pair_dict[word]}") # თუ ეს სიტყვა გვაქვს ლექსიკონში
   else:
       answer = input("გსურთ დაამატოთ ამ სიტყვის თარგმანი ლექსიკონში? (დიახ/არა): ").strip().lower() # თუ არ გვაქვს
 
       if answer in ("დიახ", "yes", "y"):
            translation = input("შეიყვანეთ თარგმანი: ").strip().lower()
 
            if not translation:
                print("თარგმანი არ შეიყვანეთ, დამატება გაუქმდა.")
                return
 
            #ამატებს ჩაწერილ თარგმანს
            pair_dict[word] = translation
            #ჩამატება რომ ცალხმრივად არ მოხდეს, ამისთვის ჯერ ვაბრუნებთ ენერბის წყვილს
            reverse_pair = "En-Ge" if language_pair == "Ge-En" else "Ge-En"
            reverse_dict = dictionary[reverse_pair] 
            #ამოწმებს არის თუარა საპირისპიროდ თარგმნისა ეს სიტყვა ლექსიკონში
            if translation not in reverse_dict:
                reverse_dict[translation] = word

            save_dictionary(dictionary) # ინახავს ამ მონაცემებს
            print("სიტყვა წარმატებით დაემატა ლექსიკონს.")
       else:
            print("დამატება გაუქმდა.")


#კონსოლის ინტერაქციულობაზეა პასუხისმგებელი
def run_translator():
     dictionary = load_dictionary()

     while True:
         print("\n==== თარჯიმანი ====")
         print("1. სიტყვის თარგმნა")
         print("2. გასვლა")

         choice = input("აირჩიერთ პუნქტი (1-2): ").strip()

         if choice == '1':
             language_pair = choose_language_pair()
             translate_word(dictionary,language_pair)

         elif choice == '2':
             print("პროგრამა დასრულებლია, მადლობა!")
             break
         else:
             print("გთხოვთ, ცადეთ ხელთავიდან!") 

if  __name__ == "__main__":
          run_translator() #როდესაც ფაილს გავუშვებთ, პირველი ეს ბრძანება გაეშვება.

