from PIL import ImageGrab
import win32gui
import time

def get_screen():
	hwnd = win32gui.FindWindow(None, r'Tetris')
	#win32gui.SetForegroundWindow(hwnd)
	win32gui.MoveWindow(hwnd, 0, 0, 500, 700, True)
	dimensions = win32gui.GetWindowRect(hwnd)
	#dimensions = (0, 0, 614, 876)

	image = ImageGrab.grab(dimensions)
	return image

img = get_screen()
img.show()