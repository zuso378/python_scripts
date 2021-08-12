import argparse
import logging
import datetime
import sys
import os

def define_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='合并生成的文件路径')
    parser.add_argument('-f', nargs='+', help='要合并的文件路径（按合并顺序填写）')
    return parser

def parse_arguments(parser):
    return parser.parse_args()

def logging_config():
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)

def logging_joint_proc(file_name, file_list):
    dir, joint_name = os.path.split(file_name)
    files_name = ""
    for i in range(len(file_list)):
        dir, name = os.path.split(file_list[i])
        files_name += name
        if i!=(len(file_list)-1):
            files_name += ' + '
    logging.info(joint_name + " = " + files_name)


def joint_files(file_name, file_list):
    with open(file_name, 'wb') as wf:
        for file in file_list:
            with open(file, 'rb') as rf:
                wf.write(rf.read())
    logging_joint_proc(file_name, file_list)


if __name__ == "__main__":
    logging_config()
    #定义命令行格式
    parser = define_arguments()
    #解析命令行参数
    args = parse_arguments(parser)
    #开始合并文件
    joint_files(args.n, args.f)