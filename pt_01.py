import os

class Practice_01:
    def __init__(self):
        pass

    def myaverage(self, a, b):
        return (a+b)/2

    def get_max_min(self, default_list):
        return (max(default_list), min(default_list))

    def get_txt_list(self, path):
        return [a for a in os.listdir(path) if a.endswith('.txt')]

    def cal_BMI(self, weight, height):
        bmi = weight / (height*height)
        if bmi < 18.5:
            print('마른체형')
        elif bmi >= 18.5 and bmi < 25.0:
            print('표준')
        elif bmi >= 25.0 and bmi < 30.0:
            print('비만')
        else:
            print('고도비만')


if __name__ == "__main__":
    pt_01 = Practice_01()
    print(pt_01.myaverage(4, 6))

    print(pt_01.get_max_min([2,3,4,5,6,7,8]))

    print(pt_01.get_txt_list(os.getcwd()))

    pt_01.cal_BMI(68, 1.68)