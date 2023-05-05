from project import Project

MENU = """- (L)oad Projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    with open("projects.txt", "r", newline='') as in_file:
        project_data = in_file.readlines()[1:]
        store_data(project_data)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            try:
                filename = input("Filename (with .txt): ")
                with open(filename, "r", newline='') as in_file:
                    new_data = in_file.readlines()[1:]
                    store_data(new_data)
                print("Load complete")
            except FileNotFoundError:
                print("File is not found")
        print(MENU)
        choice = input(">>> ").lower()
def store_data(project_data):
    projects = []
    for data in project_data:
        data = data.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))


main()