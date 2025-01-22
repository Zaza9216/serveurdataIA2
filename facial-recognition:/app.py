import face_recognition

# Charger les images
known_image = face_recognition.load_image_file('file1.jpg')
unknown_image = face_recognition.load_image_file('file2.jpg')

# Encoder les visages
known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Comparer les visages
results = face_recognition.compare_faces([known_encoding], unknown_encoding)
print("Les visages correspondent : ", results)
