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
        projects = store_data(project_data)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            try:
                filename = input("Filename: ")
                with open(f"{filename}.txt", "r", newline='') as in_file:
                    new_data = in_file.readlines()[1:]
                    projects = store_data(new_data)
                print("Load complete")
            except FileNotFoundError:
                print("File is not found")
        elif choice == "s":
            filename = input("Filename: ")
            with open(f"{filename}.txt", "w") as out_file:
                print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
                for project in projects:
                    print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}"
                          f"\t{project.completion_percentage}", file=out_file)
                print("Save complete")
        elif choice == "d":
            projects.sort()
            print("Incomplete Projects:")
            for project in projects:
                if not project.is_completed():
                    print(" ", project)
            print("Complete Projects:")
            for project in projects:
                if project.is_completed():
                    print(" ", project)

        print(MENU)
        choice = input(">>> ").lower()
def store_data(project_data):
    projects = []
    for data in project_data:
        data = data.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return projects


main()