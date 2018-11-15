import pathlib


text_path = pathlib.Path("../data/raw/test_text_2.txt")
text_l1_path = pathlib.Path("../data/processed/l1_text.txt")
text_l2_path = pathlib.Path("../data/processed/l2_text.txt")
text_l3_path = pathlib.Path("../data/processed/l3_text.txt")

if text_path.is_file():
    with text_path.open("r") as reader:
        text = reader.read()

    text = text.strip("\n")
    text = text.strip("\r")
    text = text.strip("\t")
    text_length = len(text)
    trd_len = text_length // 3
    scnd_len = text_length // 2

    l3_nr_1 = text[:trd_len]
    l3_nr_2 = text[trd_len:trd_len + trd_len]
    l3_nr_3 = text[trd_len + trd_len:]

    for file, text in (text_l1_path, l3_nr_1), (text_l2_path, l3_nr_2), (text_l3_path, l3_nr_3):
        with file.open("w+") as writer:
            writer.write(text)

    for t in (l3_nr_1, l3_nr_2, l3_nr_3):
        print(len(t))

    print("\nNR 1\n -------------------------------------------------------------------------------------")
    print(l3_nr_1)

    print("\nNR 2\n ----------------------------------------------------------------------------------------")
    print(l3_nr_2)

    print("\nNR 3\n ----------------------------------------------------------------------------------------")
    print(l3_nr_3)



