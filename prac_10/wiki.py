import wikipedia

title = input("Search keyword: ")
while title != "":
    try:
        pagechoice = wikipedia.page(title)
        print(pagechoice.title)
        print(pagechoice.summary)
        print(pagechoice.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    title = input("Search keyword: ")
