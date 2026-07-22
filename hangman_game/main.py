import random
import wordlist #არის პითონის ფაილი სიტვების სიით, რომლიდანაც ვირჩევთ  გამოსაცნობ სიტყვას
import graphics

#ასოს სწორად გამოცნობისას, დაშიფრულ ფორმატს ცვლის, რასაც მომხმარებელს ვაჩვენებთ
def new_format(ch, real_word, hidden_format ) -> str:
   final_format = ''

   for index in range(len(real_word)):
      if real_word[index] == ch:
         final_format += f'{ch}'
      else:
         final_format += hidden_format[index]
         
   return final_format

#ამოწმებს რამდენად არის ვალიდური ფორმატი
def not_valid(guessed: str):
   return   len(guessed) != 1 or not guessed.isalpha()  

#ამოწმებს იყო თუარა ეს ასო გამოცნობილი
def already_guessed(guessed: str, guessed_ch: list):
   return guessed  in guessed_ch
        


def main():
 lives = 6 # სისცოცხლის რაოდენობა
 hidden_word = random.choice(wordlist.word_list).lower() #ირჩევს გამოსაცნობ სიტყვას
 #გადაგვყავს პატარა ასოებში, რომ შეცდომა არ გამოიწვიოს

 guessed_chars = list() # ამ სიაში შეინახება გამოცნობილი ასოები
 hidden = '*' * len(hidden_word) #ქმნის დაშიფრულ ფორმატს

 while(True):
    print("\n" + "=" * 20)
    print(f"გამოსაცნობი სიტყვა: {hidden}")
    print(f"გამოყენებული ასოები: {', '.join(guessed_chars)}")

    
    
    guessed_char = input("შეიყვანეთ სავარაუდო ასო: ").lower() #პატარა ასოებზე გადაგვყავს შეცდომის
    #ასარიდებლად
    #პირველ რიგში, ამოწმებს რამდენად ვალიდური ფორმატია, ასევე იყო თუარა გამოცნობილი
    if(not_valid(guessed_char)): 
       print("არასწორი ფორმატით შეიყვანეთ, გთხოვთ ცადეთ ხელთავიდან:")
    elif(already_guessed(guessed_char, guessed_chars)):
       print("ეს ასო უკვე შეყვანილი გაქვთ, გთხოვთ ცადეთ ხელთავიდან")
    else: # თუ ორივეს გაივლის მაშინ უკვე იწყება გადამოწმება რამდენად სწორია
       print(graphics.stages[lives])  
       print(hidden)

       if guessed_char in hidden_word: # თუ სწორია, ცვლის დაშიფრული სიტყვის ფორმატს
        print("ყოჩაღ, სწორად გამოიცანი!")
        hidden = new_format(guessed_char, hidden_word, hidden)
        guessed_chars.append(guessed_char) #ამატებს გამოცნობილ ასოებში

       elif(guessed_char not in hidden_word and lives != 1): #თუ ცდების რაოდენობა დარჩა, მაშინ უბრალოდ ეუბნება რომ არასწორია
         lives -= 1
         guessed_chars.append(guessed_char)
         print(f"ცადეთ ხელთავიდან,დარჩენილი გაქვთ {lives} ცდა")

       else:
        print(f"სამწუხაროდ, ცდა ამოგეწურათ") # თუ ცდების რაოდენობა დამთავრდა, თამაში სრულებდა.
        print(graphics.stages[0])
        break

       if hidden_word == hidden: #თუ სწორად გამოიცნობს მაშინ დაშიფრული ფორმატი ბუნებრივია გაუტოლდება  გამოსაცნობს
         print(f"ყოჩაღ! შენ სწორად გამოიცანი სიტყვა:{hidden_word}")
         break

       
    
if __name__ == "__main__":
    main()
