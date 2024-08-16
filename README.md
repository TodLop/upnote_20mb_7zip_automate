# 7-Zip Compression Tool for UpNote

This Python-based GUI application is designed to help you automatically split and compress files into 20MB chunks, specifically tailored for use with UpNote's file size limit. The application leverages the 7-Zip software for compression and uses the `tkinter` library for a simple graphical user interface.

## Features

- **Automatic Splitting and Compression:** Compresses files in a selected folder into 20MB chunks to fit UpNote's upload limit.
- **Customizable Compression Settings:** The compression level and method can be easily modified by editing the script.
- **User-Friendly Interface:** The tool is designed with a simple and intuitive `tkinter` interface.
- **Output Management:** Compressed files are saved in a new `compressed` folder within the selected directory.

## Prerequisites

- **7-Zip:** Ensure that 7-Zip is installed on your system. You can download it from [7-Zip's official website](https://www.7-zip.org/).
- **Python 3.x:** Ensure that Python 3.x is installed, which includes the `tkinter` module.

## Installation

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install 7-Zip:**
   - Download and install 7-Zip from [7-Zip's official website](https://www.7-zip.org/).
   - Make sure `7z.exe` is located in the default directory `C:\Program Files\7-Zip\7z.exe`. If it's located elsewhere, update the `seven_zip_path` variable in the script accordingly.

3. **Clone or Download this Repository:**
   - Clone the repository using `git`:
     ```bash
     git clone https://github.com/your-username/7zip-compression-tool-for-upnote.git
     ```
   - Or download the ZIP file and extract it.

## Usage

1. **Run the Script:**
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```bash
     python 7zip_compression_tool.py
     ```

2. **Select a Folder:**
   - Click the "Select Folder" button to choose the folder containing the files you wish to compress.

3. **Compress Files:**
   - Click the "Compress Files" button to start compressing the files in the selected folder. The files will be split into 20MB chunks and saved in a new `compressed` folder within the selected directory.

4. **Completion:**
   - A message box will notify you once all files have been successfully compressed.

## Customization

- **Compression Level:**
   - To change the compression level, modify the `-mx=9` parameter in the `compress_file` function. The value can range from `-mx=0` (no compression) to `-mx=9` (maximum compression).

- **Compression Method:**
   - The script uses the LZMA2 method by default (`-m0=LZMA2`). You can change this by modifying the parameter in the `compress_file` function. Refer to the [7-Zip documentation](https://www.7-zip.org/) for available methods.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [7-Zip](https://www.7-zip.org/) for providing a powerful open-source compression tool.
- [Python](https://www.python.org/) for making programming accessible and fun.

---

This README.MD has been Created by OpenAI's GPT-4O.

