#OOPR-Assgn-13
#Start writing your code here
class Classroom:
    classroom_list=None
#     def __init__(self):
#         None
    "__int__ is empty so need not to declare it & \
    classsroom_list is Static Variable \
    still the Code Quality check fails don't know why"
    @staticmethod
    def search_classroom(class_room):
        for room in Classroom.classroom_list:
            if class_room.lower() == room.lower():
                return 'Found'
        return -1