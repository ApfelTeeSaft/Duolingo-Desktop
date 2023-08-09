from cx_Freeze import setup, Executable

setup(
    name="Duolingo Desktop",
    version="1.0",
    description="A Desktop Embed of Duolingo",
    executables=[Executable("DL-GUI.py", icon="icon.ico")]
)