import os


def thumbnail_filename_url_creator(filename: str, fileurl: str) -> tuple:
    '''
        This function takes two arguments:
        - filename: a string representing the name of the file
        - fileurl: a string representing the URL of the file

        The function returns a tuple containing two modified strings:
        - modified filename with "-resize" appended before the extension
        - modified fileurl with "-resize" appended before the extension
    '''
    # Split the filename and file extension
    name, extension = os.path.splitext(filename)

    # Append "-resize" to the filename and fileurl before the extension
    modified_name = f"{name}-resized{extension}"
    modified_url = f"{os.path.splitext(fileurl)[0]}-resized{extension}"

    # Return the modified filename and fileurl as a tuple
    return modified_name, modified_url
