#python project template

##Below are few basic changes required to use this template to suit your needs

1)Update below details in setup.py
REPO_NAME = <REPO_NAME>
AUTHOR_USER_NAME = <AUTHOR_USER_NAME>
SRC_REPO = <SRC_REPO>
AUTHOR_EMAIL = <AUTHOR_EMAIL>

2)Create a package using create_package.py

3)Update package name within 
[options.package_data]
<package_name>=py.typed 

4)Update requirements in requirements_dev.txt and requirements.txt
5)Update user specific details in license file(year,username)
6)Update python version in init_setup.sh and run it in bash terminal to create conda python environment and install the requirements.