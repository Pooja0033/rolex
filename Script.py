class script(object):
    START_TXT = """đ·đŽđ»đŸ {},
đŒđ đœđ°đŒđŽ đžđ <a href=https://t.me/{}>{}</a>, đž đČđ°đœ đżđđŸđđžđłđŽ đŒđŸđđžđŽđ, đčđđđ đ°đłđł đŒđŽ đđŸ đđŸđđ đ¶đđŸđđż đ°đœđł đŽđœđčđŸđ đ"""
    HELP_TXT = """đ·đŽđ {}
đ·đŽđđŽ đžđ đđ·đŽ đ·đŽđ»đż đ”đŸđ đŒđ đČđŸđŒđŒđ°đœđłđ."""
    ABOUT_TXT = """
đ§đđđŠ  đ đŠđ
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
ââââââ° êȘá„êȘźêȘđœ êȘđŽá§ â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ âáŽÊ ÉŽáŽáŽáŽ   - {}
ââŁâȘŒ đđ đđđ đđĄ  - <a href="https://t.me/KL_2335"> Prv </a>
ââŁâȘŒ đČđđŽđ°đđŸđ    - <a href="https://t.me/Prv_35"> KMTZ </a>
ââŁâȘŒ đđ„đąđšđŁ  âŸ <a href="https://t.me/kmtz_v3"> KMTZ GP1ïžâŁ </a>
ââŁâȘŒ đđ„đąđšđŁ  âŸ <a href="https://t.me/kmtz_v4"> KMTZ GP2ïžâŁ </a>
ââŁâȘŒ đđ„đąđšđŁ  âŸ <a href="https://t.me/kmtz_v5"> KMTZ GP3ïžâŁ </a>
ââŁâȘŒ đđ”đźđ»đ»đČđč  âŸ <a href="https://t.me/kmtz_channel_v3"> đđ đ§đ­ đđ”đźđ»đ»đČđč </a>
ââŁâȘŒ âđ»đžđ±đđ°đđ - đđ đ§đ­ đđđđ„đđ„đŹ
ââŁâȘŒ âđ»đ°đœđ¶đđ°đ¶đŽ - đ đđĄđđđđŠđ
ââŁâȘŒ âđ±đŸđ đđŽđđđŽđ - đšđ
ââ°ââââââââââââââââŁ âââââââââââââââââââââ±âÛȘÛȘ"""
    SOURCE_TXT = """<b>đżđđžđđ°đđŽ đ±đŸđ đ”đŸđ đđŸđ</b>

<b>âșâș đłđŸ đđŸđ đđ°đœđ đ° đ±đŸđ đđ°đŒđŽ đ»đžđșđŽ đđ·đžđ</b>

<b>âșâș đđžđđ· đ°đ»đ» đđŸđđ đČđđŽđłđžđđ</b>

<b>âșâș đđžđđ· đđŸđđ đŸđđœđŽđđđ·đžđż</b>

<b>âșâș đČđŸđœđđ°đČđ đŒđŽ <a href=https://t.me/KL_2335> đđđ </a></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Prv should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âą /filter - <code>add a filter in chat</code>
âą /filters - <code>list all the filters of a chat</code>
âą /del - <code>delete a specific filter in chat</code>
âą /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Prv Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Prv_35Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âą /connect  - <code>connect a particular chat to your PM</code>
âą /disconnect  - <code>disconnect from a chat</code>
âą /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features Prv

<b>Commands and Usage:</b>
âą /id - <code>get id of a specified user.</code>
âą /info  - <code>get information about a user.</code>
âą /imdb  - <code>get the film information from IMDb source.</code>
âą /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âą /logs - <code>to get the rescent errors</code>
âą /stats - <code>to get status of files in db.</code>
âą /delete - <code>to delete a specific file from db.</code>
âą /users - <code>to get list of my users and ids.</code>
âą /chats - <code>to get list of the my chats and ids </code>
âą /leave  - <code>to leave from a chat.</code>
âą /disable  -  <code>do disable a chat.</code>
âą /ban  - <code>to ban a user.</code>
âą /unban  - <code>to unban a user.</code>
âą /channel - <code>to get list of total connected channels</code>
âą /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â đđŸđđ°đ» đ”đžđ»đŽđ: <code>{}</code>
â đđŸđđ°đ» đđđŽđđ: <code>{}</code>
â đđŸđđ°đ» đČđ·đ°đđ: <code>{}</code>
â đđđŽđł đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±
â đ”đđŽđŽ đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
