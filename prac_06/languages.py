"""
Intermediate Exercise
Language file

estimate and actual in Programming Language file
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Test printing object
print(python)
print(ruby)
print(visual_basic)

languages = [python, ruby, visual_basic]

# Test printing is_dynamic
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
