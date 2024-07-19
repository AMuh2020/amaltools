from bs4 import BeautifulSoup
import copy 

html = """
<html>
BS4 test
<style>
    h1 {
        color: red;
    }
    .button {
        color: blue;
    }
    .yellow_button {
        color: yellow;
    }
    h2 {
        color: green;
    }
    #h2 {
        color: green;
    }
    #headerid {
        color: green;
    }
</style>
<body>
    <h1>Header 1</h1>
    <h2 id="h2">Header 2</h2>
    <div class="button">Button</div>
    <div class="yellow_button button">Yellow Button</div>
    <div id="headerid">Header ID</div>
</html>

"""
def css_to_inline(html):
    soup = BeautifulSoup(html, 'html.parser')

    # get all style tags
    style_tags = soup.find_all('style')
    print(style_tags)

    # two methods
    # grab all classes from style tags
    # or iterate over all tags and grab classes

    # get all classes from style tags
    selectors = {'elements':[], 'classes':[], 'ids':[]}
    for i in range(len(style_tags)):
        style = str(style_tags[i])
        for j in range(len(style)):
            character = style[j]
            if character == '.':
                # print("yes", character, style[j+1])
                class_name = ''
                props = ''
                k=j+1
                while style[k] != '{':
                    class_name += style[k]
                    k+=1
                class_name = class_name[:-1]
                while style[k] != '}':
                    k+=1
                    props += style[k]
                
                # remove last character
                props = props[:-1]
                properties = props.strip().split(';')
                selectors['classes'].append([class_name,properties[:-1]])
            elif character == '#':
                id_name = ''
                props = ''
                k=j+1
                while style[k] != '{':
                    id_name += style[k]
                    k+=1
                id_name = id_name[:-1]
                while style[k] != '}':
                    k+=1
                    props += style[k]
                
                # remove last character
                props = props[:-1]
                properties = props.strip().split(';')
                selectors['ids'].append([id_name,properties[:-1]])

                

    # get tags with certain class
    new_html = html
    selector_types = ['classes', 'ids']
    for selector_type in selector_types:
        print(selector_type)
        for i in range(len(selectors[selector_type])):
            soup = BeautifulSoup(new_html, 'html.parser')
            selector_name = selectors[selector_type][i][0]
            if selector_type == 'classes':
                tags = soup.find_all(class_=selector_name)
            elif selector_type == 'ids':
                tags = soup.find_all(id=selector_name)

            # deep copy of tags to avoid changing original
            tags_copy = copy.deepcopy(tags)
            for j in range(len(tags)):
                # check if style exists
                try:
                    print(tags_copy[j]['style'])
                # if not, create it
                except:
                    tags_copy[j]['style'] = ''

                # add styling to tag
                tags_copy[j]['style'] += f"{'; '.join(selectors[selector_type][i][1])}; "
                print(tags_copy[j]['style'])
            
            # replace tags with new tags
            for k in range(len(tags)):
                print("replacing", tags[k], "with", tags_copy[k])
                new_html = new_html.replace(str(tags[k]), str(tags_copy[k]))

    # return new html
    return new_html