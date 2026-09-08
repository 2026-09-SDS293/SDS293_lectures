# Course Overview

- [Course schedule](https://docs.google.com/spreadsheets/d/e/2PACX-1vToPV6gfDlIq5ni1qezMcPy3ZdyIN1MtSSKZ3GABeBvf9LYu3_1XE7DOEQh4Dg02bKG5YF0XpSFO_-B/pubhtml?gid=951666182&single=true)
- [Syllabus](https://docs.google.com/document/d/1lK7GGtBCa7a2vtsxQLncKqUdS1siXBVi27ruP0pS3SA/edit?tab=t.0#heading=h.xgrewbu2h3w3)
- Office hours: TBD

# Lec 01-2 - Thu 9/10

- Ensure you've accepted the email invitation to the class GitHub organization 
- Right before lecture, do a pull of this repo to get the latest files
- Make sure you can access the class Slack workspace https://sds-293-01-202701.slack.com 

# Lec 01-1 - Tue 9/8

- Complete the [intro survey](https://docs.google.com/forms/d/e/1FAIpQLSfXhSZsNHNlPshataatZIwl2ZacBl7o_sUbQ-kkH0hGFCkjQw/viewform)
- Install Python, VS Code, and Git

## 1. Install Visual Studio Code

Install/update to the latest version of VS Code:

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

1. Verify if you have git installed. If so, skip the rest. Open a terminal and type:
   ```
   git --version
   ```
   You should see a version number printed.
2. Go to https://git-scm.com/downloads
3. Download and run the installer for your OS.
   - **Windows**: accept all default options during installation.
   - **Mac**: if you're prompted to install Xcode Command Line Tools instead, accept that — it includes Git.
4. Verify if you have git installed again.

## 4. Set up VS Code for Python + Jupyter Notebooks

1. Open VS Code.
2. Click the **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Search for and install both:
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
   git clone https://github.com/2026-09-SDS293/SDS293_lectures.git
   cd SDS293_lectures
   ```

## 6. Open and run `lab01-1_intro_to_python_YOURSMITHLOGIN.ipynb`

1. In VS Code, go to **File > Open Folder...** and select the course repo folder you just cloned.
2. In the Explorer sidebar, navigate to `lec01-1/`
3. Make a copy of `lab01-1_intro_to_python_YOURSMITHLOGIN.ipynb` and replace `YOURSMITHLOGIN` with your Smith login e.g. `lab01-1_intro_to_python_jpark03.ipynb`
4. In the top-right corner of the notebook, click **Select Kernel**.
5. Choose **Python Environments...**, then select the Anaconda `base` environment (it should be listed automatically since Anaconda was installed in Step 2).
6. Run the first code cell (click the ▶ play button to its left, or press `Shift+Enter`). VS Code may prompt you to install the `ipykernel` package the first time — click **Install** and wait for it to finish.
7. Continue running cells top to bottom with `Shift+Enter` to work through the lab.


## 7. Getting new files each class, without conflicts

Before each class, your instructor may add new files to the repo (new labs, or solutions to a previous lab). You'll grab these with `git pull`, run from inside your repo folder:

```
git pull
```

For this to always work cleanly, **never edit the starter file itself.** Instead:

1. When a new lab file appears (e.g. `labXX-X_XXX_YOURSMITHLOGIN.ipynb`), make your own copy in the same folder, renamed with your Smith login, e.g. `labXX-X_XXX_jpark03.ipynb`.
2. Do all your work in your renamed copy. Leave the original `labXX-X_XXX_YOURSMITHLOGIN.ipynb` alone.

Because your renamed copy doesn't match any filename in the instructor's repo, `git pull` will never touch it — no matter what the instructor pushes later (including a `labXX-X_XXX_solutions.ipynb` file after class). This means `git pull` should always succeed with no extra steps.

