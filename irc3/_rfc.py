
class retcode(int):
    name = None
    re = None

RPL_TRACELINK = retcode(200)
RPL_TRACELINK.name = "RPL_TRACELINK"
RPL_TRACELINK.re = (
    "^:(?P<srv>\S+) 200 (?P<me>\S+) "
    "(?P<next_server>\S+)")
RPL_TRACELINK.params = ['srv', 'me', 'next_server']

RPL_TRACECONNECTING = retcode(201)
RPL_TRACECONNECTING.name = "RPL_TRACECONNECTING"
RPL_TRACECONNECTING.re = (
    "^:(?P<srv>\S+) 201 (?P<me>\S+) "
    "Try. (?P<class>\S+) "
    "(?P<server>\S+)")
RPL_TRACECONNECTING.params = ['srv', 'me', 'class', 'server']

RPL_TRACEHANDSHAKE = retcode(202)
RPL_TRACEHANDSHAKE.name = "RPL_TRACEHANDSHAKE"
RPL_TRACEHANDSHAKE.re = (
    "^:(?P<srv>\S+) 202 (?P<me>\S+) "
    "H.S. (?P<class>\S+) "
    "(?P<server>\S+)")
RPL_TRACEHANDSHAKE.params = ['srv', 'me', 'class', 'server']

RPL_TRACEUNKNOWN = retcode(203)
RPL_TRACEUNKNOWN.name = "RPL_TRACEUNKNOWN"
RPL_TRACEUNKNOWN.re = (
    "^:(?P<srv>\S+) 203 (?P<me>\S+) "
    "???? (?P<class>\S+) [(?P<clientip>\S+)]")
RPL_TRACEUNKNOWN.params = ['srv', 'me', 'class', 'clientip']

RPL_TRACEOPERATOR = retcode(204)
RPL_TRACEOPERATOR.name = "RPL_TRACEOPERATOR"
RPL_TRACEOPERATOR.re = (
    "^:(?P<srv>\S+) 204 (?P<me>\S+) "
    "Oper (?P<class>\S+) (?P<nick>\S+)")
RPL_TRACEOPERATOR.params = ['srv', 'me', 'class', 'nick']

RPL_TRACEUSER = retcode(205)
RPL_TRACEUSER.name = "RPL_TRACEUSER"
RPL_TRACEUSER.re = (
    "^:(?P<srv>\S+) 205 (?P<me>\S+) "
    "User (?P<class>\S+) (?P<nick>\S+)")
RPL_TRACEUSER.params = ['srv', 'me', 'class', 'nick']

RPL_TRACESERVER = retcode(206)
RPL_TRACESERVER.name = "RPL_TRACESERVER"
RPL_TRACESERVER.re = (
    "^:(?P<srv>\S+) 206 (?P<me>\S+) "
    "(?P<mask>\S+)")
RPL_TRACESERVER.params = ['srv', 'me', 'mask']

RPL_TRACENEWTYPE = retcode(208)
RPL_TRACENEWTYPE.name = "RPL_TRACENEWTYPE"
RPL_TRACENEWTYPE.re = (
    "^:(?P<srv>\S+) 208 (?P<me>\S+) "
    "(?P<newtype>\S+) 0 (?P<client>\S+)")
RPL_TRACENEWTYPE.params = ['srv', 'me', 'newtype', 'client']

RPL_STATSLINKINFO = retcode(211)
RPL_STATSLINKINFO.name = "RPL_STATSLINKINFO"
RPL_STATSLINKINFO.re = (
    "^:(?P<srv>\S+) 211 (?P<me>\S+) "
    "(?P<linkname>\S+) (?P<sendq>\S+) "
    "(?P<sent_messages>\S+) (?P<received_bytes>\S+) (?P<time_open>\S+)")
RPL_STATSLINKINFO.params = [
    'srv',
    'me',
    'linkname',
    'sendq',
    'sent_messages',
    'received_bytes',
    'time_open']

RPL_STATSCOMMANDS = retcode(212)
RPL_STATSCOMMANDS.name = "RPL_STATSCOMMANDS"
RPL_STATSCOMMANDS.re = (
    "^:(?P<srv>\S+) 212 (?P<me>\S+) "
    "(?P<command>\S+) (?P<count>\S+)")
RPL_STATSCOMMANDS.params = ['srv', 'me', 'command', 'count']

RPL_STATSCLINE = retcode(213)
RPL_STATSCLINE.name = "RPL_STATSCLINE"
RPL_STATSCLINE.re = (
    "^:(?P<srv>\S+) 213 (?P<me>\S+) "
    "C (?P<host>\S+) * (?P<name>\S+) (?P<port>\S+) (?P<class>\S+)")
RPL_STATSCLINE.params = ['srv', 'me', 'host', 'name', 'port', 'class']

RPL_STATSNLINE = retcode(214)
RPL_STATSNLINE.name = "RPL_STATSNLINE"
RPL_STATSNLINE.re = (
    "^:(?P<srv>\S+) 214 (?P<me>\S+) "
    "N (?P<host>\S+) * (?P<name>\S+) (?P<port>\S+) (?P<class>\S+)")
RPL_STATSNLINE.params = ['srv', 'me', 'host', 'name', 'port', 'class']

RPL_STATSILINE = retcode(215)
RPL_STATSILINE.name = "RPL_STATSILINE"
RPL_STATSILINE.re = (
    "^:(?P<srv>\S+) 215 (?P<me>\S+) "
    "I (?P<host>\S+) * (?P<host>\S+) (?P<port>\S+) (?P<class>\S+)")
RPL_STATSILINE.params = ['srv', 'me', 'host', 'host', 'port', 'class']

RPL_STATSKLINE = retcode(216)
RPL_STATSKLINE.name = "RPL_STATSKLINE"
RPL_STATSKLINE.re = (
    "^:(?P<srv>\S+) 216 (?P<me>\S+) "
    "K (?P<host>\S+) * (?P<username>\S+) (?P<port>\S+) (?P<class>\S+)")
RPL_STATSKLINE.params = ['srv', 'me', 'host', 'username', 'port', 'class']

RPL_STATSYLINE = retcode(218)
RPL_STATSYLINE.name = "RPL_STATSYLINE"
RPL_STATSYLINE.re = (
    "^:(?P<srv>\S+) 218 (?P<me>\S+) "
    "frequency> (?P<max_sendq>\S+)")
RPL_STATSYLINE.params = ['srv', 'me', 'max_sendq']

RPL_ENDOFSTATS = retcode(219)
RPL_ENDOFSTATS.name = "RPL_ENDOFSTATS"
RPL_ENDOFSTATS.re = (
    "^:(?P<srv>\S+) 219 (?P<me>\S+) "
    "(?P<stats_letter>\S+) :(?P<data>.*)")
RPL_ENDOFSTATS.params = ['srv', 'me', 'stats_letter', 'data']

RPL_UMODEIS = retcode(221)
RPL_UMODEIS.name = "RPL_UMODEIS"
RPL_UMODEIS.re = (
    "^:(?P<srv>\S+) 221 (?P<me>\S+) "
    "(?P<user_mode_string>\S+)")
RPL_UMODEIS.params = ['srv', 'me', 'user_mode_string']

RPL_STATSLLINE = retcode(241)
RPL_STATSLLINE.name = "RPL_STATSLLINE"
RPL_STATSLLINE.re = (
    "^:(?P<srv>\S+) 241 (?P<me>\S+) "
    "L (?P<hostmask>\S+) * (?P<servername>\S+) (?P<maxdepth>\S+)")
RPL_STATSLLINE.params = ['srv', 'me', 'hostmask', 'servername', 'maxdepth']

RPL_STATSUPTIME = retcode(242)
RPL_STATSUPTIME.name = "RPL_STATSUPTIME"
RPL_STATSUPTIME.re = (
    "^:(?P<srv>\S+) 242 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_STATSUPTIME.params = ['srv', 'me', 'data']

RPL_STATSOLINE = retcode(243)
RPL_STATSOLINE.name = "RPL_STATSOLINE"
RPL_STATSOLINE.re = (
    "^:(?P<srv>\S+) 243 (?P<me>\S+) "
    "O (?P<hostmask>\S+) * (?P<name>\S+)")
RPL_STATSOLINE.params = ['srv', 'me', 'hostmask', 'name']

RPL_STATSHLINE = retcode(244)
RPL_STATSHLINE.name = "RPL_STATSHLINE"
RPL_STATSHLINE.re = (
    "^:(?P<srv>\S+) 244 (?P<me>\S+) "
    "H (?P<hostmask>\S+) * (?P<servername>\S+)")
RPL_STATSHLINE.params = ['srv', 'me', 'hostmask', 'servername']

RPL_LUSERCLIENT = retcode(251)
RPL_LUSERCLIENT.name = "RPL_LUSERCLIENT"
RPL_LUSERCLIENT.re = (
    "^:(?P<srv>\S+) 251 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_LUSERCLIENT.params = ['srv', 'me', 'data']

RPL_LUSEROP = retcode(252)
RPL_LUSEROP.name = "RPL_LUSEROP"
RPL_LUSEROP.re = (
    "^:(?P<srv>\S+) 252 (?P<me>\S+) "
    "(?P<integer>\S+) :(?P<data>.*)")
RPL_LUSEROP.params = ['srv', 'me', 'integer', 'data']

RPL_LUSERUNKNOWN = retcode(253)
RPL_LUSERUNKNOWN.name = "RPL_LUSERUNKNOWN"
RPL_LUSERUNKNOWN.re = (
    "^:(?P<srv>\S+) 253 (?P<me>\S+) "
    "(?P<integer>\S+) :(?P<data>.*)")
RPL_LUSERUNKNOWN.params = ['srv', 'me', 'integer', 'data']

RPL_LUSERCHANNELS = retcode(254)
RPL_LUSERCHANNELS.name = "RPL_LUSERCHANNELS"
RPL_LUSERCHANNELS.re = (
    "^:(?P<srv>\S+) 254 (?P<me>\S+) "
    "(?P<integer>\S+) :(?P<data>.*)")
RPL_LUSERCHANNELS.params = ['srv', 'me', 'integer', 'data']

RPL_LUSERME = retcode(255)
RPL_LUSERME.name = "RPL_LUSERME"
RPL_LUSERME.re = (
    "^:(?P<srv>\S+) 255 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_LUSERME.params = ['srv', 'me', 'data']

RPL_ADMINME = retcode(256)
RPL_ADMINME.name = "RPL_ADMINME"
RPL_ADMINME.re = (
    "^:(?P<srv>\S+) 256 (?P<me>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
RPL_ADMINME.params = ['srv', 'me', 'server', 'data']

RPL_ADMINLOC1 = retcode(257)
RPL_ADMINLOC1.name = "RPL_ADMINLOC1"
RPL_ADMINLOC1.re = (
    "^:(?P<srv>\S+) 257 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ADMINLOC1.params = ['srv', 'me', 'data']

RPL_ADMINLOC2 = retcode(258)
RPL_ADMINLOC2.name = "RPL_ADMINLOC2"
RPL_ADMINLOC2.re = (
    "^:(?P<srv>\S+) 258 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ADMINLOC2.params = ['srv', 'me', 'data']

RPL_ADMINEMAIL = retcode(259)
RPL_ADMINEMAIL.name = "RPL_ADMINEMAIL"
RPL_ADMINEMAIL.re = (
    "^:(?P<srv>\S+) 259 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ADMINEMAIL.params = ['srv', 'me', 'data']

RPL_TRACELOG = retcode(261)
RPL_TRACELOG.name = "RPL_TRACELOG"
RPL_TRACELOG.re = (
    "^:(?P<srv>\S+) 261 (?P<me>\S+) "
    "File (?P<logfile>\S+) (?P<debug_level>\S+)")
RPL_TRACELOG.params = ['srv', 'me', 'logfile', 'debug_level']

RPL_AWAY = retcode(301)
RPL_AWAY.name = "RPL_AWAY"
RPL_AWAY.re = (
    "^:(?P<srv>\S+) 301 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
RPL_AWAY.params = ['srv', 'me', 'nick', 'data']

RPL_USERHOST = retcode(302)
RPL_USERHOST.name = "RPL_USERHOST"
RPL_USERHOST.re = (
    "^:(?P<srv>\S+) 302 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_USERHOST.params = ['srv', 'me', 'data']

RPL_ISON = retcode(303)
RPL_ISON.name = "RPL_ISON"
RPL_ISON.re = (
    "^:(?P<srv>\S+) 303 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ISON.params = ['srv', 'me', 'data']

RPL_UNAWAY = retcode(305)
RPL_UNAWAY.name = "RPL_UNAWAY"
RPL_UNAWAY.re = (
    "^:(?P<srv>\S+) 305 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_UNAWAY.params = ['srv', 'me', 'data']

RPL_NOWAWAY = retcode(306)
RPL_NOWAWAY.name = "RPL_NOWAWAY"
RPL_NOWAWAY.re = (
    "^:(?P<srv>\S+) 306 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_NOWAWAY.params = ['srv', 'me', 'data']

RPL_WHOISUSER = retcode(311)
RPL_WHOISUSER.name = "RPL_WHOISUSER"
RPL_WHOISUSER.re = (
    "^:(?P<srv>\S+) 311 (?P<me>\S+) "
    "(?P<nick>\S+) (?P<user>\S+) (?P<host>\S+) * :(?P<data>.*)")
RPL_WHOISUSER.params = ['srv', 'me', 'nick', 'user', 'host', 'data']

RPL_WHOISSERVER = retcode(312)
RPL_WHOISSERVER.name = "RPL_WHOISSERVER"
RPL_WHOISSERVER.re = (
    "^:(?P<srv>\S+) 312 (?P<me>\S+) "
    "(?P<nick>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
RPL_WHOISSERVER.params = ['srv', 'me', 'nick', 'server', 'data']

RPL_WHOISOPERATOR = retcode(313)
RPL_WHOISOPERATOR.name = "RPL_WHOISOPERATOR"
RPL_WHOISOPERATOR.re = (
    "^:(?P<srv>\S+) 313 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
RPL_WHOISOPERATOR.params = ['srv', 'me', 'nick', 'data']

RPL_WHOWASUSER = retcode(314)
RPL_WHOWASUSER.name = "RPL_WHOWASUSER"
RPL_WHOWASUSER.re = (
    "^:(?P<srv>\S+) 314 (?P<me>\S+) "
    "(?P<nick>\S+) (?P<user>\S+) (?P<host>\S+) * :(?P<data>.*)")
RPL_WHOWASUSER.params = ['srv', 'me', 'nick', 'user', 'host', 'data']

RPL_ENDOFWHO = retcode(315)
RPL_ENDOFWHO.name = "RPL_ENDOFWHO"
RPL_ENDOFWHO.re = (
    "^:(?P<srv>\S+) 315 (?P<me>\S+) "
    "(?P<name>\S+) :(?P<data>.*)")
RPL_ENDOFWHO.params = ['srv', 'me', 'name', 'data']

RPL_WHOISIDLE = retcode(317)
RPL_WHOISIDLE.name = "RPL_WHOISIDLE"
RPL_WHOISIDLE.re = (
    "^:(?P<srv>\S+) 317 (?P<me>\S+) "
    "(?P<nick>\S+) (?P<integer>\S+) :(?P<data>.*)")
RPL_WHOISIDLE.params = ['srv', 'me', 'nick', 'integer', 'data']

RPL_ENDOFWHOIS = retcode(318)
RPL_ENDOFWHOIS.name = "RPL_ENDOFWHOIS"
RPL_ENDOFWHOIS.re = (
    "^:(?P<srv>\S+) 318 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
RPL_ENDOFWHOIS.params = ['srv', 'me', 'nick', 'data']

RPL_WHOISCHANNELS = retcode(319)
RPL_WHOISCHANNELS.name = "RPL_WHOISCHANNELS"
RPL_WHOISCHANNELS.re = (
    "^:(?P<srv>\S+) 319 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
RPL_WHOISCHANNELS.params = ['srv', 'me', 'nick', 'data']

RPL_LISTSTART = retcode(321)
RPL_LISTSTART.name = "RPL_LISTSTART"
RPL_LISTSTART.re = (
    "^:(?P<srv>\S+) 321 (?P<me>\S+) "
    "Channel :(?P<data>.*)")
RPL_LISTSTART.params = ['srv', 'me', 'data']

RPL_LIST = retcode(322)
RPL_LIST.name = "RPL_LIST"
RPL_LIST.re = (
    "^:(?P<srv>\S+) 322 (?P<me>\S+) "
    "(?P<channel>\S+) (?P<visible>\S+) :(?P<data>.*)")
RPL_LIST.params = ['srv', 'me', 'channel', 'visible', 'data']

RPL_LISTEND = retcode(323)
RPL_LISTEND.name = "RPL_LISTEND"
RPL_LISTEND.re = (
    "^:(?P<srv>\S+) 323 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_LISTEND.params = ['srv', 'me', 'data']

RPL_CHANNELMODEIS = retcode(324)
RPL_CHANNELMODEIS.name = "RPL_CHANNELMODEIS"
RPL_CHANNELMODEIS.re = (
    "^:(?P<srv>\S+) 324 (?P<me>\S+) "
    "(?P<channel>\S+) (?P<mode>\S+) (?P<mode_params>\S+)")
RPL_CHANNELMODEIS.params = ['srv', 'me', 'channel', 'mode', 'mode_params']

RPL_NOTOPIC = retcode(331)
RPL_NOTOPIC.name = "RPL_NOTOPIC"
RPL_NOTOPIC.re = (
    "^:(?P<srv>\S+) 331 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
RPL_NOTOPIC.params = ['srv', 'me', 'channel', 'data']

RPL_TOPIC = retcode(332)
RPL_TOPIC.name = "RPL_TOPIC"
RPL_TOPIC.re = (
    "^:(?P<srv>\S+) 332 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
RPL_TOPIC.params = ['srv', 'me', 'channel', 'data']

RPL_INVITING = retcode(341)
RPL_INVITING.name = "RPL_INVITING"
RPL_INVITING.re = (
    "^:(?P<srv>\S+) 341 (?P<me>\S+) "
    "(?P<channel>\S+) (?P<nick>\S+)")
RPL_INVITING.params = ['srv', 'me', 'channel', 'nick']

RPL_SUMMONING = retcode(342)
RPL_SUMMONING.name = "RPL_SUMMONING"
RPL_SUMMONING.re = (
    "^:(?P<srv>\S+) 342 (?P<me>\S+) "
    "(?P<user>\S+) :(?P<data>.*)")
RPL_SUMMONING.params = ['srv', 'me', 'user', 'data']

RPL_VERSION = retcode(351)
RPL_VERSION.name = "RPL_VERSION"
RPL_VERSION.re = (
    "^:(?P<srv>\S+) 351 (?P<me>\S+) "
    "(?P<version>\S+).(?P<debuglevel>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
RPL_VERSION.params = ['srv', 'me', 'version', 'debuglevel', 'server', 'data']

RPL_WHOREPLY = retcode(352)
RPL_WHOREPLY.name = "RPL_WHOREPLY"
RPL_WHOREPLY.re = (
    "^:(?P<srv>\S+) 352 (?P<me>\S+) "
    "(?P<channel>\S+) (?P<user>\S+) (?P<host>\S+) "
    "(?P<server>\S+) (?P<nick>\S+) (?P<modes>\S+) :(?P<data>.*)")
RPL_WHOREPLY.params = [
    'srv',
    'me',
    'channel',
    'user',
    'host',
    'server',
    'nick',
    'modes',
    'data']

RPL_NAMREPLY = retcode(353)
RPL_NAMREPLY.name = "RPL_NAMREPLY"
RPL_NAMREPLY.re = (
    "^:(?P<srv>\S+) 353 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
RPL_NAMREPLY.params = ['srv', 'me', 'channel', 'data']

RPL_LINKS = retcode(364)
RPL_LINKS.name = "RPL_LINKS"
RPL_LINKS.re = (
    "^:(?P<srv>\S+) 364 (?P<me>\S+) "
    "(?P<mask>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
RPL_LINKS.params = ['srv', 'me', 'mask', 'server', 'data']

RPL_ENDOFLINKS = retcode(365)
RPL_ENDOFLINKS.name = "RPL_ENDOFLINKS"
RPL_ENDOFLINKS.re = (
    "^:(?P<srv>\S+) 365 (?P<me>\S+) "
    "(?P<mask>\S+) :(?P<data>.*)")
RPL_ENDOFLINKS.params = ['srv', 'me', 'mask', 'data']

RPL_ENDOFNAMES = retcode(366)
RPL_ENDOFNAMES.name = "RPL_ENDOFNAMES"
RPL_ENDOFNAMES.re = (
    "^:(?P<srv>\S+) 366 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
RPL_ENDOFNAMES.params = ['srv', 'me', 'channel', 'data']

RPL_BANLIST = retcode(367)
RPL_BANLIST.name = "RPL_BANLIST"
RPL_BANLIST.re = (
    "^:(?P<srv>\S+) 367 (?P<me>\S+) "
    "(?P<channel>\S+) (?P<banid>\S+)")
RPL_BANLIST.params = ['srv', 'me', 'channel', 'banid']

RPL_ENDOFBANLIST = retcode(368)
RPL_ENDOFBANLIST.name = "RPL_ENDOFBANLIST"
RPL_ENDOFBANLIST.re = (
    "^:(?P<srv>\S+) 368 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
RPL_ENDOFBANLIST.params = ['srv', 'me', 'channel', 'data']

RPL_ENDOFWHOWAS = retcode(369)
RPL_ENDOFWHOWAS.name = "RPL_ENDOFWHOWAS"
RPL_ENDOFWHOWAS.re = (
    "^:(?P<srv>\S+) 369 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
RPL_ENDOFWHOWAS.params = ['srv', 'me', 'nick', 'data']

RPL_INFO = retcode(371)
RPL_INFO.name = "RPL_INFO"
RPL_INFO.re = (
    "^:(?P<srv>\S+) 371 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_INFO.params = ['srv', 'me', 'data']

RPL_MOTD = retcode(372)
RPL_MOTD.name = "RPL_MOTD"
RPL_MOTD.re = (
    "^:(?P<srv>\S+) 372 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_MOTD.params = ['srv', 'me', 'data']

RPL_ENDOFINFO = retcode(374)
RPL_ENDOFINFO.name = "RPL_ENDOFINFO"
RPL_ENDOFINFO.re = (
    "^:(?P<srv>\S+) 374 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ENDOFINFO.params = ['srv', 'me', 'data']

RPL_MOTDSTART = retcode(375)
RPL_MOTDSTART.name = "RPL_MOTDSTART"
RPL_MOTDSTART.re = (
    "^:(?P<srv>\S+) 375 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_MOTDSTART.params = ['srv', 'me', 'data']

RPL_ENDOFMOTD = retcode(376)
RPL_ENDOFMOTD.name = "RPL_ENDOFMOTD"
RPL_ENDOFMOTD.re = (
    "^:(?P<srv>\S+) 376 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ENDOFMOTD.params = ['srv', 'me', 'data']

RPL_YOUREOPER = retcode(381)
RPL_YOUREOPER.name = "RPL_YOUREOPER"
RPL_YOUREOPER.re = (
    "^:(?P<srv>\S+) 381 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_YOUREOPER.params = ['srv', 'me', 'data']

RPL_REHASHING = retcode(382)
RPL_REHASHING.name = "RPL_REHASHING"
RPL_REHASHING.re = (
    "^:(?P<srv>\S+) 382 (?P<me>\S+) "
    "(?P<config_file>\S+) :(?P<data>.*)")
RPL_REHASHING.params = ['srv', 'me', 'config_file', 'data']

RPL_TIME = retcode(391)
RPL_TIME.name = "RPL_TIME"
RPL_TIME.re = (
    "^:(?P<srv>\S+) 391 (?P<me>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
RPL_TIME.params = ['srv', 'me', 'server', 'data']

RPL_USERSSTART = retcode(392)
RPL_USERSSTART.name = "RPL_USERSSTART"
RPL_USERSSTART.re = (
    "^:(?P<srv>\S+) 392 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_USERSSTART.params = ['srv', 'me', 'data']

RPL_USERS = retcode(393)
RPL_USERS.name = "RPL_USERS"
RPL_USERS.re = (
    "^:(?P<srv>\S+) 393 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_USERS.params = ['srv', 'me', 'data']

RPL_ENDOFUSERS = retcode(394)
RPL_ENDOFUSERS.name = "RPL_ENDOFUSERS"
RPL_ENDOFUSERS.re = (
    "^:(?P<srv>\S+) 394 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_ENDOFUSERS.params = ['srv', 'me', 'data']

RPL_NOUSERS = retcode(395)
RPL_NOUSERS.name = "RPL_NOUSERS"
RPL_NOUSERS.re = (
    "^:(?P<srv>\S+) 395 (?P<me>\S+) "
    ":(?P<data>.*)")
RPL_NOUSERS.params = ['srv', 'me', 'data']

ERR_NOSUCHNICK = retcode(401)
ERR_NOSUCHNICK.name = "ERR_NOSUCHNICK"
ERR_NOSUCHNICK.re = (
    "^:(?P<srv>\S+) 401 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
ERR_NOSUCHNICK.params = ['srv', 'me', 'nick', 'data']

ERR_NOSUCHSERVER = retcode(402)
ERR_NOSUCHSERVER.name = "ERR_NOSUCHSERVER"
ERR_NOSUCHSERVER.re = (
    "^:(?P<srv>\S+) 402 (?P<me>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
ERR_NOSUCHSERVER.params = ['srv', 'me', 'server', 'data']

ERR_NOSUCHCHANNEL = retcode(403)
ERR_NOSUCHCHANNEL.name = "ERR_NOSUCHCHANNEL"
ERR_NOSUCHCHANNEL.re = (
    "^:(?P<srv>\S+) 403 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_NOSUCHCHANNEL.params = ['srv', 'me', 'channel', 'data']

ERR_CANNOTSENDTOCHAN = retcode(404)
ERR_CANNOTSENDTOCHAN.name = "ERR_CANNOTSENDTOCHAN"
ERR_CANNOTSENDTOCHAN.re = (
    "^:(?P<srv>\S+) 404 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_CANNOTSENDTOCHAN.params = ['srv', 'me', 'channel', 'data']

ERR_TOOMANYCHANNELS = retcode(405)
ERR_TOOMANYCHANNELS.name = "ERR_TOOMANYCHANNELS"
ERR_TOOMANYCHANNELS.re = (
    "^:(?P<srv>\S+) 405 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_TOOMANYCHANNELS.params = ['srv', 'me', 'channel', 'data']

ERR_WASNOSUCHNICK = retcode(406)
ERR_WASNOSUCHNICK.name = "ERR_WASNOSUCHNICK"
ERR_WASNOSUCHNICK.re = (
    "^:(?P<srv>\S+) 406 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
ERR_WASNOSUCHNICK.params = ['srv', 'me', 'nick', 'data']

ERR_TOOMANYTARGETS = retcode(407)
ERR_TOOMANYTARGETS.name = "ERR_TOOMANYTARGETS"
ERR_TOOMANYTARGETS.re = (
    "^:(?P<srv>\S+) 407 (?P<me>\S+) "
    "(?P<target>\S+) :(?P<data>.*)")
ERR_TOOMANYTARGETS.params = ['srv', 'me', 'target', 'data']

ERR_NOORIGIN = retcode(409)
ERR_NOORIGIN.name = "ERR_NOORIGIN"
ERR_NOORIGIN.re = (
    "^:(?P<srv>\S+) 409 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOORIGIN.params = ['srv', 'me', 'data']

ERR_NORECIPIENT = retcode(411)
ERR_NORECIPIENT.name = "ERR_NORECIPIENT"
ERR_NORECIPIENT.re = (
    "^:(?P<srv>\S+) 411 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NORECIPIENT.params = ['srv', 'me', 'data']

ERR_NOTEXTTOSEND = retcode(412)
ERR_NOTEXTTOSEND.name = "ERR_NOTEXTTOSEND"
ERR_NOTEXTTOSEND.re = (
    "^:(?P<srv>\S+) 412 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOTEXTTOSEND.params = ['srv', 'me', 'data']

ERR_NOTOPLEVEL = retcode(413)
ERR_NOTOPLEVEL.name = "ERR_NOTOPLEVEL"
ERR_NOTOPLEVEL.re = (
    "^:(?P<srv>\S+) 413 (?P<me>\S+) "
    "(?P<mask>\S+) :(?P<data>.*)")
ERR_NOTOPLEVEL.params = ['srv', 'me', 'mask', 'data']

ERR_WILDTOPLEVEL = retcode(414)
ERR_WILDTOPLEVEL.name = "ERR_WILDTOPLEVEL"
ERR_WILDTOPLEVEL.re = (
    "^:(?P<srv>\S+) 414 (?P<me>\S+) "
    "(?P<mask>\S+) :(?P<data>.*)")
ERR_WILDTOPLEVEL.params = ['srv', 'me', 'mask', 'data']

ERR_UNKNOWNCOMMAND = retcode(421)
ERR_UNKNOWNCOMMAND.name = "ERR_UNKNOWNCOMMAND"
ERR_UNKNOWNCOMMAND.re = (
    "^:(?P<srv>\S+) 421 (?P<me>\S+) "
    "(?P<command>\S+) :(?P<data>.*)")
ERR_UNKNOWNCOMMAND.params = ['srv', 'me', 'command', 'data']

ERR_NOMOTD = retcode(422)
ERR_NOMOTD.name = "ERR_NOMOTD"
ERR_NOMOTD.re = (
    "^:(?P<srv>\S+) 422 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOMOTD.params = ['srv', 'me', 'data']

ERR_NOADMININFO = retcode(423)
ERR_NOADMININFO.name = "ERR_NOADMININFO"
ERR_NOADMININFO.re = (
    "^:(?P<srv>\S+) 423 (?P<me>\S+) "
    "(?P<server>\S+) :(?P<data>.*)")
ERR_NOADMININFO.params = ['srv', 'me', 'server', 'data']

ERR_NONICKNAMEGIVEN = retcode(431)
ERR_NONICKNAMEGIVEN.name = "ERR_NONICKNAMEGIVEN"
ERR_NONICKNAMEGIVEN.re = (
    "^:(?P<srv>\S+) 431 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NONICKNAMEGIVEN.params = ['srv', 'me', 'data']

ERR_ERRONEUSNICKNAME = retcode(432)
ERR_ERRONEUSNICKNAME.name = "ERR_ERRONEUSNICKNAME"
ERR_ERRONEUSNICKNAME.re = (
    "^:(?P<srv>\S+) 432 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
ERR_ERRONEUSNICKNAME.params = ['srv', 'me', 'nick', 'data']

ERR_NICKNAMEINUSE = retcode(433)
ERR_NICKNAMEINUSE.name = "ERR_NICKNAMEINUSE"
ERR_NICKNAMEINUSE.re = (
    "^:(?P<srv>\S+) 433 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
ERR_NICKNAMEINUSE.params = ['srv', 'me', 'nick', 'data']

ERR_NICKCOLLISION = retcode(436)
ERR_NICKCOLLISION.name = "ERR_NICKCOLLISION"
ERR_NICKCOLLISION.re = (
    "^:(?P<srv>\S+) 436 (?P<me>\S+) "
    "(?P<nick>\S+) :(?P<data>.*)")
ERR_NICKCOLLISION.params = ['srv', 'me', 'nick', 'data']

ERR_USERNOTINCHANNEL = retcode(441)
ERR_USERNOTINCHANNEL.name = "ERR_USERNOTINCHANNEL"
ERR_USERNOTINCHANNEL.re = (
    "^:(?P<srv>\S+) 441 (?P<me>\S+) "
    "(?P<nick>\S+) (?P<channel>\S+) :(?P<data>.*)")
ERR_USERNOTINCHANNEL.params = ['srv', 'me', 'nick', 'channel', 'data']

ERR_NOTONCHANNEL = retcode(442)
ERR_NOTONCHANNEL.name = "ERR_NOTONCHANNEL"
ERR_NOTONCHANNEL.re = (
    "^:(?P<srv>\S+) 442 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_NOTONCHANNEL.params = ['srv', 'me', 'channel', 'data']

ERR_USERONCHANNEL = retcode(443)
ERR_USERONCHANNEL.name = "ERR_USERONCHANNEL"
ERR_USERONCHANNEL.re = (
    "^:(?P<srv>\S+) 443 (?P<me>\S+) "
    "(?P<user>\S+) (?P<channel>\S+) :(?P<data>.*)")
ERR_USERONCHANNEL.params = ['srv', 'me', 'user', 'channel', 'data']

ERR_NOLOGIN = retcode(444)
ERR_NOLOGIN.name = "ERR_NOLOGIN"
ERR_NOLOGIN.re = (
    "^:(?P<srv>\S+) 444 (?P<me>\S+) "
    "(?P<user>\S+) :(?P<data>.*)")
ERR_NOLOGIN.params = ['srv', 'me', 'user', 'data']

ERR_SUMMONDISABLED = retcode(445)
ERR_SUMMONDISABLED.name = "ERR_SUMMONDISABLED"
ERR_SUMMONDISABLED.re = (
    "^:(?P<srv>\S+) 445 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_SUMMONDISABLED.params = ['srv', 'me', 'data']

ERR_USERSDISABLED = retcode(446)
ERR_USERSDISABLED.name = "ERR_USERSDISABLED"
ERR_USERSDISABLED.re = (
    "^:(?P<srv>\S+) 446 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_USERSDISABLED.params = ['srv', 'me', 'data']

ERR_NOTREGISTERED = retcode(451)
ERR_NOTREGISTERED.name = "ERR_NOTREGISTERED"
ERR_NOTREGISTERED.re = (
    "^:(?P<srv>\S+) 451 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOTREGISTERED.params = ['srv', 'me', 'data']

ERR_NEEDMOREPARAMS = retcode(461)
ERR_NEEDMOREPARAMS.name = "ERR_NEEDMOREPARAMS"
ERR_NEEDMOREPARAMS.re = (
    "^:(?P<srv>\S+) 461 (?P<me>\S+) "
    "(?P<command>\S+) :(?P<data>.*)")
ERR_NEEDMOREPARAMS.params = ['srv', 'me', 'command', 'data']

ERR_ALREADYREGISTRED = retcode(462)
ERR_ALREADYREGISTRED.name = "ERR_ALREADYREGISTRED"
ERR_ALREADYREGISTRED.re = (
    "^:(?P<srv>\S+) 462 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_ALREADYREGISTRED.params = ['srv', 'me', 'data']

ERR_NOPERMFORHOST = retcode(463)
ERR_NOPERMFORHOST.name = "ERR_NOPERMFORHOST"
ERR_NOPERMFORHOST.re = (
    "^:(?P<srv>\S+) 463 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOPERMFORHOST.params = ['srv', 'me', 'data']

ERR_PASSWDMISMATCH = retcode(464)
ERR_PASSWDMISMATCH.name = "ERR_PASSWDMISMATCH"
ERR_PASSWDMISMATCH.re = (
    "^:(?P<srv>\S+) 464 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_PASSWDMISMATCH.params = ['srv', 'me', 'data']

ERR_YOUREBANNEDCREEP = retcode(465)
ERR_YOUREBANNEDCREEP.name = "ERR_YOUREBANNEDCREEP"
ERR_YOUREBANNEDCREEP.re = (
    "^:(?P<srv>\S+) 465 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_YOUREBANNEDCREEP.params = ['srv', 'me', 'data']

ERR_KEYSET = retcode(467)
ERR_KEYSET.name = "ERR_KEYSET"
ERR_KEYSET.re = (
    "^:(?P<srv>\S+) 467 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_KEYSET.params = ['srv', 'me', 'channel', 'data']

ERR_CHANNELISFULL = retcode(471)
ERR_CHANNELISFULL.name = "ERR_CHANNELISFULL"
ERR_CHANNELISFULL.re = (
    "^:(?P<srv>\S+) 471 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_CHANNELISFULL.params = ['srv', 'me', 'channel', 'data']

ERR_UNKNOWNMODE = retcode(472)
ERR_UNKNOWNMODE.name = "ERR_UNKNOWNMODE"
ERR_UNKNOWNMODE.re = (
    "^:(?P<srv>\S+) 472 (?P<me>\S+) "
    "(?P<char>\S+) :(?P<data>.*)")
ERR_UNKNOWNMODE.params = ['srv', 'me', 'char', 'data']

ERR_INVITEONLYCHAN = retcode(473)
ERR_INVITEONLYCHAN.name = "ERR_INVITEONLYCHAN"
ERR_INVITEONLYCHAN.re = (
    "^:(?P<srv>\S+) 473 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_INVITEONLYCHAN.params = ['srv', 'me', 'channel', 'data']

ERR_BANNEDFROMCHAN = retcode(474)
ERR_BANNEDFROMCHAN.name = "ERR_BANNEDFROMCHAN"
ERR_BANNEDFROMCHAN.re = (
    "^:(?P<srv>\S+) 474 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_BANNEDFROMCHAN.params = ['srv', 'me', 'channel', 'data']

ERR_BADCHANNELKEY = retcode(475)
ERR_BADCHANNELKEY.name = "ERR_BADCHANNELKEY"
ERR_BADCHANNELKEY.re = (
    "^:(?P<srv>\S+) 475 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_BADCHANNELKEY.params = ['srv', 'me', 'channel', 'data']

ERR_NOPRIVILEGES = retcode(481)
ERR_NOPRIVILEGES.name = "ERR_NOPRIVILEGES"
ERR_NOPRIVILEGES.re = (
    "^:(?P<srv>\S+) 481 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOPRIVILEGES.params = ['srv', 'me', 'data']

ERR_CHANOPRIVSNEEDED = retcode(482)
ERR_CHANOPRIVSNEEDED.name = "ERR_CHANOPRIVSNEEDED"
ERR_CHANOPRIVSNEEDED.re = (
    "^:(?P<srv>\S+) 482 (?P<me>\S+) "
    "(?P<channel>\S+) :(?P<data>.*)")
ERR_CHANOPRIVSNEEDED.params = ['srv', 'me', 'channel', 'data']

ERR_CANTKILLSERVER = retcode(483)
ERR_CANTKILLSERVER.name = "ERR_CANTKILLSERVER"
ERR_CANTKILLSERVER.re = (
    "^:(?P<srv>\S+) 483 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_CANTKILLSERVER.params = ['srv', 'me', 'data']

ERR_NOOPERHOST = retcode(491)
ERR_NOOPERHOST.name = "ERR_NOOPERHOST"
ERR_NOOPERHOST.re = (
    "^:(?P<srv>\S+) 491 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_NOOPERHOST.params = ['srv', 'me', 'data']

ERR_UMODEUNKNOWNFLAG = retcode(501)
ERR_UMODEUNKNOWNFLAG.name = "ERR_UMODEUNKNOWNFLAG"
ERR_UMODEUNKNOWNFLAG.re = (
    "^:(?P<srv>\S+) 501 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_UMODEUNKNOWNFLAG.params = ['srv', 'me', 'data']

ERR_USERSDONTMATCH = retcode(502)
ERR_USERSDONTMATCH.name = "ERR_USERSDONTMATCH"
ERR_USERSDONTMATCH.re = (
    "^:(?P<srv>\S+) 502 (?P<me>\S+) "
    ":(?P<data>.*)")
ERR_USERSDONTMATCH.params = ['srv', 'me', 'data']

RETCODES = {
    200: RPL_TRACELINK,
    201: RPL_TRACECONNECTING,
    202: RPL_TRACEHANDSHAKE,
    203: RPL_TRACEUNKNOWN,
    204: RPL_TRACEOPERATOR,
    205: RPL_TRACEUSER,
    206: RPL_TRACESERVER,
    208: RPL_TRACENEWTYPE,
    211: RPL_STATSLINKINFO,
    212: RPL_STATSCOMMANDS,
    213: RPL_STATSCLINE,
    214: RPL_STATSNLINE,
    215: RPL_STATSILINE,
    216: RPL_STATSKLINE,
    218: RPL_STATSYLINE,
    219: RPL_ENDOFSTATS,
    221: RPL_UMODEIS,
    241: RPL_STATSLLINE,
    242: RPL_STATSUPTIME,
    243: RPL_STATSOLINE,
    244: RPL_STATSHLINE,
    251: RPL_LUSERCLIENT,
    252: RPL_LUSEROP,
    253: RPL_LUSERUNKNOWN,
    254: RPL_LUSERCHANNELS,
    255: RPL_LUSERME,
    256: RPL_ADMINME,
    257: RPL_ADMINLOC1,
    258: RPL_ADMINLOC2,
    259: RPL_ADMINEMAIL,
    261: RPL_TRACELOG,
    301: RPL_AWAY,
    302: RPL_USERHOST,
    303: RPL_ISON,
    305: RPL_UNAWAY,
    306: RPL_NOWAWAY,
    311: RPL_WHOISUSER,
    312: RPL_WHOISSERVER,
    313: RPL_WHOISOPERATOR,
    314: RPL_WHOWASUSER,
    315: RPL_ENDOFWHO,
    317: RPL_WHOISIDLE,
    318: RPL_ENDOFWHOIS,
    319: RPL_WHOISCHANNELS,
    321: RPL_LISTSTART,
    322: RPL_LIST,
    323: RPL_LISTEND,
    324: RPL_CHANNELMODEIS,
    331: RPL_NOTOPIC,
    332: RPL_TOPIC,
    341: RPL_INVITING,
    342: RPL_SUMMONING,
    351: RPL_VERSION,
    352: RPL_WHOREPLY,
    353: RPL_NAMREPLY,
    364: RPL_LINKS,
    365: RPL_ENDOFLINKS,
    366: RPL_ENDOFNAMES,
    367: RPL_BANLIST,
    368: RPL_ENDOFBANLIST,
    369: RPL_ENDOFWHOWAS,
    371: RPL_INFO,
    372: RPL_MOTD,
    374: RPL_ENDOFINFO,
    375: RPL_MOTDSTART,
    376: RPL_ENDOFMOTD,
    381: RPL_YOUREOPER,
    382: RPL_REHASHING,
    391: RPL_TIME,
    392: RPL_USERSSTART,
    393: RPL_USERS,
    394: RPL_ENDOFUSERS,
    395: RPL_NOUSERS,
    401: ERR_NOSUCHNICK,
    402: ERR_NOSUCHSERVER,
    403: ERR_NOSUCHCHANNEL,
    404: ERR_CANNOTSENDTOCHAN,
    405: ERR_TOOMANYCHANNELS,
    406: ERR_WASNOSUCHNICK,
    407: ERR_TOOMANYTARGETS,
    409: ERR_NOORIGIN,
    411: ERR_NORECIPIENT,
    412: ERR_NOTEXTTOSEND,
    413: ERR_NOTOPLEVEL,
    414: ERR_WILDTOPLEVEL,
    421: ERR_UNKNOWNCOMMAND,
    422: ERR_NOMOTD,
    423: ERR_NOADMININFO,
    431: ERR_NONICKNAMEGIVEN,
    432: ERR_ERRONEUSNICKNAME,
    433: ERR_NICKNAMEINUSE,
    436: ERR_NICKCOLLISION,
    441: ERR_USERNOTINCHANNEL,
    442: ERR_NOTONCHANNEL,
    443: ERR_USERONCHANNEL,
    444: ERR_NOLOGIN,
    445: ERR_SUMMONDISABLED,
    446: ERR_USERSDISABLED,
    451: ERR_NOTREGISTERED,
    461: ERR_NEEDMOREPARAMS,
    462: ERR_ALREADYREGISTRED,
    463: ERR_NOPERMFORHOST,
    464: ERR_PASSWDMISMATCH,
    465: ERR_YOUREBANNEDCREEP,
    467: ERR_KEYSET,
    471: ERR_CHANNELISFULL,
    472: ERR_UNKNOWNMODE,
    473: ERR_INVITEONLYCHAN,
    474: ERR_BANNEDFROMCHAN,
    475: ERR_BADCHANNELKEY,
    481: ERR_NOPRIVILEGES,
    482: ERR_CHANOPRIVSNEEDED,
    483: ERR_CANTKILLSERVER,
    491: ERR_NOOPERHOST,
    501: ERR_UMODEUNKNOWNFLAG,
    502: ERR_USERSDONTMATCH,
}
