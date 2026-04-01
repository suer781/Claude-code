#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import time

def prank():
    print("\n" + "="*60)
    print("🎉 愚人节快乐! Happy April Fools' Day! 🎉")
    print("="*60)
    print("\n你被骗了！你没有获得真正的Claude源代码。\n")
    print("这只是一个有趣的愚人节彩蛋。")
    print("真正的Claude源代码不会这样泄露 😄\n")
    print("="*60)
    time.sleep(2)
    
    # 删除自己
    print("\n正在清理文件...")
    try:
        os.remove(__file__)
        print("✓ 文件已自动删除")
    except:
        print("⚠ 无法自动删除，请手动删除此文件")
    
    print("\n祝你有美好的一天！\n")

if __name__ == "__main__":
    prank()