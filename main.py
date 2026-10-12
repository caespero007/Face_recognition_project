import cv2 
import numpy as np
import face_recognition as fr

video_capture = cv2.VideoCapture(0)
image = fr.load_image_file("boy.jpg")
image_encoding = fr.face_encoding(image)[0]
known_face_encoding = [image_face_encoding]
known_face_name = ["sarvesh"]



while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[: , : , ::-1]
    fc_locations = fr.face_locations(rgb_frame)
    fc_encodings = fr.face_encodings(rgb_frame, fc_locations)
    for(top, right, bottom, left), face encoding in zip(fc_locations, fc_encodings):
        matches = fr.compare_faces(known_face_encoding , face_encodings)


        name = "unknown"


        face_distances = fr.face_distance(known_face _encoding, face_encoding)