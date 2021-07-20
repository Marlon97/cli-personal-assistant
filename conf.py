def config_env_file(MY_MAIL, WEBDRIVERPATH, BIG_TIME_USER, BIG_TIME_PASSWORD):
    env_file = open(".env","w")
    env_file.write(f"MY_MAIL = '{MY_MAIL}'\n")
    env_file.write(f"WEBDRIVERPATH = '{WEBDRIVERPATH}'\n")
    env_file.write(f"BIG_TIME_USER = '{BIG_TIME_USER}'\n")
    env_file.write(f"BIG_TIME_PASSWORD = '{BIG_TIME_PASSWORD}'")
    env_file.close()
