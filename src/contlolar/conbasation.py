from src.model import robot

def google_img():
    "3つのステップこんにちわと処理と出来ました"
    google_robot = robot.Googlerobot()
    google_robot.hello()
    google_robot.img_move()
    google_robot.by()