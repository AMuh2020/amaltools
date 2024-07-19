# Made obsolete
def format_txt(file_path):
    #opens file (tools.txt)
    with open(file_path) as tools:
        #every line of the file is a list element
        lines = tools.readlines()

    #
    group = []
    for i in range(0,int(len(lines)),5):
        #removes trailing newline from the tool_name line
        tool_name = lines[i].replace("\n","").capitalize()
        #url
        url = lines[i+1].replace("\n","")
        #removes trailing newline from the description line
        description = lines[i+2].replace("\n","").capitalize()
        #removes dash
        description = description.replace("-","")
        #removes tags from line contianing tags
        tags = lines[i+3].replace("tags: ","")
        #removes trailing newline from tags
        tags = tags.replace("\n","")
        #splits tags into a list
        tags = tags.split(", ")
        #sorts the tags list, priorities caps first
        tags.sort()
        #appends tool with its name and respective tags together depreceated
        #using dicts
        group.append({'name':tool_name,'url':url,'description':description,'tags':tags})
    #returns list of tool names, description and tags depreceted
    # using dicts
    return group

