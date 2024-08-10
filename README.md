
# Face Authentication with Password Verification

## Overview

This project demonstrates a basic implementation of face authentication with password verification using OpenCV in Python. It captures and registers a user's face along with a password, then authenticates the user by matching their face and verifying the password.

## Features

- **Face Registration:** Captures and stores 10 images of the user's face along with a password.
- **Face Authentication:** Verifies the user's identity by matching the face against registered images and prompts for a password for two-step authentication.
- **Unauthorized Access Detection:** Detects and alerts on unauthorized access attempts.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` package)
- A working webcam

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dev261004/Face-authentication.git
   cd face-authentication
   ```

2. **Install the required Python packages:**

   ```bash
   pip install opencv-python
   ```

3. **Run the script:**

   ```bash
   python face_authentication.py
   ```

## Usage

1. **Registration:**
   - The program will ask for your username.
   - If the username doesn't exist, it will start the face registration process and capture 10 images of your face.
   - You'll be prompted to enter a password, which will be stored securely.

2. **Authentication:**
   - If the username exists, the program will start the face authentication process.
   - After detecting your face, the program will prompt you for the password.
   - If both the face and password match the registered data, authentication is successful.

3. **Exiting the Program:**
   - You can exit the face capture or authentication process anytime by pressing the 'q' key.

## Project Structure

```plaintext
face-authentication/
│
├── faces/
│   └── <username>/
│       ├── face_0.png
│       ├── face_1.png
│       ├── ...
│       └── password.txt
│
├── face_authentication.py
└── README.md
```

- **faces/**: This directory stores the registered face images and password files.
- **face_authentication.py**: The main script that handles face registration and authentication.
- **README.md**: This file containing information about the project.

## Future Improvements

- Implement more robust face recognition algorithms.
- Add password hashing for more secure storage.
- Introduce multi-user support with a more comprehensive database.
- Integrate with a GUI for a more user-friendly experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
