import arcade, random

PLAYER_PLACE_x = 100
PLAYER_PLACE_y = 420
SCREEN_WIDTH = 1280
SCREEN_HIGHT = 720

PLAYER_ATTACK = 35

ACTION = 0
ENEMY_HP = 100
ANIMATION = 0
MOB_COUNT = 3
MOB_NO = 0
ENEMY_SPEED = 5

ENEMY_ACTION = 0

BUTTON_VALUE = 1

CAN_CHANGE = 1
CANT_CHANGE = 0

CAN_ATTACK = 0
CANT_ATTACK = 1


RIGHT_FACING = 1
LEFT_FACING = 0

UPDATES_PER_FRAME = 7

SCREEN = 0

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]

class PlayerCharacter(arcade.Sprite):

    def __init__ (self) :

        super().__init__(self)

        self.character_face_direction = RIGHT_FACING

        self.scale = 0.15

        self.cur_texture = 0

        self.cur_attack = 0

        self.HP = 200

        main_path = "image/CHIBI KNIGHT-PNG/"

        self.idle_texture_pair = load_texture_pair(f"{main_path}01-Idle_/2D_KNIGHT__Idle_000.png")

        self.walk_texture = []
        for i in range (8) :
            texture = load_texture_pair(f"{main_path}02-Run_/2D_KNIGHT__Run_00{i}.png")
            self.walk_texture.append(texture)

        self.attack_texture = []
        for i in range (8) :
            texture = load_texture_pair(f"{main_path}03-Attack_/2D_KNIGHT__Attack_00{i}.png")
            self.attack_texture.append(texture)



    def update_animation(self, delta_time: float = 1/60):

        global ACTION
        global ENEMY_HP

        if ACTION == 2 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif ACTION == 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if ACTION == 0 or ACTION == 5:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            ACTION = 0
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        if ACTION == 3 :
            self.cur_attack += 1
            self.texture = self.attack_texture[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]
            if self.cur_attack > 7 * UPDATES_PER_FRAME :
                self.cur_attack = 0
                ACTION = 4
            else :
                return
        self.texture = self.walk_texture[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]


class GOBLIN (arcade.Sprite) :
    def __init__(self):
        super().__init__(self)
        self.HP = ENEMY_HP + 20

        self.ATTACK = 30

        self.scale = 0.15

        self.cur_texture = 0

        self.cur_attack = 0

        main_path = "image/2D CHIBI GOBLIN/"

        self.idle_texture_pair = load_texture_pair(f"{main_path}CHIBI GOBLIN-PNG/01-Idle_/01-NoBlink/2D_GOBLIN__Idle_000.png")

        self.character_face_direction = LEFT_FACING

        self.texture = self.idle_texture_pair[self.character_face_direction]

        self.walk_texture = []
        for i in range (8) :
            texture = load_texture_pair(f"{main_path}CHIBI GOBLIN-PNG/02-Run_/2D_GOBLIN__Run_00{i}.png")
            self.walk_texture.append(texture)

        self.attack_texture = []
        for i in range (8) :
            texture = load_texture_pair(f"{main_path}CHIBI GOBLIN-PNG/03-Attack_/2D_GOBLIN__Attack_00{i}.png")
            self.attack_texture.append(texture)

    def update_animation(self, delta_time: float = 1/60):

        global ENEMY_ACTION

        if ENEMY_ACTION == 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif ENEMY_ACTION == 2 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if ENEMY_ACTION == 0 or ENEMY_ACTION == 5:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            ENEMY_ACTION = 0
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        if ENEMY_ACTION == 3 :
            self.cur_attack += 1
            self.texture = self.attack_texture[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]
            if self.cur_attack > 7 * UPDATES_PER_FRAME :
                self.cur_attack = 0
                ENEMY_ACTION = 4
            else :
                return
        self.texture = self.walk_texture[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]

class SLIME (arcade.Sprite) :
    def __init__ (self):

        super().__init__(self)
        self.HP = ENEMY_HP
        self.ATTACK = 20

        self.cur_texture = 0

        self.cur_attack = 0

        self.idle_texture_pair = load_texture_pair("image/slime.png")
        self.character_face_direction = LEFT_FACING

        self.texture = self.idle_texture_pair[self.character_face_direction]

        self.walk_texture = []

        texture = load_texture_pair("image/slime.png")
        self.walk_texture.append(texture)

        self.attack_texture = []

        texture = load_texture_pair("image/slime.png")
        self.attack_texture.append(texture)





    def update_animation(self, delta_time: float = 1/60):

        global ENEMY_ACTION

        if ENEMY_ACTION == 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif ENEMY_ACTION == 2 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if ENEMY_ACTION == 0 or ENEMY_ACTION == 5:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            ENEMY_ACTION = 0
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0

        if ENEMY_ACTION == 3 :
            self.cur_attack += 1
            self.texture = self.attack_texture[0][self.character_face_direction]
            if self.cur_attack > 7 * UPDATES_PER_FRAME :
                self.cur_attack = 0
                ENEMY_ACTION = 4
            else :
                return
        self.texture = self.walk_texture[0][self.character_face_direction]

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()

class BUTTON (arcade.Sprite):
    def __init__(self):

        super().__init__(self)

        global BUTTON_VALUE

        self.scale = 0.3
        self.pressed = False
        self.value  = BUTTON_VALUE
        self.BUTTON_TEXTURE = []
        self.idle_texture_pair = load_texture_pair(f"image/BUTTON/{BUTTON_VALUE}.jpg")
        texture = self.idle_texture_pair [LEFT_FACING]
        self.BUTTON_TEXTURE.append(texture)
        BUTTON_VALUE += 1

        self.texture = self.BUTTON_TEXTURE[0]


    def ART(self):
        pass

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

class QUESTION(arcade.Sprite) :

    def set_answer(self,answer):
        self.answer_value = answer


class MyGame (arcade.Window) :

    def __init__ (self, width, height, title ) :

        super().__init__(width, height, title)

        self.status = CAN_ATTACK
        self.change = CAN_CHANGE
        arcade.set_background_color(arcade.color.AMAZON)



    def setup (self) :

        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = PLAYER_PLACE_x
        self.player_sprite.center_y = PLAYER_PLACE_y

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        """    SET ENEMY   """

        self.enemy_list = arcade.SpriteList()

        self.enemy_sprite = SLIME()
        self.enemy_sprite.center_x = 1100
        self.enemy_sprite.center_y = 420

        self.enemy_list.append(self.enemy_sprite)

        self.enemy_sprite = GOBLIN()
        self.enemy_sprite.center_x = 1100 + (1 * SCREEN_WIDTH)
        self.enemy_sprite.center_y = 420


        self.enemy_list.append(self.enemy_sprite)

        """   SET   ENEMY  """

        self.button_list = arcade.SpriteList()

        for i in range(2) :
            for j in range(2):
                self.button_sprite = BUTTON()
                self.button_sprite.center_x = 900 + (j * 200)
                self.button_sprite.center_y = 250 - (i * 150)
                self.button_list.append(self.button_sprite)


        self.wall_list = arcade.SpriteList()
        for x in range(0,SCREEN_WIDTH,60):
            wall = arcade.Sprite("image/ground.png")

            wall.center_x = x
            wall.center_y = 370

            self.wall_list.append(wall)

        """ SET ANSWER"""

        self.question_list = arcade.SpriteList()

        for i in range(30) :
            question_sprite = QUESTION(f"image/QUESTION/question_0{i}.png")
            question_sprite.scale = 0.5
            question_sprite.center_x = 400
            question_sprite.center_y = 170

            self.question_list.append(question_sprite)


        self.question_list[0].set_answer(1)
        self.question_list[1].set_answer(2)
        self.question_list[2].set_answer(3)
        self.question_list[3].set_answer(2)
        self.question_list[4].set_answer(1)
        self.question_list[5].set_answer(4)
        self.question_list[6].set_answer(1)
        self.question_list[7].set_answer(4)
        self.question_list[8].set_answer(3)
        self.question_list[9].set_answer(4)
        self.question_list[10].set_answer(2)
        self.question_list[11].set_answer(3)
        self.question_list[12].set_answer(1)
        self.question_list[13].set_answer(3)
        self.question_list[14].set_answer(1)

        self.question_list[15].set_answer(3)
        self.question_list[16].set_answer(4)
        self.question_list[17].set_answer(2)
        self.question_list[18].set_answer(4)
        self.question_list[19].set_answer(2)
        self.question_list[20].set_answer(2)
        self.question_list[21].set_answer(4)
        self.question_list[22].set_answer(4)
        self.question_list[23].set_answer(1)
        self.question_list[24].set_answer(2)
        self.question_list[25].set_answer(4)
        self.question_list[26].set_answer(4)
        self.question_list[27].set_answer(2)
        self.question_list[28].set_answer(2)
        self.question_list[29].set_answer(3)


        """ SET ANSWER """


        self.NUB = 0

        self.blackground =  arcade.Sprite("image/Background/BG.jpg")
        self.blackground.center_x = SCREEN_WIDTH/2
        self.blackground.center_y = SCREEN_HIGHT/2
        self.blackground.scale = 1
        self.blackground_list = arcade.SpriteList()
        self.blackground_list.append(self.blackground)

    def on_draw (self) :

        global SCREEN

        arcade.start_render()
        self.blackground.draw()
        if SCREEN == 0 and len(self.enemy_list) != 0 :
            self.button_list.draw()
            # arcade.draw_circle_filled(300, 500, 30, arcade.color.YELLOW)
            text = "ENEMY HP = " + f"{self.enemy_list[MOB_NO].HP}"
            arcade.draw_text(text, self.enemy_list[0].center_x-90, 470, arcade.color.WHITE, 20)
            # text = "ENEMY X = " + f"{self.enemy_list[MOB_NO].center_x}"
            # arcade.draw_text(text, 10, 480, arcade.color.BLACK, 12)
            text = "YOUR HP = " + f"{self.player_sprite.HP}"
            arcade.draw_text(text, self.player_sprite.center_x - 90, 470, arcade.color.WHITE, 20)

            if self.change == CAN_CHANGE :

                self.NUB = random.randint(0,len(self.question_list))
                self.change = CANT_CHANGE
            self.enemy_list.draw()
            self.question_list[self.NUB].draw()

        if SCREEN == 1:

            text = "CONGRATULATION"
            arcade.draw_text(text, 200, 360, arcade.color.RED, 100)

        if SCREEN == 2:

            text = "YOU LOSE"
            self.enemy_list.draw()
            arcade.draw_text(text, 350, 360, arcade.color.RED, 100)



        self.player_list.draw()
        self.wall_list.draw()

    def update(self, delta_time):
        global ACTION
        global MOB_NO
        global ENEMY_ACTION
        global SCREEN


        self.player_list.update_animation()

        if self.player_sprite.HP <= 0 :
            SCREEN = 2

        if len(self.enemy_list) == 0 :
            SCREEN = 1

        if  len(self.enemy_list) != 0 :
            self.enemy_list[MOB_NO].update_animation()

        # for i in range (len(BUTTON_BOX)):
        #     print (BUTTON_BOX[i])

        if self.button_list[0].pressed :
            if self.button_list[0].value == self.question_list[self.NUB].answer_value :
                ACTION = 1

            else :
                ENEMY_ACTION = 1

        if self.button_list[1].pressed:
            if self.button_list[1].value == self.question_list[self.NUB].answer_value:
                ACTION = 1

            else :
                ENEMY_ACTION = 1

        if self.button_list[2].pressed :
            if self.button_list[2].value == self.question_list[self.NUB].answer_value :
                ACTION = 1

            else :
                ENEMY_ACTION = 1

        if self.button_list[3].pressed :
            if self.button_list[3].value == self.question_list[self.NUB].answer_value :
                ACTION = 1

            else :
                ENEMY_ACTION = 1
        if len (self.enemy_list) != 0 :
            if self.enemy_list[MOB_NO].HP <= 0 :
                self.enemy_list[MOB_NO].kill()
                self.question_list[self.NUB].kill()
                self.change = CAN_CHANGE
                self.status = CANT_ATTACK

            if  self.status == CANT_ATTACK  :
                for i in range (len(self.enemy_list)) :
                    self.enemy_list[i].center_x -= ENEMY_SPEED
                    if self.enemy_list[i].center_x <= 1100 :
                        self.status = CAN_ATTACK


            if ENEMY_ACTION == 1 :
                self.enemy_list[MOB_NO].center_x -= 5
                if self.player_sprite.center_x == self.enemy_list[MOB_NO].center_x -50 :
                    ENEMY_ACTION = 3

            elif ENEMY_ACTION == 4 :
                self.player_sprite.HP -= self.enemy_list[MOB_NO].ATTACK
                ENEMY_ACTION = 2

            if ENEMY_ACTION == 2 :
                self.enemy_list[MOB_NO].center_x += 5
                if self.enemy_list[MOB_NO].center_x == 1100 :
                    ENEMY_ACTION = 5


        if ACTION == 1 :
            self.player_sprite.center_x += 5
            if self.player_sprite.center_x == self.enemy_list[MOB_NO].center_x -50 :
                ACTION = 3

        elif ACTION == 4 :
            self.enemy_list[MOB_NO].HP -= PLAYER_ATTACK
            ACTION = 2

        if ACTION == 2 :
            self.player_sprite.center_x -= 5
            if self.player_sprite.center_x == PLAYER_PLACE_x :
                ACTION = 5


    def on_key_press(self, key, key_modifier):
        pass
        # if key == arcade.key.UP :
        #     self.player_sprite.change_y += 10
        # elif key == arcade.key.LEFT :
        #     self.player_sprite.change_x += -10
        # elif key == arcade.key.RIGHT :
        #     self.player_sprite.change_x += 10
        # elif key == arcade.key.DOWN :
        #     self.player_sprite.change_y += -10

    def  on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass
        # if key == arcade.key.UP :
        #     self.player_sprite.change_y += -10
        # elif key == arcade.key.LEFT :
        #     self.player_sprite.change_x += 10
        # elif key == arcade.key.RIGHT :
        #     self.player_sprite.change_x += -10
        # elif key == arcade.key.DOWN :
        #     self.player_sprite.change_y += 10

    def  on_mouse_motion (self, x, y, delta_x, delta_y):

        # self.player_sprite.center_x = x
        # self.player_sprite.center_y = y
        pass


    def on_mouse_press (self, x, y, button, key_modifier):
        # global ACTION
        # if button == arcade.MOUSE_BUTTON_LEFT and (x > 270 and x < 330) and (y>470 and y < 530) and ACTION == 0 and self.status == CAN_ATTACK:
        #     ACTION = 1

        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifier):
        pass
        check_mouse_release_for_buttons(x, y, self.button_list)


def main():

    game  = MyGame(SCREEN_WIDTH, SCREEN_HIGHT, "TEST")
    game.setup()
    arcade.run()

if __name__ ==  "__main__" :
    main()

