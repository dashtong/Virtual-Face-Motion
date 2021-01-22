import cv2
import dlib
import ast
import numpy as np
import math

def getFirstLandmark(imgLink):
    img = cv2.imread(imgLink)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    faces = detector(img_gray)
    for face in faces:
        landmarks = predictor(img_gray, face)
        landmarks_points = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y  
            landmarks_points.append((x, y))
    # print(landmarks_points[20], landmarks_points[37])
    f = open("landmarks/1landmark.txt", "w")
    f.write(str(landmarks_points))
    f.close()

def midpt(p1, p2):
    return (int((p1[0] + p2[0])/2), int((p1[1] + p2[1])/2))

def blinkLandmark(fn):
    f = open(fn, "r") 
    landmarks_points_str = f.read()
    landmarks_points = ast.literal_eval(landmarks_points_str)
    f.close()
    
    centerTopL = midpt(landmarks_points[37], landmarks_points[38])
    centerBottomL = midpt(landmarks_points[40], landmarks_points[41])
    verLenL = math.hypot((centerTopL[0] - centerBottomL[0]), (centerTopL[1] - centerBottomL[1]))
    centerTopR = midpt(landmarks_points[44], landmarks_points[43])
    centerBottomR = midpt(landmarks_points[47], landmarks_points[46])
    verLenR = math.hypot((centerTopR[0] - centerBottomR[0]), (centerTopR[1] - centerBottomR[1]))

    varLeft, varRight = round(verLenL/5), round(verLenR/5)

    for i in range(5):
        landmarks_points_store = landmarks_points
        new_landmarks = []
        for n, landmarks in enumerate(landmarks_points_store):
            landmarks = list(landmarks)
            if (n==37 or n==38) and i!=4:
                landmarks[1] += varLeft * (i+1)
            elif n==37 or n==38:
                landmarks[1] = round(centerBottomL[1])
            elif (n==43 or n==44) and i!=4:
                landmarks[1] += varRight * (i+1)
            elif n==43 or n==44:
                landmarks[1] = round(centerBottomR[1])
            new_landmarks.append(tuple(landmarks))
        f = open("landmarks/blink_landmark{}.txt".format(i), "w")
        f.write(str(new_landmarks))
        f.close()

def noddingLandmark(fn):
    f = open(fn, "r") 
    landmarks_points_str = f.read()
    landmarks_points = ast.literal_eval(landmarks_points_str)
    f.close()

    for i in range(10):
        new_landmarks = []
        for landmarks in landmarks_points:
            landmarksList = list(landmarks)
            M2 = np.array([0, (i-4) * 0.2])
            M3 = np.subtract(landmarksList, M2)
            new_landmarks.append(tuple(M3))

        f = open("landmarks/nodding_landmark{}.txt".format(i), "w")
        f.write(str(new_landmarks))
        f.close()


if __name__ == "__main__":
    # getLandmark("kakki.jpg")
    # blinkLandmark("landmarks/landmark.txt")
    noddingLandmark("landmarks/landmark.txt")