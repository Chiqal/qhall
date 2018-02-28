# -*- coding: utf-8 -*-

import QHAL
from QHAL.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

ql = QHAL.LINE()
ql.login(token='EplnOvAHAYwYaRQIYS8f.c2hK/beMoYLo6t4JcMnWBW.kdcezWK/aYLUaf1cxQ8oS2+vy7jXEvU3vU4H5/l8wNw=')
ql.loginResult()

#ki = QHAL.LINE()
#ki.login(token='EpolqOeI1NTIVhVDRBz9.fbMcAjl5m9eOdy9zPiwPkq.JB5jHZ0Pd96RMBpPv9E6F8/4d+rDediJNfVPQs71m40=')
#ki.loginResult()

#ki2 = QHAL.LINE()
#ki2.login(token='EpxSY9zoIGa14P0R4mU7./V26Y+84iM0vgub4NBmb1W.0QSm2PAJwg8wcX7vQOj8rJBH6stJCtZECRmFJQ/2k4s=')
#ki2.loginResult()

print "╔════════════════════════════════════════════════════\n╠❂➣[LOGIN BERHASIL QHAL]\n╚════════════════════════════════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ հҽӀԹ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣ google (text)
║╠❂➣ playstore (text)
║╠❂➣ Instagram (username)
║╠❂➣ Wikipedia (text)
║╠❂➣,Idline (text)
║╠❂➣,Time
║╠❂➣ Image (text)
║╠❂➣,Runtime
║╠❂➣,Restart
║╠❂➣,Lirik (text)
║╠❂➣,Hai (mention)
║╠❂➣,Lurking
║╠❂➣,Lurkers
║╠❂➣,Protecton/off
║╠❂➣,Qron/off
║╠❂➣,Inviteon/off
║╠❂➣,Cancelon/off
║╠❂➣,Simi on/off
║╠❂➣,Read on/off
║╠❂➣,Getinfo @
║╠❂➣,Getcontact @
║╠❂➣,Vk @
║╠❂➣,Spd
║╠❂➣,Friendlist
║╠❂➣,id@en
║╠❂➣,en@id
║╠❂➣,id@jp
║╠❂➣,Keybot
║╚════════════
╚═════════════"""

keymsg ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ Ƙҽվ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣,Keypro
║╠❂➣,Keyself
║╠❂➣,Keygrup
║╠❂➣,Keyset
║╠❂➣,Keytran
║╠❂➣,On/Off
║╚════════════
╚═════════════"""

helppro ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ ƘҽվԹɾօ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣,On-Off
║╠❂➣,Protecton-off
║╠❂➣,Qron-off
║╠❂➣,Inviteon-off
║╠❂➣,Cancelon-off
║╚════════════
╚═════════════"""

helpself ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ ƘҽվՏҽӀƒ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣,Me
║╠❂➣,Myname:
║╠❂➣,Mybio:
║╠❂➣,Mypict
║╠❂➣,Mycov
║╠❂➣,Copy @
║╠❂➣,Backup
║╠❂➣,Getgroup image
║╠❂➣,Getmid @
║╠❂➣,Getprofile @
║╠❂➣,Getinfo @
║╠❂➣,Getname @
║╠❂➣,Getbio @
║╠❂➣,Spict @
║╠❂➣,Scov @
║╠❂➣,Cr (Mention)
║╠❂➣,Lurking
║╠❂➣,Lurkers
║╠❂➣,Micadd @
║╠❂➣,Micdel @
║╠❂➣,Mimic on/off
║╠❂➣,Miclist
║╚════════════
╚═════════════"""

helpset ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ ƘҽվՏҽԵ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣,C on-off
║╠❂➣,Join on/off
║╠❂➣,Leave on/off
║╠❂➣,Add on/off
║╠❂➣,Like friend
║╠❂➣,Link on
║╠❂➣,Respon on/off
║╠❂➣,Read on/off
║╠❂➣,Simi on/off
║╠❂➣,Sambut on/off
║╠❂➣,Pergi on/off
║╠❂➣,Respontag on/off
║╠❂➣,Kicktag on/off
║╚════════════
╚═════════════"""

helpgrup ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ ƘҽվցɾմԹ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣,Linkon
║╠❂➣,Url
║╠❂➣,Cancel
║╠❂➣,Gcreator
║╠❂➣,Kick @
║╠❂➣,Vk @
║╠❂➣,Gname:
║╠❂➣,Gbroadcast:
║╠❂➣,Cbroadcast:
║╠❂➣,Infogrup
║╠❂➣,Gruplist
║╠❂➣,Friendlist
║╠❂➣,Blacklist
║╠❂➣,Ban @
║╠❂➣,Banall
║╠❂➣,Unban @
║╠❂➣,Clear
║╠❂➣,Banlist
║╠❂➣,Conban
║╠❂➣,Midban
║╚════════════
╚═════════════"""

helptranslate ="""
╔═════════════
║ ✍ ՏվղժíϲɑԵҽ ƘҽվԵɾɑղ ✍
╠═════════════
║ Adiksa Setya D
║ line://ti/p/~chiqaladiksa
╠═════════════
║╔════════════
║╠❂➣Id@en
║╠❂➣En@id
║╠❂➣Id@jp
║╠❂➣Jp@id
║╠❂➣Id@th
║╠❂➣Th@id
║╠❂➣Id@ar
║╠❂➣Ar@id
║╠❂➣Id@ko
║╠❂➣Ko@id
║╠❂➣Say-id
║╠❂➣Say-en
║╠❂➣Say-jp
║╚════════════
╚═════════════"""

KAC=[ql]
mid = ql.getProfile().mid
#kimid = ki.getProfile().mid
#ki2mid = ki2.getProfile().mid
Bots=[mid]
owner =["u0b61e4f811263b294ee93e230a63706f"]
admin=["u0b61e4f811263b294ee93e230a63706f"]

wait = {
    "likeOn":True,
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    'potoMention':True,
    "steal":True,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"""Thx for add""",
    "lang":"JP",
    "comment":"Auto Like by: A ChiqaLFV",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "Wc":False,
    "Lv":False,
    'MENTION':True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = ql.getProfile()
backup = ql.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
            
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       ql.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                ql.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ql.sendText(op.param1,str(wait["message"]))
                    
        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if ql.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
              	try:
                	ql.sendText(op.param1,ql.getContact(op.param2).displayName + "Jangan Buka Kode QR Kk")
                	ql.kickoutFromGroup(op.param1,[op.param2])
                	X = ql.getGroup(op.param1)
                	X.preventJoinByTicket = True
                	ql.updateGroup(X)
                	ql.sendText(op.param1,ql.getContact(op.param2).displayName + "\n" + "Kami Masukin Kedalam Blacklis Boss")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                	X = random.choice(KAC).getGroup(op.param1)
                	X.preventJoinByTicket = True
                	random.choice(KAC).updateGroup(X)
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Kami Masukin Kedalam Blacklis Boss")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = ql.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              else:
                try:
                  ql.cancelGroupInvitation(op.param1, gMembMids)
                  ql.sendText(op.param1, "Mau Invite Siapa cuy ??? \nJangan Sok Jadi Jagoan Deh Lu Njir.\nAdmin Bukan,Owner Juga Bukan\Kick Ah 😛")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1, "Mau Invite Siapa cuy ??? \nJangan Sok Jadi Jagoan Deh Lu Njir.\nAdmin Bukan,Owner Juga Bukan\Kick Ah 😛")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ql.sendText(msg.to,text)
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in admin:
		    ql.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or admin:
                  ql.acceptGroupInvitation(op.param1)
                else:
                  ql.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kimid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
            
            if ki2mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki2.acceptGroupInvitation(op.param1)
                else:
                  ki2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
        #------Joined User Kick start------#
        if op.type == 17:
          if wait["Protectjoin"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  ql.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kalo mau Ada yang Gabung\nJoinn on/off")
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  ql.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kalo mau Ada yang Gabung\nJoinn on/off")
        #------Joined User Kick start------#
        if op.type == 32: #Yang Cancel Invitan langsung ke kick
          if wait["Protectcancel"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                random.choice(KAC).sendText(op.param1, "Jangan Sok Jadi Jagoan Deh Lu Njir.\nAdmin Bukan,Owner Juga Bukan\Kick Ah 😛")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])   
                
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in mid:
              if op.param2 not in Bots:
                try:
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  ql.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in kimid:
              if op.param2 not in Bots:
                try:
                  G = ql.getGroup(op.param1)
                  ql.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ql.updateGroup(G)
                  Ticket = ql.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G.preventJoinByTicket = True
                  ql.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki2mid:
              if op.param2 not in Bots:
                try:
                  G = ki.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #--------------------------------                      

#        if op.type == 19:
#            if op.param3 in admin:
#                ql.kickoutFromGroup(op.param1,[op.param2])
#                ql.inviteIntoGroup(op.param1,admin)
#                ql.inviteIntoGroup(op.param1,[op.param3])
#            else:
#                pass
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ql.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ql.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ql.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = ql.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            ql.updateGroup(G)
                        except:
                            ql.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ql.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                ql.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ql.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ql.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = ql.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Don't Tag Me! iam Bussy!, ",cName + "Ada perlu apa, ?",cName + " pc aja klo urgent! sedang sibuk,", "kenapa, ", cName + " kangen?","kangen bilang gak usah tag tag, " + cName, "Im bussy, " + cName, "Auto Respons, " + cName + "Bilang Kalo kangen", "No tag Kamvlet, " + cName + "?","aya naon, ?" + cName + "Tersangkut -_-" + cName + "Wooy" + cName + "Apa Sayang ?"]
                     ret_ = "." + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  ql.sendText(msg.to,ret_)
                                  break
                              
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['potoMention'] == True:
                     contact = ql.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in Bots:
                                  ql.sendImageWithURL(msg.to,ret_)
                                  break  
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = ql.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["No Tag, ",cName + " Ngapain Ngetag?, ",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja, ", "-_-, ","Chiqal lagi off, ", cName + " Kenapa Tag saya?, ","SPAM PC aja, " + cName, "Jangan Suka Tag gua, " + cName, "Apa ?", + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., "]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  ql.sendText(msg.to,ret_)
                                  ql.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = ql.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ql.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ql.findAndAddContactsByMid(target)
                                 ql.inviteIntoGroup(msg.to,[target])
                                 ql.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      ql.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            
            #if msg.contentType == 13:
            #    if wait["steal"] == True:
            #        _name = msg.contentMetadata["displayName"]
            #        copy = msg.contentMetadata["mid"]
            #        groups = kr.getGroup(msg.to)
            #        pending = groups.invitee
            #        targets = []
            #        for s in groups.members:
            #            if _name in s.displayName:
            #                print "[Target] Stealed"
            #                break                             
            #            else:
            #                targets.append(copy)
            #        if targets == []:
            #            pass
            #        else:
            #            for target in targets:
            #                try:
            #                    kr.findAndAddContactsByMid(target)
            #                    contact = kr.getContact(target)
            #                    cu = kr.channel.getCover(target)
            #                    path = str(cu)
            #                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            #                    kr.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
            #                    kr.sendText(msg.to,"Profile Picture " + contact.displayName)
            #                    kr.sendImageWithURL(msg.to,image)
            #                    kr.sendText(msg.to,"Cover " + contact.displayName)
            #                    kr.sendImageWithURL(msg.to,path)
            #                    wait["steal"] = False
            #                    break
            #                except:
            #                        pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    ql.sendChatChecked(msg.from_,msg.id)
                else:
                    ql.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ql.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ql.sendText(msg.to,"Nothing")

                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ql.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        ql.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ql.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ql.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ql.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        ql.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    ql.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ql.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ql.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ql.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ql.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ql.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ql.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    ql.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == ',key':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,helpmsg)
                else:
                    ql.sendText(msg.to,helpmsg)
            elif msg.text.lower() == ',keybot':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,keymsg)
                else:
                    ql.sendText(msg.to,keymsg)
            elif msg.text.lower() == ',keypro':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,helppro)
                else:
                    ql.sendText(msg.to,helppro)
            elif msg.text.lower() == ',keyself':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,helpself)
                else:
                    ql.sendText(msg.to,helpself)
            elif msg.text.lower() == ',keygrup':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,helpgrup)
                else:
                    ql.sendText(msg.to,helpgrup)
            elif msg.text.lower() == ',keyset':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,helpset)
                else:
                    ql.sendText(msg.to,helpset)
            elif msg.text.lower() == ',keytran':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,helptranslate)
                else:
                    ql.sendText(msg.to,helptranslate)
            elif msg.text in [",sp"]:
                start = time.time()
                ql.sendText(msg.to, "❂➣Proses.....")
                elapsed_time = time.time() - start
                ql.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text.lower() == 'crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u1f41296217e740650e0448b96851a3e2',"}
                ql.sendMessage(msg)
                ql.sendMessage(msg)
            elif msg.text.lower() == ',me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                ql.sendMessage(msg)
                
            elif ",fb" in msg.text:
                    a = msg.text.replace(",fb","")
                    b = urllib.quote(a)
                    ql.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    ql.sendText(msg.to, "https://www.facebook.com" + b)
                    ql.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")    
#======================== FOR COMMAND MODE ON STARTING ==========================#
            elif msg.text.lower() == ',on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protecion Already On")
                    else:
                        ql.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protecion Already On")
                    else:
                        ql.sendText(msg.to,"Protecion Already On")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already On")
                    else:
                        ql.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already On")
                    else:
                        ql.sendText(msg.to,"Protection Qr already On")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Invite already On")
                    else:
                        ql.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσ��є¢тισи ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
#======================== FOR COMMAND MODE OFF STARTING ==========================#
            elif msg.text.lower() == ',off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection already Off")
                    else:
                        ql.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        ql.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already off")
                    else:
                        ql.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already Off")
                    else:
                        ql.sendText(msg.to,"Protection Qr already Off")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Invite already Off")
                    else:
                        ql.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Invite already Off")
                    else:
                        ql.sendText(msg.to,"Protection Invite already Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        ql.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        ql.sendText(msg.to,"Protection Cancel already Off")
#========================== FOR COMMAND BOT STARTING =============================#
            elif msg.text.lower() == ',c on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        ql.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        ql.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == ',c off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        ql.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                    else:
                        ql.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
            elif msg.text.lower() == ',protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protecion Already On")
                    else:
                        ql.sendText(msg.to,"Protecion Already On")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protecion Already On")
                    else:
                        ql.sendText(msg.to,"Protecion Already On")
            elif msg.text.lower() == ',qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already On")
                    else:
                        ql.sendText(msg.to,"Protection Qr already On")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already On")
                    else:
                        ql.sendText(msg.to,"Protection Qr already On")
            elif ",1kick " in msg.text:
                midd = msg.text.replace(",1kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif ",2kick " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace(",2kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif msg.text.lower() == ',invite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Invite already On")
                    else:
                        ql.sendText(msg.to,"Protection Invite already On")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
            elif msg.text.lower() == ',cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
            elif msg.text.lower() == ',join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                    else:
                        ql.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
            elif msg.text.lower() == ',join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        ql.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                    else:
                        ql.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
            elif msg.text.lower() == ',protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection already Off")
                    else:
                        ql.sendText(msg.to,"Protection already Off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                    else:
                        ql.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
            elif msg.text.lower() == ',qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already off")
                    else:
                        ql.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Qr already Off")
                    else:
                        ql.sendText(msg.to,"Protection Qr already Off")
            elif msg.text.lower() == ',invite off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Invite already Off")
                    else:
                        ql.sendText(msg.to,"Protection Invite already Off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Invite already Off")
                    else:
                        ql.sendText(msg.to,"Protection Invite already Off")
            elif msg.text.lower() == ',cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        ql.sendText(msg.to,"Protection Cancel already Off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        ql.sendText(msg.to,"Protection Cancel already Off")
            elif ",grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace(",grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ql.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            ql.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ql.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            ql.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Nilai tidak benar")
                    else:
                        ql.sendText(msg.to,"Weird value")
            elif msg.text.lower() == ',leave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        ql.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        ql.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == ',leave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        ql.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        ql.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == ',share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Share set to on")
                    else:
                        ql.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Share set to on")
                    else:
                        ql.sendText(msg.to,"Share already on")
            elif msg.text.lower() == ',share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Share set to off")
                    else:
                        ql.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Share set to off")
                    else:
                        ql.sendText(msg.to,"Share already off")
            elif msg.text.lower() == ',set':
                md = """╔═════════════\n"""
                if wait["contact"] == True: md+="╠❂➣Contact:on [✅]\n"
                else: md+="╠❂➣Contact:off [❌]\n"
                if wait["autoJoin"] == True: md+="╠❂➣Auto Join:on [✅]\n"
                else: md +="╠❂➣Auto Join:off [❌]\n"
                if wait["autoCancel"]["on"] == True:md+="╠❂➣Auto cancel:" + str(wait["autoCancel"]["members"]) + "[✅]\n"
                else: md+= "╠❂➣Group cancel:off [❌]\n"
                if wait["leaveRoom"] == True: md+="╠❂➣Auto leave:on [✅]\n"
                else: md+="╠❂➣Auto leave:off [❌]\n"
                if wait["timeline"] == True: md+="╠❂➣Share:on [✅]\n"
                else:md+="╠❂➣Share:off [❌]\n"
                if wait["autoAdd"] == True: md+="╠❂➣Auto add:on [✅]\n"
                else:md+="╠❂➣Auto add:off [❌]\n"
                if wait["protect"] == True: md+="╠❂➣Protect:on [✅]\n"
                else:md+="╠❂➣Protect:off [❌]\n"
                if wait["linkprotect"] == True: md+="╠❂➣Link Protect:on [✅]\n"
                else:md+="╠❂➣Link Protect:off [❌]\n"
                if wait["inviteprotect"] == True: md+="╠❂➣Invitation Protect:on [✅]\n"
                else:md+="╠❂➣Invitation Protect:off [❌]\n"
                if wait["cancelprotect"] == True: md+="╠❂➣Cancel Protect:on [✅]\n"
                else:md+="╠❂➣Cancel Protect:off [❌]\n╚═════════════"
                ql.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u22ed21bd97a4291726fa53b756ce2f01"}
                ql.sendMessage(msg)
            elif cms(msg.text,[",creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u22ed21bd97a4291726fa53b756ce2f01"}
                ql.sendMessage(msg)
                ql.sendText(msg.to,'❂➣ Its Me')
            elif msg.text.lower() == ',add on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto add set to on")
                    else:
                        ql.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto add set to on")
                    else:
                        ql.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == ',add off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto add set to off")
                    else:
                        ql.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Auto add set to off")
                    else:
                        ql.sendText(msg.to,"Auto add already off")
            elif ",pesan set:" in msg.text:
                wait["message"] = msg.text.replace(",pesan set:","")
                ql.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == ',pesan cek':
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    ql.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif ",come Set:" in msg.text:
                c = msg.text.replace(",come Set:","")
                if c in [""," ","\n",None]:
                    ql.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    ql.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in [",come on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Aku berada di")
                    else:
                        ql.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Comment Actived")
                    else:
                        ql.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in [",come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Hal ini sudah off")
                    else:
                        ql.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Off")
                    else:
                        ql.sendText(msg.to,"To turn off")
            elif msg.text in [",comment"]:
                ql.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in [",com BL"]:
                wait["wblack"] = True
                ql.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in [",com hapus BL"]:
                wait["dblack"] = True
                ql.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in [",com BL cek"]:
                if wait["commentBlack"] == {}:
                    ql.sendText(msg.to,"Nothing in the blacklist")
                else:
                    ql.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +kr.getContact(mi_d).displayName + "\n"
                    ql.sendText(msg.to,mc)
            elif msg.text.lower() == ',jam on':
                if wait["clock"] == True:
                    ql.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = kr.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    ql.updateProfile(profile)
                    ql.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == ',jam off':
                if wait["clock"] == False:
                    ql.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    ql.sendText(msg.to,"Jam set off")
            elif ",jam say:" in msg.text:
                n = msg.text.replace(",jam say:","")
                if len(n.decode("utf-8")) > 30:
                    ql.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    ql.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == ',update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = ql.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    ql.updateProfile(profile)
                    ql.sendText(msg.to,"Diperbarui")
                else:
                    ql.sendText(msg.to,"Silahkan Aktifkan Jam")
            elif ",image " in msg.text:
                search = msg.text.replace(",image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ql.sendImageWithURL(msg.to,path)
                except:
                    pass
#========================== FOR COMMAND BOT FINISHED =============================#
            elif ",spam change:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace(",spam change:","")
                ql.sendText(msg.to,"spam changed")

            elif ",spam add:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace(",spam add:","")
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,"spam changed")
                else:
                    ql.sendText(msg.to,"Done")

            elif ",spam:" in msg.text:
                if msg.toType == 2:
                 strnum = msg.text.replace(",spam:","")
                num = int(strnum)
                for var in range(0,num):
                    ql.sendText(msg.to, wait["spam"])
#=====================================
            elif ",spam " in msg.text:
                if msg.toType == 2:
                  bctxt = msg.text.replace(",spam ", "")
                  t = ql.getAllContactIds()
                  t = 500
                  while(t):
                    ql.sendText(msg.to, (bctxt))
                    t-=1
#==============================================
            elif ",spamcontact @" in msg.text:
                _name = msg.text.replace(",spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = ql.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ql.sendText(g.mid,"Spam")
                       ql.sendText(g.mid,"Spam")
                       ql.sendText(g.mid,"Spam")
                       ql.sendText(g.mid,"Spam")
                       ql.sendText(g.mid,"Spam")
                       ql.sendText(g.mid,"Spam") 
                       ql.sendText(g.mid,"Spam")
                       ql.sendText(g.mid,"Spam")
                       print " Spammed !"

#==============================================================================#
            elif msg.text in [",1 invite"]:
                wait["invite"] = True
                ki.sendText(msg.to,"Send Contact")
                
            elif msg.text in [",2 invite"]:
                wait["invite"] = True
                ki2.sendText(msg.to,"Send Contact")
            
            elif msg.text in [",steal contact"]:
                wait["contact"] = True
                ql.sendText(msg.to,"Send Contact")
                
            elif msg.text in [",like:me",",like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                ql.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in [",like:friend",",like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                ql.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in [",like:on",",like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Already")
                        
            elif msg.text in [",like off",",like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Already")
                        
            elif msg.text in [",simi on",",simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                ql.sendText(msg.to,"Simi mode On")
                
            elif msg.text in [",simi off",",simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                ql.sendText(msg.to,"Simi mode Off")
                
            elif msg.text in [",read on"]:
                wait['alwayRead'] = True
                ql.sendText(msg.to,"Auto read On")
                
            elif msg.text in [",read off"]:
                wait['alwayRead'] = False
                ql.sendText(msg.to,"Auto read Off")
                
            elif msg.text in [",respon on"]:
                wait["detectMention"] = True
                ql.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in [",respon off"]:
                wait["detectMention"] = False
                ql.sendText(msg.to,"Auto respon tag Off")
            
            elif msg.text in [",kicktag on"]:
                wait["kickMention"] = True
                ql.sendText(msg.to,"Auto Kick tag ON")
                
            elif msg.text in ["Poto on","poto on"]:
                wait['potoMention'] = True
                ql.sendText(msg.to,"Auto respon tag poto On")
                
            elif msg.text in ["Poto off","poto off"]:
                wait['potoMention'] = False
                ql.sendText(msg.to,"Auto respon tag poto Off")
                
            elif msg.text in [",kicktag off"]:
                wait["kickMention"] = False
                ql.sendText(msg.to,"Auto Kick tag OFF")
            elif ",time" in msg.text:
              if msg.toType == 2:
                  ql.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.text in [",sambut on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"noтιғ yg joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"already on")
            elif msg.text in [",sambut off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"noтιғ yg joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif msg.text in [",pergi on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"noтιғ yg leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"already on")
            elif msg.text in [",pergi off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"noтιғ yg leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif ",cleanse" in msg.text:
				if msg.toType == 2:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace(",cleanse","")
						gs = ql.getGroup(msg.to)
						gs = ql.getGroup(msg.to)
						gs = ql.getGroup(msg.to)
						ql.sendText(msg.to,"Just some casual cleansing ô")
						ql.sendText(msg.to,"Group cleansed.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							ql.sendText(msg.to,"Not found.")
							ql.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[ki,ki2,ki]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									ql.sendText(msg.to,"Group cleanse")
									ql.sendText(msg.to,"Group cleanse")
            elif msg.text in [",salam1"]:
                ql.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                ql.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in [",salam2"]:
                ql.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                ql.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif ",salam3" in msg.text:
              if msg.from_ in owner:
                ql.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                ql.sendText(msg.to,"Assalamu'alaikum")
                ql.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                ql.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace(",salam3","")
                    gs = ql.getGroup(msg.to)
                    ql.sendText(msg.to,"maaf kalo gak sopan")
                    ql.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    ql.sendText(msg.to,"hehehhehe")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ql.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin:
                            try:
                                klist=[ki,ki2,ki]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ql.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                ql.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                ql.sendText(msg.to,"Nah salamnya jawab sendiri dah")
            elif (",kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ql.kickoutFromGroup(msg.to,[target])
                       except:
                           ql.sendText(msg.to,"LIMMIT")
            
            elif (",vk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ql.kickoutFromGroup(msg.to,[target])
                           ql.inviteIntoGroup(msg.to,[target])
                           ql.cancelGroupInvitation(msg.to,[target])
                       except:
                           ql.sendText(msg.to,"LIMMIT")
            
            elif ",kick: " in msg.text:
                midd = msg.text.replace(",kick: ","")
                ql.kickoutFromGroup(msg.to,[midd])
            
            elif ',invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    ql.findAndAddContactsByMid(key)
                    ql.inviteIntoGroup(msg.to, [key])
                    contact = ql.getContact(key)
            
            elif msg.text.lower() == ',cancel':
                if msg.toType == 2:
                    group = ql.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ql.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ql.sendText(msg.to,"Tidak ada undangan")
                        else:
                            ql.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"Tidak ada undangan")
                    else:
                        ql.sendText(msg.to,"Invitan tidak ada")
            elif msg.text in [",1cancel",",1Cancel"]:
            ##if msg.from_ in admin:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            
            elif msg.text.lower() == ',link on':
                if msg.toType == 2:
                    group = ql.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ql.updateGroup(group)
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"URL open")
                    else:
                        ql.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"It can not be used outside the group")
                    else:
                        ql.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == ',link off':
                if msg.toType == 2:
                    group = ql.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    ql.updateGroup(group)
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"URL close")
                    else:
                        ql.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        ql.sendText(msg.to,"It can not be used outside the group")
                    else:
                        ql.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text.lower() == ',1open':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"URL open")
                    else:
                        ki.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"It can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == ',1close':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    ki.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"URL close")
                    else:
                        ki.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"It can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in [",gurl"]:
                if msg.toType == 2:
                    g = ql.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        ql.updateGroup(g)
                    gurl = ql.reissueGroupTicket(msg.to)
                    ql.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif ",gcreator" == msg.text:
                try:
                    group = ql.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    ql.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    ql.sendMessage(M)
                    ql.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == ',invite:gcreator':
                if msg.toType == 2:
                       ginfo = ql.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           ql.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           ql.inviteIntoGroup(msg.to,[gcmid])
            
            elif (",gname: " in msg.text):
                if msg.toType == 2:
                    X = ql.getGroup(msg.to)
                    X.name = msg.text.replace(",gname: ","")
                    ql.updateGroup(X)
            
            elif msg.text.lower() == ',infogrup':        
                    group = ql.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    ql.sendText(msg.to,md)
            
            elif msg.text.lower() == ',grupid':
                gid = ql.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ql.getGroup(i).name,i)
                ql.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in [",glist"]:
                gid = ql.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (ql.getGroup(i).name +" ? ["+str(len(kr.getGroup(i).members))+"]")
                ql.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == ',gcancel':
                gid = ql.getGroupIdsInvited()
                for i in gid:
                    ql.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    ql.sendText(msg.to,"He declined all invitations")
                         
            elif ",autoadd" in msg.text:
                thisgroup = ql.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                ql.findAndAddContactsByMids(mi_d)
                ql.sendText(msg.to,"Success Add all")

            elif "@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = ql.getGroup(msg.to)
                    try:
                        ql.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif ",dor" == msg.text.lower():
                 group = ql.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 ql.sendMessage(cnt)

            elif "lurking" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         ql.sendText(msg.to,"Setpoint already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     ql.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    ql.sendText(msg.to,"Setpoint already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    ql.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif msg.text in ["Lukers","lukers"]:
                 if msg.toType == 2:
                    print "\nRead aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        ql.sendText(msg.to, "╔═════════════ \n╠❂➣Sider :\n╠═════════════                     %s\n╠\n╠═════════════\n╠❂➣Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "toong ready"
                        ql.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        ql.sendText(msg.to, "Ketik [Lurk] dulu, baru ketik [Lukers]")


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             ql.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = ql.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          ql.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        ql.sendText(msg.to, "Lurking has not been set.")
            elif ",gbroadcast: " in msg.text:
                bc = msg.text.replace(",gbroadcast: ","")
                gid = ql.getGroupIdsJoined()
                for i in gid:
                    ql.sendText(i, bc)
                    
            elif ",cbroadcast: " in msg.text:
                bc = msg.text.replace(",cbroadcast: ","")
                gid = ql.getAllContactIds()
                for i in gid:
                    ql.sendText(i, bc)
            
            elif ",spam change: " in msg.text:
                wait["spam"] = msg.text.replace(",spam change: ","")
                ql.sendText(msg.to,"spam changed")

            elif ",spam add: " in msg.text:
                wait["spam"] = msg.text.replace(",spam add: ","")
                if wait["lang"] == "JP":
                    ql.sendText(msg.to,"spam changed")
                else:
                    ql.sendText(msg.to,"Done")
    
            elif ",spam: " in msg.text:
                strnum = msg.text.replace(",spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    ql.sendText(msg.to, wait["spam"])
            
            elif ",spamtag @" in msg.text:
                _name = msg.text.replace(",spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = ql.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                    else:
                        pass
            
            elif ",spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace(",spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                       for x in range(jmlh):
                           ql.sendText(msg.to, teks)
                    else:
                       ql.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        ql.sendText(msg.to, tulisan)
                    else:
                        ql.sendText(msg.to, "Out Of Range!")
                        
            elif (",micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        ql.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        ql.sendText(msg.to,"Fail !")
                        break
                    
            elif (",micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        ql.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        ql.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in [",miclist"]:
                        if mimic["target"] == {}:
                            ql.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+ql.getContact(mi_d).displayName + "\n"
                            ql.sendText(msg.to,mc)

            elif ",mictar " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace(",mictar ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                ql.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                ql.sendText(msg.to,"Mimic change to target")
                            else:
                                ql.sendText(msg.to,"I dont know")
            
            elif ",mimic " in msg.text:
                cmd = msg.text.replace(",mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        ql.sendText(msg.to,"Reply Message on")
                    else:
                        ql.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        ql.sendText(msg.to,"Reply Message off")
                    else:
                        ql.sendText(msg.to,"Sudah off")
            elif ",setimage: " in msg.text:
                wait["pap"] = msg.text.replace(",setimage: ","")
                ql.sendText(msg.to, "Pap telah di Set")
            elif msg.text in [",papimage",",papim",",pap"]:
                ql.sendImageWithURL(msg.to,wait["pap"])
            elif ",setvideo: " in msg.text:
                wait["pap"] = msg.text.replace(",setvideo: ","")
                ql.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in [",papvideo",",papvid"]:
                ql.sendVideoWithURL(msg.to,wait["pap"])
            elif "TL:" in msg.text:
              if msg.toType == 2:
                tl_text = msg.text.replace("TL:","")
                ql.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ql.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==============================================================================#
            elif msg.text.lower() == ',mid':
                ql.sendText(msg.to,mid)
            elif ",midbot" == msg.text:
              ##if msg.from_ in admin:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                
            elif msg.text in ["Jebean si eta dak","Jebean si jarot dak","Jebean si puy dak","Jebean dak"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ql.sendMessage(msg)
                ki.sendMessage(msg)
            elif ",timeline: " in msg.text:
                tl_text = msg.text.replace(",timeline: ","")
                ql.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ql.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif ",myname: " in msg.text:
                string = msg.text.replace(",myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ql.getProfile()
                    profile.displayName = string
                    ql.updateProfile(profile)
                    ql.sendText(msg.to,"Aku Adalah " + string + "")
            elif ",1name:" in msg.text:
              #if msg.from_ in admin:
                string = msg.text.replace(",1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Name : " + string + "")
            elif ",2name:" in msg.text:
              #if msg.from_ in admin:
                string = msg.text.replace(",2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Update Name : " + string + "")
            elif ",mybio: " in msg.text:
                string = msg.text.replace(",mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ql.getProfile()
                    profile.statusMessage = string
                    ql.updateProfile(profile)
                    ql.sendText(msg.to,"Changed " + string)
            elif ",allbio:" in msg.text:
              #if msg.from_ in admin:
                string = msg.text.replace(",allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ql.getProfile()
                    profile.statusMessage = string
                    ql.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
            elif msg.text in [",myname"]:
                    h = ql.getContact(mid)
                    ql.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in [",mybio"]:
                    h = ql.getContact(mid)
                    ql.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in [",mypict"]:
                    h = ql.getContact(mid)
                    ql.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [",myvid"]:
                    h = ql.getContact(mid)
                    ql.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [",urlpict"]:
                    h = ql.getContact(mid)
                    ql.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [",mycov"]:
                    h = ql.getContact(mid)
                    cu = ql.channel.getCover(mid)          
                    path = str(cu)
                    ql.sendImageWithURL(msg.to, path)
            elif msg.text in [",urlcov"]:
                    h = ql.getContact(mid)
                    cu = ql.channel.getCover(mid)          
                    path = str(cu)
                    ql.sendText(msg.to, path)
#----------------------------------------------------------------------------#
            elif msg.text in [",allmid"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                ql.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)

                
            elif msg.text in [",aku"]:
              ##if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ql.sendMessage(msg)
                ql.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [",nahda"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                ki.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [",queen"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
                ki2.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in [",mybot",",bots"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ql.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ql.sendMessage(msg)
                msg.contentType = 13
            elif ",getmid @" in msg.text:
                _name = msg.text.replace(",getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = ql.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ql.sendText(msg.to, g.mid)
                    else:
                        pass
            elif ",getinfo " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ql.getContact(key1)
                cu = ql.channel.getCover(key1)
                try:
                    ql.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    ql.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif ",getbio " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ql.getContact(key1)
                cu = ql.channel.getCover(key1)
                try:
                    ql.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    ql.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif ",getname " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ql.getContact(key1)
                cu = ql.channel.getCover(key1)
                try:
                    ql.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    ql.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif ",getprofile " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ql.getContact(key1)
                cu = ql.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ql.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    ql.sendText(msg.to,"Profile Picture " + contact.displayName)
                    ql.sendImageWithURL(msg.to,image)
                    ql.sendText(msg.to,"Cover " + contact.displayName)
                    ql.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif ",getcontact " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = ql.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                ql.sendMessage(msg)
            elif ",spict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace(",spict @","")
                _nametarget = _name.rstrip('  ')
                gs = ql.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ql.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ql.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ql.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif ",svid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace(",svid @","")
                _nametarget = _name.rstrip('  ')
                gs = ql.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ql.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ql.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ql.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif ",picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace(",picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = ql.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ql.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ql.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ql.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif ",scov @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace(",scov @","")    
                _nametarget = _name.rstrip('  ')
                gs = ql.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ql.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ql.getContact(target)
                            cu = ql.channel.getCover(target)          
                            path = str(cu)
                            ql.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif ",covurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace(",covurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = ql.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ql.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ql.getContact(target)
                            cu = ql.channel.getCover(target)          
                            path = str(cu)
                            ql.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif ",getgrup image" in msg.text:
                group = ql.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ql.sendImageWithURL(msg.to,path)
            elif ",urlgrup image" in msg.text:
                group = ql.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ql.sendText(msg.to,path)
            elif ",copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace(",copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ql.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ql.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ql.CloneContactProfile(target)
                               ql.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in [",backup"]:
                try:
                    ql.updateDisplayPicture(backup.pictureStatus)
                    ql.updateProfile(backup)
                    ql.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    ql.sendText(msg.to, str(e))
#==============================================================================#
            elif ",fancytext: " in msg.text:
                txt = msg.text.replace(",fancytext: ", "")
                ql.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
                    
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                ql.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                ql.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                ql.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                ql.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                ql.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ql.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = ql.getGroup(msg.to)
                ql.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                ql.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                ql.sendAudio(msg.to,'tts.mp3')
            
            elif "/say-id " in msg.text:
                say = msg.text.replace("/say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ql.sendAudio(msg.to,"hasil.mp3")
                
            elif "/say-en " in msg.text:
                say = msg.text.replace("/say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ql.sendAudio(msg.to,"hasil.mp3")
                
            elif "/say-jp " in msg.text:
                say = msg.text.replace("/say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ql.sendAudio(msg.to,"hasil.mp3")
                
            elif "/say-ar " in msg.text:
                say = msg.text.replace("/say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ql.sendAudio(msg.to,"hasil.mp3")
                
            elif "/say-ko " in msg.text:
                say = msg.text.replace("/say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ql.sendAudio(msg.to,"hasil.mp3")
                
            elif ",kapan " in msg.text:
                  tanya = msg.text.replace(",kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  ql.sendAudio(msg.to,'tts.mp3')
                  
            elif ",apakah " in msg.text:
                  tanya = msg.text.replace(",apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  ql.sendAudio(msg.to,'tts.mp3')
            
            elif ',tubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace(',tubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        ql.sendVideoWithURL(msg.to, ght)
                    except:
                        ql.sendText(msg.to, "Could not find it")
            
            elif ",tube " in msg.text:
                    query = msg.text.replace(",tube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        ql.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif ",lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace(",lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ql.sendText(msg.to, hasil)
                except Exception as wak:
                        ql.sendText(msg.to, str(wak))
                        
            elif ",wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace(",wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ql.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              ql.sendText(msg.to, pesan)
                          except Exception as e:
                              ql.sendText(msg.to, str(e))
                              
            elif ",music " in msg.text:
                try:
                    songname = msg.text.lower().replace(",music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        ql.sendText(msg.to, hasil)
                        ql.sendText(msg.to, "Please Wait for audio...")
                        ql.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        ql.sendText(msg.to, str(njer))
            
            elif ",image " in msg.text:
                search = msg.text.replace(",image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ql.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif ",profileig " in msg.text:
                    try:
                        instagram = msg.text.replace(",profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        ql.sendImageWithURL(msg.to, profileIG)
                        ql.sendText(msg.to, str(text))
                    except Exception as e:
                        ql.sendText(msg.to, str(e))

            elif ",checkdate " in msg.text:
                tanggal = msg.text.replace(",checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                ql.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ql.sendText(msg.to, rst)
#==============================================================================#
            elif msg.text.lower() == ',ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    ql.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == ',system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    ql.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == ',kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    ql.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == ',cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    ql.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif ",restart" in msg.text:
                    print "[Command]Restart"
                    try:
                        ql.sendText(msg.to,"Restarting...")
                        ql.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        ql.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif ",turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == ',runtime':
                eltime = time.time() - mulai
                van = "Bot has been active "+waktu(eltime)
                ql.sendText(msg.to,van)

        
#================================ QHAL SCRIPT STARTED ==============================================#
            elif ",google " in msg.text:
                    a = msg.text.replace(",google ","")
                    b = urllib.quote(a)
                    ql.sendText(msg.to,"Sedang Mencari om...")
                    ql.sendText(msg.to, "https://www.google.com/" + b)
                    ql.sendText(msg.to,"Ketemu om ^")

            elif cms(msg.text,[".creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u22ed21bd97a4291726fa53b756ce2f01"}
                ql.sendMessage(msg)

            elif ",friendpp: " in msg.text:
              if msg.from_ in admin:
                suf = msg.text.replace(',friendpp: ','')
                gid = ql.getAllContactIds()
                for i in gid:
                    h = ql.getContact(i).displayName
                    gna = ql.getContact(i)
                    if h == suf:
                        ql.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

            elif ",checkmid: " in msg.text:
                saya = msg.text.replace(",checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                ql.sendMessage(msg)
                contact = ql.getContact(saya)
                cu = ql.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ql.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    ql.sendText(msg.to,"Profile Picture " + contact.displayName)
                    ql.sendImageWithURL(msg.to,image)
                    ql.sendText(msg.to,"Cover " + contact.displayName)
                    ql.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif ",checkid: " in msg.text:
                saya = msg.text.replace(",checkid: ","")
                gid = ql.getGroupIdsJoined()
                for i in gid:
                    h = ql.getGroup(i).id
                    group = ql.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            ql.sendText(msg.to,md)
                            ql.sendMessage(msg)
                            ql.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in [",friendlist"]:    
                contactlist = ql.getAllContactIds()
                kontak = ql.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                ql.sendText(msg.to, msgs)
                
            elif msg.text in [",memlist"]:   
                kontak = ql.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                ql.sendText(msg.to, msgs)
                
            elif ",friendinfo: " in msg.text:
                saya = msg.text.replace(",friendinfo: ","")
                gid = ql.getAllContactIds()
                for i in gid:
                    h = ql.getContact(i).displayName
                    contact = ql.getContact(i)
                    cu = ql.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        ql.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        ql.sendText(msg.to,"Profile Picture " + contact.displayName)
                        ql.sendImageWithURL(msg.to,image)
                        ql.sendText(msg.to,"Cover " + contact.displayName)
                        ql.sendImageWithURL(msg.to,path)
                
            elif ",friendpict: " in msg.text:
                saya = msg.text.replace(',friendpict: ','')
                gid = ql.getAllContactIds()
                for i in gid:
                    h = ql.getContact(i).displayName
                    gna = ql.getContact(i)
                    if h == saya:
                        ql.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in [",friendlistmid"]: 
                gruplist = ql.getAllContactIds()
                kontak = ql.getContacts(gruplist)
                num=1
                msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                ql.sendText(msg.to, msgs)
            
            elif msg.text in [",blocklist"]: 
                blockedlist = ql.getBlockedContactIds()
                kontak = ql.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                ql.sendText(msg.to, msgs)
                
            elif msg.text in [",gruplist"]:  
                gruplist = ql.getGroupIdsJoined()
                kontak = ql.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                ql.sendText(msg.to, msgs)
            
            elif msg.text in [",gruplistmid"]:   
                gruplist = ql.getGroupIdsJoined()
                kontak = ql.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                ql.sendText(msg.to, msgs)
                    
            elif ",grupimage: " in msg.text:
                saya = msg.text.replace(',grupimage: ','')
                gid = ql.getGroupIdsJoined()
                for i in gid:
                    h = ql.getGroup(i).name
                    gna = ql.getGroup(i)
                    if h == saya:
                        ql.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif ",grupname" in msg.text:
                saya = msg.text.replace(',grupname','')
                gid = ql.getGroup(msg.to)
                ql.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif ",grupid" in msg.text:
                saya = msg.text.replace(',grupid','')
                gid = ql.getGroup(msg.to)
                ql.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif ",grupinfo: " in msg.text:
                saya = msg.text.replace(',grupinfo: ','')
                gid = ql.getGroupIdsJoined()
                for i in gid:
                    h = ql.getGroup(i).name
                    group = ql.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            ql.sendText(msg.to,md)
                            ql.sendMessage(msg)
                            ql.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"

            elif ",spamtag @" in msg.text:
                _name = msg.text.replace(",spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = ql.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        ql.sendMessage(msg)
                        print "Spamtag Berhasil."

            elif "crashkontak @" in msg.text:
                _name = msg.text.replace("crashkontak @","")
                _nametarget = _name.rstrip(' ')
                gs = ql.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                            ql.sendMessage(g.mid,msg.to + str(msg))
                            ql.sendText(g.mid, "hai")
                            ql.sendText(g.mid, "salken")
                            ql.sendText(msg.to, "Done")
                            print " Spammed crash !"

            elif ",playstore " in msg.text.lower():
                    tob = msg.text.lower().replace(",playstore ","")
                    ql.sendText(msg.to,"Sabar Wa...")
                    ql.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    ql.sendText(msg.to,"Ketemu Wa ^")
                    
            elif '/wikipedia ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("/wikipedia ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    ql.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                            pesan+=wikipedia.page(wiki).url
                            ql.sendText(msg.to, pesan)
                        except Exception as e:
                            ql.sendText(msg.to, str(e))    
                            
            elif ",say " in msg.text.lower():
                say = msg.text.lower().replace(",say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ql.sendAudio(msg.to,"hasil.mp3")            
                
            elif msg.text in ["spam gift 25"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg) 
                ql.sendMessage(msg)
                ql.sendMessage(msg) 
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg) 
                ql.sendMessage(msg)
                ql.sendMessage(msg) 
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg) 
                ql.sendMessage(msg)
                ql.sendMessage(msg) 
                ql.sendMessage(msg)
                ql.sendMessage(msg)                
                
            elif msg.text in [",gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = ql.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       ql.findAndAddContactsByMid(gCreator)
                       ql.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in [",gcreator:kick"]:
	           if msg.from_ in admin:
                    ginfo = ql.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       ql.findAndAddContactsByMid(gCreator)
                       ql.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                   
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ql.sendText(msg.to, hasil)
                except Exception as wak:
                        ql.sendText(msg.to, str(wak))       
                   
            elif ",getcover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace(",getcover @","")
                _nametarget = _name.rstrip('  ')
                gs = ql.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ql.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ql.getContact(target)
                            cu = ql.channel.getCover(target)
                            path = str(cu)
                            ql.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif ",idline: " in msg.text:
                msgg = msg.text.replace(',idline: ','')
                conn = ql.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    ql.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    ql.sendMessage(msg)
                        
            elif ",reinvite" in msg.text.split():
                if msg.toType == 2:
                    group = ql.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            ql.findAndAddContactByMid(msg.to, grCans)
                            ql.cancelGroupInvitation(msg.to, grCans)
                            ql.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                    else:
                        if wait["lang"] == "JP":
                            ql.sendText(msg.to,"No Invited")
                        else:
                            ql.sendText(msg.to,"Error")
                else:
                    pass
                
            elif msg.text.lower() == ',runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                ql.sendText(msg.to,van)
                
            elif msg.text in [",restart"]:
                ql.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"
                
            elif msg.text in [",time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ql.sendText(msg.to, rst)
                
            elif "/image " in msg.text:
                search = msg.text.replace("/image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ql.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif ',instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(",instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "**INSTAGRAM INFO USER**\n"
                    details = "\n**INSTAGRAM INFO USER**"
                    ql.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ql.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	ql.sendText(msg.to, str(njer))    
                	
            elif msg.text in [",attack"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                ql.sendMessage(msg)
                
            elif msg.text.lower() == '...':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                ql.sendMessage(msg)    
#=================================QHAL SCRIPT FINISHED =============================================#
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in [",respon"]:
              #if msg.from_ in admin:
                #cl.sendText(msg.to,"")
                ki.sendText(msg.to," иαн∂αツ")
                ki2.sendText(msg.to," qυιииєяzツ")
                ki.sendText(msg.to,"(◕_◕)")
      #-------------Fungsi Respon Finish---------------------#
            
            elif ",ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace(",ban @","")
                    _nametarget = _name.rstrip()
                    gs = ql.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ql.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                ql.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                ql.sendText(msg.to,"Error")
                                
            elif ",unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace(",unban @","")
                    _nametarget = _name.rstrip()
                    gs = ql.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ql.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                ql.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                ql.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif ",ban:" in msg.text:                  
                       nk0 = msg.text.replace(",ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ql.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ql.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    ql.sendText(msg.to,"Error")

            elif ",unban:" in msg.text:                  
                       nk0 = msg.text.replace(",unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ql.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ql.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    ql.sendText(msg.to,_name + " Not In Blacklist")
            elif ",banall" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace(",banall","")
                       gs = ql.getGroup(msg.to)
                       ql.sendText(msg.to,"Banned all")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            ql.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       ql.sendText(msg.to,"Success Boss")
                                   except:
                                       ql.sentText(msg.to,"Berhasil Di Banned")                                    
            elif msg.text in [",clear"]:
                wait["blacklist"] = {}
                ql.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in [",ban on"]:
                wait["wblacklist"] = True
                ql.sendText(msg.to,"Send Contact")
            elif msg.text in [",ban off"]:
                wait["dblacklist"] = True
                ql.sendText(msg.to,"Send Contact")
            elif msg.text in [",banlist"]:   
                if wait["blacklist"] == {}:
                    ql.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    ql.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="*Blacklist*"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, ql.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    ql.sendText(msg.to, msgs)
            elif msg.text in [",conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    ql.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    ql.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = ql.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        ql.sendMessage(M)
            elif msg.text in [",midban","Mid ban"]:
                if msg.toType == 2:
                    group = ql.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    ql.sendText(msg.to,cocoa)
            elif msg.text.lower() == ',scan blacklist':
                if msg.toType == 2:
                    group = ql.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ql.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            ql.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        ql.kickoutFromGroup(op.param1,[op.param2])
                        G = ql.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        ql.updateGroup(G)
                    except:
                        try:
                            ql.kickoutFromGroup(op.param1,[op.param2])
                            G = ql.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            ql.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    ql.kickoutFromGroup(op.param1,[op.param2])
                    ql.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    ql.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            ql.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    ql.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = ql.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ql.updateGroup(G)
                    ql.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ql.sendText(op.param1,str(wait["message"]))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = ql.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ql.kickoutFromGroup(op.param1,[op.param3])
                    ql.updateGroup(G)
        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = ql.getGroup(op.param1)
               ql.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                ql.sendText(op.param1, "╔═════════════\n║Baper Tuh Orang :v \n║Semoga Bahagia ya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#------------------------------------------------------------------------------#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in ql.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   ql.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          ql.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = ql.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          ql.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ql.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: A ChiqaLFV")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = ql.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    ql.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ql.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: A ChiqaLFV")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


while True:
    try:
        Ops = ql.fetchOps(ql.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ql.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ql.Poll.rev = max(ql.Poll.rev, Op.revision)
            bot(Op)
