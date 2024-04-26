import random
import time

events = {
    10001:"你出生了，是一个男孩",
    10002:"你出生了，是一个女孩",
    10003:"你生了场重病",
    10004:"你开始看动漫",
    10005:"你从小生活在农村",
    10006:"你从小生活在城市",
    10007:"你运动天赋不错",
    10008:"你很漂亮",
    10009:"你小有名气",
    10010:"你智力过高，被抓去做实验",
    10011:"你经常在家做发明",
    10012:"你徒手抓到了一只老鼠",
}

age0_events = [10001,10002]
age1_events = [10005,10006]
age10_events = age9_events = age8_events = age7_events = age6_events = age5_events = age4_events = age3_events = age2_events = [10003,10004,10007,10008,10009,10010,10011,10012]

age_events_list = [age0_events,age1_events,age2_events,age3_events,age4_events,age5_events,age6_events,age7_events,age8_events,age9_events,age10_events]

past = []

print("**************************************")
print("                                      ")
print("    《人生重开模拟器》————python版      ")
print("                                      ")
print("                                      ")
print("**************************************")

input("按回车重开")

age = 0

while (age < 10):
    event_id = random.choice(age_events_list[age])
    while(event_id in past):
        event_id = random.choice(age_events_list[age])
    print(age,"岁" + events[event_id])
    past.append(event_id)
    age = age + 1
    time.sleep(1)