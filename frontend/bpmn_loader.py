import markdown2

def import_mmd_file(file_path):
    try:
        # Open the .mmd file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse Markdown content using markdown2
        parsed_content = markdown2.markdown(content)
        
        return str(parsed_content)
    except FileNotFoundError:
        print("Error: File not found!")
        return None
#model_shoes = import_mmd_file("../testing/shoes_example/shoes_GM.mmd")     
    
  