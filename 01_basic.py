import pyautogui as pg

def locate_click(icon:str, x_offset = 0, y_offset = 0):
    '''Function finds object from .png file 
    and simulates left mouse button click. 
    Additionally user is able to put offset in both axis.
    By default offset is set to zero.
    '''
    x, y = pg.locateCenterOnScreen(icon)
    pg.click(x + x_offset, y + y_offset)


# Run function 
locate_click(icon='icons/let.png')