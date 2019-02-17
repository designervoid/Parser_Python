import json


def add_gender_to_message(message, authors):
    author_id = message['author']
    gender = authors.get(author_id)
    message['gender'] = gender


def get_authors_with_gender():
    authors_genders = {}
    file = open('path to file => public.jsonlines', 'r')
    for line in file:
        author = json.loads(line)
        author_id = author["author"]
        authors_genders[author_id] = author["gender"]
    file.close()
    return authors_genders


def main():
    authors = get_authors_with_gender()
    with open('path to file => messages.jsonlines', 'r') as file, \
            open('path to file => new_file.jsonlines', 'a+') as new_file:
        for line in file:
            message = json.loads(line)
            add_gender_to_message(message, authors)
            if message['gender']:
                print(message, file=new_file)


if __name__ == '__main__':
    main()
