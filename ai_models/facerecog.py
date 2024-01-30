import cv2
from TapsiFAceAddons import TapsilogFaceReco

   
class TapsiRecogs:
    def __init__(self):
        self.tapsi_ai = TapsilogFaceReco()
        self.tapsi_ai.load_encoding_images("practice_faces/")

        # Loads the cam
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FPS, 60)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

        while True:
            ret, frame = self.cap.read()

            # Detect Face
            self.face_location, self.face_names = self.tapsi_ai.detect_known_faces(frame)
            for face_loc, name in zip(self.face_location, self.face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (163, 196, 234), 4)

            cv2.imshow("Live Feed", frame)

            key = cv2.waitKey(100)
            if key == ord(" "):
                break

        self.cap.release()
        cv2.destroyAllWindows()


run = TapsiRecogs()