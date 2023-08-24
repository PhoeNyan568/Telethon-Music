import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6413040986:AAENMMywWgeBJyAHZwuYkn0Zk_L1WJprGlw)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIEBuyrZ9UqpTZRW_Ssk2phOCgXqXGZ2D3JnpcIHXyybqXzVVkFY2oldIX_jQjfRSlDKMK7VN0kU9xAGJz_m2vM6O6hSuZt0mqcb3GPnSD61axIiYus5Gq8wkLyTTPAeFwmjLNixGNNG0dTlbGQwwvWQGLbGBWz6PPRgQRg1DG91g6tZci45v9DSsNEM2F4UvAgdtGt6OINXxOFkAme3wvIzjg5Mwm0hEpOgejdqF_otYG_-L6lqFGTNslnUM8vyfejp4B4WZkYJdMAil90rcL393J2CIuZJquuKypUtUXe3L9VzGBx1hNd9UIAO-Szb7xyMZTI5ZbasuMIAxcvRFUW-Um4=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
