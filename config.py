# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22561857")

API_HASH = os.environ.get("API_HASH", "6581d3daf4b40f722a22ddb5ca1281c2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6470850974:AAGP24ngL7AwmmdqdkJUDnTxURw0mWg8J_4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "MAPOriginal") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://zishankhan1:zishankhan1@cluster0.pnwq7om.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '684727861').split()]

PORT = os.environ.get("PORT", "1414")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
