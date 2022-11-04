import json
import stanza
# stanza.download('en')
en_nlp = stanza.Pipeline('en',  download_method=stanza.DownloadMethod.REUSE_RESOURCES)


def read_files(file_path: str):
    file = open(file_path, "r", encoding="utf-8")
    lines = file.readlines()
    datas = [line for line in lines]
    for tmp in datas:
        # print(tmp)
        text = json.loads(tmp)['sentence']
        doc = en_nlp(text)
        print(doc)
        # for i in range(len(doc.sentences)):
        #     sent = doc.sentences[i]
        #     for j in range(len(sent.tokens)):
        #         word = sent.words[j]
        #         word_set.add(word.text)


if __name__ == '__main__':
    read_files("./ace2005_origin/sample_origin.json")
