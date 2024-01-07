import Validator


def menu():
    print('to enter collection with file enter                  1')
    print('to search in collection enter                        2')
    print('to sort collection enter                             3')
    print('to delete element by ID enter                        4')
    print('to add freelancer enter                              5')
    print('to change freelancer enter                           6')
    print('to write into file enter                             7')
    print('to show collection enter                             8')
    print('to exit menu enter                                   0')
    switch = input('write your choice: ')
    return switch


def fill_collection_of_freelancers_with_file(collection_of_freelancers):
    file_path = Validator.Validator.get_file_name('enter name of file: ')
    collection_of_freelancers.fill_collection_of_freelancers_with_file(file_path)
    show_collection(collection_of_freelancers)


def search_in_collection_of_freelancers(collection_of_freelancers):
    data_to_search = input('enter sequence of letters you want to search: ')
    occurrences_of_freelancers = collection_of_freelancers.partial_overlapping_find(data_to_search)
    for element in occurrences_of_freelancers:
        print(f'{str(element)}')


def sort_collection_of_freelancers(collection_of_freelancers):
    print('your collection before the sorting is: ')
    print()
    for element in collection_of_freelancers:
        print(str(element))
    print()
    collection_of_freelancers.sort()
    print('your collection after the sorting is: ')
    print()
    for element in collection_of_freelancers:
        print(str(element))


# task 4
def delete_freelancer(collection_of_freelancers):
    # file_path = Validator.Validator.get_file_name('enter name of file: ')
    if collection_of_freelancers.is_empty():
        print('you cannot delete element from empty collection')
        return None
    collection_of_freelancers.delete_freelancer()
    print('delete successful')


def add_freelancer(collection_of_freelancers):
    # file_path = Validator.Validator.get_file_name('enter name of file: ')
    collection_of_freelancers.add_freelancer()
    print('appending successful')


def change_freelancer(collection_of_freelancers):
    if collection_of_freelancers.is_empty():
        print('you cannot change element from empty collection')
        return None
    # file_path = Validator.Validator.get_file_name('enter name of file: ')
    collection_of_freelancers.change_freelancer()
    print('changing successful')


def write_into_file(collection_of_freelancers):
    file_path = Validator.Validator.get_file_name('enter name of file: ')
    collection_of_freelancers.write_into_file(file_path)


def show_collection(collection_of_freelancers):
    for element in collection_of_freelancers:
        print(element)
