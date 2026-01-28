import pickle
import cv2
import mediapipe as mp
import numpy as np 
import tkinter as tk
from tkinter import Label, Button, Frame
from PIL import Image, ImageTk  
# import threading
# import pyttsx3

class SignLanguageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Translator") 
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50") 
        
        self.model_dict = pickle.load(open('./model.p', 'rb'))
        self.model = self.model_dict['model']
        
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

        self.labels_dict = {0: ' اهلا', 1: 'حبيبي', 2: 'شكرًا', 3: 'أسف',
                             4: 'انا مبسوط', 5: 'أب', 6: 'أم', 7: 'أخ',
                              8: 'مريض', 9: 'ساعدنى', 10: 'أوعدك', 11: 'صاحب', 12: 'مستشفى'
                            }
        
        # self.engine = pyttsx3.init()
        # self.engine.setProperty('rate', 150)
        # self.current_prediction = "Waiting..."

        self.title_label = Label(root, text="Sign Language Interpreter", font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.title_label.pack(pady=10)

        self.video_frame = Frame(root, bg="black", bd=2, relief="sunken")
        self.video_frame.pack(pady=10)
        
        self.lmain = Label(self.video_frame)
        self.lmain.pack()

        self.result_label = Label(root, text="Waiting for hand...", font=("Helvetica", 20), bg="#2c3e50", fg="#f1c40f") 
        self.result_label.pack(pady=20)

        self.btn_frame = Frame(root, bg="#2c3e50")
        self.btn_frame.pack(pady=10)

       
        # self.speak_btn = Button(self.btn_frame, text="🔊 SPEAK", font=("Helvetica", 16, "bold"), bg="#27ae60", fg="white", command=self.speak_text, width=15, height=2)
        # self.speak_btn.pack(side="left", padx=20)
     
        self.quit_btn = Button(self.btn_frame, text="❌ EXIT", font=("Helvetica", 16, "bold"), bg="#c0392b", fg="white", command=root.quit, width=10, height=2)
        self.quit_btn.pack(side="left", padx=20)

        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            H, W, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            results = self.hands.process(frame_rgb)
            
            data_aux = []
            x_ = []
            y_ = []

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style())

                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                expected_length = 84
                if len(data_aux) < expected_length:
                    data_aux.extend([0] * (expected_length - len(data_aux)))
                
                final_data = data_aux[:84]

                try:
                    prediction = self.model.predict([np.asarray(data_aux)])
                    predicted_character = self.labels_dict[int(prediction[0])]
                    self.current_prediction = predicted_character
                    self.result_label.config(text=f"Detected: {predicted_character}", fg="#f1c40f")
                except:
                    pass
            else:
                self.current_prediction = None
                self.result_label.config(text="Waiting for hand...", fg="#bdc3c7")

            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    # --- دالة النطق (Threaded) ---
    # def speak_text(self):
    #     if self.current_prediction:
    #         threading.Thread(target=self._speak_thread).start()
    
    # def _speak_thread(self):
    #     try:
    #         self.engine.stop()
    #         self.engine.say(self.current_prediction)
    #         self.engine.runAndWait()
    #     except:
    #         pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SignLanguageApp(root)
    root.mainloop()