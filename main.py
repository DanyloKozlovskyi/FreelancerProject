# Клас FREELANCER з полями: ID, name, email, phone_number,
# availability (hrs/week), salary,
# position (BE Developer / FE Developer / DevOps).
import FREELANCER
import FreelancerCollection
import interface


def main():
    check = str()
    collection_of_freelancers = FreelancerCollection.FreelancerCollection()
    while check != '+' and check != '-':
        check = input('if you want to enter(continue) the program press +, if you want exit press -: ')
        while check == '+':
            switch = interface.menu()
            match switch:
                case '1':
                    interface.fill_collection_of_freelancers_with_file(collection_of_freelancers)
                case '2':
                    interface.search_in_collection_of_freelancers(collection_of_freelancers)
                case '3':
                    interface.sort_collection_of_freelancers(collection_of_freelancers)
                case '4':
                    interface.delete_freelancer(collection_of_freelancers)
                case '5':
                    interface.add_freelancer(collection_of_freelancers)
                case '6':
                    interface.change_freelancer(collection_of_freelancers)
                case '7':
                    interface.write_into_file(collection_of_freelancers)
                case '8':
                    interface.show_collection(collection_of_freelancers)
                case '0':
                    check = ''
                case _:
                    print('try again')


if __name__ == '__main__':
    main()
