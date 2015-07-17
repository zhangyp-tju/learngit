# coding=gbk
__author__ = "ouyuanbiao"

import sys
import urllib
import json


log_character = "GET /pv.gif?uigs_productid=appsearch&applog=info"
head_character = "GET /pv.gif?uigs_productid=appsearch&applog=info:"
action_character = "log:"


def parse_head(head_info):
    info_dict = {}
    infos = head_info.split(";")
    try:
        info_dict["productid"] = infos[0]
        info_dict["version"] = infos[1]
        info_dict["brand"] = infos[2]
        info_dict["model"] = infos[3]
        info_dict["device"] = infos[4]
        info_dict["product"] = infos[5]
        info_dict["sdk"] = infos[6]
        info_dict["os"] = infos[7]
        info_dict["mid"] = infos[8]
        info_dict["net"] = infos[9]
        info_dict["channel"] = infos[10]
        info_dict["w"] = infos[11]
        info_dict["h"] = infos[12]
        info_dict["sim"] = infos[13]
        info_dict["ori_channel"] = infos[14]
        info_dict["code"] = infos[15]
    except IndexError:
        pass
    return info_dict


def parse_action(action_info):
    infos = action_info.split(";") 
    try:
        parent = infos[1]
    except:
        return {}
    try:
        content = infos[2]
    except IndexError:
        content = ""
    try:
        optime = infos[3]
    except IndexError:
        optime = ""
    action = parent + "_" + content
    result = {}
    result["action"] = action
    result["optime"] = optime
    return result


def parse_log_content(log_content):
    result = {}
    log_lines = log_content.split("\n")
    for line in log_lines:
        info_pos = line.find(head_character)
        if info_pos != -1:
            head_dict = parse_head(line[info_pos+len(head_character):])
            if head_dict == {}:
                return {}
            try:
                result["channel"] = head_dict["channel"]
                result["device"] = head_dict["device"]
                result["mid"] = head_dict["mid"]
            except:
                return {}
            continue
        if line.startswith(action_character):
            action_pos = len(action_character)
            action_dict = parse_action(line[action_pos:])
            if "actions" not in result:
                result["actions"] = []
            result["actions"].append(action_dict)
            continue
    return result


def url_unquote(line):
    unquote_line = urllib.unquote(line)
    while line != unquote_line:
        line = unquote_line
        unquote_line = urllib.unquote(line)
    return line

if __name__ == "__main__":
    for line in sys.stdin:
        if line.find(log_character) == -1:
            continue
        log_content = urllib.unquote(line).decode("utf8", "ignore")
        user_log = parse_log_content(log_content)
        if user_log != {} and "channel" in user_log:
            print user_log["channel"].encode("gbk", "ignore") + "\t" + json.dumps(user_log, ensure_ascii=False).encode("gbk", "ignore")

