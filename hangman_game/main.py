import random
import wordlist


def new_format(ch, real_word, hidden_format ) -> str:
   final_format = ''
   for index in range(len(real_word)):
      if real_word[index] == ch:
         final_format += f'{ch}'
      else:
         final_format += hidden_format[index]
         
      

   return final_format
         
        



lives = 6 # სისცოცხლის რაოდენობა


hidden_word = random.choice(wordlist.word_list) #ირჩევს გამოსაცნობ სიტყვას

guessed_chars = list()

print(hidden_word)
hidden = '*' * len(hidden_word)

while(True):
    print(hidden)
    print(f"გამოცნობილი ასოები: {guessed_chars}")
    guessed_char = input("შეიყვანეთ სავარაუდო ასე: ")

    if guessed_char in hidden_word:
        print("ყოჩაღ, სწორად გამოიცანი!")
        hidden = new_format(guessed_char, hidden_word, hidden)
        guessed_chars.append(guessed_char)

    elif(guessed_char not in hidden_word and lives != 1):
      lives -= 1
      print(f"ცადეთ ხელთავიდან,დარჩენილი გაქვთ {lives} ცდა")

    else:
      print(f"სამწუხაროდ, ცდა ამოგეწურათ")
      break

    if hidden_word == hidden:
       print("ყოჩაღ! შენ სწორად გამოიცანი სიტყვა!")
       break
       
    

