# Version 1, function getImportance() takes list of Employee object as parameters

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    empl_impt = 0

    # Search all subordinates and calculate the sum of importance value
    def calc_subord_impt(self, empls, id_lst, id_loc):
        self.empl_impt = self.empl_impt + empls[id_loc][1]
        if empls[id_loc][2]:
            for subord_id in empls[id_loc][2]:
                subord_id_loc = id_lst.index(subord_id)
                self.calc_subord_impt(empls, id_lst, subord_id_loc)

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        print(employees)
        empl_id_lst = [empl_info[0] for empl_info in employees]
        # Check if employee id exist and
        # find out its subordinate's id location
        if id in empl_id_lst:
            start_id_loc = empl_id_lst.index(id)
        else:
            print('Employee ID not found')
            return 0

        self.calc_subord_impt(employees, empl_id_lst, start_id_loc)
        print(self.empl_impt)
        return self.empl_impt

empl_A = Employee(1, 5, [2, 3])
empl_A_attr = [x[1] for x in vars(empl_A).items()]
empl_B = Employee(2, 3, [])
empl_B_attr = [x[1] for x in vars(empl_B).items()]
empl_C = Employee(3, 3, [])
empl_C_attr = [x[1] for x in vars(empl_C).items()]
solution = Solution()
solution.getImportance([empl_A_attr, empl_B_attr, empl_C_attr], 1)
