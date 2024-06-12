import cv2
from flet import ElevatedButton, MainAxisAlignment, Page, app


def main(page: Page):
    def video_capture(e):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        while True:
            ret, frame = cap.read()
            cv2.imshow('FRAMES', frame)
            t = cv2.waitKey(5)
            if t == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    page.title = "LEGOURMET"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.add(ElevatedButton(text="Tomar pedido", on_click=video_capture))
    page.update()


app(main)