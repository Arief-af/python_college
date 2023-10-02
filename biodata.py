import uuid

data = []
toggleStore = 'yes'
toggleIndex = 'yes'
toggleSearch = 'yes'

def store():
    print('--------------------------------------------------------------')
    print('                   Welcome To Biodata App                     ')
    print('--------------------------------------------------------------')
    idBiodata = str(uuid.uuid1())
    data.append({
        'id': idBiodata,
        'name': input('Please write your name: '),
        'kelas': input('Please write your class: '),
        'status': input('Please write your status: '),
        'age': input('Please write your age: '),
        'hobbies': input('Please write your hobbies separated by commas: ').split(',')
    })
    print(f"data with id {idBiodata} has been created")
    print('--------------------------------------------------------------')

def index():
    global data
    print('--------------------------------------------------------------')
    print('                        Biodata List                           ')
    for item in data:
        print('--------------------------------------------------------------')
        print(F'ID    : {item["id"]}')
        print(F'Name  : {item["name"]}')
        print(F'Class : {item["kelas"]}')
        print(F'Status: {item["status"]}')
        print(F'Age   : {item["age"]}')
        print(F'Hobbies: {", ".join(item["hobbies"])}')
    print('--------------------------------------------------------------')

def search(id_to_search):
    global data
    for item in data:
        if item['id'] == id_to_search:
            print('--------------------------------------------------------------')
            print('                       Biodata Details                        ')
            print('--------------------------------------------------------------')
            print(F'ID    : {item["id"]}')
            print(F'Name  : {item["name"]}')
            print(F'Class : {item["kelas"]}')
            print(F'Status: {item["status"]}')
            print(F'Age   : {item["age"]}')
            print(F'Hobbies: {", ".join(item["hobbies"])}')
            print('--------------------------------------------------------------')
            return
    print(f'No biodata found with ID {id_to_search}')

def show_married():
    global data
    print('--------------------------------------------------------------')
    print('                  Biodata with Status: Married                 ')
    print('--------------------------------------------------------------')
    for item in data:
        if item['status'].lower() == 'married':
            print('--------------------------------------------------------------')
            print(F'ID    : {item["id"]}')
            print(F'Name  : {item["name"]}')
            print(F'Class : {item["kelas"]}')
            print(F'Status: {item["status"]}')
            print(F'Age   : {item["age"]}')
            print(F'Hobbies: {", ".join(item["hobbies"])}')
    print('--------------------------------------------------------------')

while toggleStore == 'yes':
    store()
    toggleStore = input('Do you want to input data again? (yes/no): ')

while toggleIndex == 'yes':
    index()
    toggleIndex = input('Do you want to view data again? (yes/no): ')

while toggleSearch == 'yes':
    search_id = input('Enter the ID to search for: ')
    search(search_id)
    toggleSearch = input('Do you want to search again? (yes/no): ')

show_married()