# midterm_project

Three small console applications written in Python for a midterm assignment:

| Project | Description |
| --- | --- |
| [`hangman_game`](hangman_game/) | Classic Hangman with ASCII-art gallows |
| [`student_portal`](student_portal/) | Student management system with JSON persistence |
| [`translator`](translator/) | Georgian ⇄ English dictionary that learns new words |

> The user interface (prompts, messages) and code comments are in Georgian.

## Requirements

- Python 3.9+
- No third-party packages; only the standard library (`random`, `json`, `os`)

## Running

Run every program **from the repository root**, because the translator and the student portal use paths relative to the current working directory:

```bash
git clone https://github.com/mberd7/midterm_project.git
cd midterm_project

python hangman_game/main.py
python student_portal/main.py
python translator/main.py
```

---

## Hangman (`hangman_game/`)

| File | Purpose |
| --- | --- |
| `main.py` | Game loop and helper functions |
| `wordlist.py` | `word_list`: about 850 English words to pick from |
| `graphics.py` | `stages`: ASCII drawings of the gallows, one for each number of lives left |

How it works:

- A random word is picked and shown masked as `*****`.
- The player has **6 lives**. A wrong guess costs one life and draws more of the hangman.
- Input is validated: it must be a single letter, and a letter that was already guessed is rejected without costing a life.
- Input is case-insensitive.
- The game ends when the word is fully revealed or the lives run out. If the player loses, the word is revealed.

Helper functions:

- `new_format(ch, real_word, hidden_format)` reveals every position of a correctly guessed letter
- `not_valid(guessed)` checks that the input is exactly one alphabetic character
- `already_guessed(guessed, guessed_ch)` checks whether the letter was already tried

---

## Student Portal (`student_portal/`)

A menu-driven CRUD application for managing students.

### Menu

```
1. Add a new student
2. Show all students
3. Search for a student by roll number
4. Update a student's grade
5. Delete a student
6. Exit
```

### Design

- **`Student`** has `name`, `roll_number` and `grade`, each validated through `@property` setters:
  - `name` must be non-empty and contain only letters; multi-word names are allowed
  - `roll_number` must be a positive integer
  - `grade` must be one of `A`, `B`, `C`, `D`, `E`, `F`
  - `to_dict()` and `from_dict()` handle JSON serialization, and `__str__` formats the student for display
- **`StudentManagementSystem`**
  - Loads `students.json` at startup and saves it after every change
  - Uses interactive input helpers (`get_valid_number`, `get_valid_name`, `get_valid_grade`) that re-prompt on bad input instead of crashing
  - Rejects duplicate roll numbers

### Data file

Students are stored in `students.json` in the current working directory, which is the repository root if you follow the instructions above:

```json
[
    { "name": "Nino", "roll_number": 1, "grade": "A" }
]
```

---

## Translator (`translator/`)

A small bilingual dictionary backed by `translator/dictionary.json`.

- Choose a direction: **Georgian → English** (`Ge-En`) or **English → Georgian** (`En-Ge`).
- Enter a word or phrase. If it is in the dictionary, the translation is printed.
- If it is not, you can add a translation. The program saves the new entry **in both directions**, so the reverse pair is added too unless it already exists.
- The dictionary ships with about 200 entries per direction.
- If `dictionary.json` is missing, the program starts with an empty dictionary and creates the file when the first word is saved.

Dictionary format:

```json
{
  "Ge-En": { "ამინდი": "weather" },
  "En-Ge": { "weather": "ამინდი" }
}
```
