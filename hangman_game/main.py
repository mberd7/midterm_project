import random
import wordlist


def new_format(ch, real_word, hidden_format ) -> str:
   final_format = hidden_format
   i = -1
   for _ in real_word:
      i +=1
      if _ ==  ch:
         final_format[i] == ch

   return final_format
         
        



lives = 6 # სისცოცხლის რაოდენობა


hidden_word = random.choice(wordlist.word_list) #ირჩევს გამოსაცნობ სიტყვას

print(hidden_word)
hidden = '__ ' * len(hidden_word)

while(True):
    print(hidden)
    guessed_char = input("შეიყვანეთ სავარაუდო ასე: ")

    if guessed_char in hidden_word:
        print("ყოჩაღ, სწორად გამოიცანი!")
        hidden = new_format(guessed_char, hidden_word, hidden)
        
    elif(guessed_char not in hidden_word and lives != 1):
      lives -= 1
      print(f"ცადეთ ხელთავიდან,დარჩენილი გაქვთ {lives} ცდა")
    else:
      print(f"სამწუხაროდ, ცდა ამოგეწურათ")
      break
       
    

