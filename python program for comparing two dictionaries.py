from deepdiff import DeepDiff

Python_package_1 = {'matplot': 1.7, 'numpy':3.4 , 'caret':2.0,'textlive':4.0}
Python_package_2 = {'matplot': 1.7, 'numpy':3.6 , 'caret':2.2,'textlive':4.1}

diff = DeepDiff(Python_package_1, Python_package_2)
print(diff)
if Python_package_1 == Python_package_2:
    print("package is same in the version")
else:
    print("package is differ in the version")
