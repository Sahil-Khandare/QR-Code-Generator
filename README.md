# QR Code Generator

A simple Python application that generates a QR code from any user-provided text or URL using the `qrcode` library. The generated QR code is saved as an image (`qrcode.png`) in the project directory.

## Features

- Generate QR codes from any text or URL
- Saves the QR code as a PNG image
- Simple command-line interface
- Lightweight and beginner-friendly

## Technologies Used

- Python 3
- qrcode
- Pillow (PIL)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Qr-Code-Generator.git
```

2. Navigate to the project folder:

```bash
cd Qr-Code-Generator
```

3. Install the required package:

```bash
pip install qrcode[pil]
```

## Usage

Run the program:

```bash
python QrGenrator.py
```

Enter any text or URL when prompted:

```
Enter any text: https://github.com/your-username
```

The program will generate and save:

```
qrcode.png
```

## Project Structure

```
QR-Code-Generator/
│── QrGenerator.py
│── qrcode.png        # Generated after running the program
└── README.md
```

## Example

**Input**

```
Enter any text:
Hello!! I'm Sahil Khandare
" Every expert was once a begineer."
I enjoy learning AI, Machine Learning and creating practical Python applications.
```

**Output**

```
QR Code was generated!
```

Scanning the generated QR code displays:

![Qr Code](qrcode.png)

## Future Improvements

- Custom QR code colors
- Custom file name option
- QR code size adjustment
- Logo embedding in QR code

---

## Author

**Sahil Khandare**

Engineering Student | AI & Machine Learning Enthusiast

---

## ⭐ If you found this project useful, consider giving the repository a star!

