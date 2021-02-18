
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty

import random

N_OF_PIECES_FOR_1_PLAYER = 12
N_OF_PIECES = N_OF_PIECES_FOR_1_PLAYER * 2
N_COLS = 8


class Black(Label):
    pass


class White(Widget):
    pass




class Piece(Widget):
    selected = BooleanProperty(False)

    # def on_touch_down(self, touch):
    #     if self.collide_point(*touch.pos):
    #         print("mode")
    #         if self.selected and self.parent.your_turn is True:
    #             self.x += self.width
    #             self.y += self.height
    #             self.parent.your_turn = False

    #         if self.selected is False:
    #             self.selected = True


class WhitePiece(Piece):
    pass


class BlackPiece(Piece):
    pass


class Game(Widget):
    # Piece = ObjectProperty(None)
    your_turn = BooleanProperty(True)

    def __init__(self, app):
        super().__init__()
        self.cols = N_COLS
        self.app = app
        self.width_of_a_square = self.app.window.width / self.cols
        self.height_of_a_square = self.app.window.height / self.cols
        print(self.width_of_a_square, self.height_of_a_square)

        # create board:
        for line in range(N_COLS):
            for col in range(N_COLS):
                if (line + col) % 2 == 0:
                    self.add_widget(White(pos=(col * self.width_of_a_square, line * self.height_of_a_square)))
                else:
                    self.add_widget(Black(pos=(col * self.width_of_a_square, line * self.height_of_a_square)))

        # put all the pieces:
        self.mob_pieces_pos = [
            (0, 7), (2, 7), (4, 7), (6, 7),
            (1, 6), (3, 6), (5, 6), (7, 6),
            (0, 5), (2, 5), (4, 5), (6, 5),
            ]
        self.player_pieces_pos = [
            (1, 0), (3, 0), (5, 0), (7, 0),
            (0, 1), (2, 1), (4, 1), (6, 1),
            (1, 2), (3, 2), (5, 2), (7, 2),
            ]
        self.mob_pieces = []
        self.player_pieces = []

        for mob_pos_x, mob_pos_y in self.mob_pieces_pos:
            new_piece = BlackPiece(pos=(mob_pos_x * self.width_of_a_square, mob_pos_y * self.height_of_a_square))
            self.add_widget(new_piece)
            self.mob_pieces.append(new_piece)
        for player_pos_x, player_pos_y in self.player_pieces_pos:
            new_piece = WhitePiece(pos=(player_pos_x * self.width_of_a_square, player_pos_y * self.height_of_a_square))
            self.add_widget(new_piece)
            self.player_pieces.append(new_piece)

    def on_touch_down(self, touch):
        print(0, touch, touch.profile, touch.button)
        for player_piece in self.player_pieces:
            if player_piece.collide_point(*touch.pos):
                print(1, player_piece, player_piece.pos, player_piece.children)
                pos_0 = player_piece.pos.copy()
                player_piece.y += player_piece.height
                if touch.button == "right":
                    player_piece.x += player_piece.width
                if touch.button == "left":
                    player_piece.x -= player_piece.width
                # check if it's possible:
                print(player_piece, player_piece.pos, pos_0)
                print(player_piece.x, self.app.window.width)

                # handle board boarders 
                if player_piece.x >= self.app.window.width:
                    print("can't pass the right")
                    player_piece.pos = pos_0
                    return
                if player_piece.x < 0:
                    print("can't pass the left")
                    player_piece.pos = pos_0
                    return
                print(player_piece, player_piece.pos, pos_0)

                # handle mob colisions:
                for mob_piece in self.mob_pieces:
                    # print(player_piece.pos, mob_piece.pos)
                    # print(player_piece.pos == mob_piece.pos)
                    if player_piece.pos == mob_piece.pos:
                        print("collide with a mob piece")
                        player_piece.pos = pos_0
                        return
                        
                # handle self colisions:
                for player_piece2 in self.player_pieces:
                    if player_piece2 is player_piece:
                        continue
                    if player_piece.pos == player_piece2.pos:
                        print("collide with a self piece")
                        player_piece.pos = pos_0
                        return
        self.mob_plays()

    def mob_plays(self):
        print("mob_plays")
        i = 0

        mobs_to_check = {"right": self.mob_pieces.copy(), "left": self.mob_pieces.copy()}

        while True:
            i += 1
            print(i)
            ok = True
            right_or_left = random.choice(["right", "left"])
            mob_piece = random.choice(mobs_to_check[right_or_left])
            mobs_to_check[right_or_left].remove(mob_piece)

            pos_0 = mob_piece.pos.copy()
            mob_piece.x += mob_piece.width * random.choice([-1, 1])
            mob_piece.y -= mob_piece.height

            print(pos_0, mob_piece.pos)

            # handle board boarders 
            if mob_piece.x >= self.app.window.width:
                print("can't pass the right")
                mob_piece.pos = pos_0
                ok = False
                continue
            if mob_piece.x < 0:
                print("can't pass the left")
                mob_piece.pos = pos_0
                ok = False
                continue
            print(mob_piece, mob_piece.pos, pos_0)

            # handle self mob colisions:
            for mob_piece2 in self.mob_pieces:
                if mob_piece2 is mob_piece:
                    continue
                if mob_piece.pos == mob_piece2.pos:
                    print("collide with a mob piece")
                    mob_piece.pos = pos_0
                    ok = False
                    break

                    
            # handle player colisions:
            for player_piece in self.player_pieces:
                if mob_piece.pos == player_piece.pos:
                    print("collide with a player piece")
                    mob_piece.pos = pos_0
                    ok = False
                    break
            
            
            if i > 1000:
                break
        
            if ok:
                break

class DamasApp(App):
    window = ObjectProperty(Window)
    n_cols = NumericProperty(N_COLS)

    def build(self):
        self.window.clearcolor = (0.3, 0, 0, 1)
        game = Game(self)
        return game

if __name__ == "__main__":
    DamasApp().run()