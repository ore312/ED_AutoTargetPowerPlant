# { "timestamp":"2020-09-26T12:32:52Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"viper", "Ship_Localised":"Viper Mk III", "ScanStage":3, "PilotName":"$ShipName_Police_Independent;", "PilotName_Localised":"System Authority Vessel", "PilotRank":"Master", "ShieldHealth":100.000000, "HullHealth":100.000000, "Faction":"Aseveljet", "LegalStatus":"Clean" }
# { "timestamp":"2020-09-26T12:32:57Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"viper", "Ship_Localised":"Viper Mk III", "ScanStage":3, "PilotName":"$ShipName_Police_Independent;", "PilotName_Localised":"System Authority Vessel", "PilotRank":"Master", "ShieldHealth":100.000000, "HullHealth":100.000000, "Faction":"Aseveljet", "LegalStatus":"Clean", "Subsystem":"$int_powerdistributor_size3_class3_name;", "Subsystem_Localised":"Power Distributor", "SubsystemHealth":100.000000 }
# { "timestamp":"2020-09-26T12:32:58Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"viper", "Ship_Localised":"Viper Mk III", "ScanStage":3, "PilotName":"$ShipName_Police_Independent;", "PilotName_Localised":"System Authority Vessel", "PilotRank":"Master", "ShieldHealth":100.000000, "HullHealth":100.000000, "Faction":"Aseveljet", "LegalStatus":"Clean", "Subsystem":"$int_lifesupport_size2_class3_name;", "Subsystem_Localised":"Life Support", "SubsystemHealth":100.000000 }
# { "timestamp":"2020-09-26T12:32:58Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"viper", "Ship_Localised":"Viper Mk III", "ScanStage":3, "PilotName":"$ShipName_Police_Independent;", "PilotName_Localised":"System Authority Vessel", "PilotRank":"Master", "ShieldHealth":100.000000, "HullHealth":100.000000, "Faction":"Aseveljet", "LegalStatus":"Clean", "Subsystem":"$int_hyperdrive_size3_class3_name;", "Subsystem_Localised":"FSD", "SubsystemHealth":100.000000 }
# { "timestamp":"2020-09-26T12:32:59Z", "event":"ShipTargeted", "TargetLocked":true, "Ship":"viper", "Ship_Localised":"Viper Mk III", "ScanStage":3, "PilotName":"$ShipName_Police_Independent;", "PilotName_Localised":"System Authority Vessel", "PilotRank":"Master", "ShieldHealth":100.000000, "HullHealth":100.000000, "Faction":"Aseveljet", "LegalStatus":"Clean", "Subsystem":"$int_powerplant_size3_class3_name;", "Subsystem_Localised":"Power Plant", "SubsystemHealth":100.000000 }

# "event":"ShipTargeted"
# "TargetLocked":true
# "ScanStage":3
# "Subsystem_Localised":"Power Plant"

from EDJournalLib import *
from directKeys import PressKey, ReleaseKey

import json
import time
import keyboard

VERSION = "0.0.3"

CONFIG_PATH = "config.json"

TAG_EVENT = "event"
TAG_TARGETLOCKED = "TargetLocked"
TAG_SCANSTAGE = "ScanStage"
TAG_SUBSYSTEMLOCALISED = "Subsystem_Localised"

EVENT_SHIPTARGETED = "ShipTargeted"
EVENT_TARGETLOCKED = True
EVENT_SCANSTAGE = 3

mStartFlag = False
mRightFlag = False
mNextCnt = 0
mNowSystem = ""
mNowStage = 0
mFastLoopFlag = False
mSystemIdx = -1

#config
mSystem = []
mKeyNext = [56, 37, 37]
mKeyBack = [56, 37, 38]
mKeyDelay = 0.025
mNextRightFlag = False

class clsSystem():
    def __init__(self, pSys, pKey, pSkip):
        self.Subsystem = pSys
        self.Key = pKey
        self.KeySkip = pSkip

def cnvNoneToStr(pData):
    if pData == None:
        return ""
    else:
        return pData

def cnvNoneToInt(pData):
    if pData == None:
        return -1
    else:
        return pData

def sendKey(pVKs):
    for aK in pVKs:
        PressKey(aK)

    time.sleep(mKeyDelay)

    for aK in reversed(pVKs):
        ReleaseKey(aK)

    time.sleep(mKeyDelay)

def initFlag():
    global mStartFlag
    global mRightFlag
    global mNextCnt
    global mFastLoopFlag
    global mSystemIdx

    mStartFlag = False
    mRightFlag = mNextRightFlag
    mNextCnt = 0
    mFastLoopFlag = False
    mSystemIdx = -1

def loadConfig():
    global mSystem
    global mKeyNext
    global mKeyBack
    global mKeyDelay
    global mNextRightFlag

    def readConfig(pPath):
        aStr = ""
        with open(pPath, mode="r", encoding="utf-8") as aFNo:
            aStr = aFNo.read()
        return json.loads(aStr)

    aJson = readConfig(CONFIG_PATH)

    if aJson == None:
        print("config data is none")
        return

    for aSys in aJson.get("Target"):
        mSystem.append(clsSystem( \
            aSys.get("Subsystem"), \
            aSys.get("Key"), \
            aSys.get("KeySkip") - 1 \
        ))

    mKeyNext = aJson.get("CYCLE_PREVIOUS_SUBSYSTEM")
    mKeyBack = aJson.get("CYCLE_NEXT_SUBSYSTEM")
    mKeyDelay = aJson.get("KeyDelay")
    mNextRightFlag = aJson.get("NextRightFlag")


    print("config data:")
    print("\tSystemData:")
    for aSys in mSystem:
        print("\t\tSubsystem:", end="")
        print(aSys.Subsystem)
        print("\t\t\tKey:", end="")
        print(aSys.Key)
        print("\t\t\tKeySkip:", end="")
        print(aSys.KeySkip + 1)
    print("\tKeyNext:", end="")
    print(mKeyNext)
    print("\tKeyBack:", end="")
    print(mKeyBack)
    print("\tKeyDelay:", end="")
    print(mKeyDelay)
    print("\tNextRightFlag:", end="")
    print(mNextRightFlag)
    print()

def chgFastSystem(pSkip):
    global mFastLoopFlag

    print("fast loop:" + str(pSkip))
    mFastLoopFlag = True
    #一番初めはmKeyNextPowerPlant回数連打する
    for i in range(pSkip):
        sendKey(mKeyNext)

def chgSystem():
    global mRightFlag
    global mNextCnt

    #開始位置から左右に揺れるように動く
    # -|--|--|--|--|-
    #        --->
    #     <------

    mNextCnt += 1
    print("RightFlag:" + str(mRightFlag) + " NextCnt:" + str(mNextCnt))
    if mRightFlag == True:
        mRightFlag = False
        #右
        for i in range(mNextCnt):
            sendKey(mKeyNext)
    else:
        mRightFlag = True
        #左
        for i in range(mNextCnt):
            sendKey(mKeyBack)

def hookKey(pKey):
    global mStartFlag
    global mSystemIdx

    for i in range(len(mSystem)):
        aFlag = True
        for aK in mSystem[i].Key:
            if keyboard.is_pressed(aK) != True:
                aFlag = False
                break
        if aFlag == True:
            aFlag = mStartFlag
            initFlag()
            mStartFlag = True
            mSystemIdx = i
            if aFlag == False:
                if mNowSystem == mSystem[i].Subsystem:
                    print("is " + mSystem[i].Subsystem)
                    continue
                if mNowSystem == "" and mNowStage == EVENT_SCANSTAGE:
                    chgFastSystem(mSystem[i].KeySkip)
                    break
                if mNowStage != EVENT_SCANSTAGE:
                    break
                else:
                    #右
                    for i in range(mNextCnt):
                        sendKey(mKeyNext)
                    #左
                    for i in range(mNextCnt):
                        sendKey(mKeyBack)
            break

def fncJrl(pJrl):
    global mStartFlag
    global mNowSystem
    global mNowStage

    for i in range(len(pJrl) - 1):
        aJson = None
        try:
            aJson = json.loads(pJrl[i])
        except Exception:
            continue
        if aJson == None:
            continue

        #ターゲットのサブシステムとスキャンステージを保持する
        aFastLoop = False
        if cnvNoneToStr(aJson.get(TAG_EVENT)) == EVENT_SHIPTARGETED:
            if cnvNoneToStr(aJson.get(TAG_TARGETLOCKED)) != EVENT_TARGETLOCKED:
                mNowSystem = ""
            else:
                mNowSystem = cnvNoneToStr(aJson.get(TAG_SUBSYSTEMLOCALISED))
            if mNowStage != cnvNoneToInt(aJson.get(TAG_SCANSTAGE)):
                aFastLoop = True
            mNowStage = cnvNoneToInt(aJson.get(TAG_SCANSTAGE))

        if mSystemIdx == -1:
            continue

        #ターゲット
        if cnvNoneToStr(aJson.get(TAG_EVENT)) == EVENT_SHIPTARGETED and \
                cnvNoneToStr(aJson.get(TAG_TARGETLOCKED)) == EVENT_TARGETLOCKED and \
                cnvNoneToInt(aJson.get(TAG_SCANSTAGE)) == EVENT_SCANSTAGE:

            #パワープラント
            if mStartFlag == True:
                if cnvNoneToStr(aJson.get(TAG_SUBSYSTEMLOCALISED)) == mSystem[mSystemIdx].Subsystem:
                    print("is " + mSystem[mSystemIdx].Subsystem)
                    initFlag()
                    continue

                if mStartFlag == True:
                    #はじめの連打がされていなかった場合にする
                    if mFastLoopFlag != True and aFastLoop == True:
                        chgFastSystem(mSystem[mSystemIdx].KeySkip)
                        continue

                    chgSystem()
                    continue

def main():
    print("version:" + VERSION, end="\n\n")

    #コンフィグ読み込み
    print("load config")
    loadConfig()

    #内部変数初期化
    print("initialize flags")
    initFlag()

    #キーボード監視
    print("start keyboard hook")
    keyboard.hook(hookKey)

    #ジャーナル読み込み
    print("start journal hook", end="\n\n")
    init()
    setInterval(100)
    setFnc(fncJrl)
    startJournal()

if __name__ == "__main__":
    main()
