from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

print(cv2.__version__)

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720+0+0")
        self.root.title("student")

        # button
        b1_1 = Button(
            self.root,
            text="Train Data",
            cursor="hand2",
            command=self.train_classifier,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width="10",
        )
        b1_1.place(width=1080, height=60)

    def train_classifier(self):
        data_dir = r"C:\Users\91799\Desktop\pythonprojectmainpratik\data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # convert inot grey scale
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) & 0xFF

        ids = np.array(ids)

        ### TRAIN THE CLASSIFIER AND SAVE
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf = (
            cv2.face.LBPHFaceRecognizer_create()
            if cv2.__version__.startswith("4")
            else cv2.face.LBPHFaceRecognizer()
        )
        # if cv2.__version__.startswith("4"):
        #     clf = cv2.face.LBPHFaceRecognizer_create()
        # else:
        #     clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed.")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
