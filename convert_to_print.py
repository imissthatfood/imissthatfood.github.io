import glob

def main():

    for filename in glob.glob('_recipes/*'):
        with open(filename, 'r') as f:
            text = f.readlines()
            new_text = "".join(line for line in text if '<'  not in line)
            assert "layout: recipe" in new_text
            new_text = new_text.replace("layout: recipe", "layout: print")
            with open(filename.replace('_recipes', '_print'), 'w') as g:
                g.write(new_text)

if __name__ == "__main__":
    main()

