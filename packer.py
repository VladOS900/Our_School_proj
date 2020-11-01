from cx_Freeze import setup, Executable

executables = [Executable('Qt.py',
                          targetName='PandaScript',
                          base='Win32GUI',
                          icon='icon.ico')]

includes = ['PyQt5', 'os', 'sys', 'tkinter', 'copy', 'PIL']

zip_include_packages = ['PyQt5', 'os', 'sys', 'tkinter', 'copy', 'PIL']

include_files = ['Working_with_saved_files.py', 'Calculator.py', 'Blueprinter.py', 'Turtle.py',
                 'Fileik.py', 'Photoedit.py', 'documentation', 'icon.ico', 'loading.gif', 'panda.jpg', 'resized.gif',
                 'text0', 'text1', 'text2', 'text3', 'text4', 'text5']

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
        'excludes': ['mpl_toolkits']
    }
}

setup(name='Qt.py',
      version='0.0.1',
      description='PandaScript',
      executables=executables,
      options=options)
