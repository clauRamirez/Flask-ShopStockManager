import os

def get_title(path: str) -> str:
    '''@path: __file__
    
    returns first bit of current filename capitalized in order
    to extract title that is passed down to the templates.
    '''
    file = os.path.basename(os.path.realpath(path))
    title = file.split("_")[0].title()
    return title
