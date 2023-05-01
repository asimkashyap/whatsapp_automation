import pyautogui as pg
import time
import emoji

# ..............................1 way.....................
# count = 1
# while count <= 5:
#     # pg.click(477, 692)
#     time.sleep(0.1)
#     pg.write('tum kya chahte ho')
#     time.sleep(0.1)
#     pg.press('enter')
#     time.sleep(0.1)
#     count += 1
# print(emoji.emojize(" :thumbs_up:"))
# print(emoji.demojize('😁😈'))


# ........................2nd way.....................................

time.sleep(1)
for i in range(10):
    time.sleep(0.1)
    pg.write('khna :-)')  # '^_^' .... ':-)'......':-D'
    time.sleep(0.1)
    pg.press('enter')
