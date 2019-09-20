# Delete hidden files '.DS_Store' in Mac and 'Thumbs.db' in Windows.
# Need to add hidden file's name if other OS is being used

def del_hidden(file_list):
    # add hiddle file name in ['.DS_Store', 'Thumbs.db', 'HiddenFile']
    for file in ['.DS_Store','Thumbs.db']:
        try:
            file_list.remove(file)
        except ValueError:
            continue
    return file_list
