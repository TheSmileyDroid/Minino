import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH,SCREEN_HEIGHT,'Minino',False)


def handle_keys():
    global playerx, playery

    # movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1


#
#
#   Lógica
#
#
while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, int(playerx), int(playery), '@', libtcod.BKGND_NONE)
    libtcod.console_flush()
    key = libtcod.console_wait_for_keypress(True)
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        break  # exit game
