from FacebookWebBot import *
import os, json, random, jsonpickle
from Spam import spam
from loginInfo import Info
posts_=[]


selfProfile = "https://mbasic.facebook.com/profile.php?fref=pb"
grups = ["https://mbasic.facebook.com/groups/830198010427436",
         "https://m.facebook.com/groups/1660869834170435",
         "https://m.facebook.com/groups/100892180263901",
         "https://m.facebook.com/groups/1649744398596548",
         "https://m.facebook.com/groups/421300388054652",
         "https://m.facebook.com/groups/675838025866331",
         "https://m.facebook.com/groups/1433809846928404",
         "https://m.facebook.com/groups/1625415104400173",
         "https://m.facebook.com/groups/424478411092230",
         "https://m.facebook.com/groups/1056447484369528",
         "https://m.facebook.com/groups/1433809846928404",
         "https://m.facebook.com/groups/421300388054652",
         "https://m.facebook.com/groups/1649744398596548",
         "https://m.facebook.com/groups/751450114953723",
         "https://m.facebook.com/groups/943175872420249"
]

postsList = list()
peopleList = list()
saluteText = "Buenos días usuarios, gracias por activar su unidad moderadora 3000\n" \
             "\nPara información sobre su uso presione la tecla F1, para ayuda presione F2 \n" \
             "Para otras instrucciones remitase al manual de usuario adjunto en el CD instalador"

eula = """Unidad Moderadora 3000 0.69
Copyright (c) 2001 Unit0x78A

*** END USER LICENSE AGREEMENT ***

IMPORTANT: PLEASE READ THIS LICENSE CAREFULLY BEFORE USING THIS SOFTWARE.

1. LICENSE

By receiving, opening the file package, and/or using Unidad Moderadora 3000 0.69("Software") containing this software, you agree that this End User User License Agreement(EULA) is a legally binding and valid contract and agree to be bound by it. You agree to abide by the intellectual property laws and all of the terms and conditions of this Agreement.

Unless you have a different license agreement signed by Unit0x78A your use of Unidad Moderadora 3000 0.69 indicates your acceptance of this license agreement and warranty.

Subject to the terms of this Agreement, Unit0x78A grants to you a limited, non-exclusive, non-transferable license, without right to sub-license, to use Unidad Moderadora 3000 0.69 in accordance with this Agreement and any other written agreement with Unit0x78A. Unit0x78A does not transfer the title of Unidad Moderadora 3000 0.69 to you; the license granted to you is not a sale. This agreement is a binding legal agreement between Unit0x78A and the purchasers or users of Unidad Moderadora 3000 0.69.

If you do not agree to be bound by this agreement, remove Unidad Moderadora 3000 0.69 from your computer now and, if applicable, promptly return to Unit0x78A by mail any copies of Unidad Moderadora 3000 0.69 and related documentation and packaging in your possession.

2. DISTRIBUTION

Unidad Moderadora 3000 0.69 and the license herein granted shall not be copied, shared, distributed, re-sold, offered for re-sale, transferred or sub-licensed in whole or in part except that you may make one copy for archive purposes only. For information about redistribution of Unidad Moderadora 3000 0.69 contact Unit0x78A.

3. USER AGREEMENT

3.1 Use

Your license to use Unidad Moderadora 3000 0.69 is limited to the number of licenses purchased by you. You shall not allow others to use, copy or evaluate copies of Unidad Moderadora 3000 0.69.

3.2 Use Restrictions

You shall use Unidad Moderadora 3000 0.69 in compliance with all applicable laws and not for any unlawful purpose. Without limiting the foregoing, use, display or distribution of Unidad Moderadora 3000 0.69 together with material that is pornographic, racist, vulgar, obscene, defamatory, libelous, abusive, promoting hatred, discriminating or displaying prejudice based on religion, ethnic heritage, race, sexual orientation or age is strictly prohibited.

Each licensed copy of Unidad Moderadora 3000 0.69 may be used on one single computer location by one user. Use of Unidad Moderadora 3000 0.69 means that you have loaded, installed, or run Unidad Moderadora 3000 0.69 on a computer or similar device. If you install Unidad Moderadora 3000 0.69 onto a multi-user platform, server or network, each and every individual user of Unidad Moderadora 3000 0.69 must be licensed separately.

You may make one copy of Unidad Moderadora 3000 0.69 for backup purposes, providing you only have one copy installed on one computer being used by one person. Other users may not use your copy of Unidad Moderadora 3000 0.69 . The assignment, sublicense, networking, sale, or distribution of copies of Unidad Moderadora 3000 0.69 are strictly forbidden without the prior written consent of Unit0x78A. It is a violation of this agreement to assign, sell, share, loan, rent, lease, borrow, network or transfer the use of Unidad Moderadora 3000 0.69. If any person other than yourself uses Unidad Moderadora 3000 0.69 registered in your name, regardless of whether it is at the same time or different times, then this agreement is being violated and you are responsible for that violation!

3.3 Copyright Restriction

This Software contains copyrighted material, trade secrets and other proprietary material. You shall not, and shall not attempt to, modify, reverse engineer, disassemble or decompile Unidad Moderadora 3000 0.69. Nor can you create any derivative works or other works that are based upon or derived from Unidad Moderadora 3000 0.69 in whole or in part.

Unit0x78A's name, logo and graphics file that represents Unidad Moderadora 3000 0.69 shall not be used in any way to promote products developed with Unidad Moderadora 3000 0.69 . Unit0x78A retains sole and exclusive ownership of all right, title and interest in and to Unidad Moderadora 3000 0.69 and all Intellectual Property rights relating thereto.

Copyright law and international copyright treaty provisions protect all parts of Unidad Moderadora 3000 0.69, products and services. No program, code, part, image, audio sample, or text may be copied or used in any way by the user except as intended within the bounds of the single user program. All rights not expressly granted hereunder are reserved for Unit0x78A.

3.4 Limitation of Responsibility

You will indemnify, hold harmless, and defend Unit0x78A , its employees, agents and distributors against any and all claims, proceedings, demand and costs resulting from or in any way connected with your use of Unit0x78A's Software.

In no event (including, without limitation, in the event of negligence) will Unit0x78A , its employees, agents or distributors be liable for any consequential, incidental, indirect, special or punitive damages whatsoever (including, without limitation, damages for loss of profits, loss of use, business interruption, loss of information or data, or pecuniary loss), in connection with or arising out of or related to this Agreement, Unidad Moderadora 3000 0.69 or the use or inability to use Unidad Moderadora 3000 0.69 or the furnishing, performance or use of any other matters hereunder whether based upon contract, tort or any other theory including negligence.

Unit0x78A's entire liability, without exception, is limited to the customers' reimbursement of the purchase price of the Software (maximum being the lesser of the amount paid by you and the suggested retail price as listed by Unit0x78A ) in exchange for the return of the product, all copies, registration papers and manuals, and all materials that constitute a transfer of license from the customer back to Unit0x78A.

3.5 Warranties

Except as expressly stated in writing, Unit0x78A makes no representation or warranties in respect of this Software and expressly excludes all other warranties, expressed or implied, oral or written, including, without limitation, any implied warranties of merchantable quality or fitness for a particular purpose.

3.6 Governing Law

This Agreement shall be governed by the law of the Afghanistan applicable therein. You hereby irrevocably attorn and submit to the non-exclusive jurisdiction of the courts of Afghanistan therefrom. If any provision shall be considered unlawful, void or otherwise unenforceable, then that provision shall be deemed severable from this License and not affect the validity and enforceability of any other provisions.

3.7 Termination

Any failure to comply with the terms and conditions of this Agreement will result in automatic and immediate termination of this license. Upon termination of this license granted herein for any reason, you agree to immediately cease use of Unidad Moderadora 3000 0.69 and destroy all copies of Unidad Moderadora 3000 0.69 supplied under this Agreement. The financial obligations incurred by you shall survive the expiration or termination of this license.

4. DISCLAIMER OF WARRANTY

THIS SOFTWARE AND THE ACCOMPANYING FILES ARE SOLD "AS IS" AND WITHOUT WARRANTIES AS TO PERFORMANCE OR MERCHANTABILITY OR ANY OTHER WARRANTIES WHETHER EXPRESSED OR IMPLIED. THIS DISCLAIMER CONCERNS ALL FILES GENERATED AND EDITED BY Unidad Moderadora 3000 0.69 AS WELL.

5. CONSENT OF USE OF DATA

You agree that Unit0x78A may collect and use information gathered in any manner as part of the product support services provided to you, if any, related to Unidad Moderadora 3000 0.69.Unit0x78A may also use this information to provide notices to you which may be of use or interest to you."""


def getPost():
    global postsList


def saluteAll():
    global grups, bot, saluteText
    for g in grups:
        try:
            bot.postInGroup(g, eula)
            print("DONE")
        except Exception:
            print("Fail")


def getUsers():
    global peopleList, grups, bot
    for g in grups:
        try:
            pg = bot.getGroupMembers(g, 1, random.randint(0, 20))
            peopleList += pg
            print("DONE", len(pg))
        except Exception:
            print("fail")
    print(len(peopleList))


def addAll():
    global bot, grups, peopleList
    for p in peopleList:
        try:
            bot.sendFriendRequest(p.profileLink)
            print("Added: ", p.name)
        except Exception:
            print("Fail to add: ", p.name)


def spam_group():
    global bot, groups,posts_
    for g in grups:
        try:
            posts_ += bot.getPostInGroup(g)[0]
            print("Number of posts: ", len(posts_))
        except Exception:
            print("Fail get posts in :", bot.title)
    for p in posts_:
        try:
            n=bot.commentInPost(p.linkToComment, random.choice(spam))
            bot.save_screenshot(n)
            print("Commenting in", bot.title)
        except Exception:
            print("Fail comment in ", bot.title)


if __name__ == "__main__":
    bot = FacebookBot()
    bot.login(Info["email"], Info["pass"], False)
    bot.save_screenshot("debug.jpg")
    while True:
        try:
            saluteAll()
            spam_group()
            time.sleep(5*60)
        except Exception:
            print ("ERROR!!!")
