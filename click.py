import cv2
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
def click_event(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print (x,",",y)
	elif event == cv2.EVENT_RBUTTONDOWN:
		print (x,",",y)
click_event