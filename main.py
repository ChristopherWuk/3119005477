import math
from sys import argv
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

    def getHash(self, getstr):
        seg = jieba.cut(getstr)
        Keywords = jieba.analyse.extract_tags("|".join(seg), topK=100, withWeight=True)
        Ret = []
        for keyword, weight in Keywords:
            source_str = self.get_string(keyword)
            keylists = []

            for c in source_str:
                weight = math.ceil(weight)
                if c == "1":
                    keylists.append(int(weight))
                else:
                    keylists.append(-int(weight))
            Ret.append(keylists)

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


class PlagiarismChecker():

    def analyze_similar_text(self, text1, text2):
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

    def check_similar_level(self, argv):
        try:

            origin_file = open(argv[1], 'rt', encoding='utf-8')
            plagiarize_file = open(argv[2], 'rt', encoding='utf-8')
            similar_level_value = open(argv[3], 'a+', encoding='utf-8')

            origin_file_source = origin_file.read()
            plagiarize_file_source = plagiarize_file.read()

            similar = self.analyze_similar_text(origin_file_source, plagiarize_file_source)
            correct_similar = round(similar, 2)

            similar_level_value.writelines(
                "The similar level is:" + str(correct_similar) + "between the two articles.\n")
            print(f"The similar level is: %.2f between article:{argv[1]} and article:{argv[2]}.\n" % correct_similar)

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


if __name__ == '__main__':
    Check = PlagiarismChecker()
    Check.check_similar_level(argv)
