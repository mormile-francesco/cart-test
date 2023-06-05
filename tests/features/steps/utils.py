import allure


def attach_file(path):
    try:
        file = open(path)
        allure.attach(file.read(), name=path, attachment_type=allure.attachment_type.TEXT)
    except:
        print("Can't attach the file!")