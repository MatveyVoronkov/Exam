class Grandparent:
    def about(self):
        print('I am Grandparent')

    def about_myself(self):
        print('About myself Grandparent')

class Parent(Grandparent):
    def about(self):
        print('I am Parent')
