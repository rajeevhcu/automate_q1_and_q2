file = ["data/summarization-ndaq-953df9cd-15b0-43ce-85dd-172134cfb0df.csv", "data/adidas.csv"]
for file_ in file:
    max = 0
    size_ = {}
    with open(file_) as fp:
        for i, line in enumerate(fp.readlines()[1:]):
            # print(line)
            len_ = len(line)
            size_[i] = len_
            if len_ > max:
                max = len_
        print("size dict : {}".format(size_))
        print("max size : {}".format(max))
