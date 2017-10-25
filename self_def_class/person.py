class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "%s %s" %(self.first_name, self.last_name)

    def __len__(self):
        return 0

    def __iter__(self):
        return 0

    def __contains__(self):
        return False
