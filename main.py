import math
import jieba
import jieba.analyse
from simhash import Simhash


class SimHash(object):

    def get_string(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            return str(x)

    '''
    get_string:获取原字符串内容用于分词以及后续操作
    '''

    def getHash(self, getstr):
        seg = jieba.cut(getstr)
        Keywords = jieba.analyse.extract_tags("|".join(seg), topK=100, withWeight=True)
        Ret = []
        for keyword, weight in Keywords:
            source_str = self.get_string(keyword)
            keylists = []
            '''
            分词，并进行hash操作
            '''
            for c in source_str:
                weight = math.ceil(weight)
                if c == "1":
                    keylists.append(int(weight))
                else:
                    keylists.append(-int(weight))
            Ret.append(keylists)
            '''
            加权，为1置正值，为0置赋值    
            '''

        rows = len(Ret)
        cols = len(Ret[0])
        result = []
        for i in range(cols):
            tmp = 0
            for j in range(rows):
                tmp = tmp + int(Ret[j][i])
            if tmp > 0:
                tmp = "1"
            elif tmp <= 0:
                tmp = "0"
            result.append(tmp)
        return "".join(result)

    '''
    合并，并且降维    
    '''


def analyze_similar_text(text1, text2):
    new_simash = SimHash()
    first_hash = new_simash.getHash(text1)
    second_hash = new_simash.getHash(text2)

    text_first_hash = Simhash(first_hash)
    text_second_hash = Simhash(second_hash)

    distance = text_first_hash.distance(text_second_hash)
    '''
        .distance is a way in Simhash pack
        '''

    max_hashbit = max(len(bin(text_first_hash.value)), (len(bin(text_second_hash.value))))

    if max_hashbit == 0:
        return 0
    else:
        similar_level = 1 - distance / max_hashbit
        return (similar_level)

    '''
         analyze_similar_text 分析并求出相似度（海明距离）
        '''


def check_similar_level():
    try:

        path1 = input("origin file:")
        path2 = input("plagiarized file:")
        path3 = 'C:/Users/70421/Desktop/homework1/3119005477/test/check.txt'

        origin_file = open(path1, 'rt', encoding='utf-8')
        plagiarize_file = open(path2, 'rt', encoding='utf-8')
        similar_level_value = open(path3, 'a+', encoding='utf-8')

        origin_file_source = origin_file.read()
        plagiarize_file_source = plagiarize_file.read()

        similar = analyze_similar_text(origin_file_source, plagiarize_file_source)
        correct_similar = round(similar, 2)

        str1 = "The similar level is: "
        str2 = " between the two articles.\n"

        similar_level_value.writelines(
            str1 + str(correct_similar) + str2)
        return correct_similar

        origin_file.close()
        plagiarize_file.close()
        similar_level_value.close()
    except IndexError:
        print("Your input is wrong.")
    except FileNotFoundError:
        print("Can't find your files. Please check your files.")
    except Exception as e:
        print(f"Unknown Error:{e}")
    return 0

    '''
        check_similar_level 打开文件，调用analyze_similar_level求出相似度并写入check.txt文件，然后关闭并释放资源
        '''


if __name__ == '__main__':
    check_similar_level()
