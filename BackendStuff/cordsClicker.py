import cv2
import json

cords_lst = []


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        cords_lst.append((x, y))


# driver function
if __name__ == "__main__":
    # reading the image
    img = cv2.imread('screenshot.png', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()

print(cords_lst)
with open("colorRatings.json", "w") as f:
    json.dump(cords_lst, f)
