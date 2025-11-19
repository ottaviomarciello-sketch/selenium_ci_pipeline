C:\Users\ottav\PyCharmMiscProject\.venv\Scripts\python.exe C:\Users\ottav\PyCharmMiscProject\wikipedia_python.py 
Esecuzione test Selenium: 2025-11-19 19:32:10.572770
Traceback (most recent call last):
  File "C:\Users\ottav\PyCharmMiscProject\.venv\Lib\site-packages\selenium\webdriver\common\driver_finder.py", line 64, in _binary_paths
    raise ValueError(f"The path is not a valid file: {path}")
ValueError: The path is not a valid file: /usr/bin/chromedriver

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\ottav\PyCharmMiscProject\wikipedia_python.py", line 61, in <module>
    run_selenium_test()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\ottav\PyCharmMiscProject\wikipedia_python.py", line 30, in run_selenium_test
    driver = webdriver.Chrome(
        service=Service("/usr/bin/chromedriver"),
        options=options
    )
  File "C:\Users\ottav\PyCharmMiscProject\.venv\Lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 45, in __init__
    super().__init__(
    ~~~~~~~~~~~~~~~~^
        browser_name=DesiredCapabilities.CHROME["browserName"],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
        keep_alive=keep_alive,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\ottav\PyCharmMiscProject\.venv\Lib\site-packages\selenium\webdriver\chromium\webdriver.py", line 50, in __init__
    if finder.get_browser_path():
       ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\ottav\PyCharmMiscProject\.venv\Lib\site-packages\selenium\webdriver\common\driver_finder.py", line 47, in get_browser_path
    return self._binary_paths()["browser_path"]
           ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\ottav\PyCharmMiscProject\.venv\Lib\site-packages\selenium\webdriver\common\driver_finder.py", line 78, in _binary_paths
    raise NoSuchDriverException(msg) from err
selenium.common.exceptions.NoSuchDriverException: Message: Unable to obtain driver for chrome; For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location


Process finished with exit code 1
