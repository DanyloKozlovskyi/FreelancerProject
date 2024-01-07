import FREELANCER
import Validator


class FreelancerCollection:
    def __init__(self):
        # clear
        self.IDs = []
        self.freelancers = []

    def append(self, freelancer: FREELANCER.Freelancer):
        try:
            self.IDs.append(freelancer.ID)
            self.freelancers.append(freelancer)
            return True
        except:
            return False

    # probably work
    def __iter__(self):
        return iter(self.freelancers)

    def find(self, freelancer_to_search: FREELANCER.Freelancer):
        try:
            # clear
            self.IDs.index(freelancer_to_search.ID)
        except Exception as exc:
            return None
        return self.freelancers[self.IDs.index(freelancer_to_search.ID)]

    def find_ID(self, ID):
        try:
            self.IDs.index(ID)
        except Exception as exc:
            return -1
        return self.IDs.index(ID)

    def is_empty(self):
        return not bool(len(self.freelancers))

    def partial_overlapping_find(self, parameter):
        freelancers_found_lst = []
        # replaced something
        for element in self:
            if element.partial_overlapping_equal(parameter):
                freelancers_found_lst.append(element)
        return freelancers_found_lst

    @Validator.validateInputInClass('enter parameter: ', FREELANCER.Freelancer.validate_parameter)
    def sort(self, name=''):
        # validate fieldname
        # fieldname = FREELANCER.Freelancer.get_parameter('')
        self.freelancers.sort(key=lambda x: x.get_fieldname(name))
        self.IDs = [fr.ID for fr in self.freelancers]

    # delete by identificator
    def pop_by_ID(self, ID):
        if Validator.Validator.validate_ID(ID):
            if self.find_ID(ID) != -1:
                index = self.IDs.index(ID)
                self.IDs.pop(index)
                return self.freelancers.pop(index)
        return None

    # is this function used
    # clear?
    def write_in_file_by_ID(self, file, ID):
        try:
            with open(file, 'w') as f:
                if not self.pop_by_ID(ID) is None:
                    f.write(self.pop_by_ID(ID))
                    return True
        except Exception as exc:
            print(f'file {file} not found')
        return False

    def __setitem__(self, key, value):
        # throw exception
        if not Validator.Validator.validate_ID(key):
            return
        if not isinstance(value, FREELANCER.Freelancer):
            return
        if self.find_ID(key) != -1:
            self.freelancers[self.find_ID(key)] = value

    def __getitem__(self, key):
        if self.find_ID(key) != -1:
            return self.freelancers[self.find_ID(key)]
        return None

    def write_into_file(self, file_path):
        try:
            with open(file_path, 'w') as f:
                for element in self:
                    f.write(str(element))
                    f.write('\n')
                return True
        except Exception as exc:
            print(f'file {file_path} not found, {exc}')
        return False

    def delete_freelancer(self):
        ID = self.get_ID_of_existing_freelancer('enter ID of already existing freelancer(must contain 8 digits): ')
        self.pop_by_ID(ID)

    def add_freelancer(self):
        ID = self.get_ID_of_not_existing_freelancer('enter ID of not yet existing freelancer(must contain 8 digits): ')
        freelancer_to_add = FREELANCER.Freelancer.get_freelancer(ID)
        self.append(freelancer_to_add)
        # self.write_into_file(file_path)

    def get_ID_of_not_existing_freelancer(self, caption):
        while True:
            ID = Validator.Validator.get_ID(caption)
            if self.find_ID(ID) == -1:
                break
        return ID

    def get_ID_of_existing_freelancer(self, caption):
        ID = None
        while self.find_ID(ID) == -1:
            ID = Validator.Validator.get_ID(caption)
        return ID

    def change_freelancer(self):
        ID = self.get_ID_of_existing_freelancer('enter ID of already existing freelancer(must contain 8 digits): ')
        freelancer_to_add = FREELANCER.Freelancer.get_freelancer(ID)
        self[freelancer_to_add.ID] = freelancer_to_add
        # self.write_into_file(file_path)

    def fill_collection_of_freelancers_with_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                list_of_data = file.readlines()
                for line in list_of_data:
                    try:
                        errors = FREELANCER.Freelancer.validateFreelancer(*line.split())
                        freelancer = FREELANCER.Freelancer.string_to_freelancer(line)
                    except Exception as exc:
                        print('{')
                        for row in errors:
                            print(row, end=',\n')
                        print('},')
                        continue
                    self.append(freelancer)
        except Exception as exc:
            print(f'try again, {exc}')
