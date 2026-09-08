# Lec 1.1 - Tue 9/8: Setup Python, VS Code, and Git

Complete these steps; they assume you have no software installed yet.

## 1. Install Visual Studio Code

1. Go to https://code.visualstudio.com/
2. Download the installer for your operating system (Windows or Mac) and run it, accepting the default options.
3. Open VS Code once installation finishes to confirm it launches.

## 2. Install Python (via the Anaconda distribution)

We'll use the **Anaconda distribution**, which bundles Python with the data science libraries (`pandas`, `numpy`, `matplotlib`) used in this course, plus Jupyter notebook support.

1. Go to https://www.anaconda.com/download
2. Download the installer for your OS.
3. Run the installer, accepting the default options.
   - **Windows**: when prompted, it's fine to leave "Add Anaconda to my PATH environment variable" unchecked (default) — VS Code will find it automatically.
   - **Mac**: accept the default install location.
4. Verify the install: open a terminal (Mac: **Terminal** app; Windows: **Anaconda Prompt**, found in your Start menu) and type:
   ```
   python --version
   ```
   You should see a Python 3.x version number printed.

## 3. Install Git

3. Verify if you have git installed. If so, skip the rest. Open a terminal and type:
   ```
   git --version
   ```
   You should see a version number printed.
1. Go to https://git-scm.com/downloads
2. Download and run the installer for your OS.
   - **Windows**: accept all default options during installation.
   - **Mac**: if you're prompted to install Xcode Command Line Tools instead, accept that — it includes Git.
3. Verify the install: open a terminal and type:
   ```
   git --version
   ```
   You should see a version number printed.

## 4. Set up VS Code for Python + Jupyter Notebooks

1. Open VS Code.
2. Click the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Search for and install:
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)
4. Restart VS Code after both are installed.

## 5. Get the course files

1. Open a terminal (Mac: **Terminal**; Windows: **Anaconda Prompt** or **Git Bash**).
2. Navigate to a folder where you want to keep your course work, e.g.:
   ```
   cd Documents
   ```
3. Clone the course repository:
   ```
   git clone <COURSE_REPO_URL>
   cd <REPO_FOLDER_NAME>
   ```
   *(Your instructor will provide the exact repo URL in class.)*

## 6. Open and run `lab00_intro_to_python.ipynb`

1. In VS Code, go to **File > Open Folder...** and select the course repo folder you just cloned.
2. In the Explorer sidebar, navigate to `Labs/` and click `lab00_intro_to_python.ipynb` to open it.
3. In the top-right corner of the notebook, click **Select Kernel**.
4. Choose **Python Environments...**, then select the Anaconda `base` environment (it should be listed automatically since Anaconda was installed in Step 2).
5. Run the first code cell (click the ▶ play button to its left, or press `Shift+Enter`). VS Code may prompt you to install the `ipykernel` package the first time — click **Install** and wait for it to finish.
6. Continue running cells top to bottom with `Shift+Enter` to work through the lab.

