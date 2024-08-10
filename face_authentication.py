import cv2
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to capture user's face images and password for registration
def register_faces_and_password(username):
    cap = cv2.VideoCapture(0)

    count = 0

    user_dir = 'faces/' + username
    os.makedirs(user_dir, exist_ok=True)

    # Capture face images
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces:
            # Save detected face images
            img_name = f'{user_dir}/face_{count}.png'
            cv2.imwrite(img_name, frame[y:y+h, x:x+w])
            count += 1

            # Display the face rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Register Face', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 10:  
            break

    password = input("Enter your password: ")
    with open(f'{user_dir}/password.txt', 'w') as f:
        f.write(password)

    cap.release()
    cv2.destroyAllWindows()

# Function to perform face authentication and password verification
def authenticate(username):
    cap = cv2.VideoCapture(0)

    # Load user's registered face images
    user_dir = 'faces/' + username
    face_images = [cv2.imread(os.path.join(user_dir, file_name)) for file_name in os.listdir(user_dir) if file_name.endswith('.png')]

    # Load user's registered password
    with open(f'{user_dir}/password.txt', 'r') as f:
        registered_password = f.read().strip()

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces:
            # Perform face matching with registered faces
            match = any(cv2.matchTemplate(face_img, frame[y:y+h, x:x+w], cv2.TM_CCOEFF_NORMED).max() > 0.8 for face_img in face_images)

            if match:
                cv2.putText(frame, "Face authentication verified.", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                print('Face matched!')

                # Prompt user for password verification
                password_attempt = input("Enter your password: ")
                if password_attempt == registered_password:
                    print("Password verified. Two-step verification successful.")
                    return
                else:
                    print("Incorrect password.")
            else:
                cv2.putText(frame, "Unauthorized", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                print("Unauthorized access attempt detected")
                return

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Authentication', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    
    username = input("Enter your username: ")
    
    user_dir = 'faces/' + username
    if os.path.exists(user_dir):
        print("User already exists. Proceeding to authentication.")
        authenticate(username)
    else:
        print("New user. Starting face enrollment.")
        register_faces_and_password(username)
        print("Face and password registered successfully.")

        print("Face authentication started...")
        authenticate(username)

if __name__ == "__main__":
    main()
