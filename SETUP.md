# Toolkit Setup Guide

Regent University College, Accra, Ghana

This guide walks you through installing the tools you need to work with the
Python teaching examples in this repository:

1. **Python** — to run the scripts
2. **Git** — to download (clone) and manage the repository
3. **Visual Studio Code (VS Code)** — a code editor
4. **Python extension for VS Code** — to run and debug Python from the editor

Work through the steps in order. If you already have a tool installed, you
can skip that step.

---

## 1. Install Python

Python is the programming language used for all the scripts in this
repository.

### Windows

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the yellow **Download Python 3.x** button (the latest stable version).
3. Run the installer you downloaded.
4. **Important:** Check the box that says **Add Python to PATH** before
   clicking Install.
5. Click **Install Now** and wait for the installation to finish.
6. Click **Close**.

### macOS

macOS comes with an older version of Python. We recommend installing the
latest version from python.org:

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the yellow **Download Python 3.x** button for macOS.
3. Open the downloaded `.pkg` file and follow the installation steps.

Alternatively, if you use [Homebrew](https://brew.sh/):

```bash
brew install python
```

### Linux

Most Linux distributions come with Python 3 pre-installed. Check your
version:

```bash
python3 --version
```

If Python 3 is not installed, or you want a newer version:

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3
```

### Verify the installation

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS
and Linux) and run:

```bash
python3 --version
# or on Windows:
python --version
```

You should see something like `Python 3.14.x`.

Also verify `pip` (Python's package installer) is available:

```bash
python3 -m pip --version
```

---

## 2. Install Git

Git is a version-control tool. We use it to download ("clone") this
repository and to track changes.

### Windows

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download and run the installer.
3. Keep the default options during installation and click **Next** through
   the wizard.
4. When finished, click **Finish**.
5. Restart your terminal so the `git` command is available.

### macOS

If you have the Xcode Command Line Tools installed, Git is already available.
If not, install it:

```bash
xcode-select --install
```

Or download the installer from [https://git-scm.com/download/mac](https://git-scm.com/download/mac).

### Linux

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install git
```

**Fedora:**
```bash
sudo dnf install git
```

### Verify the installation

Open a terminal and run:

```bash
git --version
```

You should see something like `git version 2.x.x`.

---

## 3. Clone this Repository

Cloning downloads a copy of the repository to your computer so you can run
and edit the scripts locally.

### Step 1: Get the repository URL

The repository URL is the web address of this Git repository (for example,
`https://github.com/<your-username>/python-teaching.git`).

### Step 2: Clone it

Open a terminal and run:

```bash
git clone <REPOSITORY_URL>
```

Replace `<REPOSITORY_URL>` with the actual URL of this repository. For
example:

```bash
git clone https://github.com/your-username/python-teaching.git
```

This creates a new folder called `python-teaching/` containing all the
scripts and lecture materials.

### Step 3: Enter the folder

```bash
cd python-teaching
```

You are now inside the repository. You can run any script from here:

```bash
python3 01_intro_basics/hello_addition.py
```

---

## 4. Install Visual Studio Code (VS Code)

VS Code is a free code editor that makes it easy to write, run, and debug
Python code.

### Windows

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click **Download for Windows**.
3. Run the downloaded `.exe` installer.
4. Accept the license agreement and click through the wizard.
5. We recommend checking **Add to PATH** and **Register as an editor for
   supported file types**.
6. Click **Install**, then **Finish**.

### macOS

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click **Download for Mac**.
3. Open the downloaded `.zip` file and drag **Visual Studio Code.app** into
   your **Applications** folder.

### Linux

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt install code
```

Or download the `.deb` package from
[https://code.visualstudio.com/](https://code.visualstudio.com/) and install it.

### Verify the installation

Open VS Code by typing:

```bash
code
```

or launch it from your applications menu.

---

## 5. Install the Python Extension in VS Code

The Python extension adds IntelliSense (code completion), linting, debugging,
and the ability to run Python files directly from VS Code.

### Step 1: Open VS Code

Launch VS Code from your applications menu or by typing `code` in a terminal.

### Step 2: Open the Extensions view

Click the **Extensions** icon on the left sidebar (it looks like four
squares, one slightly detached), or press:

* **Windows/Linux:** `Ctrl + Shift + X`
* **macOS:** `Cmd + Shift + X`

### Step 3: Install the Python extension

1. In the search box at the top of the Extensions view, type **Python**.
2. Look for the extension published by **Microsoft** (it is usually the top
   result and has millions of downloads).
3. Click the **Install** button.

### Step 4: Select a Python interpreter

1. Open any `.py` file from this repository in VS Code.
2. In the bottom-right corner, VS Code will show a Python version (for
   example `Python 3.14.x`). Click it if you want to choose a different
   interpreter.
3. Alternatively, press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS),
   type **Python: Select Interpreter**, and choose the Python 3 version you
   installed.

### Step 5: Run a script

1. Open a script, for example `01_intro_basics/hello_addition.py`.
2. Click the **Run** button (play triangle) in the top-right corner of the
   editor, or press **F5**.
3. The output appears in the terminal panel at the bottom of VS Code.

---

## 6. Quick Checklist

Make sure everything is working:

| Tool | Command | What you should see |
|------|---------|---------------------|
| Python | `python3 --version` | `Python 3.x.x` |
| Git | `git --version` | `git version 2.x.x` |
| VS Code | `code` | VS Code window opens |
| Repo | `ls` inside `python-teaching/` | Folders like `01_intro_basics/`, `02_data_structures/`, etc. |

---

## 7. Troubleshooting

**"python" is not recognized (Windows)**

* Re-run the Python installer and make sure **Add Python to PATH** is checked.
* Or use `python3` instead of `python` in commands.

**"git" is not recognized**

* Re-run the Git installer and restart your terminal.
* On Windows, make sure you selected the option to use Git from the command
  prompt during installation.

**Cannot run `.py` files in VS Code**

* Make sure you installed the **Python** extension from Microsoft.
* Make sure you selected a Python interpreter (Step 4 above).

**Permission denied when running scripts (Linux/macOS)**

* You do not need to make `.py` files executable. Always run them with
  `python3 filename.py`, not `./filename.py`.

---

## Next Steps

Once your toolkit is set up, work through the folders in order:

1. `01_intro_basics/` — variables, arithmetic, input, conditionals
2. `02_data_structures/` — lists and dictionaries
3. `03_functions/` — defining and calling functions
4. `04_object_oriented/` — classes, inheritance, polymorphism, encapsulation
5. `05_applications_electronics/` — real-world electronics applications

See **USAGE.md** for more details on how to run the scripts and how the
repository is organized.
