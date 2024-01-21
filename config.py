import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29250051")) #optional
API_HASH = getenv("API_HASH", "5a8e5c861695595f38ec59b6e0a0f6cc") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6155567796").split()))
OWNER_ID = int(getenv("5366891026"))
MONGO_URL = getenv("mongodb+srv://Jatin:Jatin@cluster0.zdkvzab.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6444309600:AAGM2jtq4LRkNrN7xv_m_c7GAxe83F9pUuo")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/d735867c2930509c1283b.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMxLIGIT/Ligit-Userbot")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQHH73AARZJ4Lst76qYuhbYvHGSTK2p_YpM-4C-Q2Xi4giBlVSgtRlj1IpE8xMPooL6YQpepPP0PV-ES7fIGSu9Bc7kyNCxkFm8Yqdff1F7yQprzEPgdG3sZgJBT-lkWtoliAdB6EDk44MIbeDcpjOBCJIvi02mNHevxFNVLiLQpGoOJsbkuQqG8fqgkOxz3wIXMcbGVstwWlymVPA-bTwPur3Kow1JMVJPq4pVgxpVTtsVBFXJD-PztCIB9cH1GrjM9j_KBDAwWsgmlmgj6_Jav3Vsa0trNWniXj7JnxaSl3CmQtGmh0x1WecANAP9aBOX3oc8VQSH6BceX3fSGPc6yWHIFqQAAAAFu5oK0AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
