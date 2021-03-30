# -*- coding: utf-8 -*-
import re
import sys
import File
import argparse

out_set = set()
match_flag = False


def process_lines(args, line):
    global match_flag
    global out_set
    regex = re.compile(args.pattern)
    defstr = args.replacement
    if args.mode == 0:
        ma = regex.search(line)
        if ma:
            match_flag = True
            print(line,end='')
    elif args.mode == 1:
        # 在匹配字符串的前方插入
        ma = regex.search(line)
        if ma:
            match_flag = True
            line = line[:ma.start()] + defstr + line[ma.start():]
        print(line, end='')
    elif args.mode == 2:
        # 在匹配字符串的后方插入
        ma = regex.search(line)
        if ma:
            match_flag = True
            line = line[:ma.end()] + defstr + line[ma.end():]
        print(line, end='')
    elif args.mode == 3:
        # 输出匹配的字符串
        ma = regex.search(line)
        if ma:
            match_flag = True
            print(line[ma.start():ma.end()])
    elif args.mode == 4:
        # 输出第一个匹配的字符串
        ma = regex.search(line)
        if ma:
            match_flag = True
            print(line[ma.start():ma.end()])
            sys.exit(0)
    elif args.mode == 5:
        # 输出所以匹配的字符串
        ma = regex.search(line)
        if ma:
            match_flag = True
            out_set.add(line[ma.start():ma.end()])
    elif args.mode == 6:
        line = regex.sub(defstr, line)
        match_flag = True
        print(line, end='')


def process_end():
    global out_set
    for i in out_set:
        print(i)
    if not match_flag:
        sys.exit(-1)


def main():
    parser = argparse.ArgumentParser(prog="pattern", description="正则表达式命令行工具")
    parser.add_argument("-f", "--filename", metavar="filename", type=str, required=False,
                        dest="filename", help="目标文件名,如果未提供文件则运行为流模式")
    parser.add_argument("-p", type=str, required=True, dest="pattern", help="正则匹配表达式")
    parser.add_argument("-r", type=str, dest="replacement", default="*", help="需要替换成字符串的值(mode等于3、4、5时忽略)")
    parser.add_argument("-m", "--mode", type=int, required=False, choices=[0, 1, 2, 3, 4, 5, 6], dest="mode",
                        help="模式选择: 0(输出匹配的行,default), 1(前边插入), 2(后边插入), 3(输出匹配字符串), "
                             "4(输出第一个匹配的字符串), 5(输出所以匹配的字符串), 6(替换模式, 输出替换后的字符串)", default=0)
    args = parser.parse_args()
    if args.filename:
        file = File.File(args.filename)
        if not file.exists() or file.isDirectory():
            print("File Not Found", end='')
            sys.exit(-1)
        with open(args.filename, 'r', encoding='utf-8', errors="ignore") as f:
            for line in f:
                process_lines(args, line)
    else:
        for line in sys.stdin:
            process_lines(args, line)
    process_end()


if __name__ == "__main__":
    main()
