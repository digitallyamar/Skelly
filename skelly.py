import sys, ast
import time
import cssutils
from bs4 import BeautifulSoup

def responsive():
    cmd_responsive_dialog_header = "Generating responsive HTML5 boilerplate code..."

    with open('templates/responsive.html', 'r') as ftemp:
        html5_responsive_code = ftemp.read()
        print (cmd_responsive_dialog_header + '\n')

    output_file = 'Skelly_' + time.strftime("%Y%m%d_%H%M%S") + '.html'

    with open(output_file, 'w') as fout:
        fout.write(html5_responsive_code)
        print ("Output File: " + output_file)
        fout.close()

def add_title(input_file, title):
    try:
        with open(input_file, 'r+') as fin:
            content = fin.read()
            soup = BeautifulSoup(content, "html5lib")
            print ("Adding title: " + title)
            soup.title.string = title
            fin.seek(0)
            fin.write(str(soup))
            fin.truncate()
    except:
        print ("Error adding title")


def set_body_font_size(input_file, size):
    try:
        with open(input_file, 'r+') as fin:
            content = fin.read()
            soup = BeautifulSoup(content, "html5lib")

            # Link new style.css file if not already linked
            if (soup.head.link['href'] == ""):
                soup.head.link['href'] = "style.css"
            fin.seek(0)
            fin.write(str(soup))
            fin.truncate()

            try:
                sheet = cssutils.parseFile("style.css")
            except:
                print ("Error: style.css file does not exist")
                return

            for rule in sheet:
                print (rule)
                if rule.type == rule.STYLE_RULE and rule.selectorText == 'body':
                    rule.style.setProperty('font-size', size)

            #Finally, write back new CSS rules to the stylesheet
            try:
                with open('style.css', 'wb+') as fout:
                    fout.write(sheet.cssText)
            except:
                print ("Error opening/writing to style.css file")
    except:
        print("Unexpected error:", sys.exc_info()[0])



def set_body_color(input_file, color):
    try:
        with open(input_file, 'r+') as fin:
            content = fin.read()
            soup = BeautifulSoup(content, "html5lib")

            # Link new style.css file if not already linked
            if (soup.head.link['href'] == ""):
                soup.head.link['href'] = "style.css"
            fin.seek(0)
            fin.write(str(soup))
            fin.truncate()

            try:
                sheet = cssutils.parseFile("style.css")
            except:
                print ("Error: style.css file does not exist")
                return

            for rule in sheet:
                print (rule)
                if rule.type == rule.STYLE_RULE and rule.selectorText == 'body':
                    rule.style.setProperty('color', color)

            #Finally, write back new CSS rules to the stylesheet
            try:
                with open('style.css', 'wb+') as fout:
                    fout.write(sheet.cssText)
            except:
                print ("Error opening/writing to style.css file")
    except:
        print("Unexpected error:", sys.exc_info()[0])


def set_body_bg_color(input_file, color):
    try:
        with open(input_file, 'r+') as fin:
            content = fin.read()
            soup = BeautifulSoup(content, "html5lib")
            # Link new style.css file if not already linked
            if (soup.head.link['href'] == ""):
                soup.head.link['href'] = "style.css"
            fin.seek(0)
            fin.write(str(soup))
            fin.truncate()

            try:
                sheet = cssutils.parseFile("style.css")
            except:
                print ("Error: style.css file does not exist")
                return

            for rule in sheet:
                print (rule)
                if rule.type == rule.STYLE_RULE and rule.selectorText == 'body':
                    rule.style.setProperty('background-color', color)

            #Finally, write back new CSS rules to the stylesheet
            try:
                with open('style.css', 'wb+') as fout:
                    fout.write(sheet.cssText)
            except:
                print ("Error opening/writing to style.css file")
    except:
        print("Unexpected error:", sys.exc_info()[0])


def add_menu_item(input_file, items):
    with open(input_file, 'r+') as fin:
        content = fin.read()
        soup = BeautifulSoup(content, "html5lib")

        if (soup.body.nav.ul == None):
            print('No Menu detected, bailing out')
            return

        cur_items = []
        #Append existing li elements from an existing ul
        #for ul in soup.body.nav.ul:
        #    cur_items.append(ul)

        itemList = ast.literal_eval(items)

        #Append new items to the cur_items list
        for item in itemList:
            cur_items.append(item)

        print (cur_items)

        #Finally update new ul list
        index = 0
        for item in cur_items:
            li = soup.new_tag('li')
            li.append(item)
            soup.body.nav.ul.insert(index, li)
            index = index + 1

        fin.seek(0)
        fin.write(str(soup))
        fin.truncate()


def create_main_menu(input_file):
    with open(input_file, 'r+') as fin:
        content = fin.read()
        soup = BeautifulSoup(content, "html5lib")

        #Create nav element
        if (soup.body.nav == None):
            print ('Adding nav element..')
            nav = soup.new_tag('nav')
            soup.body.insert(0, nav)
        
        else:
            print ("Nav element already exists!")
        
        #Add ul if nav does not contain it yet
        if (soup.body.nav.ul == None):
            print ('Adding ul element..')
            ul = soup.new_tag('ul')
            soup.body.nav.insert(0, ul)

        else:
            print("ul element already exists! Bailing out..")

        fin.seek(0)
        fin.write(str(soup))
        fin.truncate()



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ('Usage: python skelly.py <cmd>')
        print ('Type python skelly.py --help for list of commands')
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == "--help" or cmd == "--h":
        cmd_help_dialog_header = "Here is the list of Skelly commands:"
        print (cmd_help_dialog_header)
        print ("-" * len(cmd_help_dialog_header) + '\n')
        print ("responsive - Generates responsive HTML5 boilerplate code")
        print ("add_title <htmlFileName> <title> - Adds title to the HTML document")
        print ("set_body_color <htmlFileName> <color> - Set new text color for the body tag")        
        print ("set_body_bg_color <htmlFileName> <color> - Set new background color for the body tag")
        print ("set_body_font_size <htmlFileName> <size> - Set new font size for the body tag")
        print ("create_main_menu <htmlFileName> - Creates main nav menu with an empty ul tag")
        print ("add_menu_item <htmlFileName> <itemsList> - Adds new item(s) in main menu")
    
    elif cmd == "responsive":
        responsive()
    
    elif cmd == "add_title":
        if (len(sys.argv) < 4):
            print ("Usage: python skelly.py add_title <htmlFileName> <title>")
            sys.exit(0)
        
        add_title(sys.argv[2], sys.argv[3])
    
    elif cmd == "set_body_bg_color":
        if (len(sys.argv) < 4):
            print ("Usage: python skelly.py set_body_bg_color <htmlFileName> <color>")
            sys.exit(0)

        set_body_bg_color(sys.argv[2], sys.argv[3])
        
    elif cmd == "set_body_color":
        if (len(sys.argv) < 4):
            print ("Usage: python skelly.py set_body_color <htmlFileName> <color>")
            sys.exit(0)

        set_body_color(sys.argv[2], sys.argv[3])
    
    elif cmd == "set_body_font_size":
        if (len(sys.argv) < 4):
            print ("Usage: python skelly.py set_body_color <htmlFileName> <color>")
            sys.exit(0)

        set_body_font_size(sys.argv[2], sys.argv[3])

    elif cmd == "create_main_menu":
        if (len(sys.argv) < 3):
            print ("Usage: python skelly.py create_main_menu <htmlFileName>")
            sys.exit(0)

        create_main_menu(sys.argv[2])
    
    elif cmd == "add_menu_item":
        if (len(sys.argv) < 4):
            print ("Usage: python skelly.py add_menu_item <htmlFileName> [itemsList]")
            sys.exit(0)

        add_menu_item(sys.argv[2], sys.argv[3])