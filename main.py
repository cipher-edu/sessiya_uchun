import json
def save_question(question, answer):
    with open('question_database.json', 'a') as file:
        data = {'question': question, 'answer': answer}
        json.dump(data, file)
        file.write('\n')

def load_database():
    try:
        with open('question_database.json', 'r') as file:
            lines = file.readlines()
            database = [json.loads(line) for line in lines]
            return database
    except FileNotFoundError:
        return []

def get_user_input():
    user_input = input("Savolingiz yoki ma'lumotingizni kiriting: ")
    return user_input

def ask_question(user_input, database):
    for entry in database:
        if entry['question'] == user_input:
            return entry['answer']
    return None

def main():
    # database = load_database()

    while True:
        database = load_database()
        user_input = get_user_input()
        answer = ask_question(user_input, database)

        if answer:
            print(answer)
        else:
            new_answer = input("Menda javob yo'q. Iltimos, savolga to'g'ri aniq javob bering: ")
            save_question(user_input, new_answer)
            print("Yashasin savol va javob muvaffaqiyatli saqlandi! Endi davom etamiz")

        continue_prompt = input("Sizda boshqa savol yoki ma'lumot bormi? (y/n): ")

        if continue_prompt.lower() == 'n':
            continue

if __name__ == '__main__':
    main()
