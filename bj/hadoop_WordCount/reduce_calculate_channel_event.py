# coding=gbk
__author__ = "ouyuanbiao"

import sys
import json
import traceback

def calculate_channel_event_num():
    channel_dict = {}
    last_channel = ""
    for line in sys.stdin:
        try:
            parts = line.strip('\n').split('\t')
            if len(parts) < 2:
                continue
            channel = parts[0]
            if channel != last_channel:
                for mid in channel_dict:
                    for action in channel_dict[mid]:
                        print last_channel + '\t' + str(mid) + '\t' + action.encode("gbk", "ignore") + '\t' + str(channel_dict[mid][action])
                channel_dict = {}
                last_channel = channel
            jo_str = parts[1]
            user_action = json.loads(jo_str, encoding="gbk")
            current_channel = user_action["channel"]
            current_mid = user_action["mid"]
            current_device = user_action["device"]
            if current_mid not in channel_dict:
                channel_dict[current_mid] = {}
            if current_device not in channel_dict[current_mid]:
                channel_dict[current_mid][current_device] = 0
            channel_dict[current_mid][current_device] += 1
            if "actions" not in user_action:
                continue
            action_dict = channel_dict[current_mid]
            for action in user_action["actions"]:
                if "action" not in action:
                    continue
                action_name = action["action"]
                if action_name not in action_dict:
                    action_dict[action_name] = 0
                action_dict[action_name] += 1
        except:
            traceback.print_exc()
            sys.stderr.write(line)
    for mid in channel_dict:
        for action in channel_dict[mid]:
            try:
                print last_channel + '\t' + mid + '\t' + action.encode("gbk", "ignore") + '\t' + str(channel_dict[mid][action])
            except:
                traceback.print_exc()
                sys.stderr.write(line)
            
if __name__ == "__main__":
    calculate_channel_event_num()

