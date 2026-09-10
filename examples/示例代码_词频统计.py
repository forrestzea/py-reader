"""词频统计小工具：统计一个英文文本文件里每个单词出现的次数"""

import re
from collections import Counter


def read_file(file_path):
    """读取文本文件内容，返回字符串"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def split_words(text):
    """把文本切分成单词列表（只保留字母单词，统一转小写）"""
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return words


def count_words(words):
    """统计每个单词出现的次数"""
    counter = Counter(words)
    return counter


def show_top(counter, top_n=5):
    """打印出现次数最多的前 top_n 个单词"""
    print("===== 单词出现次数排行 =====")
    for word, count in counter.most_common(top_n):
        print(f"{word:<15} {count} 次")


def main():
    file_path = "article.txt"
    text = read_file(file_path)
    words = split_words(text)
    counter = count_words(words)
    show_top(counter)


if __name__ == "__main__":
    main()
