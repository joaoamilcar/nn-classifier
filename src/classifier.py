from src.metrics import distance_euclid


def nn(sample, dataset):
    count_classified_correctly = 0

    for s in sample:
        Xnew = s[:(len(s) - 1)]  # unknown class
        Xnear = []
        near_distance = 0

        for d in dataset:
            distance = distance_euclid(Xnew, d)

            if distance <= near_distance or near_distance == 0:
                near_distance = distance
                Xnear = d
                # print("sample  ", s)
                # print("neighbor", Xnear)
                # print("distance", near_distance)
                # print("")
            else:
                continue

        if s[len(s) - 1] == Xnear[len(Xnear) - 1]:
            print('success')
            print("sample  ", s)
            print("neighbor", Xnear)
            print("distance", near_distance)
            print("-")
            count_classified_correctly += 1
            dataset.append(s)
        else:
            print('fail')
            print("sample  ", s)
            print("neighbor", Xnear)
            print("distance", near_distance)
            print("-")
            continue

    print("")
    print("Classified     : ", len(sample))
    print("Correct        : ", count_classified_correctly)
    print("Sucess rate (%): ", (count_classified_correctly * 100) / len(sample))