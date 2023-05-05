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
        projects = []
        project_data = in_file.readlines()[1:]
        for data in project_data:
            data = data.strip().split("\t")
            projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))




main()