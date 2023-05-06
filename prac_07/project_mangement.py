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
    filename = "projects"
    with open(f"{filename}.txt", "r", newline='') as in_file:
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
            save_data(filename, projects)
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
            date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects(date, projects)
            sort_filtered_projects(filtered_projects)
            for project in filtered_projects:
                print(project)
        elif choice == "a":
            name = get_valid_name()
            start_date = get_valid_start_date()
            priority = get_valid_priority()
            cost_estimate = get_valid_estimate()
            completion_percentage = get_valid_percentage()
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
        elif choice == "u":
            for index in range(len(projects)):
                project = projects[index]
                print(f"{index} {project}")
            project_choice = get_valid_project_choice(projects)
            chosen_project = projects[project_choice]
            print(chosen_project)
            new_percentage = get_valid_new_number()
            if new_percentage is not None:
                chosen_project.completion_percentage = new_percentage
            new_priority = get_valid_new_number()
            if new_priority is not None:
                chosen_project.priority = new_priority
        print(MENU)
        choice = input(">>> ").lower()
        save_data(filename, projects)
        print("Thank you for using custom-built project management software")


def save_data(filename, projects):
    with open(f"{filename}.txt", "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}", file=out_file)


def get_valid_new_number():
    is_valid = False
    while not is_valid:
        new_number_string = input("New percentage: ")
        if new_number_string != "":
            try:
                new_number = int(new_number_string)
                if new_number < 0 or new_number > 100:
                    print("Invalid number")
                else:
                    is_valid = True
                    return new_number
            except ValueError:
                print("Invalid value, integer needed")
        else:
            is_valid = True


def get_valid_project_choice(projects):
    project_choice = get_valid_integer("Project choice: ")
    while project_choice < 0 or project_choice > (len(projects) - 1):
        print("Invalid project choice")
        project_choice = get_valid_integer("Project choice: ")
    return project_choice


def get_valid_estimate():
    cost_estimate = get_valid_float_value()
    while cost_estimate < 0:
        print("Invalid input, must be more than $0")
        cost_estimate = float(get_valid_integer("Cost estimate: $"))
    return cost_estimate


def get_valid_float_value():
    is_valid = False
    while not is_valid:
        try:
            decimal = float(input("Cost estimate: $"))
            is_valid = True
            return decimal
        except ValueError:
            print("Invalid input, numbers only")


def get_valid_percentage():
    completion_percentage = get_valid_integer("Completion percentage: ")
    while completion_percentage < 0 or completion_percentage > 100:
        print("Invalid percentage, between 0% and 100%")
        completion_percentage = get_valid_percentage()
    return completion_percentage


def get_valid_priority():
    priority = get_valid_integer("Priority: ")
    while priority <= 0:
        print("Invalid input, must be higher than 0")
        priority = get_valid_integer("Priority: ")
    return priority


def get_valid_integer(prompt):
    is_valid = False
    while not is_valid:
        try:
            number = int(input(prompt))
            is_valid = True
            return number
        except ValueError:
            print("Invalid input, integer only")


def get_valid_start_date():
    date = get_valid_date("Start date: ")
    start_date = f"{date.strftime('%d%m%Y')}"
    return start_date


def get_valid_name():
    name = input("Project name: ").title()
    while name == "":
        print("Input can not be blank")
        name = input("Project name: ").title()
    return name


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


def get_valid_date(prompt):
    is_valid = False
    while not is_valid:
        try:
            date_string = input(prompt)
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid = True
            return date
        except ValueError:
            print("Invalid date, it should be a valid date in dd/mm/yyyy format")


def store_data(project_data):
    projects = []
    for data in project_data:
        data = data.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return projects


main()
