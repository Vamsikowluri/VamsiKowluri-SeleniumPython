# import pytest
#
#
# @pytest.mark.usefixtures("dataLoad")
# class TestExample2:
#
#     def test_editProfile(self,dataLoad):
#         print(dataLoad[2])
#

a=6
b=4.816
c= -3
str1 = '{0:.4f} {0:-3d} {2} {1}'.format(a, b, c)
print(str1)