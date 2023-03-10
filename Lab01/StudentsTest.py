import unittest
import Students
def Mex(ids):
    ret = 0

    for i in range(len(ids)):
        if ret in ids:
            ret = ret + 1
    return ret

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        #TODO
        print("Start set_name test")
        for i in range(len(self.user_name)):
            self.user_id.append(self.students.set_name(self.user_name[i]))
            print(self.user_id[i], self.user_name[i])
            for j in range(len(self.user_id)-1):
                self.assertNotEqual(self.user_id[i], self.user_id[j])
        print("\nFinish set_name test\n\n")


    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        #TODO
        print("Start get_name test\n")
        print("user_id length =", len(self.user_id))
        print("user_name length =", len(self.user_name), "\n")
        self.user_id.append(Mex(self.user_id))
        for i in range(len(self.user_name)+1):
            name = self.students.get_name(self.user_id[i])
            print("id", self.user_id[i], ":", name)
            if i<len(self.user_name):
                self.assertIs(name, self.user_name[self.user_id[i]])
            else:
                self.assertNotIn(name, self.students.name)
