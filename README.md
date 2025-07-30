# LogoSign 🖋️

**LogoSign** is a Django app that prints an ASCII logo or custom banner when your app starts. It supports common run modes like `runserver`, `gunicorn`, `uwsgi`, and others. This adds a personal or professional touch to your Django project's startup process.

---

## 🔧 Installation

Install the package via `pip`:

```bash
pip install logosign
```

Or directly from the source:

```bash
pip install git+https://github.com/yourusername/logosign.git
```

---

## ⚙️ Configuration

### 1. Add to Installed Apps

In your Django `settings.py`, add `logosign` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # ...
    "logosign",
]
```

### 2. Add a Logo in Project

Add a Logo File ex:(logo.png) in your project:


### 3. Set Variables in settings.py

You can configure optional settings in your `settings.py`:

```python
LOGOSIGN_WIDTH = 60 #as width of ascii logo 
LOGOSIGN_FILENAME = "logo.png" #path and name of your logo
```

These settings are optional. If not provided, the default behavior will be used.

---


## ✅ Example Output

```txt
   __          __  _                            
   \ \        / / | |                           
    \ \  /\  / /__| | ___ ___  _ __ ___   ___   
     \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \  
      \  /\  /  __/ | (_| (_) | | | | | |  __/  
       \/  \/ \___|_|\___\___/|_| |_| |_|\___|  
```

```txt
██████╗  █████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██████╔╝███████║██████╔╝ ╚████╔╝ 
██╔═══╝ ██╔══██║██╔═══╝   ╚██╔╝  
██║     ██║  ██║██║        ██║   
╚═╝     ╚═╝  ╚═╝╚═╝        ╚═╝   
```
---

## 🙋‍♂️ Author

**Amirhosein Vali**  
📧 [amirhosein.vali@yahoo.com](mailto:amirhosein.vali@yahoo.com)

---

## 📃 License

MIT License – Feel free to use, modify, and distribute.
