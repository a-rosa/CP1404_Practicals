from project import Project
import datetime

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
        elif choice == "f":
            date = get_valid_date()
            filtered_projects = filter_projects(date, projects)
            sort_filtered_projects(filtered_projects)
            for project in filtered_projects:
                print(project)

        print(MENU)
        choice = input(">>> ").lower()


def sort_filtered_projects(filtered_projects):
    for first_pointer in range(len(filtered_projects)):
        for second_pointer in range(len(filtered_projects)):
            comparison_date = datetime.datetime.strptime(filtered_projects[second_pointer].start_date,
                                                         "%d/%m/%Y").date()
            base_date = datetime.datetime.strptime(filtered_projects[first_pointer].start_date, "%d/%m/%Y").date()
            if comparison_date > base_date:
                temporary_storage = filtered_projects[second_pointer]
                filtered_projects[second_pointer] = filtered_projects[first_pointer]
                filtered_projects[first_pointer] = temporary_storage


def filter_projects(date, projects):
    filtered_projects = []
    for project in projects:
        project_start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_start_date >= date:
            filtered_projects.append(project)
    return filtered_projects

def get_valid_date():
    is_valid = False
    while not is_valid:
        try:
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid = True
        except ValueError:
            print("Must input in the dd/mm/yyyy format")
    return date


def store_data(project_data):
    projects = []
    for data in project_data:
        data = data.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return projects


main()